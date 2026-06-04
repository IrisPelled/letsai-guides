import base64, sys
sys.stdout.reconfigure(encoding='utf-8')

ASSETS = r'C:\Users\irisp\OneDrive\שולחן העבודה\ClaudeCodeTut\copilot lisence guide\assets'
ROOT   = r'C:\Users\irisp\OneDrive\שולחן העבודה\ClaudeCodeTut'
OUT    = r'C:\Users\irisp\OneDrive\שולחן העבודה\ClaudeCodeTut\copilot lisence guide\index.html'

def b64(path):
    with open(path, 'rb') as f: return base64.b64encode(f.read()).decode()

def data(path, mime='image/png'):
    return f'data:{mime};base64,{b64(path)}'

imgs        = [data(f'{ASSETS}\\{i}.png') for i in range(1, 8)]
logo_cop    = data(f'{ASSETS}\\copilot logo.png')
logo_lets   = data(f'{ROOT}\\LetsAIlogo.svg', 'image/svg+xml')
arrow       = data(f'{ASSETS}\\arrow.png')
iris_img    = data(f'{ASSETS}\\Iris Image.png')
outlook_img = data(f'{ASSETS}\\outlook.png')
teams_img   = data(f'{ASSETS}\\Teams.png')

imgs_js = '{\n' + ',\n'.join(f"  {i+1}: '{imgs[i]}'" for i in range(7)) + '\n}'

