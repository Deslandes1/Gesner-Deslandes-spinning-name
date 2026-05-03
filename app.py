import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Gesner Deslandes | Best Programmer Solution",
    page_icon="⭐",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------- CONTACT INFO (EDIT WITH YOUR REAL DETAILS) ----------
PHONE = "+509 1234 5678"          # <-- Replace with your actual phone number
EMAIL = "gesner@example.com"      # <-- Replace with your actual email

# ---------- CUSTOM HTML/CSS/JS FOR SPINNING TEXT & FALLING STARS ----------
st.markdown(f"""
<style>
    /* Full screen background (dark, makes stars and text pop) */
    .stApp {{
        background: linear-gradient(135deg, #0a0f2a, #0a1a3a);
        color: white;
    }}
    /* Container for the spinning name */
    .spinner-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        height: 60vh;
        flex-direction: column;
    }}
    /* Spinning text style */
    .spinning-name {{
        font-size: 4rem;
        font-weight: bold;
        font-family: 'Poppins', 'Segoe UI', sans-serif;
        background: linear-gradient(135deg, #FFD700, #FFB347);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        display: inline-block;
        animation: spin 4s linear infinite;
        text-shadow: 0 0 10px rgba(255,215,0,0.5);
        margin-bottom: 1rem;
    }}
    @keyframes spin {{
        0% {{ transform: rotate(0deg); }}
        100% {{ transform: rotate(360deg); }}
    }}
    /* Tagline style */
    .tagline {{
        font-size: 1.5rem;
        color: #FFD966;
        text-align: center;
        letter-spacing: 1px;
        font-family: 'Poppins', sans-serif;
        margin-top: 20px;
        border-top: 2px solid gold;
        padding-top: 20px;
        display: inline-block;
    }}
    /* Contact info style */
    .contact {{
        margin-top: 3rem;
        text-align: center;
        font-size: 1.2rem;
        background: rgba(0,0,0,0.5);
        padding: 1rem;
        border-radius: 30px;
        backdrop-filter: blur(5px);
    }}
    .contact a {{
        color: #FFD700;
        text-decoration: none;
        font-weight: bold;
    }}
    /* Fixed area for falling stars (canvas-like) */
    .star-container {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 999;
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

<div class="spinner-container">
    <div class="spinning-name">Gesner Deslandes</div>
    <div class="tagline">⭐ your best choice of programmer solution ⭐</div>
</div>

<div class="contact">
    📞 <strong>Phone:</strong> {PHONE} &nbsp;&nbsp;|&nbsp;&nbsp;
    ✉️ <strong>Email:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a>
</div>

<div id="starField" class="star-container"></div>

<script>
    // Function to create a falling star
    function createStar() {{
        const star = document.createElement('div');
        star.innerHTML = '⭐';
        star.classList.add('falling-star');
        const leftPos = Math.random() * window.innerWidth;
        const duration = 2 + Math.random() * 3; // 2 to 5 seconds
        star.style.left = leftPos + 'px';
        star.style.fontSize = (0.8 + Math.random() * 1.5) + 'rem';
        star.style.animationDuration = duration + 's';
        document.getElementById('starField').appendChild(star);
        // Remove star after animation ends
        setTimeout(() => {{
            star.remove();
        }}, duration * 1000);
    }}

    // Drop stars constantly (every 300ms)
    setInterval(createStar, 300);
</script>
""", unsafe_allow_html=True)

# Optional: footer note
st.markdown("---")
st.caption("✨ Built with Streamlit • Deployed on Streamlit Cloud • Stars keep falling ✨")
