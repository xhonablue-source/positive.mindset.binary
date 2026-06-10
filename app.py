import streamlit as st
import io
import requests

# --- Page Configuration ---
st.set_page_config(
    page_title="CognitiveCloud.ai: Growth Mindset Explorer",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS ---
st.markdown("""
<style>
    body {
        font-family: 'Inter', sans-serif;
        background-color: #F8F7F4;
        color: #333333;
    }
    .main-header {
        text-align: center;
        color: #6A0572;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .sub-header {
        text-align: center;
        color: #4B0082;
        font-size: 1.8rem;
        margin-bottom: 2rem;
    }
    .section-header {
        color: #005A9C;
        font-size: 2.2rem;
        font-weight: bold;
        margin-top: 2.5rem;
        margin-bottom: 1.5rem;
        border-bottom: 2px solid #E0E0E0;
        padding-bottom: 0.5rem;
    }
    .card {
        background-color: #FFFFFF;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        margin-bottom: 1.5rem;
        border: 1px solid #E0E0E0;
    }
    .highlight-box {
        background-color: #E8F5E9;
        border-left: 5px solid #4CAF50;
        padding: 1rem;
        border-radius: 8px;
        margin-top: 1.5rem;
        margin-bottom: 1.5rem;
    }
    .stButton > button {
        background-color: #005A9C;
        color: white;
        padding: 0.75rem 1.5rem;
        border-radius: 25px;
        font-weight: bold;
        transition: background-color 0.3s ease;
        cursor: pointer;
        border: none;
        margin-top: 10px;
    }
    .stButton > button:hover {
        background-color: #004070;
    }
</style>
""", unsafe_allow_html=True)

# --- Header ---
col1, col2 = st.columns([1, 4])
with col1:
    try:
        st.image("https://placehold.co/80x80/6A0572/FFFFFF?text=CC", width=80)
    except:
        st.markdown("🌱")

with col2:
    st.markdown("### www.cognitivecloud.ai")
    st.markdown("**Developed by Xavier Honablue M.Ed**")

st.markdown("---")

st.markdown('<h1 class="main-header">🌱 CognitiveCloud.ai: Growth Mindset Explorer</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Unlock Your Potential: Embrace Challenges, Learn from Mistakes, and Grow!</p>', unsafe_allow_html=True)

# --- Welcome Card with Quotes ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<h2 class="section-header">Welcome, Future Achiever!</h2>', unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 1.1rem;'>Your abilities grow with effort, mistakes, and perseverance. Let these voices guide your journey:</p>
<div class="highlight-box">
    <p style='font-weight: bold; color: #388E3C;'>"The power of 'not yet'!" - Carol Dweck</p>
    <p style='color: #4CAF50;'>Instead of saying "I can't do it," try "I can't do it *yet*!" This simple shift opens up possibilities for learning and improvement.</p>
</div>
<div class="highlight-box">
    <p style='font-weight: bold; color: #388E3C;'>"Success is not to be measured by where you stand in life, but by the obstacles you have overcome." - Booker T. Washington</p>
    <p style='color: #4CAF50;'>This powerful quote reminds us that true achievement comes from facing and conquering difficulties, not just from natural talent. Every challenge you overcome builds your capacity for future success.</p>
</div>
<div class="highlight-box">
    <p style='font-weight: bold; color: #388E3C;'>"The tragedy of life is not that it ends so soon, but that we wait so long to begin it." - Benjamin Elijah Mays</p>
    <p style='color: #4CAF50;'>Dr. Mays' words encourage us to seize the moment, embrace learning, and start pursuing our potential now, without hesitation or fear of failure. Every day is an opportunity to grow!</p>
</div>
<div class="highlight-box">
    <p style='font-weight: bold; color: #388E3C;'>"Invest in the human soul. Who knows, it might be a diamond in the rough." - Mary McLeod Bethune</p>
    <p style='color: #4CAF50;'>Mary McLeod Bethune's inspiring words highlight the immense, often hidden, potential within each individual, encouraging us to nurture and believe in our own and others' capacity for greatness.</p>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- Common Core Connections Section ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<h2 class="section-header">Connections to Common Core Standards</h2>', unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 1.1rem; line-height: 1.6;'>
    A growth mindset is a powerful tool that supports learning across all subjects and grade levels.
    While not a specific content standard, fostering a growth mindset directly impacts students' ability to meet and exceed Common Core State Standards (CCSS) in various disciplines.
</p>
<ul style='font-size:1rem; line-height:1.8;'>
    <li><strong>Mathematics (CCSS.Math.Practice.MP1-8):</strong> The Standards for Mathematical Practice emphasize problem-solving, perseverance, reasoning, and precision. A growth mindset directly cultivates these practices by encouraging students to make sense of problems and persevere (MP1), reason abstractly (MP2), and attend to precision (MP6).</li>
    <li><strong>English Language Arts (CCSS.ELA-Literacy):</strong> A growth mindset helps students read closely and make logical inferences (R.CCR.1) and embrace the iterative process of drafting, revising, and editing (W.CCR.4).</li>
    <li><strong>Science & Engineering Practices (NGSS):</strong> A growth mindset is essential for scientific inquiry — asking questions (SEP1) and constructing explanations and iterating on designs (SEP6).</li>
</ul>
<p style='font-size: 1.1rem; line-height: 1.6;'>
    By developing a growth mindset, students build the resilience and intellectual curiosity needed to master academic content and thrive in a rapidly changing world.
</p>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# BINARY ACTION — Interactive concept section (replaces Dr. X chat + journal)
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="card">
<h2 class="section-header">⚡ Binary Action — Not All 1s Are the Same</h2>
<p style='font-size: 1.1rem; line-height: 1.7; margin-bottom: 1.5rem;'>
    In physics, binary is <strong>certain</strong>. A switch is on or off. An object hits the ground or it doesn't.
    No interpretation. No doubt.<br><br>
    But <em>knowledge</em> isn't a switch. You can mark yourself a 1 and still be wrong.
    You can mark yourself a 0 and be closer than you think.<br><br>
    <strong>Binary Action</strong> is what happens in that gap —
    acting even when your knowledge state is still 0.
    That move, from uncertainty into action, is where real learning lives.
</p>
</div>
""", unsafe_allow_html=True)

st.components.v1.html("""
<!DOCTYPE html>
<html>
<head>
<style>
  * { margin:0; padding:0; box-sizing:border-box; }
  html, body { background: transparent; font-family: 'Inter', 'Segoe UI', sans-serif; overflow: hidden; height: auto; }

  .demo-wrapper {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    padding: 4px;
  }

  .panel {
    background: #F0F7FF;
    border: 1px solid #BFDBFE;
    border-radius: 14px;
    padding: 20px;
    text-align: center;
  }

  .panel-label {
    font-size: 9px;
    letter-spacing: 3px;
    color: #6B7280;
    text-transform: uppercase;
    margin-bottom: 8px;
    font-family: monospace;
  }

  .panel-title {
    font-size: 14px;
    font-weight: 700;
    color: #1E3A5F;
    margin-bottom: 16px;
  }

  /* ── SWITCH ── */
  .switch-scene {
    height: 150px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 12px;
  }

  .switch-body {
    width: 54px;
    height: 90px;
    background: #E8F0FE;
    border: 2px solid #93C5FD;
    border-radius: 10px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
    padding: 8px 0;
    cursor: pointer;
    transition: border-color 0.2s, box-shadow 0.2s;
  }
  .switch-body:hover { border-color: #005A9C; box-shadow: 0 0 12px rgba(0,90,156,0.2); }

  .switch-pip {
    width: 28px;
    height: 28px;
    border-radius: 6px;
    transition: all 0.15s;
  }
  .switch-pip.top     { background: #EF4444; }
  .switch-pip.top.off { background: #EF4444; border: none; }
  .switch-pip.bottom  { background: #FCA5A5; border: 1px solid #FCA5A5; }
  .switch-pip.bottom.on { background: #4CAF50; border: none; }

  .bit-display {
    font-family: monospace;
    font-size: 32px;
    font-weight: 700;
    transition: color 0.15s;
  }
  .bit-display.on  { color: #4CAF50; }
  .bit-display.off { color: #EF4444; }

  .certainty-tag {
    font-size: 9px;
    letter-spacing: 2px;
    font-family: monospace;
    padding: 3px 10px;
    border-radius: 20px;
    margin-top: 4px;
  }
  .certain   { background: #E8F5E9; color: #388E3C; border: 1px solid #A5D6A7; }
  .uncertain { background: #F3F4F6; color: #9CA3AF; border: 1px solid #E5E7EB; }

  /* ── DROP SCENE ── */
  .drop-scene {
    height: 150px;
    position: relative;
    overflow: hidden;
    cursor: pointer;
    border-radius: 10px;
    background: #EFF6FF;
    border: 1px solid #BFDBFE;
  }
  .ground {
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 3px;
    background: #4CAF50;
    opacity: 0.5;
  }
  .ball {
    width: 28px; height: 28px;
    background: radial-gradient(circle at 35% 35%, #86EFAC, #4CAF50);
    border-radius: 50%;
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    top: 10px;
    box-shadow: 0 4px 12px rgba(76,175,80,0.35);
    transition: background 0.15s, box-shadow 0.15s;
  }
  .ball.hit {
    background: radial-gradient(circle at 35% 35%, #FCA5A5, #EF4444);
    box-shadow: 0 4px 12px rgba(239,68,68,0.45);
  }
  .impact-ring {
    position: absolute;
    bottom: 3px; left: 50%;
    transform: translateX(-50%) scale(0);
    width: 40px; height: 12px;
    border: 2px solid #EF4444;
    border-radius: 50%;
    opacity: 0;
  }
  .drop-hint {
    position: absolute;
    bottom: 10px; left: 0; right: 0;
    text-align: center;
    font-size: 9px;
    letter-spacing: 2px;
    color: #9CA3AF;
    font-family: monospace;
  }

  /* ── KNOWLEDGE METER ── */
  .knowledge-panel {
    grid-column: 1 / -1;
    background: #FFFBEB;
    border: 1px solid #FDE68A;
    border-radius: 14px;
    padding: 20px 24px;
  }
  .k-title { font-size: 14px; font-weight: 700; color: #1E3A5F; margin-bottom: 4px; }
  .k-sub   { font-size: 10px; color: #9CA3AF; margin-bottom: 16px; font-family: monospace; letter-spacing: 1px; }

  .meter-track {
    height: 12px;
    background: #E5E7EB;
    border-radius: 999px;
    position: relative;
    overflow: visible;
    margin-bottom: 8px;
  }
  .meter-fill {
    height: 100%;
    border-radius: 999px;
    background: linear-gradient(90deg, #93C5FD, #4CAF50);
    transition: width 0.6s cubic-bezier(.34,1.56,.64,1);
    position: relative;
  }
  .meter-fuzz {
    position: absolute;
    right: -6px; top: -5px;
    width: 22px; height: 22px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(76,175,80,0.5) 0%, transparent 70%);
    animation: fuzz 1.8s ease-in-out infinite;
  }
  @keyframes fuzz {
    0%,100% { transform: scale(1) translateX(0);  opacity: 0.5; }
    33%      { transform: scale(1.4) translateX(2px); opacity: 1;   }
    66%      { transform: scale(0.7) translateX(-2px); opacity: 0.3; }
  }
  .meter-labels {
    display: flex;
    justify-content: space-between;
    font-size: 9px;
    font-family: monospace;
    letter-spacing: 1px;
    color: #9CA3AF;
    margin-bottom: 16px;
  }
  .k-buttons { display: flex; gap: 8px; flex-wrap: wrap; }
  .k-btn {
    background: #FFFFFF;
    border: 1px solid #E5E7EB;
    color: #374151;
    font-size: 11px;
    font-family: 'Inter', sans-serif;
    padding: 7px 14px;
    border-radius: 999px;
    cursor: pointer;
    transition: all 0.2s;
  }
  .k-btn:hover { border-color: #005A9C; color: #005A9C; background: #EFF6FF; }

  .k-state-display {
    margin-top: 14px;
    font-size: 12px;
    color: #6B7280;
    min-height: 20px;
    font-style: italic;
    line-height: 1.6;
  }
  .k-state-display strong { color: #005A9C; }

  /* ── INSIGHT ── */
  .insight {
    grid-column: 1 / -1;
    background: #E8F5E9;
    border-left: 5px solid #4CAF50;
    border-radius: 0 12px 12px 0;
    padding: 16px 20px;
    font-size: 13px;
    color: #374151;
    line-height: 1.8;
  }
  .insight strong { color: #005A9C; }
</style>
</head>
<body>
<div class="demo-wrapper">

  <!-- SWITCH -->
  <div class="panel">
    <div class="panel-label">Physical Binary</div>
    <div class="panel-title">The Switch</div>
    <div class="switch-scene">
      <div class="switch-body" onclick="toggleSwitch()">
        <div class="switch-pip top" id="pipTop"></div>
        <div class="switch-pip bottom" id="pipBottom"></div>
      </div>
      <div class="bit-display off" id="switchBit">0</div>
      <div class="certainty-tag certain">CERTAIN · INSTANT</div>
    </div>
  </div>

  <!-- DROP -->
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
        <div class="meter-fuzz" id="meterFuzz" style="opacity:0.3"></div>
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
      ball.style.transition = 'top 0.55s cubic-bezier(0.5, 0, 1, 1)';
      ball.style.top = groundY + 'px';
    }, 30);
    setTimeout(() => {
      ball.style.transition = 'all 0.08s';
      ball.style.transform = 'translateX(-50%) scaleX(1.5) scaleY(0.5)';
      ball.classList.add('hit');
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
      ball.classList.remove('hit');
      dropping = false;
    }, 1100);
  }

  const states = {
    0:    { msg: "Honest. <strong>0</strong> is where every expert once stood.", w: "0%" },
    0.3:  { msg: "Familiarity isn't knowledge — but it's a start. <strong>Binary Action:</strong> try a problem anyway.", w: "30%" },
    0.6:  { msg: "You think you know it. But can you explain it? <strong>Binary Action:</strong> teach it to someone.", w: "62%" },
    0.85: { msg: "Pretty sure — but notice the fuzz at the edge. <strong>Binary Action:</strong> find the one thing that would break your understanding.", w: "85%" },
    1.0:  { msg: "You marked <strong>1</strong> — but unlike the switch, knowledge stays open. What would change this?", w: "97%" },
  };

  function setKnowledge(val) {
    const s = states[val];
    document.getElementById('meterFill').style.width = s.w;
    document.getElementById('kStateDisplay').innerHTML = s.msg;
    document.getElementById('meterFuzz').style.opacity = val >= 0.85 ? '1' : '0.3';
  }
</script>
</body>
</html>
""", height=520, scrolling=False)

# --- Grow Your Brain Section ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<h2 class="section-header">Grow Your Brain, Shape Your Future!</h2>', unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 1.1rem; line-height: 1.6;'>
    Your brain is like a muscle — the more you challenge it and learn from your experiences, the stronger it gets!
    This growth mindset isn't just for school; it's a superpower for life.
    It helps you tackle new technologies, solve complex problems, and innovate in fields like:
</p>
<ul style='font-size:1rem; line-height:2;'>
    <li><strong>Artificial Intelligence & Machine Learning:</strong> Learning new algorithms and debugging code.</li>
    <li><strong>Biotechnology & Medicine:</strong> Discovering new treatments and understanding complex biological systems.</li>
    <li><strong>Engineering & Robotics:</strong> Designing, building, and refining innovative solutions.</li>
    <li><strong>Creative Arts & Design:</strong> Pushing boundaries and developing unique styles.</li>
</ul>
<p style='font-size: 1.1rem; line-height: 1.6;'>
    Every time you persist, every time you learn from a mistake, you're building the skills you'll need to excel in these future-forward careers!
</p>
<div class="highlight-box">
    <p style='font-weight: bold; color: #388E3C;'>Remember: Consistency is key to growth! You've got this! 💪</p>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- Footer ---
st.markdown("---")
st.markdown("""
<div style="text-align: center; margin-top: 2rem; color: #666;">
    <p>💡 <strong>Empowering Young Minds in STEAM</strong></p>
    <p>Developed by Xavier Honablue M.Ed for CognitiveCloud.ai Education</p>
</div>
""", unsafe_allow_html=True)
