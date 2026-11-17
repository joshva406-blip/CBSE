# templates.py

COMMON_CSS = r'''
    :root {
      --primary: #0c2340;
      --primary-dark: #071526;
      --primary-light: #183b63;
      --accent: #f59e0b;
      --accent-hover: #d97706;
      --accent-gold2: #fbbf24;
      --bg-body: #ffffff;
      --bg-surface: #f8fafc;
      --bg-surface-alt: #f1f5f9;
      --border-color: #e2e8f0;
      --border-light: #edf2f7;
      --text-main: #1e293b;
      --text-muted: #64748b;
      --text-white: #ffffff;
      --font-body: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      --font-heading: 'Outfit', 'Inter', sans-serif;
      --shadow-sm: 0 2px 4px rgba(12, 35, 64, 0.04);
      --shadow-md: 0 8px 24px rgba(12, 35, 64, 0.08);
      --shadow-lg: 0 16px 36px rgba(12, 35, 64, 0.12);
      --radius-sm: 6px;
      --radius-md: 12px;
      --radius-lg: 20px;
      --radius-full: 9999px;
      --transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    }
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; font-size: 16px; }
    body { font-family: var(--font-body); color: var(--text-main); background-color: var(--bg-body); line-height: 1.65; overflow-x: hidden; }
    h1, h2, h3, h4, h5, h6 { font-family: var(--font-heading); color: var(--primary); font-weight: 700; line-height: 1.25; }
    a { color: inherit; text-decoration: none; transition: var(--transition); }
    img { max-width: 100%; height: auto; display: block; }
    button, input, select, textarea { font-family: inherit; }
    .container { width: 100%; max-width: 1360px; margin: 0 auto; padding: 0 24px; }
    .section-padding { padding: 70px 0; }
    
    .btn { display: inline-flex; align-items: center; justify-content: center; gap: 8px; font-weight: 600; font-size: 0.94rem; padding: 12px 28px; border-radius: var(--radius-full); cursor: pointer; border: 2px solid transparent; transition: var(--transition); white-space: nowrap; }
    .btn-accent { background-color: var(--accent); color: var(--primary-dark); box-shadow: 0 4px 15px rgba(245, 158, 11, 0.35); }
    .btn-accent:hover { background-color: var(--accent-hover); color: #fff; transform: translateY(-2px); }
    .btn-primary { background-color: var(--primary); color: #fff; }
    .btn-primary:hover { background-color: var(--primary-light); transform: translateY(-2px); }
    .btn-outline { background: transparent; border-color: var(--border-color); color: var(--text-main); }
    .btn-outline:hover { border-color: var(--primary); color: var(--primary); background: rgba(12, 35, 64, 0.04); }
    .btn-outline-white { background: transparent; border-color: rgba(255, 255, 255, 0.4); color: #fff; }
    .btn-outline-white:hover { border-color: #fff; background: rgba(255, 255, 255, 0.12); }

    /* Topbar */
    .topbar { background-color: var(--primary-dark); color: #cbd5e1; font-size: 0.85rem; padding: 9px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.08); position: relative; z-index: 101; }
    .topbar-wrap { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; }
    .topbar-info { display: flex; align-items: center; gap: 20px; flex-wrap: wrap; }
    .topbar-item { display: inline-flex; align-items: center; gap: 7px; }
    .topbar-item svg { width: 14px; height: 14px; fill: var(--accent-gold2); }
    .topbar-item a:hover { color: var(--accent-gold2); }
    .topbar-actions { display: flex; align-items: center; gap: 16px; }
    .topbar-btn { background-color: var(--accent); color: var(--primary-dark); padding: 5px 16px; border-radius: var(--radius-full); font-weight: 700; font-size: 0.78rem; text-transform: uppercase; }
    .topbar-btn:hover { background-color: var(--accent-hover); color: #fff; }

    /* Header & Nav */
    .header { background: #fff; box-shadow: 0 4px 20px rgba(0,0,0,0.06); position: sticky; top: 0; z-index: 100; }
    .header-wrap { display: flex; align-items: center; justify-content: space-between; height: 84px; gap: 16px; }
    .brand-logo { display: flex; align-items: center; gap: 12px; flex-shrink: 0; text-decoration: none; }
    .logo-crest { width: 48px; height: 48px; background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%); border-radius: 12px; display: flex; align-items: center; justify-content: center; color: var(--accent); border: 2px solid var(--accent); box-shadow: 0 4px 12px rgba(12, 35, 64, 0.15); flex-shrink: 0; }
    .logo-crest svg { width: 28px; height: 28px; fill: var(--accent); }
    .brand-text h1 { font-size: 1.28rem; font-weight: 800; color: var(--primary); line-height: 1.15; letter-spacing: -0.3px; white-space: nowrap; }
    .brand-text span { font-size: 0.72rem; color: var(--text-muted); display: block; letter-spacing: 0.5px; font-weight: 600; text-transform: uppercase; white-space: nowrap; }
    
    .nav-menu { display: flex; align-items: center; gap: 4px; list-style: none; margin: 0; padding: 0; flex-wrap: nowrap; flex-shrink: 0; }
    .nav-item { position: relative; flex-shrink: 0; }
    .nav-link { display: inline-flex; align-items: center; gap: 5px; padding: 8px 12px; font-size: 0.92rem; font-weight: 600; color: var(--text-main); border-radius: 8px; white-space: nowrap; line-height: 1; text-decoration: none; transition: var(--transition); }
    .nav-link svg { width: 9px; height: 9px; fill: currentColor; flex-shrink: 0; margin-left: 1px; transition: transform 0.2s ease; }
    .nav-link:hover, .nav-item.active .nav-link { color: var(--accent-hover); background: rgba(245, 158, 11, 0.08); }
    
    .dropdown { position: absolute; top: 100%; left: 0; width: 260px; background: #fff; border-radius: var(--radius-md); box-shadow: var(--shadow-lg); border: 1px solid var(--border-color); padding: 8px 0; opacity: 0; visibility: hidden; transform: translateY(10px); transition: all 0.25s ease; z-index: 110; list-style: none; }
    .nav-item:hover .dropdown { opacity: 1; visibility: visible; transform: translateY(0); }
    .nav-item:hover .nav-link svg { transform: rotate(180deg); }
    .dropdown li a { display: block; padding: 9px 18px; font-size: 0.88rem; color: var(--text-main); font-weight: 500; }
    .dropdown li a:hover { background: var(--bg-surface); color: var(--accent-hover); padding-left: 22px; }
    
    .header-cta { display: flex; align-items: center; gap: 12px; flex-shrink: 0; }
    .hamburger-btn { display: none; background: none; border: none; cursor: pointer; padding: 8px; color: var(--primary); }
    .hamburger-btn svg { width: 26px; height: 26px; fill: currentColor; }

    /* Page Hero Banner */
    .page-hero { background: linear-gradient(135deg, #071526 0%, #0c2340 60%, #153966 100%); color: #fff; padding: 60px 0 50px 0; position: relative; text-align: center; }
    .page-hero::before { content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: radial-gradient(circle at 50% 30%, rgba(245, 158, 11, 0.12) 0%, transparent 65%); pointer-events: none; }
    .breadcrumb { display: inline-flex; align-items: center; gap: 8px; font-size: 0.82rem; color: #94a3b8; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 14px; }
    .breadcrumb a:hover { color: var(--accent-gold2); }
    .page-hero h1 { font-size: 2.85rem; color: #fff; font-weight: 800; margin-bottom: 12px; }
    .gold-divider { width: 60px; height: 4px; background: var(--accent); border-radius: 2px; margin: 14px auto 18px auto; }
    .page-hero p { font-size: 1.1rem; color: #e2e8f0; max-width: 720px; margin: 0 auto; line-height: 1.65; }

    /* Two-Column Page Layout */
    .page-layout { display: grid; grid-template-columns: 1fr 340px; gap: 40px; align-items: start; }
    .content-main { background: #fff; border-radius: var(--radius-lg); border: 1px solid var(--border-color); padding: 40px; box-shadow: var(--shadow-sm); }
    .main-featured-img { width: 100%; height: 420px; object-fit: cover; border-radius: var(--radius-md); margin-bottom: 28px; box-shadow: var(--shadow-md); }
    .content-main h2 { font-size: 1.85rem; color: var(--primary); margin-bottom: 16px; margin-top: 24px; }
    .content-main h2:first-of-type { margin-top: 0; }
    .content-main p { color: #334155; font-size: 1.02rem; line-height: 1.8; margin-bottom: 20px; }
    
    .feature-points-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 30px 0; }
    .point-card { background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 22px; transition: var(--transition); }
    .point-card:hover { border-color: var(--accent); transform: translateY(-3px); box-shadow: var(--shadow-sm); }
    .point-card h4 { font-size: 1.1rem; color: var(--primary); margin-bottom: 8px; display: flex; align-items: center; gap: 8px; }
    .point-card h4 svg { width: 18px; height: 18px; fill: var(--accent); flex-shrink: 0; }
    .point-card p { font-size: 0.92rem; color: var(--text-muted); margin-bottom: 0; line-height: 1.55; }

    .highlight-quote { border-left: 4px solid var(--accent); background: rgba(245, 158, 11, 0.08); padding: 20px 24px; border-radius: 0 var(--radius-md) var(--radius-md) 0; margin: 30px 0; font-size: 1.05rem; font-style: italic; color: var(--primary); font-weight: 500; }

    /* Sidebar */
    .sidebar { display: flex; flex-direction: column; gap: 28px; }
    .widget-box { background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: var(--radius-lg); padding: 28px; box-shadow: var(--shadow-sm); }
    .widget-box h3 { font-size: 1.2rem; color: var(--primary); margin-bottom: 18px; position: relative; padding-bottom: 8px; }
    .widget-box h3::after { content: ''; position: absolute; bottom: 0; left: 0; width: 32px; height: 2px; background: var(--accent); }
    .widget-links { list-style: none; display: flex; flex-direction: column; gap: 10px; }
    .widget-links li a { display: flex; align-items: center; justify-content: space-between; padding: 8px 12px; border-radius: 6px; font-weight: 500; font-size: 0.92rem; color: var(--text-main); background: #fff; border: 1px solid var(--border-light); }
    .widget-links li a:hover, .widget-links li.active a { background: var(--primary); color: #fff; border-color: var(--primary); }
    .admissions-cta-box { background: linear-gradient(135deg, var(--primary) 0%, #153966 100%); color: #fff; border-radius: var(--radius-lg); padding: 32px 24px; text-align: center; }
    .admissions-cta-box h3 { color: #fff; font-size: 1.35rem; margin-bottom: 10px; }
    .admissions-cta-box p { color: #cbd5e1; font-size: 0.9rem; margin-bottom: 20px; line-height: 1.6; }

    /* Footer */
    .footer { background-color: var(--primary-dark); color: #94a3b8; padding-top: 70px; border-top: 1px solid rgba(255, 255, 255, 0.08); font-size: 0.92rem; }
    .footer-grid { display: grid; grid-template-columns: 1.4fr 1fr 1fr 1.2fr; gap: 40px; margin-bottom: 50px; }
    .footer-col h3 { color: #fff; font-size: 1.15rem; margin-bottom: 20px; position: relative; padding-bottom: 10px; }
    .footer-col h3::after { content: ''; position: absolute; bottom: 0; left: 0; width: 36px; height: 2px; background: var(--accent); }
    .footer-links { list-style: none; display: flex; flex-direction: column; gap: 10px; }
    .footer-links li a { color: #cbd5e1; display: inline-flex; align-items: center; gap: 6px; }
    .footer-links li a:hover { color: var(--accent-gold2); transform: translateX(4px); }
    .footer-contact-item { display: flex; align-items: flex-start; gap: 12px; color: #cbd5e1; line-height: 1.5; margin-bottom: 12px; }
    .footer-contact-item svg { width: 16px; height: 16px; fill: var(--accent-gold2); flex-shrink: 0; margin-top: 3px; }
    .sub-footer { background-color: #030a13; padding: 22px 0; border-top: 1px solid rgba(255, 255, 255, 0.05); font-size: 0.84rem; }
    .sub-footer-wrap { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px; }
    .sub-footer-links { display: flex; gap: 20px; }
    .sub-footer-links a:hover { color: var(--accent-gold2); }

    /* Floating Utilities */
    .floating-whatsapp { position: fixed; bottom: 24px; right: 24px; width: 58px; height: 58px; background-color: #25d366; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #fff; box-shadow: 0 8px 24px rgba(37, 211, 102, 0.4); z-index: 99; }
    .floating-whatsapp svg { width: 32px; height: 32px; fill: #fff; }
    .back-to-top { position: fixed; bottom: 24px; left: 24px; width: 44px; height: 44px; background-color: var(--primary); color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 90; opacity: 0; visibility: hidden; transition: var(--transition); border: 1px solid rgba(255,255,255,0.2); }
    .back-to-top.show { opacity: 1; visibility: visible; }

    @media (max-width: 1024px) {
      .nav-menu { display: none; }
      .hamburger-btn { display: block; }
      .page-layout { grid-template-columns: 1fr; }
      .feature-points-grid { grid-template-columns: 1fr; }
      .footer-grid { grid-template-columns: 1fr 1fr; }
    }
    @media (max-width: 768px) {
      .topbar-wrap { justify-content: center; }
      .footer-grid { grid-template-columns: 1fr; }
      .page-hero h1 { font-size: 2.2rem; }
      .main-featured-img { height: 260px; }
    }
'''

