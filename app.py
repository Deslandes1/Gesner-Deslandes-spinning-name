import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Gesner Deslandes | GlobalInternet.py",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

PHONE = "(509)-47385663"
EMAIL = "deslandes78@gmail.com"

# Hide Streamlit UI and style the contact bar
st.markdown(f"""
<style>
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    .block-container {{ padding: 0rem; }}
    
    .contact-bar {{
        position: fixed; 
        bottom: 30px; 
        left: 50%; 
        transform: translateX(-50%);
        text-align: center; 
        background: rgba(0, 0, 0, 0.85);
        padding: 12px 25px; 
        border-radius: 50px; 
        backdrop-filter: blur(10px);
        z-index: 9999; 
        color: #FFD700; 
        font-family: 'Poppins', sans-serif;
        border: 1px solid rgba(255, 215, 0, 0.4);
        box-shadow: 0 0 20px rgba(0,0,0,0.5);
        white-space: nowrap;
    }}
    .contact-bar a {{ color: #FFD700; text-decoration: none; font-weight: bold; }}
</style>

<div class="contact-bar">
    📞 <strong>Phone:</strong> {PHONE} &nbsp;&nbsp;|&nbsp;&nbsp; 
    ✉️ <strong>Email:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a>
</div>
""", unsafe_allow_html=True)

# High-performance Canvas Component with stylized globe
components.html("""
<html>
<body style="margin: 0; padding: 0; overflow: hidden; background: #000;">
<canvas id="universeCanvas" style="display: block;"></canvas>

<script>
    const canvas = document.getElementById('universeCanvas');
    const ctx = canvas.getContext('2d');
    let width, height, stars = [];
    let rotation = 0;

    function resize() {
        width = window.innerWidth;
        height = window.innerHeight;
        canvas.width = width;
        canvas.height = height;
        initStars();
    }

    function initStars() {
        stars = [];
        for (let i = 0; i < 300; i++) {
            stars.push({
                x: Math.random() * width,
                y: Math.random() * height,
                size: Math.random() * 1.5,
                twinkle: Math.random() * 0.05
            });
        }
    }

    let orbitAngle = 0;

    function drawGlobe(cx, cy, r) {
        rotation += 0.01;
        
        // Globe Background (the blue depths)
        ctx.save();
        ctx.beginPath();
        ctx.arc(cx, cy, r, 0, Math.PI * 2);
        ctx.fillStyle = "#001a33";
        ctx.fill();
        
        // Outer Ring Glow
        ctx.strokeStyle = "rgba(0, 191, 255, 0.5)";
        ctx.lineWidth = 3;
        ctx.stroke();
        ctx.restore();

        // Draw Meridians (Vertical Curves)
        ctx.strokeStyle = "rgba(0, 255, 255, 0.6)";
        ctx.lineWidth = 1.5;
        for (let i = 0; i < 4; i++) {
            let shift = (rotation + (i * Math.PI / 2)) % Math.PI;
            let curveWidth = Math.cos(shift) * r;
            
            ctx.beginPath();
            ctx.ellipse(cx, cy, Math.abs(curveWidth), r, 0, 0, Math.PI * 2);
            ctx.stroke();
        }

        // Draw Parallels (Horizontal Lines)
        for (let i = -2; i <= 2; i++) {
            let h = (i * r) / 3;
            let w = Math.sqrt(r * r - h * h);
            ctx.beginPath();
            ctx.moveTo(cx - w, cy + h);
            ctx.lineTo(cx + w, cy + h);
            ctx.stroke();
        }
        
        // Circular Rim
        ctx.beginPath();
        ctx.arc(cx, cy, r, 0, Math.PI * 2);
        ctx.stroke();
    }

    function draw() {
        // Deep Space Gradient
        const skyGrad = ctx.createRadialGradient(width/2, height/2, 10, width/2, height/2, width);
        skyGrad.addColorStop(0, "#01011a");
        skyGrad.addColorStop(1, "#000000");
        ctx.fillStyle = skyGrad;
        ctx.fillRect(0, 0, width, height);

        // Draw Stars
        stars.forEach(s => {
            ctx.fillStyle = `rgba(255, 215, 0, ${0.3 + Math.abs(Math.sin(Date.now() * s.twinkle))})`;
            ctx.beginPath();
            ctx.arc(s.x, s.y, s.size, 0, Math.PI * 2);
            ctx.fill();
        });

        const cx = width / 2;
        const cy = height / 2;
        const r = Math.min(width, height) * 0.15;

        // Draw the "Globe Emoji" Symbol
        drawGlobe(cx, cy, r);

        // Orbiting Text
        orbitAngle += 0.005;
        const orbitR = r * 1.8;
        const tx = cx + Math.cos(orbitAngle) * orbitR;
        const ty = cy + Math.sin(orbitAngle) * orbitR;

        ctx.font = "bold 30px 'Poppins', sans-serif";
        ctx.fillStyle = "#FFD700";
        ctx.textAlign = "center";
        ctx.shadowBlur = 15;
        ctx.shadowColor = "gold";
        ctx.fillText("✨ Gesner Deslandes ✨", tx, ty);
        ctx.shadowBlur = 0;

        // Tagline
        ctx.font = "18px 'Poppins', sans-serif";
        ctx.fillStyle = "#FFD966";
        ctx.fillText("⭐ your best choice of programmer solution ⭐", cx, cy + r + 60);

        requestAnimationFrame(draw);
    }

    window.addEventListener('resize', resize);
    resize();
    draw();
</script>
</body>
</html>
""", height=800)
