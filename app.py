import streamlit as st

st.set_page_config(
    page_title="Gesner Deslandes | GlobalInternet.py",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

PHONE = "(509)-47385663"
EMAIL = "deslandes78@gmail.com"

st.markdown(f"""
<style>
    .main .block-container {{ padding: 0rem; max-width: 100%; }}
    .stApp {{ margin: 0; padding: 0; height: 100vh; overflow: hidden; background: radial-gradient(circle at center, #01011a, #000000); }}
    canvas {{ position: fixed; top: 0; left: 0; width: 100%; height: 100%; display: block; z-index: 1; }}
    .contact {{
        position: fixed; bottom: 2%; left: 50%; transform: translateX(-50%);
        text-align: center; font-size: 1.1rem; background: rgba(0,0,0,0.7);
        padding: 0.8rem 1.5rem; border-radius: 40px; backdrop-filter: blur(8px);
        white-space: nowrap; z-index: 20; color: #FFD700; font-family: 'Poppins', sans-serif;
        pointer-events: auto; border: 1px solid rgba(255,215,0,0.3);
    }}
    .contact a {{ color: #FFD700; text-decoration: none; font-weight: bold; }}
    @media (max-width: 768px) {{
        .contact {{ font-size: 0.8rem; white-space: normal; width: 90%; text-align: center; }}
    }}
</style>

<canvas id="universeCanvas"></canvas>

<div class="contact">
    📞 <strong>Phone:</strong> {PHONE} &nbsp;&nbsp;|&nbsp;&nbsp;
    ✉️ <strong>Email:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a>
</div>

<script>
    const canvas = document.getElementById('universeCanvas');
    const ctx = canvas.getContext('2d');
    let width, height;
    let earthImg = new Image();
    let earthLoaded = false;
    earthImg.src = 'https://threejs.org/examples/textures/planets/earth_atmos_2048.jpg';
    earthImg.onload = () => {{ earthLoaded = true; }};
    
    let orbitAngle = 0;
    let stars = [];
    const STAR_COUNT = 300;
    
    function resizeCanvas() {{
        width = window.innerWidth;
        height = window.innerHeight;
        canvas.width = width;
        canvas.height = height;
        const minDim = Math.min(width, height);
        window.earthRadius = minDim * 0.12;
        window.textRadius = minDim * 0.22;
    }}
    
    function initStars() {{
        stars = [];
        for (let i = 0; i < STAR_COUNT; i++) {{
            stars.push({{
                x: Math.random() * width,
                y: Math.random() * height,
                radius: Math.random() * 2 + 1,
                alpha: Math.random() * 0.5 + 0.3,
                twinkleSpeed: 0.02 + Math.random() * 0.03,
                phase: Math.random() * Math.PI * 2
            }});
        }}
    }}
    
    function drawStars() {{
        for (let s of stars) {{
            const twinkle = 0.5 + 0.5 * Math.sin(Date.now() * s.twinkleSpeed + s.phase);
            ctx.beginPath();
            ctx.arc(s.x, s.y, s.radius, 0, Math.PI * 2);
            ctx.fillStyle = `rgba(255, 215, 0, ${{s.alpha * twinkle}})`;
            ctx.fill();
        }}
    }}
    
    function drawEarth() {{
        if (!earthLoaded) {{
            ctx.beginPath();
            ctx.arc(width/2, height/2, window.earthRadius, 0, Math.PI*2);
            ctx.fillStyle = '#2a6f8f';
            ctx.fill();
            return;
        }}
        ctx.save();
        ctx.translate(width/2, height/2);
        const earthRotation = (Date.now() / 20000) % (Math.PI * 2);
        ctx.rotate(earthRotation);
        ctx.drawImage(earthImg, -window.earthRadius, -window.earthRadius, window.earthRadius*2, window.earthRadius*2);
        ctx.restore();
        ctx.beginPath();
        ctx.arc(width/2, height/2, window.earthRadius + 5, 0, Math.PI*2);
        ctx.fillStyle = 'rgba(255,215,0,0.1)';
        ctx.fill();
    }}
    
    function drawOrbitingText() {{
        orbitAngle += (Math.PI * 2) / (12 * 60 / 1000 * 60);
        if (orbitAngle > Math.PI * 2) orbitAngle -= Math.PI * 2;
        const x = width/2 + Math.cos(orbitAngle) * window.textRadius;
        const y = height/2 + Math.sin(orbitAngle) * window.textRadius;
        ctx.save();
        ctx.font = `bold ${{Math.max(24, window.innerWidth / 25)}}px 'Poppins', 'Segoe UI'`;
        ctx.shadowBlur = 10;
        ctx.shadowColor = 'gold';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        const grad = ctx.createLinearGradient(x-50, y-20, x+50, y+20);
        grad.addColorStop(0, '#FFD700');
        grad.addColorStop(1, '#FFB347');
        ctx.fillStyle = grad;
        ctx.fillText('✨ Gesner Deslandes ✨', x, y);
        ctx.restore();
    }}
    
    function drawTagline() {{
        ctx.font = `${{Math.max(18, window.innerWidth / 40)}}px 'Poppins'`;
        ctx.fillStyle = '#FFD966';
        ctx.shadowBlur = 4;
        ctx.shadowColor = 'rgba(0,0,0,0.5)';
        ctx.textAlign = 'center';
        ctx.fillText('⭐ your best choice of programmer solution ⭐', width/2, height/2 + window.earthRadius + 40);
        ctx.shadowBlur = 0;
    }}
    
    function animate() {{
        if (width !== window.innerWidth || height !== window.innerHeight) {{
            resizeCanvas();
            initStars();
        }}
        ctx.clearRect(0, 0, width, height);
        const grad = ctx.createLinearGradient(0, 0, width, height);
        grad.addColorStop(0, '#01011a');
        grad.addColorStop(1, '#0a1a3a');
        ctx.fillStyle = grad;
        ctx.fillRect(0, 0, width, height);
        drawStars();
        drawEarth();
        drawOrbitingText();
        drawTagline();
        requestAnimationFrame(animate);
    }}
    
    window.addEventListener('resize', () => {{ resizeCanvas(); initStars(); }});
    resizeCanvas();
    initStars();
    animate();
</script>
""", unsafe_allow_html=True)
