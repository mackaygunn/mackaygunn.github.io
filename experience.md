---
layout: page
title: Professional & Leadership Experience
---

<style>
  .timeline {
    position: relative;
    max-width: 900px;
    margin: 3rem auto;
    padding-left: 2rem;
  }
  
  /* Vertical Line */
  .timeline::before {
    content: '';
    position: absolute;
    top: 0;
    left: 8px; /* Center of the 16px dot */
    height: 100%;
    width: 2px;
    background: var(--border-color, #333);
  }

  .timeline-item {
    position: relative;
    margin-bottom: 3rem;
  }

  /* The Glowing Dot */
  .timeline-dot {
    position: absolute;
    top: 6px;
    left: -2rem;
    width: 18px;
    height: 18px;
    border-radius: 50%;
    background: var(--accent-color, #1e429f);
    border: 3px solid var(--bg-color, #121212);
    box-shadow: 0 0 10px var(--accent-color, #1e429f);
    z-index: 2;
  }

  .timeline-content {
    background: var(--card-bg, #1e1e1e);
    border: 1px solid var(--border-color, #333);
    border-radius: 8px;
    padding: 2rem;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
    cursor: pointer;
  }
  
  .timeline-content:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 15px rgba(0,0,0,0.2);
    border-color: #555;
  }

  .card-details {
    display: none;
    margin-top: 1.5rem;
    padding-top: 1.5rem;
    border-top: 1px solid var(--border-color, #333);
    animation: fadeIn 0.3s ease-in-out;
  }

  .timeline-content.expanded .card-details {
    display: block;
  }

  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(-5px); }
    to { opacity: 1; transform: translateY(0); }
  }

  .timeline-content.expanded .expand-icon {
    transform: rotate(180deg);
  }

  .timeline-header-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.5rem;
  }

  .timeline-title {
    font-size: 1.8rem;
    font-weight: 700;
    color: var(--text-color, #fff);
    margin-bottom: 0.25rem;
    margin-top: 0;
  }

  .timeline-company-container {
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .company-logo {
    width: 24px;
    height: 24px;
    border-radius: 4px;
    background: #fff;
    padding: 2px;
    object-fit: contain;
  }

  .timeline-company {
    font-size: 1.05rem;
    font-weight: 500;
    color: #a0a0a0;
    margin: 0;
  }

  .timeline-date {
    display: inline-block;
    background: #2a2a2a;
    color: #b0b0b0;
    padding: 0.4rem 1rem;
    border-radius: 99px;
    font-size: 0.9rem;
    font-weight: 500;
  }

  .timeline-responsibilities {
    color: var(--text-secondary, #ddd);
    font-size: 0.95rem;
    line-height: 1.6;
    margin-bottom: 1.5rem;
    padding-left: 1.2rem;
  }

  .timeline-responsibilities li {
    margin-bottom: 0.8rem;
  }

  .timeline-responsibilities strong {
    color: var(--text-color, #fff);
  }

  .logbook-btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: transparent;
    color: var(--text-color, #fff);
    border: 1px solid var(--border-color, #555);
    padding: 0.6rem 1.2rem;
    border-radius: 6px;
    text-decoration: none;
    font-weight: 500;
    font-size: 0.9rem;
    transition: all 0.2s ease;
  }
  
  .logbook-btn:hover {
    background: rgba(255, 255, 255, 0.05);
    border-color: #8bb4f7;
    color: #8bb4f7;
  }

  /* Mini Gallery for Experience */
  .timeline-gallery {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
    gap: 10px;
    margin-top: 1.5rem;
    margin-bottom: 1.5rem;
  }
  .timeline-gallery img {
    width: 100%;
    height: 120px;
    object-fit: cover;
    border-radius: 6px;
    border: 1px solid var(--border-color, #444);
    transition: transform 0.2s ease;
  }
  .timeline-gallery img:hover {
    transform: scale(1.05);
  }

  /* Tech Stack Pills */
  .tech-stack-footer {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 1.5rem;
    padding-top: 1.5rem;
    border-top: 1px solid var(--border-color, #333);
  }

  .tech-stack-footer .tag {
    background: var(--bg-secondary, #2a2a2a);
    color: var(--text-color, #eee);
    padding: 0.3rem 0.75rem;
    border-radius: 99px;
    font-size: 0.8rem;
    font-weight: 600;
    border: 1px solid var(--border-color, #444);
  }

  @media (max-width: 768px) {
    .timeline {
      padding-left: 1.5rem;
    }
    .timeline-dot {
      left: -1.5rem;
    }
    .timeline::before {
      left: 7px;
    }
    .timeline-content {
      padding: 1.5rem;
    }
    .timeline-header-container {
      flex-direction: column;
      gap: 10px;
    }
  }
</style>

<div class="timeline">
  
  <!-- ICC Plant & Equipment -->
  <div class="timeline-item">
    <div class="timeline-dot"></div>
    <div class="timeline-content" onclick="this.classList.toggle('expanded')">
      
      <div class="card-summary">
        <div class="timeline-header-container">
          <h2 class="timeline-title">Mechanical Engineering Intern</h2>
          <div style="display: flex; align-items: center; gap: 1rem;">
            <div class="timeline-date">July 2026 – Sept 2026</div>
            <svg class="expand-icon" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--text-secondary, #888)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="transition: transform 0.3s ease;"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </div>
        </div>
        
        <div class="timeline-company-container">
          <img src="{{ '/assets/images/experience/icc-logo.png' | relative_url }}" alt="ICC Logo" class="company-logo">
          <h3 class="timeline-company">International Construction Consortium (Pvt) Ltd – Plant & Equipment Div.</h3>
        </div>
      </div>
      
      <div class="card-details">
        <ul class="timeline-responsibilities">
          <li>Gained structured exposure to a professional industrial environment, measured by documented repair closure across 10+ heavy plant equipment types including crawler cranes, wheel loaders, forklifts, and rebar cutters, by completing an 8-week industrial attachment at a leading Sri Lankan construction company.</li>
          <li>Restored a ZL30H Wheel Loader to full operational service, measured by return-to-operation sign-off, by executing a complete drivetrain overhaul covering Cummins 6BT engine installation, planetary final drive rebuild, and preventive maintenance checks on the cooling and hydraulic systems.</li>
          <li>Resolved an active hydraulic leak on a Tadano TR-250 rough terrain crane, measured by leak-free multi-stage boom extension under load, by fault-isolating and repairing the rotary union on the telescopic boom hose reel — demonstrating motivated, hands-on problem-solving in a live industrial environment.</li>
          <li>Developed hands-on competency across hydraulic fault isolation, pneumatic diagnostics, precision lathe machining, and electronic control panel inspection — applied across diverse heavy plant including cranes, compressors, and generator sets across a fully operational heavy plant workshop.</li>
        </ul>

      <!-- Experience Image Gallery (Images lazy-loaded and compressed) -->
      <div class="timeline-gallery">
        <img src="{{ '/assets/images/experience/icc-1.jpg?v=2' | relative_url }}" alt="Industry Training Photo 1" loading="lazy">
        <img src="{{ '/assets/images/experience/icc-2.jpg?v=2' | relative_url }}" alt="Industry Training Photo 2" loading="lazy">
        <img src="{{ '/assets/images/experience/icc-3.jpg?v=2' | relative_url }}" alt="Industry Training Photo 3" loading="lazy">
        <img src="{{ '/assets/images/experience/icc-4.jpg?v=2' | relative_url }}" alt="Industry Training Photo 4" loading="lazy">
      </div>

      <!-- Link hardcoded to expect the PDF in the assets/docs folder -->
      <a href="{{ '/assets/docs/industrial-training-logbook.pdf' | relative_url }}" target="_blank" class="logbook-btn" onclick="event.stopPropagation()">
        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="12" y1="18" x2="12" y2="12"></line><line x1="9" y1="15" x2="15" y2="15"></line></svg>
        View Training Logbook
      </a>

      <!-- Tech Stack Footer -->
      <div class="tech-stack-footer">
        <span class="tag">Fluid Power Systems</span>
        <span class="tag">ERP Software</span>
        <span class="tag">Diesel Prime Movers</span>
        <span class="tag">Electro-Pneumatics</span>
        <span class="tag">3-Phase Industrial Circuits</span>
        <span class="tag">Power Transmission</span>
      </div>
      
      </div>

    </div>
  </div>

  <!-- IESL Student Chapter -->
  <div class="timeline-item">
    <div class="timeline-dot"></div>
    <div class="timeline-content" onclick="this.classList.toggle('expanded')">

      <div class="card-summary">
        <div class="timeline-header-container">
          <h2 class="timeline-title">Assistant Secretary</h2>
          <div style="display: flex; align-items: center; gap: 1rem;">
            <div class="timeline-date">2026 / 2027</div>
            <svg class="expand-icon" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--text-secondary, #888)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="transition: transform 0.3s ease;"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </div>
        </div>

        <div class="timeline-company-container">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--accent-color, #1e429f)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
          <h3 class="timeline-company">IESL Student Chapter – SLIIT</h3>
        </div>
      </div>

      <div class="card-details">
        <ul class="timeline-responsibilities">
          <li>Elected as <strong>Assistant Secretary</strong> for the Institution of Engineers Sri Lanka (IESL) Student Chapter at SLIIT for the academic year 2026/2027, representing the chapter's student body in a formal administrative capacity.</li>
          <li>Responsible for managing official correspondence, coordinating chapter meetings, maintaining records, and supporting the Secretary in the smooth operation of the student chapter's activities and events.</li>
        </ul>

        <!-- Tech Stack Footer -->
        <div class="tech-stack-footer">
          <span class="tag">Leadership</span>
          <span class="tag">Administration</span>
          <span class="tag">Event Coordination</span>
          <span class="tag">IESL</span>
        </div>
      </div>

    </div>
  </div>

  <!-- Professional Memberships -->
  <div class="timeline-item">
    <div class="timeline-dot" style="background: var(--accent-orange, #f97316); box-shadow: 0 0 10px var(--accent-orange, #f97316);"></div>
    <div class="timeline-content">

      <div class="card-summary">
        <div class="timeline-header-container">
          <h2 class="timeline-title">Professional Memberships</h2>
        </div>
      </div>

      <div style="display: flex; flex-wrap: wrap; gap: 1.5rem; margin-top: 1rem;">

        <!-- IESL -->
        <div style="display: flex; align-items: flex-start; gap: 1rem; flex: 1; min-width: 220px;">
          <div style="width: 44px; height: 44px; background: var(--bg-secondary, #2a2a2a); border: 1px solid var(--border-color, #444); border-radius: 8px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
            <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--accent-color, #1e429f)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg>
          </div>
          <div>
            <p style="margin: 0; font-weight: 600; color: var(--text-color, #fff);">Institution of Engineers Sri Lanka</p>
            <p style="margin: 0.2rem 0 0; font-size: 0.9rem; color: #a0a0a0;">Student Member · IESL</p>
          </div>
        </div>

        <!-- IMechE -->
        <div style="display: flex; align-items: flex-start; gap: 1rem; flex: 1; min-width: 220px;">
          <div style="width: 44px; height: 44px; background: var(--bg-secondary, #2a2a2a); border: 1px solid var(--border-color, #444); border-radius: 8px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
            <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--accent-orange, #f97316)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M12 1v4M12 19v4M4.22 4.22l2.83 2.83M16.95 16.95l2.83 2.83M1 12h4M19 12h4M4.22 19.78l2.83-2.83M16.95 7.05l2.83-2.83"/></svg>
          </div>
          <div>
            <p style="margin: 0; font-weight: 600; color: var(--text-color, #fff);">Institution of Mechanical Engineers</p>
            <p style="margin: 0.2rem 0 0; font-size: 0.9rem; color: #a0a0a0;">Student Member · IMechE</p>
          </div>
        </div>

      </div>
    </div>
  </div>

</div>
