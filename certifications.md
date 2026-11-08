---
layout: page
title: Certifications & Memberships
---

<style>
  .cert-section-title {
    font-size: 1.6rem;
    font-weight: 700;
    margin: 3rem 0 1.5rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid var(--border-color, #333);
    color: var(--text-color, #fff);
  }

  .membership-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
    margin-bottom: 2rem;
  }

  .membership-card {
    background: var(--card-bg, #1e1e1e);
    border: 1px solid var(--border-color, #333);
    border-radius: 10px;
    padding: 1.5rem;
    display: flex;
    align-items: flex-start;
    gap: 1.2rem;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }

  .membership-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.2);
  }

  .membership-logo {
    width: 52px;
    height: 52px;
    border-radius: 10px;
    background: var(--bg-secondary, #2a2a2a);
    border: 1px solid var(--border-color, #444);
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }

  .membership-info h3 {
    margin: 0 0 0.25rem;
    font-size: 1.05rem;
    font-weight: 600;
    color: var(--text-color, #fff);
  }

  .membership-info p {
    margin: 0;
    font-size: 0.88rem;
    color: #a0a0a0;
  }

  .membership-badge {
    display: inline-block;
    margin-top: 0.5rem;
    padding: 0.2rem 0.65rem;
    border-radius: 99px;
    font-size: 0.78rem;
    font-weight: 600;
    background: rgba(30, 66, 159, 0.2);
    color: #8bb4f7;
    border: 1px solid rgba(30, 66, 159, 0.4);
  }

  .membership-badge.orange {
    background: rgba(249, 115, 22, 0.15);
    color: #fb923c;
    border-color: rgba(249, 115, 22, 0.35);
  }

  .coming-soon-card {
    background: var(--card-bg, #1e1e1e);
    border: 1px dashed var(--border-color, #444);
    border-radius: 10px;
    padding: 2.5rem;
    text-align: center;
    color: #555;
    font-size: 0.95rem;
  }
</style>

## Professional Memberships

<div class="membership-grid">

  <!-- IESL -->
  <div class="membership-card">
    <div class="membership-logo" style="background: #fff;">
      <img src="{{ '/assets/images/experience/iesl-logo.png' | relative_url }}" alt="IESL Logo" style="width: 100%; height: 100%; object-fit: contain;">
    </div>
    <div class="membership-info">
      <h3>Institution of Engineers Sri Lanka</h3>
      <p>Student Member</p>
      <span class="membership-badge">IESL</span>
    </div>
  </div>

  <!-- IMechE -->
  <div class="membership-card">
    <div class="membership-logo" style="background: #000; overflow: hidden;">
      <img src="{{ '/assets/images/experience/imeche-sliit-logo.png' | relative_url }}" alt="IMechE SLIIT Logo" style="width: 100%; height: 100%; object-fit: contain;">
    </div>
    <div class="membership-info">
      <h3>Institution of Mechanical Engineers</h3>
      <p>Student Member</p>
      <span class="membership-badge orange">IMechE</span>
    </div>
  </div>

</div>

## Technical Certifications

<div class="coming-soon-card">
  ?? Certifications will be added here as they are earned.
</div>
