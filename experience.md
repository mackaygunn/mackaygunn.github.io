---
layout: page
title: Experience
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
        <li><strong>Heavy Machinery Diagnostics:</strong> Restored operational readiness across earthmoving and lifting fleets by diagnosing and repairing complex drivetrain, high-pressure hydraulic, and pneumatic control failures.</li>
        <li><strong>Diesel Powertrain Integration:</strong> Achieved 100% field commissioning success on diesel prime movers by executing complete integrations, calibrating hydrostatic linkages, and verifying mechanical tolerances under dynamic load.</li>
        <li><strong>Plant Equipment Overhaul:</strong> Extended lifecycle of small plant machinery (Sakai vibratory rollers, Simpedil rebar benders, electric hoists) by executing comprehensive mechanical and electrical overhauls.</li>
        <li><strong>Industrial Electrical Diagnostics:</strong> Resolved critical logic circuit failures on 3-phase control panels and AC induction motors by performing precision teardowns, wire-mapping, and ground fault diagnostics.</li>
        <li><strong>Power Transmission Repair:</strong> Restored peak cutting torque to heavy-duty rebar equipment by diagnosing and repairing multi-stage spur gear reduction trains and V-belt drive systems.</li>
        <li><strong>Maintenance Management:</strong> Maintained strict adherence to 500-hour preventative maintenance schedules by managing workshop parts inventory and processing work orders through ERP software.</li>
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

</div>
