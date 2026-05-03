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

# ---------- FULL SCREEN SPINNING NAME + FALLING STARS ----------
st.markdown(f"""
<style>
    /* Remove all default Streamlit padding/margins */
    .main .block-container {{
        padding: 0rem;
        max-width: 100%;
    }}
    .stApp {{
        background: linear-gradient(135deg, #0a0f2a, #0a1a3a);
        margin: 0;
        padding: 0;
        height: 100vh;
        overflow: hidden;
    }}
    /* Full-screen container that truly centers both axes */
    .fullscreen {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        z-index: 10;
        text-align: center;
        pointer-events: none;
    }}
    /* Spinning name – perfectly centered */
    .spinning-name {{
        font-size: 3.5rem;
        font-weight: bold;
        font-family: 'Poppins', 'Segoe UI', sans-serif;
        background: linear-gradient(135deg, #FFD700, #FFB347);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        display: inline-block;
        animation: spin 4s linear infinite;
        text-shadow: 0 0 20px rgba(255,215,0,0.6);
        white-space: nowrap;
        margin: 0 auto;
    }}
    @keyframes spin {{
        0% {{ transform: rotate(0deg); }}
        100% {{ transform: rotate(360deg); }}
    }}
    /* Tagline below the spinning name */
    .tagline {{
        font-size: 1.8rem;
        color: #FFD966;
        text-align: center;
        font-family: 'Poppins', sans-serif;
        margin-top: 2rem;
        background: rgba(0,0,0,0.4);
        padding: 0.5rem 1.5rem;
        border-radius: 50px;
        backdrop-filter: blur(4px);
        pointer-events: none;
    }}
    /* Contact info fixed at bottom – all YELLOW */
    .contact {{
        position: fixed;
        bottom: 2%;
        left: 50%;
        transform: translateX(-50%);
        text-align: center;
        font-size: 1.1rem;
        background: rgba(0,0,0,0.6);
        padding: 0.8rem 1.5rem;
        border-radius: 30px;
        backdrop-filter: blur(5px);
        white-space: nowrap;
        z-index: 20;
        color: #FFD700;
        pointer-events: auto;
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
        opacity: 0.9;
        animation: fall linear forwards;
        pointer-events: none;
    }}
    @keyframes fall {{
        0% {{ transform: translateY(0) rotate(0deg); opacity: 1; }}
        100% {{ transform: translateY(100vh) rotate(360deg); opacity: 0; }}
    }}
    /* Responsive: smaller font on mobile to fit name */
    @media (max-width: 768px) {{
        .spinning-name {{ font-size: 2.2rem; white-space: normal; }}
        .tagline {{ font-size: 1.2rem; }}
        .contact {{ font-size: 0.8rem; white-space: normal; width: 90%; }}
    }}
    @media (max-width: 480px) {{
        .spinning-name {{ font-size: 1.8rem; }}
    }}
</style>

<div class="fullscreen">
    <div class="spinning-name">✨ Gesner Deslandes ✨</div>
    <div class="tagline">⭐ your best choice of programmer solution ⭐</div>
</div>

<div class="contact">
    📞 <strong>Phone:</strong> {PHONE} &nbsp;&nbsp;|&nbsp;&nbsp;
    ✉️ <strong>Email:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a>
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