HTML = f'''<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>איזה Copilot יש לי? — Let's AI</title>
<link href="https://fonts.googleapis.com/css2?family=Frank+Ruhl+Libre:wght@400;500;700;900&family=Heebo:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
:root {{
  --purple:      #13008a;
  --purple2:     #5e17eb;
  --pink:        #ff5bc0;
  --cyan:        #5ce1e6;
  --white:       #ffffff;
  --black:       #1a1a1a;
  --glass-bg:    rgba(255,255,255,0.55);
  --glass-bdr:   rgba(255,255,255,0.35);
  --ease-out:    cubic-bezier(0.16,1,0.3,1);
  --spring:      cubic-bezier(0.34,1.56,0.64,1);
  --content-max: 860px;
  --purple-light:#ede8ff;
  --pink-light:  #ffe0f5;
}}
*,*::before,*::after{{margin:0;padding:0;box-sizing:border-box;}}
html{{direction:rtl;scroll-behavior:smooth;}}
body{{font-family:'Heebo',sans-serif;color:var(--black);overflow-x:hidden;line-height:1.7;
  background:linear-gradient(135deg,#e8f4ff 0%,#f0e8ff 25%,#ffe8f5 50%,#fff0e0 75%,#e8fff0 100%);
  background-attachment:fixed;}}
h1,h2,h3,h4{{font-family:'Frank Ruhl Libre',serif;line-height:1.3;}}

/* ===== Logo Bar ===== */
.logo-bar{{
  width:100%;padding:6px 20px;
  display:flex;align-items:center;justify-content:space-between;
  direction:ltr;
  background:rgba(255,255,255,0.9);
  backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);
  border-bottom:1px solid rgba(19,0,138,0.1);
}}
.logo-bar .lets-logo{{height:64px;width:auto;}}
.logo-bar .cop-logo{{height:38px;width:auto;object-fit:contain;}}
.app-logo-bar{{position:fixed;top:0;left:0;right:0;z-index:500;}}
.hero .logo-bar{{position:absolute;top:0;left:0;right:0;z-index:10;background:rgba(255,255,255,0.85);}}

/* ===== Hero ===== */
.hero{{
  position:relative;min-height:100vh;
  display:flex;align-items:center;justify-content:center;
  overflow:hidden;
}}
.hero-video{{position:absolute;top:0;left:0;width:100%;height:100%;object-fit:cover;z-index:0;}}
.hero-overlay{{position:absolute;inset:0;background:rgba(255,255,255,0.48);z-index:1;}}
.hero-side-fade{{position:absolute;top:0;width:22%;height:100%;z-index:2;pointer-events:none;}}
.hero-side-fade.left{{left:0;background:linear-gradient(to right,rgba(232,232,255,0.95) 0%,rgba(232,232,255,0) 100%);}}
.hero-side-fade.right{{right:0;background:linear-gradient(to left,rgba(255,232,245,0.95) 0%,rgba(255,232,245,0) 100%);}}
.hero-content{{
  position:relative;z-index:3;text-align:center;
  padding:2.5rem 3rem 3rem;max-width:580px;width:90%;
  background:rgba(255,255,255,0.45);
  backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);
  border-radius:24px;border:1px solid rgba(255,255,255,0.5);
  box-shadow:0 8px 40px rgba(19,0,138,0.12);
  margin-top:80px;
}}
.hero-cop-logo{{
  width:320px;height:320px;object-fit:contain;
  margin:0 auto 24px;display:block;
  animation:float 4s ease-in-out infinite;
  filter:drop-shadow(0 8px 24px rgba(19,0,138,0.18));
}}
@keyframes float{{0%,100%{{transform:translateY(0);}} 50%{{transform:translateY(-12px);}}}}
.hero-badge{{
  display:inline-block;padding:5px 18px;
  background:rgba(19,0,138,0.1);color:var(--purple);
  border-radius:50px;font-size:0.78rem;font-weight:700;
  margin-bottom:1rem;opacity:0;transform:translateY(20px);
  letter-spacing:0.05em;
}}
.hero-content h1{{font-size:clamp(2rem,5vw,3rem);font-weight:900;margin-bottom:0.5rem;opacity:0;transform:translateY(30px);color:var(--purple);}}
.hero-subtitle{{font-size:1.05rem;color:#444;font-weight:500;margin-bottom:0.5rem;opacity:0;transform:translateY(30px);}}
.hero-content p{{font-size:0.92rem;color:#666;margin-bottom:1.75rem;opacity:0;transform:translateY(30px);}}
.hero-btn{{
  display:inline-block;padding:14px 48px;
  background:linear-gradient(135deg,var(--purple),var(--purple2));
  color:var(--white);border:none;border-radius:50px;
  font-family:'Heebo',sans-serif;font-size:1.05rem;font-weight:700;
  cursor:pointer;opacity:0;transform:translateY(30px);
  transition:transform 0.2s var(--spring),box-shadow 0.2s ease;
  box-shadow:0 4px 20px rgba(19,0,138,0.3);
}}
.hero-btn:hover{{transform:translateY(-3px);box-shadow:0 8px 32px rgba(19,0,138,0.4);}}
.hero-btn:active{{transform:scale(0.97);}}
.hero.animate .hero-badge    {{animation:fadeUp 0.8s var(--ease-out) 0.2s forwards;}}
.hero.animate h1             {{animation:fadeUp 0.8s var(--ease-out) 0.4s forwards;}}
.hero.animate .hero-subtitle {{animation:fadeUp 0.8s var(--ease-out) 0.6s forwards;}}
.hero.animate p              {{animation:fadeUp 0.8s var(--ease-out) 0.8s forwards;}}
.hero.animate .hero-btn      {{animation:fadeUp 0.8s var(--ease-out) 1.0s forwards;}}
@keyframes fadeUp{{to{{opacity:1;transform:translateY(0);}}}}

/* ===== App ===== */
.app{{display:none;min-height:100vh;flex-direction:column;}}
.app.visible{{display:flex;}}
.app-body{{display:flex;flex:1;}}

/* ===== Top Nav ===== */
.top-nav{{
  position:fixed;top:76px;left:0;right:0;z-index:100;
  background:rgba(255,255,255,0.96);
  backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);
  border-bottom:1px solid rgba(19,0,138,0.1);
  display:none;flex-direction:column;
}}
.top-nav.visible{{display:flex;}}
.nav-progress{{height:3px;background:rgba(19,0,138,0.08);}}
.nav-progress-fill{{height:100%;background:linear-gradient(90deg,var(--purple),var(--pink));transition:width 0.5s var(--ease-out);width:0%;}}
.nav-steps{{display:flex;align-items:center;justify-content:center;padding:0.55rem 1rem;gap:0;overflow-x:auto;}}
.nav-step{{
  display:flex;align-items:center;gap:0.35rem;
  padding:0.3rem 0.6rem;border:none;background:none;
  cursor:pointer;font-family:'Heebo',sans-serif;font-size:0.76rem;color:#999;
  transition:color 0.2s;white-space:nowrap;border-radius:8px;
}}
.nav-step:hover{{color:var(--black);}}
.nav-step.active{{color:var(--purple);font-weight:700;}}
.nav-step.completed{{color:var(--purple2);}}
.nav-step-num{{
  width:22px;height:22px;border-radius:50%;
  background:rgba(19,0,138,0.08);color:var(--purple);
  display:flex;align-items:center;justify-content:center;
  font-size:0.66rem;font-weight:700;flex-shrink:0;
  transition:background 0.2s,color 0.2s;
}}
.nav-step.active    .nav-step-num{{background:var(--purple);color:var(--white);box-shadow:0 0 0 3px rgba(19,0,138,0.2);}}
.nav-step.completed .nav-step-num{{background:var(--pink);color:var(--white);}}
.nav-step-line{{width:14px;height:1px;background:rgba(0,0,0,0.1);flex-shrink:0;}}

/* ===== Main Content ===== */
.main-content{{
  flex:1;padding:2rem 2rem 6rem;padding-top:6rem;
  max-width:var(--content-max);margin:0 auto;width:100%;
}}

/* ===== Step ===== */
.step{{display:none;}}
.step.active{{display:block;animation:stepIn 0.45s var(--ease-out) both;}}
@keyframes stepIn{{from{{opacity:0;transform:translateY(22px);}} to{{opacity:1;transform:translateY(0);}}}}
.step-header{{margin-bottom:1.5rem;padding-bottom:1.25rem;border-bottom:2px solid rgba(19,0,138,0.12);}}
.step-tag{{font-size:0.72rem;font-weight:700;color:var(--pink);letter-spacing:0.18em;text-transform:uppercase;margin-bottom:0.3rem;}}
.step-title{{font-size:clamp(1.55rem,3vw,2.1rem);font-weight:800;color:var(--purple);}}
.step-desc{{font-size:0.95rem;color:#555;margin-top:0.3rem;}}

/* ===== Instruction box ===== */
.instruction-box{{
  background:rgba(19,0,138,0.04);
  border:1px solid rgba(19,0,138,0.1);
  border-right:4px solid var(--purple);
  border-radius:14px;padding:14px 18px;margin-bottom:20px;
  font-size:0.93rem;line-height:1.75;color:#222;
}}
.instruction-box strong{{color:var(--purple);}}
.instruction-box a{{color:var(--pink);font-weight:600;text-decoration:none;direction:ltr;display:inline-block;}}
.instruction-box a:hover{{text-decoration:underline;}}

/* ===== Screenshot ===== */
.screenshot-wrap{{
  border-radius:16px;overflow:hidden;
  border:1px solid rgba(19,0,138,0.1);
  box-shadow:0 6px 28px rgba(19,0,138,0.1);
  position:relative;margin-bottom:20px;
}}
.screenshot-wrap img{{width:100%;display:block;}}
.screenshot-label{{
  position:absolute;top:10px;left:10px;
  background:rgba(19,0,138,0.85);color:white;
  font-size:0.72rem;font-weight:700;padding:4px 12px;border-radius:50px;
  backdrop-filter:blur(4px);
}}
.screenshot-row{{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:20px;}}
.screenshot-row .screenshot-wrap{{margin-bottom:0;}}
.screenshot-wrap.compact{{max-height:160px;overflow:hidden;}}
.screenshot-wrap.compact img{{width:100%;height:160px;object-fit:cover;object-position:top;}}
.screenshot-wrap.compact-full img{{width:75%;display:block;margin:0 auto;}}

/* ===== Question ===== */
.question-text{{
  font-size:1.1rem;font-weight:700;color:var(--black);
  margin-bottom:18px;text-align:center;
  padding:12px 0;
}}

/* ===== Flip Cards ===== */
.answer-grid{{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:24px;}}
.flip-card{{perspective:1200px;cursor:pointer;min-height:170px;}}
.flip-card-inner{{
  position:relative;width:100%;height:100%;min-height:170px;
  transition:transform 0.65s cubic-bezier(0.4,0,0.2,1);
  transform-style:preserve-3d;
}}
.flip-card.flipped .flip-card-inner{{transform:rotateY(180deg);}}
.flip-front,.flip-back{{
  position:absolute;inset:0;
  backface-visibility:hidden;-webkit-backface-visibility:hidden;
  border-radius:18px;padding:18px 16px;
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  text-align:center;
}}
.flip-front{{
  background:rgba(255,255,255,0.75);
  backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);
  border:2px solid rgba(19,0,138,0.12);
  box-shadow:0 4px 20px rgba(19,0,138,0.07);
  transition:border-color 0.2s,box-shadow 0.2s;
}}
.flip-card:hover .flip-front{{
  border-color:rgba(19,0,138,0.3);
  box-shadow:0 8px 32px rgba(19,0,138,0.15);
  transform:translateY(-2px);
}}
.flip-back{{
  background:linear-gradient(135deg,#13008a,#5e17eb);
  backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);
  border:2px solid rgba(255,255,255,0.15);
  box-shadow:0 8px 32px rgba(19,0,138,0.35);
  transform:rotateY(180deg);
}}
.answer-letter{{
  font-size:1.6rem;font-weight:900;color:var(--purple);
  width:44px;height:44px;border-radius:50%;
  background:var(--purple-light);
  display:flex;align-items:center;justify-content:center;
  margin-bottom:10px;flex-shrink:0;font-family:'Frank Ruhl Libre',serif;
}}
.answer-text{{font-size:0.88rem;color:#333;line-height:1.5;font-weight:500;}}
.feedback-icon{{font-size:1.3rem;margin-bottom:4px;}}
.feedback-title{{font-size:0.92rem;font-weight:900;color:#ffffff;margin-bottom:4px;}}
.feedback-text{{font-size:0.78rem;color:rgba(255,255,255,0.88);line-height:1.45;margin-bottom:10px;font-weight:600;}}
.feedback-continue{{
  padding:8px 22px;border-radius:50px;border:2px solid rgba(255,255,255,0.6);
  background:rgba(255,255,255,0.15);
  color:white;font-family:'Heebo',sans-serif;font-size:0.84rem;font-weight:700;
  cursor:pointer;transition:transform 0.15s var(--spring),box-shadow 0.2s,background 0.2s;
}}
.feedback-continue:hover{{background:rgba(255,255,255,0.3);box-shadow:0 4px 16px rgba(0,0,0,0.2);transform:translateY(-1px);}}

/* ===== Bottom Nav ===== */
.bottom-nav{{
  position:fixed;bottom:0;left:0;right:0;z-index:200;
  display:none;align-items:center;justify-content:space-between;
  padding:0.8rem 2rem;
  background:rgba(255,255,255,0.96);
  backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);
  border-top:1px solid rgba(19,0,138,0.08);
}}
.bottom-nav.visible{{display:flex;}}
.nav-btn{{
  padding:9px 26px;border-radius:50px;
  font-family:'Heebo',sans-serif;font-size:0.87rem;font-weight:600;
  cursor:pointer;border:2px solid rgba(19,0,138,0.25);
  background:none;color:var(--purple);
  transition:transform 0.15s var(--spring),box-shadow 0.2s;
}}
.nav-btn.primary{{background:linear-gradient(135deg,var(--purple),var(--purple2));color:white;border-color:transparent;}}
.nav-btn:hover{{box-shadow:0 4px 14px rgba(19,0,138,0.2);}}
.nav-btn:active{{transform:scale(0.97);}}
.nav-btn.hidden{{visibility:hidden;}}
.nav-dots{{display:flex;gap:6px;}}
.nav-dot{{
  width:8px;height:8px;border-radius:50%;border:none;cursor:pointer;
  background:rgba(19,0,138,0.15);
  transition:background 0.2s,transform 0.2s var(--spring);
}}
.nav-dot.active{{background:var(--purple);transform:scale(1.35);}}

/* ===== Result screen ===== */
.result-screen{{display:none;}}
.result-screen.active{{display:flex;flex-direction:column;min-height:calc(100vh - 110px);animation:stepIn 0.5s var(--ease-out) both;}}
.result-hero{{
  text-align:center;padding:1.2rem 0 0.5rem;
}}
.result-emoji{{font-size:4rem;display:block;margin-bottom:0.75rem;animation:popIn 0.5s var(--spring) both;}}
.result-emoji-img{{width:100px;height:100px;object-fit:contain;display:block;margin:0 auto 0.6rem;animation:popIn 0.5s var(--spring) both;}}
@keyframes popIn{{from{{opacity:0;transform:scale(0.5);}} to{{opacity:1;transform:scale(1);}}}}
.result-tier-badge{{
  display:inline-block;padding:5px 18px;
  background:linear-gradient(135deg,var(--purple),var(--purple2));
  color:white;border-radius:50px;font-size:0.78rem;font-weight:700;
  margin-bottom:1rem;letter-spacing:0.05em;
}}
.result-title{{font-size:clamp(1.8rem,4vw,2.5rem);font-weight:900;color:var(--purple);margin-bottom:0.4rem;}}
.result-subtitle{{font-size:1rem;color:#666;margin-bottom:0.5rem;}}
.result-tier-desc{{
  background:rgba(255,255,255,0.7);backdrop-filter:blur(8px);
  border-radius:14px;border:1px solid rgba(19,0,138,0.1);
  padding:16px 20px;margin:1.25rem 0;font-size:0.93rem;color:#333;line-height:1.7;
  box-shadow:0 4px 16px rgba(19,0,138,0.06);
}}

/* Features grid */
.features-label{{font-size:0.75rem;font-weight:700;letter-spacing:0.15em;text-transform:uppercase;color:var(--purple);margin:0.5rem 0 0.5rem;opacity:0.75;}}
.features-grid{{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:0.75rem;}}
.feature-item{{
  display:flex;align-items:center;gap:10px;
  padding:10px 16px;border-radius:14px;
  background:rgba(255,255,255,0.8);border:1px solid rgba(0,0,0,0.07);
  font-size:0.88rem;color:#222;font-weight:600;
  box-shadow:0 2px 10px rgba(0,0,0,0.04);
  transition:box-shadow 0.2s;
}}
.feature-check{{font-size:1rem;flex-shrink:0;}}

/* Workshop verdict */
.workshop-verdict{{
  border-radius:18px;padding:18px 24px 18px 24px;margin:1rem 0;
  box-shadow:0 4px 20px rgba(0,0,0,0.07);
  text-align:right;
}}
.workshop-verdict.good   {{background:linear-gradient(135deg,#d1fae5,#a7f3d0);border:1px solid #6ee7b7;}}
.workshop-verdict.bad    {{background:linear-gradient(135deg,#fee2e2,#fecaca);border:1px solid #fca5a5;}}
.workshop-verdict.partial{{background:linear-gradient(135deg,rgba(94,23,235,0.12),rgba(255,91,192,0.12));border:1px solid rgba(94,23,235,0.25);}}
.verdict-icon{{font-size:2.2rem;flex-shrink:0;}}
.verdict-body .verdict-title{{font-size:1rem;font-weight:800;margin-bottom:4px;}}
.workshop-verdict.partial .verdict-title{{font-size:1.15rem;font-weight:900;}}
.workshop-verdict.good    .verdict-title{{color:#065f46;}}
.workshop-verdict.bad     .verdict-title{{color:#991b1b;}}
.workshop-verdict.partial .verdict-title{{color:#13008a;}}
.verdict-body p{{font-size:0.88rem;line-height:1.6;}}
.workshop-verdict.good    p{{color:#064e3b;}}
.workshop-verdict.bad     p{{color:#7f1d1d;}}
.workshop-verdict.partial p{{color:#13008a;font-size:1rem;font-weight:700;}}

.result-actions{{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin:0.5rem 0 0.5rem;}}
.result-btn{{
  padding:11px 30px;border-radius:50px;
  font-family:'Heebo',sans-serif;font-size:0.95rem;font-weight:700;
  cursor:pointer;border:2px solid var(--purple);
  transition:transform 0.15s var(--spring),box-shadow 0.2s;
}}
.result-btn.primary{{background:linear-gradient(135deg,var(--purple),var(--purple2));color:white;border-color:transparent;}}
.result-btn.secondary{{background:none;color:var(--purple);}}
.result-btn:hover{{box-shadow:0 4px 18px rgba(19,0,138,0.25);transform:translateY(-2px);}}

/* Arrow pin */
.arrow-pin{{
  position:absolute;
  width:60px;height:auto;
  pointer-events:none;z-index:10;
  animation:arrowBounce 0.8s ease-in-out infinite alternate;
  filter:drop-shadow(2px 3px 5px rgba(0,0,0,0.3));
}}
@keyframes arrowBounce{{
  from{{transform:translate(0,0) scale(1);}}
  to  {{transform:translate(-8px,-12px) scale(1.08);}}
}}

/* Confetti */
#confetti-canvas{{position:fixed;inset:0;pointer-events:none;z-index:9999;}}
.bottom-fade{{position:fixed;bottom:0;left:0;right:0;height:120px;background:linear-gradient(to top,rgba(255,255,255,0.85) 0%,rgba(255,255,255,0) 100%);pointer-events:none;z-index:49;}}

/* Responsive */
@media(max-width:640px){{
  .answer-grid{{grid-template-columns:1fr;}}
  .features-grid{{grid-template-columns:1fr;}}
  .screenshot-row{{grid-template-columns:1fr;}}
  .nav-step span:not(.nav-step-num){{display:none;}}
  .main-content{{padding-top:6rem;padding-right:1rem;padding-left:1rem;}}
}}
</style>
</head>
<body>

<!-- ===== Hero ===== -->
<section class="hero" id="hero">
  <div class="logo-bar">
    <img src="{logo_lets}" class="lets-logo" alt="Let's AI">
    <img src="{logo_cop}" class="cop-logo" alt="Microsoft Copilot">
  </div>
  <video class="hero-video" autoplay muted loop playsinline preload="auto">
    <source src="../kling_intro.mp4" type="video/mp4">
  </video>
  <div class="hero-overlay"></div>
  <div class="hero-side-fade left"></div>
  <div class="hero-side-fade right"></div>
  <div class="hero-content">
    <img src="{logo_cop}" class="hero-cop-logo" alt="Copilot">
    <div class="hero-badge">Workshop Guide · Let's AI · 2026</div>
    <h1>איזה Copilot יש לי?</h1>
    <p class="hero-subtitle">6 שאלות פשוטות לזיהוי סוג הרישיון שלכם</p>
    <p>גלו בדיוק אילו יכולות Microsoft Copilot זמינות לכם</p>
    <button class="hero-btn" onclick="startQuiz()">בואו נגלה ←</button>
  </div>
</section>

<!-- ===== App ===== -->
<div class="app" id="app">

  <!-- Fixed logo bar -->
  <div class="app-logo-bar logo-bar">
    <img src="{logo_lets}" class="lets-logo" alt="Let's AI">
    <img src="{logo_cop}" class="cop-logo" alt="Copilot">
  </div>

  <!-- Top nav -->
  <nav class="top-nav" id="topNav">
    <div class="nav-progress"><div class="nav-progress-fill" id="progressFill"></div></div>
    <div class="nav-steps" id="navSteps">
      <!-- generated by JS -->
    </div>
  </nav>

  <!-- Body -->
  <div class="app-body">
    <main class="main-content">
      <div id="stepContainer"></div>
      <div id="resultContainer"></div>
    </main>
  </div>

  <!-- Bottom nav -->
  <nav class="bottom-nav visible" id="bottomNav">
    <button class="nav-btn hidden" id="btnPrev" onclick="navPrev()">→ הקודמת</button>
    <div class="nav-dots" id="navDots"></div>
    <button class="nav-btn primary" id="btnNext" onclick="navNext()">הבאה ←</button>
  </nav>
</div>

<canvas id="confetti-canvas"></canvas>
<div class="bottom-fade"></div>

<script>
// ── Data ──
const IMGS = {imgs_js};
const OUTLOOK_IMG = '{outlook_img}';
const TEAMS_IMG   = '{teams_img}';

const questions = [
  {{
    id: 1, tag: 'שאלה 1 מתוך 6',
    title: 'זיהוי מסך הבית של Copilot',
    instruction: `היכנסו לקישור: <a href="https://copilot.microsoft.com" target="_blank">copilot.microsoft.com</a><br>התחברו עם החשבון שבו אתם משתמשים ב־Copilot. <strong>איזה מסך אתם רואים?</strong>`,
    screenshots: [IMGS[2], IMGS[1]],
    screenshotCaptions: ['בחירת חשבון (עבודה / אישי)', 'מסך Copilot Chat חינמי'],
    question: 'באיזה מסך נחתתם?',
    answers: [
      {{ letter: 'א', text: 'אני רואה מסך Copilot עם חשבון ארגוני — מייל של מקום העבודה' }},
      {{ letter: 'ב', text: 'אני רואה מסך Copilot רגיל, בלי מייל ארגוני — חשבון אישי' }}
    ],
    feedbacks: [
      {{ icon: '🏢', title: 'נראה שמדובר בחשבון ארגוני', text: 'מצוין! <strong>נמשיך לבדוק</strong> אילו יכולות Copilot זמינות לכם בפועל.', next: 'q2' }},
      {{ icon: '👤', title: 'חשבון אישי (לא ארגוני)', text: '<strong>לא נורא!</strong> גם עם חשבון אישי אפשר להשתמש ב-Copilot. נמשיך לבדוק אילו יכולות זמינות לכם.', next: 'q2' }}
    ]
  }},
  {{
    id: 2, tag: 'שאלה 2 מתוך 6',
    title: 'בדיקת 9 הנקודות',
    instruction: `במסך הבית של Copilot, <strong>הסתכלו בפינה הימנית העליונה</strong>. האם אתם רואים סמלול של 9 נקודות?`,
    screenshots: [IMGS[3]],
    screenshotCaptions: ['סמלול 9 הנקודות — מסומן בעיגול אדום'],
    showArrow: true,
    compactScreenshot: true,
    question: 'האם אתם רואים סמלול של 9 נקודות?',
    answers: [
      {{ letter: 'כן', text: 'כן, אני רואה אייקון של 9 נקודות בפינה ✓' }},
      {{ letter: 'לא', text: 'לא, אני לא רואה אייקון כזה ✗' }}
    ],
    feedbacks: [
      {{ icon: '✅', title: 'מצוין!', text: 'מצאתם את אייקון ה-9 נקודות. <strong>ממשיכים לשלב הבא.</strong>', next: 'q3' }},
      {{ icon: '💬', title: 'אין Microsoft 365', text: 'ללא אייקון 9 הנקודות, סביר שיש לכם רק Copilot Chat החינמי. <strong>נעבור לסיכום.</strong>', next: 'result_chat_only' }}
    ]
  }},
  {{
    id: 3, tag: 'שאלה 3 מתוך 6',
    title: 'בדיקת Office בתפריט 9 הנקודות',
    instruction: `<strong>לחצו על אייקון 9 הנקודות</strong> שמצאתם. האם בתפריט שנפתח אתם רואים אפליקציות Office כמו Word, Excel או PowerPoint?`,
    screenshots: [IMGS[4]],
    screenshotCaptions: ['תפריט 9 הנקודות — בדקו אם Word/Excel/PowerPoint מופיעים'],
    showArrow: true,
    arrowStyle: 'top:58%;right:28%;',
    compactScreenshot: true,
    screenshotHeight: 240,
    question: 'האם אתם רואים Word, Excel או PowerPoint בתפריט?',
    answers: [
      {{ letter: 'כן', text: 'כן, אני רואה Word, Excel או PowerPoint ✓' }},
      {{ letter: 'לא', text: 'לא, אני לא רואה אפליקציות Office ✗' }}
    ],
    feedbacks: [
      {{ icon: '✅', title: 'יש Office!', text: 'מצוין — יש לכם גישה לאפליקציות Office. <strong>ממשיכים לבדוק</strong> האם Copilot פעיל בתוכן.', next: 'q4' }},
      {{ icon: '➡️', title: 'ממשיכים לבדוק', text: 'אין Office בתפריט? ייתכן שיש לכם Copilot בתוך אפליקציות Office ישירות. <strong>ממשיכים לבדוק.</strong>', next: 'q4' }}
    ]
  }},
  {{
    id: 4, tag: 'שאלה 4 מתוך 6',
    title: 'בדיקת Copilot בתוך Office',
    instruction: `פתחו אחת מהתוכנות: <strong>Word, Excel או PowerPoint</strong> (מספיק לבדוק באחת). האם אתם רואים בתוך התוכנה <strong>כפתור או סמל של Copilot</strong>?`,
    screenshots: [IMGS[5]],
    screenshotCaptions: ['לוגו Copilot בתוך Word — מסומן בעיגול אדום'],
    compactFull: true,
    question: 'האם אתם רואים כפתור Copilot בתוך Word/Excel/PowerPoint?',
    answers: [
      {{ letter: 'כן', text: 'כן, אני רואה את Copilot בתוך Word / Excel / PowerPoint ✓' }},
      {{ letter: 'לא', text: 'לא, אני לא רואה כפתור Copilot בתוך Office ✗' }}
    ],
    feedbacks: [
      {{ icon: '🚀', title: 'יש Copilot בתוך Office!', text: 'מעולה! יש לכם Copilot פעיל בתוך אפליקציות Office. <strong>ממשיכים לבדוק</strong> עוד יכולות.', next: 'q5' }},
      {{ icon: '⚠️', title: 'אין Copilot בתוך Office', text: 'יש לכם Microsoft 365, אבל <strong>Copilot אינו פעיל</strong> בתוך Word, Excel ו-PowerPoint — החלק המרכזי של הסדנה.', next: 'result_no_office_copilot' }}
    ]
  }},
  {{
    id: 5, tag: 'שאלה 5 מתוך 7',
    title: 'Copilot באופיס',
    instruction: `פתחו את ה-<strong>Outlook</strong> ואת ה-<strong>Teams</strong>. האם אתם רואים שם את כפתור Copilot כמו בתמונה?`,
    screenshots: [OUTLOOK_IMG, TEAMS_IMG],
    screenshotCaptions: ['Copilot ב-Outlook', 'Copilot ב-Teams'],
    labelStyles: ['', 'left:auto;right:10px;'],
    question: 'האם אתם רואים Copilot ב-Outlook ו-Teams?',
    answers: [
      {{ letter: 'כן', text: 'כן, אני רואה Copilot ב-Outlook / Teams ✓' }},
      {{ letter: 'לא', text: 'לא, אני לא רואה Copilot שם ✗' }}
    ],
    feedbacks: [
      {{ icon: '📧', title: 'יש Copilot ב-Outlook ו-Teams!', text: 'מעולה! יש לכם Copilot גם בכלי התקשורת. <strong>ממשיכים לבדוק.</strong>', next: 'q6' }},
      {{ icon: '➡️', title: 'אין Copilot ב-Outlook/Teams', text: 'בסדר — ממשיכים לבדוק יכולות נוספות.', next: 'q6' }}
    ]
  }},
  {{
    id: 6, tag: 'שאלה 6 מתוך 7',
    title: 'בדיקת Create (יצירה)',
    instruction: `חזרו למסך הבית של Copilot. לחצו שוב על <strong>אייקון 9 הנקודות</strong>. האם אתם רואים שם אפשרות בשם <strong>Create</strong> או <strong>יצירה</strong>?`,
    screenshots: [IMGS[6]],
    screenshotCaptions: ['"יצירה" (Create) — מסומן בעיגול אדום'],
    compactFull: true,
    question: 'האם אתם רואים "Create" או "יצירה" בתפריט?',
    answers: [
      {{ letter: 'כן', text: 'כן, אני רואה Create / יצירה ✓' }},
      {{ letter: 'לא', text: 'לא, אני לא רואה Create / יצירה ✗' }}
    ],
    feedbacks: [
      {{ icon: '✨', title: 'יש Create!', text: 'מצוין! יש לכם גישה לאזור ה-Create / יצירה. <strong>שאלה אחת נוספת!</strong>', next: 'q7' }},
      {{ icon: '💡', title: 'אין Create כרגע', text: 'לא נורא! יש לכם Copilot בתוך Office. <strong>ממשיכים לבדיקה אחרונה.</strong>', next: 'q7' }}
    ]
  }},
  {{
    id: 7, tag: 'שאלה 7 מתוך 7',
    title: 'בדיקת סוכנים (Agents)',
    instruction: `במסך הבית של Copilot, האם אתם רואים אפשרות בשם <strong>Agents</strong>, <strong>סוכנים</strong>, <strong>Create agent</strong> או <strong>סוכן חדש</strong>?`,
    screenshots: [IMGS[7]],
    screenshotCaptions: ['לשונית "סוכנים" ו-"סוכן חדש" — מסומנים בעיגולים אדומים'],
    compactFull: true,
    question: 'האם אתם רואים Agents / סוכנים?',
    answers: [
      {{ letter: 'כן', text: 'כן, אני רואה Agents / סוכנים / סוכן חדש ✓' }},
      {{ letter: 'לא', text: 'לא, אני לא רואה Agents או סוכנים ✗' }}
    ],
    feedbacks: [
      {{ icon: '🤖', title: 'יש סוכנים!', text: 'מדהים — יש לכם את כל היכולות! <strong>בואו לראות את הסיכום.</strong>', next: 'result_full' }},
      {{ icon: '✅', title: 'אין סוכנים, אבל יש הרבה!', text: 'יש לכם Copilot מלא בתוך Office. <strong>בואו לראות את הסיכום.</strong>', next: 'result_no_agents' }}
    ]
  }}
];

const results = {{
  result_chat_only: {{
    emoji:'', emojiImg:'{logo_cop}', title:'Copilot Chat בלבד',
    subtitle:"גישה לצ'אט — ללא Microsoft 365",
    tierName:'Copilot Chat חינמי / בסיסי',
    tierDesc:"יש לכם גישה לצ'אט של Copilot, אבל לא לסביבת Microsoft 365 Copilot המלאה הנדרשת לסדנה.",
    features:[
      {{yes:true,  text:'Copilot Chat'}},
      {{yes:false, text:'Word / Excel / PowerPoint'}},
      {{yes:false, text:'Copilot בתוך Office'}},
      {{yes:false, text:'Create / יצירה'}},
      {{yes:false, text:'Agents / סוכנים'}},
      {{yes:false, text:'OneDrive, Teams, Outlook'}}
    ],
    verdictType:'bad', verdictTitle:'הסדנה פחות מתאימה',
    verdictText:'רוב ההדגמות יתבצעו בתוך Word, Excel, PowerPoint, OneDrive, Outlook ו-Teams. ללא מנוי Copilot 365 לא תוכלו לבצע אותן בעצמכם.'
  }},
  result_no_office_copilot: {{
    emoji:'', emojiImg:'{logo_cop}', title:'Microsoft 365 ללא Copilot',
    subtitle:'Office פעיל — Copilot לא מופעל',
    tierName:'Microsoft 365 ללא Copilot',
    tierDesc:'יש לכם גישה לאפליקציות Office, אבל Copilot אינו מופעל בתוך Word, Excel ו-PowerPoint.',
    features:[
      {{yes:true,  text:'Copilot Chat'}},
      {{yes:true,  text:'Word / Excel / PowerPoint'}},
      {{yes:false, text:'Copilot בתוך Office'}},
      {{yes:false, text:'Create / יצירה'}},
      {{yes:false, text:'Agents / סוכנים'}},
      {{yes:true,  text:'OneDrive, Teams, Outlook'}}
    ],
    verdictType:'bad', verdictTitle:'הסדנה פחות מתאימה',
    verdictText:'החלק המרכזי של הסדנה מבוסס על עבודה עם Copilot בתוך Office. ייתכן שתצטרכו לשדרג את המנוי לפני הסדנה.'
  }},
  result_no_agents: {{
    emoji:'', emojiImg:'{logo_cop}', title:'Copilot 365',
    subtitle:'Copilot מלא — ללא סוכנים',
    tierName:'Copilot 365',
    tierDesc:'יש לכם Copilot בתוך Word, Excel ו-PowerPoint.',
    features:[
      {{yes:true,  text:'Copilot Chat'}},
      {{yes:true,  text:'Word / Excel / PowerPoint'}},
      {{yes:true,  text:'Copilot בתוך Office'}},
      {{yes:false, text:'Create / יצירה (לא ברור)'}},
      {{yes:false, text:'Agents / סוכנים'}},
      {{yes:true,  text:'OneDrive, Teams, Outlook'}}
    ],
    verdictType:'partial', verdictTitle:'ישש!! הסדנה בדיוק בשבילכם 🎉',
    verdictText:'מחכה לכם!'
  }},
  result_full: {{
    emoji:'', emojiImg:'{logo_cop}', title:'Copilot 365 מורחב',
    subtitle:'גישה מלאה — Office + Create + Agents',
    tierName:'Copilot 365 מורחב — מנוי פרמיום',
    tierDesc:'יש לכם את כל היכולות: Copilot בתוך Office, יצירה, וסוכנים. הסדנה מותאמת בדיוק לכם.',
    features:[
      {{yes:true, text:'Copilot Chat'}},
      {{yes:true, text:'Word / Excel / PowerPoint'}},
      {{yes:true, text:'Copilot בתוך Office'}},
      {{yes:true, text:'Create / יצירה'}},
      {{yes:true, text:'Agents / סוכנים'}},
      {{yes:true, text:'OneDrive, Teams, Outlook'}}
    ],
    verdictType:'good', verdictTitle:'ישש!! הסדנה בדיוק בשבילכם 🎉',
    verdictText:'מחכה לכם!'
  }}
}};

// ── State ──
let currentStep = 0;
let userAnswers = {{}}; // שמירת תשובות לפי stepIdx
const TOTAL = questions.length;
const stepNames = ['זיהוי מסך','9 נקודות','חיבור לאפליקציות','Copilot ב-Office','Copilot באופיס','Create','קו הסיום'];

// ── Build UI ──
function buildUI() {{
  // Nav steps
  const ns = document.getElementById('navSteps');
  ns.innerHTML = questions.map((q,i) => `
    <button class="nav-step" id="navStep${{i}}" onclick="goToStep(${{i}})">
      ${{i>0 ? '<span class="nav-step-line"></span>' : ''}}
      <span class="nav-step-num">${{i+1}}</span>
      <span>${{stepNames[i]}}</span>
    </button>`).join('');

  // Nav dots
  const nd = document.getElementById('navDots');
  nd.innerHTML = questions.map((_,i) =>
    `<button class="nav-dot" id="dot${{i}}" onclick="goToStep(${{i}})"></button>`).join('');

  // Steps
  const sc = document.getElementById('stepContainer');
  sc.innerHTML = questions.map(q => `
    <div class="step" id="step${{q.id-1}}">
      <div class="step-header">
        <div class="step-tag">${{q.tag}}</div>
        <h2 class="step-title">${{q.title}}</h2>
      </div>
      <div class="instruction-box">${{q.instruction}}</div>
      ${{q.screenshots.length === 2
        ? `<div class="screenshot-row">
            <div class="screenshot-wrap"><img src="${{q.screenshots[0]}}" alt="${{q.screenshotCaptions[0]}}"><span class="screenshot-label" style="${{q.labelStyles?.[0]||''}}">${{q.screenshotCaptions[0]}}</span></div>
            <div class="screenshot-wrap"><img src="${{q.screenshots[1]}}" alt="${{q.screenshotCaptions[1]}}"><span class="screenshot-label" style="${{q.labelStyles?.[1]||''}}">${{q.screenshotCaptions[1]}}</span></div>
          </div>`
        : q.showArrow
          ? `<div style="position:relative;">
               <div class="screenshot-wrap${{q.compactScreenshot ? ' compact' : ''}}" style="${{q.screenshotHeight ? 'max-height:'+q.screenshotHeight+'px' : ''}}"><img src="${{q.screenshots[0]}}" alt="${{q.screenshotCaptions[0]}}" style="${{q.screenshotHeight ? 'height:'+q.screenshotHeight+'px;object-fit:cover;object-position:top' : ''}}"><span class="screenshot-label">${{q.screenshotCaptions[0]}}</span></div>
               <img class="arrow-pin" src="{arrow}" style="${{q.arrowStyle || 'top:10%;right:7%;'}}" alt="">
             </div>`
          : `<div class="screenshot-wrap${{q.compactScreenshot ? ' compact' : ''}}${{q.compactFull ? ' compact-full' : ''}}" style="${{q.screenshotHeight ? 'max-height:'+q.screenshotHeight+'px' : ''}}"><img src="${{q.screenshots[0]}}" alt="${{q.screenshotCaptions[0]}}" style="${{q.screenshotHeight ? 'height:'+q.screenshotHeight+'px;object-fit:cover;object-position:top' : ''}}"><span class="screenshot-label">${{q.screenshotCaptions[0]}}</span></div>`
      }}
      <div class="answer-grid" id="answerGrid${{q.id-1}}">
        ${{q.answers.map((a,ai) => `
          <div class="flip-card" id="flip_${{q.id-1}}_${{ai}}" onclick="selectAnswer(${{q.id-1}}, ${{ai}})">
            <div class="flip-card-inner">
              <div class="flip-front">
                <div class="answer-letter">${{a.letter}}</div>
                <div class="answer-text">${{a.text}}</div>
              </div>
              <div class="flip-back">
                <div class="feedback-icon">${{q.feedbacks[ai].icon}}</div>
                <div class="feedback-title">${{q.feedbacks[ai].title}}</div>
                <div class="feedback-text">${{q.feedbacks[ai].text}}</div>
                <button class="feedback-continue" onclick="event.stopPropagation();handleNext('${{q.feedbacks[ai].next}}')">
                  ${{q.feedbacks[ai].next.startsWith('result') ? '← ראה תוצאה' : '← המשך'}}
                </button>
              </div>
            </div>
          </div>`).join('')}}
      </div>
    </div>`).join('');

  // Results
  const rc = document.getElementById('resultContainer');
  rc.innerHTML = Object.entries(results).map(([key, r]) => `
    <div class="result-screen" id="${{key}}">
      <div class="result-hero">
        ${{r.emojiImg ? `<img src="${{r.emojiImg}}" class="result-emoji-img" alt="logo">` : `<span class="result-emoji">${{r.emoji}}</span>`}}
        <div class="result-tier-badge">${{r.tierName}}</div>
        <h2 class="result-title">${{r.title}}</h2>
      </div>
      <div class="features-label">מה כלול ברישיון שלך</div>
      <div class="features-grid">
        ${{r.features.map(f =>
          `<div class="feature-item">
            <span class="feature-check">${{f.yes ? '✅' : '❌'}}</span>
            <span>${{f.text}}</span>
          </div>`).join('')}}
      </div>
      <div class="workshop-verdict ${{r.verdictType}}">
        <div class="verdict-body">
          <div class="verdict-title">${{r.verdictTitle}}</div>
          <p>${{r.verdictText}}</p>
        </div>
      </div>
      <div class="result-actions" style="position:relative;display:flex;align-items:center;justify-content:center;min-height:50px;margin-top:0.75rem;padding-bottom:0.5rem;">
        <button class="result-btn primary" onclick="restartQuiz()">⟳ התחל מחדש</button>
        <img src="{iris_img}" style="position:fixed;left:0;bottom:0;height:380px;width:auto;object-fit:contain;z-index:50;pointer-events:none;transform:translateX(-45%);" alt="Iris">
      </div>
    </div>`).join('');
}}

// ── Navigation ──
function goToStep(idx) {{
  if (idx < 0 || idx >= TOTAL) return;
  currentStep = idx;
  document.querySelectorAll('.step').forEach(s => s.classList.remove('active'));
  document.querySelectorAll('.result-screen').forEach(r => r.classList.remove('active'));
  document.getElementById('step' + idx)?.classList.add('active');
  document.getElementById('bottomNav').classList.add('visible');
  updateNav();
  window.scrollTo({{top:0, behavior:'smooth'}});
}}

function updateNav() {{
  document.querySelectorAll('.nav-step').forEach((el,i) => {{
    el.classList.toggle('active', i === currentStep);
    el.classList.toggle('completed', i < currentStep);
  }});
  document.querySelectorAll('.nav-dot').forEach((el,i) => {{
    el.classList.toggle('active', i === currentStep);
  }});
  const pct = ((currentStep) / TOTAL) * 100;
  document.getElementById('progressFill').style.width = pct + '%';
  document.getElementById('btnPrev').classList.toggle('hidden', currentStep === 0);
  document.getElementById('btnNext').classList.add('hidden');
}}

function navPrev() {{ goToStep(currentStep - 1); }}
function navNext() {{ goToStep(currentStep + 1); }}

function selectAnswer(stepIdx, answerIdx) {{
  // אם כבר בחרו — לא מאפשרים שוב
  if (document.querySelector(`#answerGrid${{stepIdx}} .flip-card.flipped`)) return;
  userAnswers[stepIdx] = answerIdx; // שמור תשובה
  const card = document.getElementById(`flip_${{stepIdx}}_${{answerIdx}}`);
  card.classList.add('flipped');
  // גרא כרטיס שני fade out
  const other = document.getElementById(`flip_${{stepIdx}}_${{answerIdx===0?1:0}}`);
  other.style.opacity = '0.35';
  other.style.pointerEvents = 'none';
}}

function handleNext(nextKey) {{
  if (nextKey.startsWith('result_')) {{
    showResult(nextKey);
  }} else {{
    const idx = parseInt(nextKey.replace('q','')) - 1;
    goToStep(idx);
  }}
}}

function showResult(key) {{
  // עדכן features לפי תשובות המשתמש
  const hasCreate        = userAnswers[5] === 0;  // שאלה 6: Create
  const hasOfficeCP      = userAnswers[3] === 0;  // שאלה 4: Copilot בתוך Office
  const hasOffice        = userAnswers[3] === 0;  // שאלה 4: Word/Excel/PowerPoint
  const hasOutlookTeams  = userAnswers[4] === 0;  // שאלה 5: Outlook / Teams
  results[key].features = results[key].features.map(f => {{
    if (f.text.includes('Create')) return {{...f, yes: hasCreate}};
    if (f.text.includes('Copilot') && f.text.includes('Office')) return {{...f, yes: hasOfficeCP}};
    if (f.text.includes('Word') || f.text.includes('PowerPoint')) return {{...f, yes: hasOffice}};
    if (f.text.includes('OneDrive') || f.text.includes('Teams') || f.text.includes('Outlook')) return {{...f, yes: hasOutlookTeams}};
    return f;
  }});
  // בנה מחדש את ה-HTML של מסך התוצאה
  const r = results[key];
  const screen = document.getElementById(key);
  if (screen) {{
    screen.querySelector('.features-grid').innerHTML = r.features.map(f =>
      `<div class="feature-item"><span class="feature-check">${{f.yes ? '✅' : '❌'}}</span><span>${{f.text}}</span></div>`
    ).join('');
  }}
  document.querySelectorAll('.step').forEach(s => s.classList.remove('active'));
  document.querySelectorAll('.result-screen').forEach(r => r.classList.remove('active'));
  document.getElementById(key)?.classList.add('active');
  document.getElementById('progressFill').style.width = '100%';
  document.querySelectorAll('.nav-step').forEach(el => el.classList.add('completed'));
  document.getElementById('bottomNav').classList.remove('visible');
  window.scrollTo({{top:0, behavior:'smooth'}});
  if (key !== 'result_chat_only') launchConfetti();
}}

function startQuiz() {{
  document.getElementById('hero').style.display = 'none';
  const app = document.getElementById('app');
  app.classList.add('visible');
  document.getElementById('topNav').classList.add('visible');
  goToStep(0);
}}

function restartQuiz() {{
  userAnswers = {{}}; // איפוס תשובות
  // איפוס flip cards
  document.querySelectorAll('.flip-card').forEach(c => {{
    c.classList.remove('flipped');
    c.style.opacity = '';
    c.style.pointerEvents = '';
  }});
  document.getElementById('hero').style.display = '';
  document.getElementById('app').classList.remove('visible');
  document.getElementById('topNav').classList.remove('visible');
  document.querySelectorAll('.result-screen').forEach(r => r.classList.remove('active'));
  currentStep = 0;
  window.scrollTo({{top:0, behavior:'smooth'}});
}}

// ── Confetti ──
function launchConfetti() {{
  const canvas = document.getElementById('confetti-canvas');
  const ctx = canvas.getContext('2d');
  canvas.width = window.innerWidth; canvas.height = window.innerHeight;
  const pieces = Array.from({{length:120}}, () => ({{
    x: Math.random()*canvas.width, y: -20,
    r: Math.random()*8+4,
    d: Math.random()*5+2,
    c: ['#13008a','#ff5bc0','#5e17eb','#5ce1e6','#fbbf24'][Math.floor(Math.random()*5)],
    t: Math.random()*Math.PI*2
  }}));
  let frame = 0;
  function draw() {{
    ctx.clearRect(0,0,canvas.width,canvas.height);
    pieces.forEach(p => {{
      ctx.beginPath(); ctx.arc(p.x, p.y, p.r, 0, Math.PI*2);
      ctx.fillStyle = p.c; ctx.fill();
      p.y += p.d; p.x += Math.sin(p.t)*2; p.t += 0.05;
      if (p.y > canvas.height) {{ p.y = -20; p.x = Math.random()*canvas.width; }}
    }});
    if (frame++ < 180) requestAnimationFrame(draw);
    else ctx.clearRect(0,0,canvas.width,canvas.height);
  }}
  draw();
}}

// ── Init ──
buildUI();
document.getElementById('hero').classList.add('animate');
</script>
</body>
</html>'''

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(HTML)

print(f'Done! Written to {OUT}')
print(f'File size: {{len(HTML)//1024}} KB')
