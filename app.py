import streamlit as st
import time
import datetime
import requests

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Binary Mind | CognitiveCloud.ai",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Space+Mono:wght@400;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Space Grotesk', sans-serif;
    background-color: #0a0e1a;
    color: #e8eaf0;
}

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 1.5rem 4rem; max-width: 720px; }

.binary-bg {
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    color: #1a2a1a;
    letter-spacing: 4px;
    text-align: center;
    line-height: 2;
    margin-bottom: -1.5rem;
    opacity: 0.6;
    animation: pulse 4s ease-in-out infinite;
}
@keyframes pulse { 0%,100%{opacity:0.3} 50%{opacity:0.7} }

.site-label {
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    letter-spacing: 4px;
    color: #4ade80;
    text-transform: uppercase;
    text-align: center;
    margin-bottom: 0.25rem;
}
.main-title {
    font-size: 2.8rem;
    font-weight: 700;
    text-align: center;
    color: #ffffff;
    line-height: 1.1;
    margin-bottom: 0.25rem;
}
.main-title span { color: #4ade80; }
.subtitle {
    text-align: center;
    font-size: 0.95rem;
    color: #7a8399;
    letter-spacing: 1px;
    margin-bottom: 2.5rem;
}
.week-badge {
    display: inline-block;
    background: #111827;
    border: 1px solid #2a3a2a;
    border-radius: 999px;
    padding: 0.3rem 1.1rem;
    font-family: 'Space Mono', monospace;
    font-size: 0.75rem;
    color: #4ade80;
    letter-spacing: 2px;
    margin-bottom: 2rem;
}
.card {
    background: #111827;
    border: 1px solid #1e2d3d;
    border-radius: 16px;
    padding: 1.8rem 2rem;
    margin-bottom: 1.5rem;
}
.card-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 3px;
    color: #4ade80;
    text-transform: uppercase;
    margin-bottom: 0.6rem;
}
.card h3 { font-size: 1.25rem; font-weight: 600; color: #ffffff; margin-bottom: 0.5rem; }
.card p { color: #9aa5b8; font-size: 0.95rem; line-height: 1.7; }
.breath-container { display: flex; flex-direction: column; align-items: center; padding: 2rem 0; }
.breath-circle {
    width: 120px; height: 120px; border-radius: 50%;
    background: radial-gradient(circle, #1a4a2a 0%, #0d1f17 60%, #0a0e1a 100%);
    border: 2px solid #4ade80;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Space Mono', monospace; font-size: 0.8rem; color: #4ade80;
    animation: breathe 8s ease-in-out infinite;
    box-shadow: 0 0 30px rgba(74,222,128,0.15); margin-bottom: 1rem;
}
@keyframes breathe {
    0%,100% { transform: scale(1); box-shadow: 0 0 20px rgba(74,222,128,0.1); }
    50% { transform: scale(1.4); box-shadow: 0 0 50px rgba(74,222,128,0.35); }
}
.breath-label { font-family: 'Space Mono', monospace; font-size: 0.7rem; letter-spacing: 2px; color: #4ade80; }
.reflection-header { font-size: 1.05rem; font-weight: 600; color: #e8eaf0; margin-bottom: 0.4rem; }
.reflection-sub { font-size: 0.85rem; color: #7a8399; margin-bottom: 1rem; font-style: italic; }
.log-entry {
    border-left: 2px solid #4ade80; padding: 0.6rem 1rem; margin-bottom: 0.75rem;
    background: #0d1117; border-radius: 0 8px 8px 0;
}
.log-date { font-family:'Space Mono',monospace; font-size:0.65rem; color:#4ade80; letter-spacing:2px; }
.log-text { font-size:0.9rem; color:#9aa5b8; margin-top:0.2rem; }
.divider { border: none; border-top: 1px solid #1e2d3d; margin: 2rem 0; }
.stTextArea textarea {
    background: #0d1117 !important; border: 1px solid #1e2d3d !important;
    color: #e8eaf0 !important; border-radius: 10px !important;
    font-family: 'Space Grotesk', sans-serif !important;
}
.stSlider > div > div { background: #1e2d3d !important; }
.stButton > button {
    background: #4ade80 !important; color: #0a0e1a !important; border: none !important;
    border-radius: 999px !important; font-family: 'Space Mono', monospace !important;
    font-size: 0.75rem !important; letter-spacing: 2px !important;
    padding: 0.6rem 2rem !important; font-weight: 700 !important;
}
.stButton > button:hover { background: #86efac !important; }
.stSelectbox > div > div {
    background: #0d1117 !important; border: 1px solid #1e2d3d !important;
    color: #e8eaf0 !important; border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)

# ── Dr. X API ─────────────────────────────────────────────────────────────────
def ask_drx(message):
    try:
        response = requests.post(
            'https://ask-drx-730124987572.us-central1.run.app',
            json={'message': message}, timeout=30
        )
        if response.status_code == 200:
            return response.json().get('reply', "Sorry, I couldn't process that.")
        else:
            return "I'm having trouble connecting right now. Please try again."
    except requests.exceptions.Timeout:
        return "I'm having trouble connecting right now. The request timed out. Please try again."
    except requests.exceptions.ConnectionError:
        return "I'm having trouble connecting right now. Please check your internet connection."
    except Exception as e:
        return f"An unexpected error occurred: {e}. Please try again."

# ── Session state ─────────────────────────────────────────────────────────────
if "weekly_log" not in st.session_state:
    st.session_state.weekly_log = []
if "knowledge_bits" not in st.session_state:
    st.session_state.knowledge_bits = [0] * 8

# ── Helpers ───────────────────────────────────────────────────────────────────
def get_week_label():
    week_num = datetime.date.today().isocalendar()[1]
    return f"WEEK {week_num} · GRADE 8 · 8.NS"

def bits_to_decimal(bits):
    return sum(b * (2 ** (7 - i)) for i, b in enumerate(bits))

def binary_string(bits):
    return "".join(str(b) for b in bits)

TOPICS = [
    "Rational vs. Irrational Numbers",
    "Approximating Irrational Numbers",
    "Number Line Placement",
    "Ordering Real Numbers",
    "Converting Repeating Decimals",
    "Square Roots & Cube Roots",
    "Scientific Notation",
    "Comparing with Scientific Notation",
]

AFFIRMATIONS = [
    "Not knowing is the beginning of knowing.",
    "Every 0 is just a 1 waiting to happen.",
    "Your brain rewires itself every time you try.",
    "The struggle IS the learning.",
    "0 → 1. That's growth. That's you.",
    "Confusion is your mind making new connections.",
    "There is no failure in this room — only data.",
    "You are always closer than you think.",
]

# ── BINARY BACKGROUND ─────────────────────────────────────────────────────────
st.markdown("""
<div class="binary-bg">
01001011 01001110 01001111 01010111 00100000 01001001 01010100<br>
00000000 00000001 00000000 00000001 00000001 00000000 00000001<br>
01000111 01010010 01001111 01010111 00100000 01001110 01001111
</div>
""", unsafe_allow_html=True)

# ── HEADER ────────────────────────────────────────────────────────────────────
st.markdown('<div class="site-label">COGNITIVECLOUD.AI</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align:center; font-family:\'Space Grotesk\',sans-serif; font-size:1.05rem; font-weight:600; color:#4ade80; letter-spacing:1px; margin-bottom:0.15rem;">Positive Mindset Growth Mindset Math</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align:center; font-family:\'Space Mono\',monospace; font-size:0.7rem; color:#4a5568; letter-spacing:3px; margin-bottom:1rem;">COMMON CORE · GRADE 8 · 8.NS</div>', unsafe_allow_html=True)
st.markdown('<div class="main-title">BINARY<span> MIND</span></div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">A weekly mindset opener · The Number System</div>', unsafe_allow_html=True)
st.markdown(f'<div style="text-align:center"><span class="week-badge">{get_week_label()}</span></div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# BINARY ACTION — Interactive concept section
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="card">
    <div class="card-label">Binary Action · The Concept</div>
    <h3>Not all 1s are the same.</h3>
    <p>
        In physics, binary is <em>certain</em>. A switch is on or off. 
        An object hits the ground or it doesn't. No interpretation. No doubt.<br><br>
        But <em>knowledge</em> isn't a switch. You can mark yourself a 1 and still be wrong. 
        You can mark yourself a 0 and be closer than you think.<br><br>
        <strong style="color:#4ade80">Binary Action</strong> is what happens in that gap — 
        acting even when your knowledge state is still 0. 
        That move, from uncertainty into action, is where real learning lives.
    </p>
</div>
""", unsafe_allow_html=True)

# ── Interactive Binary Action Demo ────────────────────────────────────────────
st.components.v1.html("""
<!DOCTYPE html>
<html>
<head>
<style>
  * { margin:0; padding:0; box-sizing:border-box; }
  body { background: transparent; font-family: 'Space Grotesk', 'Segoe UI', sans-serif; }

  .demo-wrapper {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    padding: 4px;
  }

  .panel {
    background: #0d1117;
    border: 1px solid #1e2d3d;
    border-radius: 14px;
    padding: 20px;
    text-align: center;
  }

  .panel-label {
    font-size: 9px;
    letter-spacing: 3px;
    color: #4a5568;
    text-transform: uppercase;
    margin-bottom: 10px;
    font-family: monospace;
  }

  .panel-title {
    font-size: 13px;
    font-weight: 600;
    color: #e8eaf0;
    margin-bottom: 16px;
  }

  /* ── SWITCH ── */
  .switch-scene {
    height: 140px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 12px;
  }

  .switch-body {
    width: 54px;
    height: 90px;
    background: #1a2233;
    border: 2px solid #2a3a4a;
    border-radius: 10px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
    padding: 8px 0;
    cursor: pointer;
    transition: border-color 0.2s;
    position: relative;
  }
  .switch-body:hover { border-color: #4ade80; }

  .switch-pip {
    width: 28px;
    height: 28px;
    border-radius: 6px;
    transition: all 0.15s;
  }
  .switch-pip.top { background: #4ade80; }
  .switch-pip.top.off { background: #1e2d1e; }
  .switch-pip.bottom { background: #1e2d1e; }
  .switch-pip.bottom.on { background: #4ade80; }

  .switch-label-row {
    display: flex;
    gap: 6px;
    align-items: center;
  }
  .bit-display {
    font-family: monospace;
    font-size: 28px;
    font-weight: 700;
    transition: color 0.15s;
  }
  .bit-display.on { color: #4ade80; }
  .bit-display.off { color: #2a3a2a; }

  .certainty-tag {
    font-size: 9px;
    letter-spacing: 2px;
    font-family: monospace;
    padding: 3px 10px;
    border-radius: 20px;
    margin-top: 4px;
  }
  .certain { background: #0d2d1a; color: #4ade80; border: 1px solid #2a5a3a; }
  .uncertain { background: #1a1a2a; color: #7a8399; border: 1px solid #2a3a4a; }

  /* ── FALLING OBJECT ── */
  .drop-scene {
    height: 140px;
    position: relative;
    overflow: hidden;
    cursor: pointer;
    border-radius: 8px;
    background: #080c14;
    border: 1px solid #1e2d3d;
  }

  .ground {
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 3px;
    background: #4ade80;
    opacity: 0.4;
  }

  .ball {
    width: 28px;
    height: 28px;
    background: radial-gradient(circle at 35% 35%, #86efac, #4ade80);
    border-radius: 50%;
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    top: 10px;
    box-shadow: 0 0 12px rgba(74,222,128,0.4);
  }

  .impact-ring {
    position: absolute;
    bottom: 3px;
    left: 50%;
    transform: translateX(-50%) scale(0);
    width: 40px; height: 12px;
    border: 2px solid #4ade80;
    border-radius: 50%;
    opacity: 0;
  }

  .drop-hint {
    position: absolute;
    bottom: 10px; left: 0; right: 0;
    text-align: center;
    font-size: 9px;
    letter-spacing: 2px;
    color: #4a5568;
    font-family: monospace;
  }

  /* ── KNOWLEDGE METER ── */
  .knowledge-panel {
    grid-column: 1 / -1;
    background: #0d1117;
    border: 1px solid #1e2d3d;
    border-radius: 14px;
    padding: 20px 24px;
  }

  .k-title {
    font-size: 12px;
    font-weight: 600;
    color: #e8eaf0;
    margin-bottom: 4px;
  }
  .k-sub {
    font-size: 11px;
    color: #4a5568;
    margin-bottom: 16px;
    font-family: monospace;
    letter-spacing: 1px;
  }

  .meter-track {
    height: 10px;
    background: #1a2233;
    border-radius: 999px;
    position: relative;
    overflow: visible;
    margin-bottom: 8px;
  }
  .meter-fill {
    height: 100%;
    border-radius: 999px;
    background: linear-gradient(90deg, #2a5a3a, #4ade80);
    transition: width 0.6s cubic-bezier(.34,1.56,.64,1);
    position: relative;
  }
  .meter-fuzz {
    position: absolute;
    right: -6px; top: -4px;
    width: 18px; height: 18px;
    border-radius: 50%;
    background: radial-gradient(circle, #4ade8088 0%, transparent 70%);
    animation: fuzz 1.8s ease-in-out infinite;
  }
  @keyframes fuzz {
    0%,100% { transform: scale(1) translateX(0); opacity: 0.6; }
    33% { transform: scale(1.3) translateX(2px); opacity: 1; }
    66% { transform: scale(0.8) translateX(-2px); opacity: 0.4; }
  }

  .meter-labels {
    display: flex;
    justify-content: space-between;
    font-size: 9px;
    font-family: monospace;
    letter-spacing: 2px;
    color: #4a5568;
    margin-bottom: 14px;
  }

  .k-buttons {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
  }
  .k-btn {
    background: #111827;
    border: 1px solid #1e2d3d;
    color: #9aa5b8;
    font-size: 10px;
    font-family: monospace;
    letter-spacing: 1px;
    padding: 6px 14px;
    border-radius: 999px;
    cursor: pointer;
    transition: all 0.2s;
  }
  .k-btn:hover { border-color: #4ade80; color: #4ade80; }

  .k-state-display {
    margin-top: 14px;
    font-family: monospace;
    font-size: 11px;
    color: #7a8399;
    min-height: 18px;
    font-style: italic;
  }
  .k-state-display span { color: #4ade80; }

  /* ── INSIGHT BOX ── */
  .insight {
    grid-column: 1 / -1;
    background: #0d1f17;
    border-left: 3px solid #4ade80;
    border-radius: 0 12px 12px 0;
    padding: 14px 18px;
    font-size: 12px;
    color: #9aa5b8;
    line-height: 1.7;
  }
  .insight strong { color: #4ade80; font-family: monospace; }
</style>
</head>
<body>
<div class="demo-wrapper">

  <!-- SWITCH PANEL -->
  <div class="panel">
    <div class="panel-label">Physical Binary</div>
    <div class="panel-title">The Switch</div>
    <div class="switch-scene">
      <div class="switch-body" onclick="toggleSwitch()" id="switchBody">
        <div class="switch-pip top" id="pipTop"></div>
        <div class="switch-pip bottom" id="pipBottom"></div>
      </div>
      <div class="switch-label-row">
        <div class="bit-display off" id="switchBit">0</div>
      </div>
      <div class="certainty-tag certain">CERTAIN · INSTANT</div>
    </div>
  </div>

  <!-- DROP PANEL -->
  <div class="panel">
    <div class="panel-label">Physical Binary</div>
    <div class="panel-title">The Drop</div>
    <div class="drop-scene" onclick="dropBall()" id="dropScene">
      <div class="ball" id="ball"></div>
      <div class="impact-ring" id="impactRing"></div>
      <div class="ground"></div>
      <div class="drop-hint" id="dropHint">TAP TO DROP</div>
    </div>
    <div style="margin-top:10px;">
      <div class="certainty-tag certain" style="display:inline-block">CERTAIN · OBSERVABLE</div>
    </div>
  </div>

  <!-- KNOWLEDGE METER -->
  <div class="knowledge-panel">
    <div class="k-title">Knowledge State — Is 1 really certain?</div>
    <div class="k-sub">MARK YOUR STATE · WATCH WHAT HAPPENS</div>
    <div class="meter-track">
      <div class="meter-fill" id="meterFill" style="width:0%">
        <div class="meter-fuzz" id="meterFuzz"></div>
      </div>
    </div>
    <div class="meter-labels">
      <span>0 · DON'T KNOW YET</span>
      <span>0.5 · THINK I KNOW</span>
      <span>1 · CERTAIN?</span>
    </div>
    <div class="k-buttons">
      <button class="k-btn" onclick="setKnowledge(0)">0 · I don't know it yet</button>
      <button class="k-btn" onclick="setKnowledge(0.3)">I've seen this before</button>
      <button class="k-btn" onclick="setKnowledge(0.6)">I think I know it</button>
      <button class="k-btn" onclick="setKnowledge(0.85)">I'm pretty sure</button>
      <button class="k-btn" onclick="setKnowledge(1.0)">1 · I know it</button>
    </div>
    <div class="k-state-display" id="kStateDisplay">Choose your state above.</div>
  </div>

  <!-- INSIGHT -->
  <div class="insight">
    The switch snaps to <strong>1</strong> — no hesitation, no doubt. The ball hits the ground — physics doesn't negotiate.
    But knowledge? Even at <strong>1</strong>, it wobbles. It's provisional. Open to new information.<br><br>
    <strong>Binary Action</strong> means moving anyway — acting from a <strong>0</strong> state, before certainty arrives.
    Because in learning, the action <em>is</em> how you get to 1.
  </div>

</div>

<script>
  // ── SWITCH ──
  let switchOn = false;
  function toggleSwitch() {
    switchOn = !switchOn;
    const bit = document.getElementById('switchBit');
    const top = document.getElementById('pipTop');
    const bot = document.getElementById('pipBottom');
    bit.textContent = switchOn ? '1' : '0';
    bit.className = switchOn ? 'bit-display on' : 'bit-display off';
    top.className = switchOn ? 'switch-pip top off' : 'switch-pip top';
    bot.className = switchOn ? 'switch-pip bottom on' : 'switch-pip bottom';
  }

  // ── DROP ──
  let dropping = false;
  function dropBall() {
    if (dropping) return;
    dropping = true;
    const ball = document.getElementById('ball');
    const ring = document.getElementById('impactRing');
    const hint = document.getElementById('dropHint');
    const scene = document.getElementById('dropScene');
    const groundY = scene.clientHeight - 31;

    hint.style.opacity = '0';
    ball.style.top = '10px';
    ball.style.transition = 'none';

    setTimeout(() => {
      ball.style.transition = `top ${0.55}s cubic-bezier(0.5, 0, 1, 1)`;
      ball.style.top = groundY + 'px';
    }, 30);

    setTimeout(() => {
      // impact squash
      ball.style.transition = 'all 0.08s';
      ball.style.transform = 'translateX(-50%) scaleX(1.5) scaleY(0.5)';
      ring.style.transition = 'transform 0.4s ease-out, opacity 0.4s ease-out';
      ring.style.transform = 'translateX(-50%) scale(3)';
      ring.style.opacity = '1';
    }, 580);

    setTimeout(() => {
      ball.style.transition = 'all 0.15s';
      ball.style.transform = 'translateX(-50%) scaleX(1) scaleY(1)';
      ring.style.opacity = '0';
      ring.style.transform = 'translateX(-50%) scale(0)';
      hint.style.opacity = '1';
      ball.style.top = '10px';
      dropping = false;
    }, 1100);
  }

  // ── KNOWLEDGE METER ──
  const states = {
    0:    { msg: "Honest. <span>0</span> is where every expert once stood.", w: "0%" },
    0.3:  { msg: "Familiarity isn't knowledge — but it's a start. <span>Binary Action:</span> try a problem anyway.", w: "30%" },
    0.6:  { msg: "You think you know it. But can you explain it? <span>Binary Action:</span> teach it to someone.", w: "62%" },
    0.85: { msg: "Pretty sure — but notice the fuzz at the edge. <span>Binary Action:</span> find the one thing that would break your understanding.", w: "85%" },
    1.0:  { msg: "You marked <span>1</span> — but unlike the switch, knowledge stays open. What would change this?", w: "97%" },
  };

  function setKnowledge(val) {
    const s = states[val];
    const fill = document.getElementById('meterFill');
    const display = document.getElementById('kStateDisplay');
    fill.style.width = s.w;
    display.innerHTML = s.msg;
    // fuzz is always present but more visible near 1
    const fuzz = document.getElementById('meterFuzz');
    fuzz.style.opacity = val >= 0.85 ? '1' : '0.4';
  }
</script>
</body>
</html>
""", height=520, scrolling=False)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# PHASE 1 — BREATH
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="card">
    <div class="card-label">Phase 01 · Breathe</div>
    <h3>Before you think — just breathe.</h3>
    <p>
        In binary, everything starts at <strong style="color:#4ade80; font-family:'Space Mono',monospace">0</strong>.
        Zero isn't empty — it's <em>ready</em>. Right now, your mind is at zero.
        That's exactly where we want to be.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="breath-container">
    <div class="breath-circle">0 → 1</div>
    <div class="breath-label">INHALE · HOLD · RELEASE</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="background:#0d1117; border-radius:12px; padding:1.2rem 1.5rem; margin-bottom:1.5rem; border:1px solid #1e2d3d;">
<p style="color:#9aa5b8; font-size:0.9rem; line-height:1.9; margin:0;">
🫁 &nbsp;<strong style="color:#e8eaf0">Inhale</strong> for 4 counts &nbsp;·&nbsp;
<strong style="color:#e8eaf0">Hold</strong> for 4 counts &nbsp;·&nbsp;
<strong style="color:#e8eaf0">Exhale</strong> for 6 counts<br>
<span style="font-family:'Space Mono',monospace; font-size:0.75rem; color:#4ade80; letter-spacing:2px;">Repeat 3× · Do this now before moving forward.</span>
</p>
</div>
""", unsafe_allow_html=True)

breath_confirmed = st.checkbox("✅  I completed my breathing. I'm ready.", key="breath_check")

# ═══════════════════════════════════════════════════════════════════════════════
# PHASE 2 — BINARY SELF-SCAN
# ═══════════════════════════════════════════════════════════════════════════════
if breath_confirmed:
    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <div class="card-label">Phase 02 · Binary Self-Scan</div>
        <h3>Map what you know.</h3>
        <p>
            In the number system (8.NS), there are 8 core concepts.
            For each one, mark your current state:<br><br>
            <strong style="font-family:'Space Mono',monospace; color:#4ade80">1 = I know it</strong> &nbsp;&nbsp;
            <strong style="font-family:'Space Mono',monospace; color:#2a4a3a">0 = Not yet</strong>
            <br><br>
            There are no wrong answers. This is data — not judgment.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="margin-bottom:0.5rem">
        <span style="font-family:'Space Mono',monospace; font-size:0.7rem; color:#4ade80; letter-spacing:3px;">YOUR BINARY KNOWLEDGE STATE</span>
    </div>
    """, unsafe_allow_html=True)

    for i, topic in enumerate(TOPICS):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f'<p style="color:#9aa5b8; font-size:0.9rem; margin:0; padding-top:0.5rem">{i+1}. {topic}</p>', unsafe_allow_html=True)
        with col2:
            val = st.selectbox("", ["0", "1"], key=f"bit_{i}", label_visibility="collapsed")
            st.session_state.knowledge_bits[i] = int(val)

    bits = st.session_state.knowledge_bits
    decimal_val = bits_to_decimal(bits)
    ones_count = sum(bits)

    colored_bits = ""
    for b in bits:
        if b == 1:
            colored_bits += f'<span style="color:#4ade80">{b}</span>'
        else:
            colored_bits += f'<span style="color:#2a3a2a">{b}</span>'

    st.markdown(f"""
    <div style="background:#0d1117; border:1px solid #1e2d3d; border-radius:12px; padding:1.5rem; text-align:center; margin:1.5rem 0;">
        <div style="font-family:'Space Mono',monospace; font-size:2rem; letter-spacing:8px; margin-bottom:0.5rem">{colored_bits}</div>
        <div style="font-family:'Space Mono',monospace; font-size:0.7rem; color:#4a5568; letter-spacing:3px">= {decimal_val} in decimal · {ones_count}/8 concepts lit</div>
    </div>
    """, unsafe_allow_html=True)

    affirmation = AFFIRMATIONS[min(ones_count, 7)]
    st.markdown(f"""
    <div style="border-left:3px solid #4ade80; padding:0.8rem 1.2rem; background:#0d1f17; border-radius:0 10px 10px 0; margin-bottom:1.5rem;">
        <p style="color:#4ade80; font-size:0.95rem; font-style:italic; margin:0">"{affirmation}"</p>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# PHASE 3 — INTROSPECTION
# ═══════════════════════════════════════════════════════════════════════════════
    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <div class="card-label">Phase 03 · Introspection</div>
        <h3>One honest thought.</h3>
        <p>
            Look at your binary state above. Choose <em>one</em> concept where you marked <strong style="font-family:'Space Mono',monospace; color:#2a4a3a">0</strong>.
            What do you think is blocking the signal?
        </p>
    </div>
    """, unsafe_allow_html=True)

    prompts = [
        "Which concept feels most like a closed door right now — and why?",
        "What story are you telling yourself about the zeros in your scan?",
        "If a 0 could speak, what would it say it needs from you this week?",
        "What's the smallest step that could flip one 0 to a 1 this week?",
    ]
    week_num = datetime.date.today().isocalendar()[1]
    prompt = prompts[(week_num - 1) % len(prompts)]

    st.markdown(f"""
    <div class="reflection-header">This week's prompt:</div>
    <div class="reflection-sub">"{prompt}"</div>
    """, unsafe_allow_html=True)

    reflection = st.text_area(
        "",
        placeholder="Write freely. This is for you, not a grade.",
        height=130,
        key="reflection_input",
        label_visibility="collapsed"
    )

# ═══════════════════════════════════════════════════════════════════════════════
# PHASE 4 — INTENTION
# ═══════════════════════════════════════════════════════════════════════════════
    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <div class="card-label">Phase 04 · Intention</div>
        <h3>Set your signal for the week.</h3>
        <p>
            Binary systems work because every bit has a job.
            This week, <em>you</em> are a bit in the system.
            What is your signal going to be?
        </p>
    </div>
    """, unsafe_allow_html=True)

    intention_options = [
        "I will ask one question I've been afraid to ask.",
        "I will try a problem even if I don't know the answer.",
        "I will help someone else flip a 0 to a 1.",
        "I will sit with confusion instead of quitting.",
        "I will notice when I say 'I can't' and replace it.",
        "I will review one concept I marked 0 this week.",
    ]

    intention = st.selectbox(
        "Choose your intention — or type your own below:",
        [""] + intention_options,
        key="intention_select",
    )

    custom_intention = st.text_input(
        "Or write your own intention:",
        placeholder="This week I will...",
        key="custom_intention",
    )

    final_intention = custom_intention if custom_intention else intention

    if final_intention and final_intention != "":
        st.markdown(f"""
        <div style="background:#0d1f17; border:1px solid #4ade80; border-radius:12px; padding:1.2rem 1.5rem; margin:1rem 0;">
            <div style="font-family:'Space Mono',monospace; font-size:0.65rem; color:#4ade80; letter-spacing:3px; margin-bottom:0.4rem">YOUR SIGNAL THIS WEEK</div>
            <div style="font-size:1rem; color:#e8eaf0;">📡 &nbsp;{final_intention}</div>
        </div>
        """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# PHASE 5 — LOCK IT IN
# ═══════════════════════════════════════════════════════════════════════════════
    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("LOCK IN MY WEEK →", key="lock_in"):
            entry = {
                "date": datetime.date.today().strftime("%b %d, %Y"),
                "week": get_week_label(),
                "binary": binary_string(st.session_state.knowledge_bits),
                "decimal": bits_to_decimal(st.session_state.knowledge_bits),
                "ones": sum(st.session_state.knowledge_bits),
                "reflection": reflection[:120] + "..." if len(reflection) > 120 else reflection,
                "intention": final_intention,
            }
            st.session_state.weekly_log.insert(0, entry)
            st.balloons()
            st.success("✅ Week locked in. Your binary state is saved.")

# ═══════════════════════════════════════════════════════════════════════════════
# PHASE 6 — LONG TERM LOG
# ═══════════════════════════════════════════════════════════════════════════════
    if st.session_state.weekly_log:
        st.markdown('<hr class="divider">', unsafe_allow_html=True)
        st.markdown('<div class="card-label" style="margin-bottom:1rem">Long-Term Practice · Your Binary Journey</div>', unsafe_allow_html=True)

        for entry in st.session_state.weekly_log:
            ones = entry["ones"]
            bar = "█" * ones + "░" * (8 - ones)
            st.markdown(f"""
            <div class="log-entry">
                <div class="log-date">{entry['date']} · {entry['week']}</div>
                <div style="font-family:'Space Mono',monospace; font-size:0.85rem; color:#4ade80; letter-spacing:4px; margin:0.4rem 0">{entry['binary']} = {entry['decimal']}</div>
                <div style="font-family:'Space Mono',monospace; font-size:0.75rem; color:#2a5a3a; letter-spacing:2px">{bar} {ones}/8</div>
                {f'<div class="log-text">"{entry["intention"]}"</div>' if entry.get("intention") else ""}
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        <div style="text-align:center; padding:1rem 0;">
            <p style="font-family:'Space Mono',monospace; font-size:0.7rem; color:#4a5568; letter-spacing:2px;">
                TRACK YOUR BITS OVER TIME · WATCH YOUR DECIMAL RISE
            </p>
        </div>
        """, unsafe_allow_html=True)

else:
    st.markdown("""
    <div style="background:#0d1117; border:1px dashed #1e2d3d; border-radius:12px; padding:2rem; text-align:center; margin-top:1rem;">
        <p style="font-family:'Space Mono',monospace; font-size:0.75rem; color:#4a5568; letter-spacing:3px;">
            PHASES 02–04 UNLOCK AFTER BREATHING
        </p>
        <p style="color:#2a4a3a; font-size:2rem; letter-spacing:8px; font-family:'Space Mono',monospace">0 0 0 0 0 0 0 0</p>
    </div>
    """, unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; padding:3rem 0 1rem; border-top:1px solid #1e2d3d; margin-top:3rem;">
    <p style="font-family:'Space Mono',monospace; font-size:0.65rem; color:#2a3a2a; letter-spacing:3px;">
        COGNITIVECLOUD.AI · XAVIER HONABLUE M.ED · 8.NS · BINARY MIND
    </p>
</div>
""", unsafe_allow_html=True)