def get_header_html(active_link=""):
    return f'''
  <aside class="topbar">
    <div class="container topbar-wrap">
      <div class="topbar-info">
        <div class="topbar-item">
          <svg viewBox="0 0 24 24"><path d="M6.62 10.79a15.053 15.053 0 006.59 6.59l2.2-2.2a1 1 0 011.02-.24 11.72 11.72 0 003.68.59 1 1 0 011 1V20a1 1 0 01-1 1A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1 11.72 11.72 0 00.59 3.68 1 1 0 01-.24 1.02l-2.23 2.09z"/></svg>
          <a href="tel:04222271367">0422-2271367</a> &bull; <a href="tel:+919443022345">+91 94430 22345</a>
        </div>
        <div class="topbar-item">
          <svg viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
          <a href="mailto:admissions@luffyinternationalschool.edu">admissions@luffyinternationalschool.edu</a>
        </div>
        <div class="topbar-item">
          <svg viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
          <span>Ondipudur, Coimbatore - 641016</span>
        </div>
      </div>
      <div class="topbar-actions">
        <a href="contact.html#map" class="topbar-link">Location</a>
        <a href="contact.html" class="topbar-link">Parent Login</a>
        <a href="contact.html" class="topbar-btn">Apply Now</a>
      </div>
    </div>
  </aside>

  <header class="header">
    <div class="container header-wrap">
      <a href="index.html" class="brand-logo">
        <div class="logo-crest">
          <svg viewBox="0 0 24 24"><path d="M12 3L1 9l11 6 9-4.91V17h2V9L12 3z M5 13.18v4L12 21l7-3.82v-4L12 17l-7-3.82z"/></svg>
        </div>
        <div class="brand-text">
          <h1>Luffy International School</h1>
        </div>
      </a>

      <nav>
        <ul class="nav-menu">
          <li class="nav-item {'active' if active_link=='home' else ''}"><a href="index.html" class="nav-link">Home</a></li>
          
          <li class="nav-item {'active' if active_link=='about' else ''}">
            <a href="about.html" class="nav-link">About Us <svg viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg></a>
            <ul class="dropdown">
              <li><a href="about.html">Overview &amp; Heritage</a></li>
              <li><a href="about.html#leadership">Principal's Address</a></li>
              <li><a href="about.html#why-choose">Why Choose Luffy</a></li>
              <li><a href="about.html#notices">Notice Board &amp; Circulars</a></li>
            </ul>
          </li>

          <li class="nav-item {'active' if active_link=='curriculum' else ''}">
            <a href="curriculum.html" class="nav-link">Curriculum <svg viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg></a>
            <ul class="dropdown">
              <li><a href="foundation-stage.html">Foundation (Nursery - Gr 2)</a></li>
              <li><a href="preparatory-stage.html">Preparatory (Grades 3 - 5)</a></li>
              <li><a href="middle-school.html">Middle School (Grades 6 - 8)</a></li>
              <li><a href="senior-secondary.html">Senior Secondary (Gr 9 - 12)</a></li>
            </ul>
          </li>

          <li class="nav-item {'active' if active_link in ['beyond', 'academics'] else ''}">
            <a href="post-school-activities.html" class="nav-link">Academics <svg viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg></a>
            <ul class="dropdown">
              <li><a href="post-school-activities.html">Post-School Activities</a></li>
              <li><a href="celebrations-cultural-day.html">Celebrations &amp; Cultural Day</a></li>
              <li><a href="career-counselling.html">Career Counselling</a></li>
              <li><a href="cbse-cluster-athletics.html">CBSE Cluster &amp; Athletics</a></li>
              <li><a href="guest-lectures-hackathons.html">Guest Lectures &amp; Hackathons</a></li>
            </ul>
          </li>

          <li class="nav-item {'active' if active_link=='facilities' else ''}">
            <a href="advanced-stem-labs.html" class="nav-link">Facilities <svg viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg></a>
            <ul class="dropdown">
              <li><a href="advanced-stem-labs.html">Advanced STEM Labs</a></li>
              <li><a href="synthetic-sports-arena.html">Synthetic Sports Arena</a></li>
              <li><a href="central-library.html">Central Library</a></li>
              <li><a href="performing-arts-studio.html">Performing Arts Studio</a></li>
              <li><a href="smart-coding-innovation-hub.html">Smart Coding Innovation Hub</a></li>
            </ul>
          </li>

          <li class="nav-item {'active' if active_link=='blog' else ''}"><a href="blog.html" class="nav-link">Blog</a></li>
          <li class="nav-item {'active' if active_link=='contact' else ''}"><a href="contact.html" class="nav-link">Contact</a></li>
        </ul>
      </nav>

      <div class="header-cta">
        <a href="contact.html" class="btn btn-accent" style="padding: 9px 22px; font-size: 0.88rem;">Enquire Now</a>
        <button class="hamburger-btn" onclick="toggleMobileNav()" aria-label="Toggle Navigation">
          <svg viewBox="0 0 24 24"><path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z"/></svg>
        </button>
      </div>
    </div>
  </header>
'''

