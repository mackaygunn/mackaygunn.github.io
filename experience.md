---
layout: page
title: Experience
permalink: /experience/
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
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }
  
  .timeline-content:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 15px rgba(0,0,0,0.2);
  }

  .timeline-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--text-color, #fff);
    margin-bottom: 0.25rem;
  }

  .timeline-company {
    font-size: 1.15rem;
    font-weight: 500;
    color: #8bb4f7;
    margin-bottom: 0.5rem;
  }

  .timeline-date {
    display: inline-block;
    background: rgba(255, 255, 255, 0.1);
    color: var(--text-muted, #aaa);
    padding: 0.3rem 0.8rem;
    border-radius: 99px;
    font-size: 0.85rem;
    font-weight: 600;
    margin-bottom: 1.5rem;
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
  }
</style>

<div class="timeline">
  
  <!-- ICC Plant & Equipment -->
  <div class="timeline-item">
    <div class="timeline-dot"></div>
    <div class="timeline-content">
      <h3 class="timeline-title">Mechanical Engineering Industrial Trainee</h3>
      <div class="timeline-company">International Construction Consortium (Pvt) Ltd (ICC) – Plant & Equipment (P&E) Division, Kaduwela</div>
      <div class="timeline-date">July 20, 2026 – September 14, 2026</div>
      
      <ul class="timeline-responsibilities">
        <li>Diagnosed and repaired heavy plant machinery drivetrains, high-pressure hydraulic circuits, and pneumatic control systems across earthmoving and lifting equipment fleets.</li>
        <li>Executed complete diesel prime mover integrations and calibrated hydrostatic pump linkages, verifying mechanical tolerances through dynamic field commissioning under load.</li>
        <li>Overhauled and maintained small plant machinery, including Sakai walk-behind vibratory rollers, Simpedil rebar bending machines, and portable electric builder's hoists.</li>
        <li>Performed precision electrical teardowns, wire-mapping, and ground fault diagnostics on 3-phase industrial control panels and AC induction motors to resolve logic circuit failures.</li>
        <li>Diagnosed and repaired mechanical power transmission systems, including multi-stage spur gear reduction trains and V-belt drives on heavy-duty rebar cutting equipment.</li>
        <li>Managed workshop parts inventory and processed mechanical work orders using Enterprise Resource Planning (ERP) software to strictly track 500-hour preventative maintenance schedules.</li>
      </ul>

      <!-- Link hardcoded to expect the PDF in the assets/docs folder -->
      <a href="{{ '/assets/docs/industrial-training-logbook.pdf' | relative_url }}" target="_blank" class="logbook-btn">
        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="12" y1="18" x2="12" y2="12"></line><line x1="9" y1="15" x2="15" y2="15"></line></svg>
        View Training Logbook
      </a>
    </div>
  </div>

</div>
