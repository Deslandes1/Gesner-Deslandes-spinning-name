import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Gesner Deslandes | GlobalInternet.py",
    page_icon="⭐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- YOUR CONTACT INFO ----------
PHONE = "(509)-47385663"
EMAIL = "deslandes78@gmail.com"
WEBSITE = "https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/"

# ---------- FULL SCREEN SPINNING NAME + FALLING STARS + DESCRIPTION ----------
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
    /* Full-screen container for central content */
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
        overflow-y: auto;  /* allow scrolling if content overflows (safe) */
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
    /* Tagline below spinning name */
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
    /* Description card – new content */
    .description-card {{
        max-width: 800px;
        margin-top: 2rem;
        background: rgba(0,0,0,0.6);
        backdrop-filter: blur(8px);
        border-radius: 20px;
        padding: 1.5rem;
        text-align: left;
        color: #f0f0f0;
        font-family: 'Poppins', sans-serif;
        pointer-events: auto;
        border-left: 4px solid #FFD700;
    }}
    .description-card h3 {{
        color: #FFD700;
        margin-top: 0;
        text-align: center;
    }}
    .description-card ul {{
        margin: 0.5rem 0;
        padding-left: 1.5rem;
    }}
    .description-card li {{
        margin: 0.5rem 0;
    }}
    .website-link {{
        display: inline-block;
        margin-top: 1rem;
        background: #FFD700;
        color: #0a0f2a;
        text-decoration: none;
        padding: 0.5rem 1rem;
        border-radius: 30px;
        font-weight: bold;
        transition: 0.2s;
    }}
    .website-link:hover {{
        background: #FFB347;
        transform: scale(1.02);
    }}
    /* Contact info fixed at bottom – yellow */
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
    /* Responsive */
    @media (max-width: 768px) {{
        .spinning-name {{ font-size: 2.2rem; white-space: normal; }}
        .tagline {{ font-size: 1.2rem; }}
        .description-card {{ margin: 1rem; padding: 1rem; }}
        .contact {{ font-size: 0.8rem; white-space: normal; width: 90%; }}
    }}
    @media (max-width: 480px) {{
        .spinning-name {{ font-size: 1.8rem; }}
        .description-card {{ font-size: 0.9rem; }}
    }}
</style>

<div class="fullscreen">
    <div class="spinning-name">✨ Gesner Deslandes ✨</div>
    <div class="tagline">⭐ your best choice of programmer solution ⭐</div>

    <!-- GlobalInternet.py description card -->
    <div class="description-card">
        <h3>🌍 GlobalInternet.py</h3>
        <p><strong>Founded by Gesner Deslandes</strong> – owner, founder, and lead engineer.<br>
        We build Python‑based software on demand for clients worldwide. Like Silicon Valley, but with a Haitian touch and outstanding outcomes.</p>
        <ul>
            <li>🧠 <strong>AI‑powered solutions</strong> – chatbots, data analysis, automation</li>
            <li>🗳️ <strong>Complete election & voting systems</strong> – secure, multi‑language, real‑time</li>
            <li>🌐 <strong>Web applications</strong> – dashboards, internal tools, online platforms</li>
            <li>📦 <strong>Full package delivery</strong> – we email you the complete code and guide you through installation</li>
        </ul>
        <p>Whether you need a company website, a custom software tool, or a full‑scale online platform – we build it, you own it.</p>
        <div style="text-align: center;">
            <a href="{WEBSITE}" target="_blank" class="website-link">🔗 Visit our website →</a>
        </div>
    </div>
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