def get_footer_html():
    return '''
  <footer class="footer">
    <div class="container footer-grid">
      <div class="footer-col">
        <h3>About Us</h3>
        <p>Luffy International School is operated and managed by Luffy Educational Trust, committed to delivering holistic, globally benchmarked education in Ondipudur, Coimbatore.</p>
        <div style="font-size:0.84rem;color:#cbd5e1;margin-bottom:18px;">
          <strong>CBSE Affiliation No:</strong> 1930452<br>
          <strong>School Code:</strong> 55341 &bull; ISO 9001:2015
        </div>
      </div>

      <div class="footer-col">
        <h3>Curriculum Stages</h3>
        <ul class="footer-links">
          <li><a href="foundation-stage.html">&rsaquo; Foundation Stage (Nursery - Gr 2)</a></li>
          <li><a href="preparatory-stage.html">&rsaquo; Preparatory Stage (Grades 3 - 5)</a></li>
          <li><a href="middle-school.html">&rsaquo; Middle School (Grades 6 - 8)</a></li>
          <li><a href="senior-secondary.html">&rsaquo; Senior Secondary (Grades 9 - 12)</a></li>
          <li><a href="curriculum.html">&rsaquo; All Curriculum Framework</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h3>Campus Facilities</h3>
        <ul class="footer-links">
          <li><a href="advanced-stem-labs.html">&rsaquo; Advanced STEM Labs</a></li>
          <li><a href="synthetic-sports-arena.html">&rsaquo; Synthetic Sports Arena</a></li>
          <li><a href="central-library.html">&rsaquo; Two-Story Library</a></li>
          <li><a href="performing-arts-studio.html">&rsaquo; Performing Arts Studio</a></li>
          <li><a href="smart-coding-innovation-hub.html">&rsaquo; Smart Coding Hub</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h3>Contact RPS Campus</h3>
        <div class="footer-contact-item">
          <svg viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
          <span>Trichy Main Road, Ondipudur, Coimbatore &ndash; 641016, Tamil Nadu.</span>
        </div>
        <div class="footer-contact-item">
          <svg viewBox="0 0 24 24"><path d="M6.62 10.79a15.053 15.053 0 006.59 6.59l2.2-2.2a1 1 0 011.02-.24 11.72 11.72 0 003.68.59 1 1 0 011 1V20a1 1 0 01-1 1A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1 11.72 11.72 0 00.59 3.68 1 1 0 01-.24 1.02l-2.23 2.09z"/></svg>
          <span>0422-2271367 &bull; +91 94430 22345</span>
        </div>
        <div class="footer-contact-item">
          <svg viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
          <span>admissions@luffyinternationalschool.edu</span>
        </div>
      </div>
    </div>

    <div class="sub-footer">
      <div class="container sub-footer-wrap">
        <div>&copy; 2026 Luffy International School. All Rights Reserved.</div>
        <div class="sub-footer-links">
          <a href="#">Privacy Policy</a>
          <a href="#">Terms &amp; Conditions</a>
          <a href="#">CBSE SARAS</a>
          <a href="contact.html">Contact Us</a>
        </div>
      </div>
    </div>
  </footer>

  <a href="https://wa.me/919443022345?text=Hello%20Luffy%20International%20School%2C%20I%20would%20like%20to%20enquire%20about%20admissions." target="_blank" rel="noopener noreferrer" class="floating-whatsapp" aria-label="Chat on WhatsApp">
    <svg viewBox="0 0 24 24"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0012.04 2zm.01 1.67c2.2 0 4.26.86 5.82 2.42a8.225 8.225 0 012.41 5.83c0 4.54-3.7 8.24-8.24 8.24-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.196 8.196 0 01-1.26-4.38c0-4.54 3.7-8.24 8.24-8.24zm4.52 11.66c-.25-.13-1.47-.72-1.7-.81-.23-.08-.39-.13-.56.13-.17.25-.64.81-.79.97-.14.17-.29.19-.54.06-.25-.13-1.06-.39-2.02-1.25-.75-.67-1.26-1.5-1.4-1.75-.15-.25-.02-.39.11-.51.11-.11.25-.29.37-.44.12-.14.17-.25.25-.42.08-.17.04-.31-.02-.44-.06-.13-.56-1.35-.77-1.85-.2-.49-.41-.42-.56-.43h-.48c-.17 0-.44.06-.67.31-.23.25-.88.86-.88 2.1 0 1.24.9 2.44 1.03 2.61.12.17 1.77 2.71 4.3 3.79.6.26 1.07.41 1.44.53.61.19 1.16.17 1.6.1.49-.07 1.47-.6 1.68-1.18.21-.58.21-1.07.15-1.18-.06-.11-.22-.18-.47-.3z"/></svg>
  </a>

  <div class="back-to-top" id="backToTop" onclick="window.scrollTo({top: 0, behavior: 'smooth'})" aria-label="Scroll to top">
    <svg viewBox="0 0 24 24" width="22" height="22" fill="currentColor"><path d="M7.41 15.41L12 10.83l4.59 4.58L18 14l-6-6-6 6z"/></svg>
  </div>

  <script>
    window.addEventListener('scroll', () => {
      const btt = document.getElementById('backToTop');
      if (btt && window.scrollY > 400) btt.classList.add('show');
      else if (btt) btt.classList.remove('show');
    });
    function toggleMobileNav() {
      const menu = document.querySelector('.nav-menu');
      if (menu.style.display === 'flex') menu.style.display = 'none';
      else {
        menu.style.display = 'flex';
        menu.style.flexDirection = 'column';
        menu.style.position = 'absolute';
        menu.style.top = '84px';
        menu.style.left = '0';
        menu.style.right = '0';
        menu.style.background = '#fff';
        menu.style.padding = '20px';
        menu.style.boxShadow = '0 10px 25px rgba(0,0,0,0.15)';
      }
    }
  </script>
'''
