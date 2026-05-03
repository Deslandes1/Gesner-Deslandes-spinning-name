import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Gesner Deslandes | Best Programmer Solution",
    page_icon="⭐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- YOUR CONTACT INFO ----------
PHONE = "(509)-47385663"
EMAIL = "deslandes78@gmail.com"

# ---------- CUSTOM CSS/JS FOR CIRCULAR MOVEMENT + FALLING STARS ----------
st.markdown(f"""
<style>
    /* Remove default Streamlit padding/margins for full-screen effect */
    .main .block-container {{
        padding-top: 0rem;
        padding-bottom: 0rem;
        max-width: 100%;
    }}
    .stApp {{
        background: linear-gradient(135deg, #0a0f2a, #0a1a3a);
        overflow: hidden;
        height: 100vh;
        margin: 0;
        padding: 0;
    }}
    /* Container that covers the whole screen */
    .fullscreen-container {{
        position: relative;
        width: 100vw;
        height: 100vh;
        overflow: hidden;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }}
    /* Moving name - circular path, always upright */
    .moving-name {{
        position: absolute;
        font-size: 3.5rem;
        font-weight: bold;
        font-family: 'Poppins', 'Segoe UI', sans-serif;
        background: linear-gradient(135deg, #FFD700, #FFB347);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        text-shadow: 0 0 15px rgba(255,215,0,0.6);
        white-space: nowrap;
        animation: circleMove 12s linear infinite;
        z-index: 10;
    }}
    @keyframes circleMove {{
        0% {{ top: 10%; left: 10%; transform: translate(0, 0); }}
        25% {{ top: 10%; left: 80%; transform: translate(0, 0); }}
        50% {{ top: 80%; left: 80%; transform: translate(0, 0); }}
        75% {{ top: 80%; left: 10%; transform: translate(0, 0); }}
        100% {{ top: 10%; left: 10%; transform: translate(0, 0); }}
    }}
    /* Tagline below the moving name? Actually we show it fixed at bottom */
    .tagline {{
        position: fixed;
        bottom: 15%;
        left: 0;
        right: 0;
        text-align: center;
        font-size: 1.8rem;
        color: #FFD966;
        font-family: 'Poppins', sans-serif;
        background: rgba(0,0,0,0.5);
        padding: 12px;
        border-radius: 50px;
        width: fit-content;
        margin: 0 auto;
        backdrop-filter: blur(5px);
        z-index: 15;
        pointer-events: none;
    }}
    /* Contact info fixed at bottom */
    .contact {{
        position: fixed;
        bottom: 2%;
        left: 0;
        right: 0;
        text-align: center;
        font-size: 1.1rem;
        background: rgba(0,0,0,0.6);
        padding: 0.8rem;
        border-radius: 30px;
        backdrop-filter: blur(5px);
        width: 90%;
        margin: 0 auto;
        z-index: 15;
    }}
    .contact a {{
        color: #FFD700;
        text-decoration: none;
        font-weight: bold;
    }}
    /* Falling stars container */
    .star-container {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 5;
        overflow: hidden;
    }}
    .falling-star {{
        position: absolute;
        color: gold;
        font-size: 1.2rem;
        opacity: 0.8;
        animation: fall linear forwards;
        pointer-events: none;
    }}
    @keyframes fall {{
        0% {{ transform: translateY(0) rotate(0deg); opacity: 1; }}
        100% {{ transform: translateY(100vh) rotate(360deg); opacity: 0; }}
    }}
</style>

<div class="fullscreen-container">
    <div class="moving-name">✨ Gesner Deslandes ✨</div>
    <div class="tagline">⭐ your best choice of programmer solution ⭐</div>
    <div class="contact">
        📞 <strong>Phone:</strong> {PHONE} &nbsp;&nbsp;|&nbsp;&nbsp;
        ✉️ <strong>Email:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a>
    </div>
</div>

<div id="starField" class="star-container"></div>

<script>
    function createStar() {{
        const star = document.createElement('div');
        star.innerHTML = '⭐';
        star.classList.add('falling-star');
        const leftPos = Math.random() * window.innerWidth;
        const duration = 2 + Math.random() * 3;
        star.style.left = leftPos + 'px';
        star.style.fontSize = (0.8 + Math.random() * 1.5) + 'rem';
        star.style.animationDuration = duration + 's';
        document.getElementById('starField').appendChild(star);
        setTimeout(() => {{
            star.remove();
        }}, duration * 1000);
    }}
    setInterval(createStar, 200);
</script>
""", unsafe_allow_html=True)

# No extra Streamlit elements needed – everything is in custom HTML
