import streamlit as st
import time
import datetime

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

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 1.5rem 4rem; max-width: 720px; }

/* ── Binary background pulse ── */
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

/* ── Header ── */
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

/* ── Week badge ── */
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

/* ── Cards ── */
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
.card h3 {
    font-size: 1.25rem;
    font-weight: 600;
    color: #ffffff;
    margin-bottom: 0.5rem;
}
.card p {
    color: #9aa5b8;
    font-size: 0.95rem;
    line-height: 1.7;
}

/* ── Breath circle ── */
.breath-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2rem 0;
}
.breath-circle {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    background: radial-gradient(circle, #1a4a2a 0%, #0d1f17 60%, #0a0e1a 100%);
    border: 2px solid #4ade80;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Space Mono', monospace;
    font-size: 0.8rem;
    color: #4ade80;
    animation: breathe 8s ease-in-out infinite;
    box-shadow: 0 0 30px rgba(74,222,128,0.15);
    margin-bottom: 1rem;
}
@keyframes breathe {
    0%,100% { transform: scale(1); box-shadow: 0 0 20px rgba(74,222,128,0.1); }
    50% { transform: scale(1.4); box-shadow: 0 0 50px rgba(74,222,128,0.35); }
}
.breath-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 2px;
    color: #4ade80;
    animation: breathe-text 8s ease-in-out infinite;
}
@keyframes breathe-text {
    0%,100% { opacity: 0.5; content: "BREATHE IN"; }
    50% { opacity: 1; }
}

/* ── Binary meter ── */
.binary-meter {
    font-family: 'Space Mono', monospace;
    font-size: 1.4rem;
    letter-spacing: 6px;
    text-align: center;
    margin: 1rem 0;
    color: #4ade80;
}
.binary-meter .zero { color: #2a3a2a; }

/* ── Reflection box ── */
.reflection-header {
    font-size: 1.05rem;
    font-weight: 600;
    color: #e8eaf0;
    margin-bottom: 0.4rem;
}
.reflection-sub {
    font-size: 0.85rem;
    color: #7a8399;
    margin-bottom: 1rem;
    font-style: italic;
}

/* ── State toggle ── */
.state-row {
    display: flex;
    gap: 1rem;
    margin: 1rem 0;
}
.state-card-0 {
    flex: 1;
    background: #0d1117;
    border: 2px solid #2a3a2a;
    border-radius: 12px;
    padding: 1.2rem;
    text-align: center;
}
.state-card-0 .bit { font-family:'Space Mono',monospace; font-size:2rem; color:#2a3a2a; }
.state-card-0 .state-label { font-size:0.8rem; color:#4a5568; margin-top:0.3rem; }

.state-card-1 {
    flex: 1;
    background: #0d1f17;
    border: 2px solid #4ade80;
    border-radius: 12px;
    padding: 1.2rem;
    text-align: center;
    box-shadow: 0 0 20px rgba(74,222,128,0.1);
}
.state-card-1 .bit { font-family:'Space Mono',monospace; font-size:2rem; color:#4ade80; }
.state-card-1 .state-label { font-size:0.8rem; color:#4ade80; margin-top:0.3rem; }

/* ── Progress log ── */
.log-entry {
    border-left: 2px solid #4ade80;
    padding: 0.6rem 1rem;
    margin-bottom: 0.75rem;
    background: #0d1117;
    border-radius: 0 8px 8px 0;
}
.log-date { font-family:'Space Mono',monospace; font-size:0.65rem; color:#4ade80; letter-spacing:2px; }
.log-text { font-size:0.9rem; color:#9aa5b8; margin-top:0.2rem; }

/* ── Divider ── */
.divider {
    border: none;
    border-top: 1px solid #1e2d3d;
    margin: 2rem 0;
}

/* ── Streamlit widget overrides ── */
.stTextArea textarea {
    background: #0d1117 !important;
    border: 1px solid #1e2d3d !important;
    color: #e8eaf0 !important;
    border-radius: 10px !important;
    font-family: 'Space Grotesk', sans-serif !important;
}
.stSlider > div > div { background: #1e2d3d !important; }
.stButton > button {
    background: #4ade80 !important;
    color: #0a0e1a !important;
    border: none !important;
    border-radius: 999px !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.75rem !important;
    letter-spacing: 2px !important;
    padding: 0.6rem 2rem !important;
    font-weight: 700 !important;
}
.stButton > button:hover { background: #86efac !important; }
.stSelectbox > div > div {
    background: #0d1117 !important;
    border: 1px solid #1e2d3d !important;
    color: #e8eaf0 !important;
    border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)

# ── Session state init ────────────────────────────────────────────────────────
if "step" not in st.session_state:
    st.session_state.step = 0
if "weekly_log" not in st.session_state:
    st.session_state.weekly_log = []
if "breath_done" not in st.session_state:
    st.session_state.breath_done = False
if "knowledge_bits" not in st.session_state:
    st.session_state.knowledge_bits = [0] * 8
if "reflection" not in st.session_state:
    st.session_state.reflection = ""

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

    # Live binary display
    bits = st.session_state.knowledge_bits
    binary_str = binary_string(bits)
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

    # Affirmation based on ones count
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
        label_visibility="visible"
    )

    custom_intention = st.text_input(
        "Or write your own intention:",
        placeholder="This week I will...",
        key="custom_intention",
        label_visibility="visible"
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
        st.markdown("""
        <div class="card-label" style="margin-bottom:1rem">Long-Term Practice · Your Binary Journey</div>
        """, unsafe_allow_html=True)

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
    # Teaser for locked phases
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
