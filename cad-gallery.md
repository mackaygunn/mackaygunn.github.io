---
layout: page
title: Design & Simulation Gallery
permalink: /cad-gallery/
---

<style>
  .gallery-layout {
    display: flex;
    gap: 2.5rem;
    align-items: flex-start;
    flex-wrap: wrap;
    margin-top: 1rem;
  }
  .sidebar-filters {
    flex: 0 0 220px;
    position: sticky;
    top: 100px;
  }
  .sidebar-filters .filter-controls {
    display: flex;
    flex-direction: column;
    gap: 0.8rem;
    background: var(--card-bg, #1e1e1e);
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid var(--border-color, #333);
  }
  .sidebar-filters .filter-btn {
    width: 100%;
    text-align: left;
    padding: 0.8rem 1rem;
    border-radius: 6px;
  }
  .gallery-main {
    flex: 1;
    min-width: 300px;
  }
  @media (max-width: 768px) {
    .sidebar-filters {
      position: static;
      flex: 1 1 100%;
      margin-bottom: 1rem;
    }
    .sidebar-filters .filter-controls {
      flex-direction: row;
      flex-wrap: wrap;
      justify-content: center;
      padding: 1rem;
    }
    .sidebar-filters .filter-btn {
      width: auto;
      text-align: center;
    }
  }
</style>

<div class="gallery-layout">
  <aside class="sidebar-filters">
    <div class="filter-controls">
      <button class="filter-btn active" data-filter="*">All Projects</button>
      <button class="filter-btn" data-filter="autocad">AutoCAD</button>
      <button class="filter-btn" data-filter="solidworks">SolidWorks</button>
      <button class="filter-btn" data-filter="matlab">MATLAB</button>
      <button class="filter-btn" data-filter="programming">Programming</button>
    </div>
  </aside>

  <main class="gallery-main">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2rem;">
      {% for work in site.data.technical_works %}
      <div class="project-card {{ work.software | downcase }}" style="border: 1px solid var(--border-color, #333); border-radius: 6px; overflow: hidden; background: var(--card-bg, #1e1e1e); display: flex; flex-direction: column;">
        <div style="height: 220px; background: var(--bg-color, #121212); display: flex; align-items: center; justify-content: center; border-bottom: 1px solid var(--border-color, #333); overflow: hidden; padding: 0.5rem;">
          <a href="{{ work.image_path | relative_url }}" target="_blank" style="display: flex; align-items: center; justify-content: center; width: 100%; height: 100%;" title="Click to view full size">
            <img src="{{ work.image_path | relative_url }}" alt="{{ work.title }}" style="max-width: 100%; max-height: 100%; object-fit: contain; border-radius: 4px;">
          </a>
        </div>
        
        <div style="padding: 1.5rem; flex-grow: 1; display: flex; flex-direction: column;">
          <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
            <h3 style="margin: 0; font-size: 1.2rem; color: var(--text-color, #fff);">{{ work.title }}</h3>
            <span style="background: rgba(30, 66, 159, 0.3); color: #8bb4f7; font-size: 0.75rem; font-weight: bold; padding: 3px 8px; border-radius: 4px;">{{ work.software }}</span>
          </div>
          
          {% if work.engineering_intent %}
          <p style="color: var(--text-muted, #aaa); font-size: 0.95rem; line-height: 1.6; margin-bottom: 1.5rem; flex-grow: 1;">{{ work.engineering_intent }}</p>
          {% endif %}
          
          {% if work.technical_skills %}
          <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: auto;">
            {% for skill in work.technical_skills %}
              <span style="background: rgba(255,255,255,0.1); color: var(--text-muted, #ddd); font-size: 0.8rem; padding: 4px 10px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.2);">{{ skill }}</span>
            {% endfor %}
          </div>
          {% endif %}
        </div>
      </div>
      {% endfor %}
    </div>
  </main>
</div>
