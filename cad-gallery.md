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
    margin-top: 2rem;
  }
  @media (min-width: 769px) {
    .gallery-layout {
      /* Break out of the centered wrapper to take up the full screen width */
      width: 94vw;
      margin-left: calc(-47vw + 50%);
    }
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
  .gallery-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1.5rem;
  }
  
  /* Lightbox Styles */
  #lightbox {
    display: none;
    position: fixed;
    z-index: 9999;
    top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0,0,0,0.9);
    align-items: center;
    justify-content: center;
  }
  #lightbox.active {
    display: flex;
  }
  #lightbox img {
    max-width: 90%;
    max-height: 90vh;
    border-radius: 8px;
    box-shadow: 0 5px 25px rgba(0,0,0,0.5);
  }
  #lightbox .close-btn {
    position: absolute;
    top: 20px;
    right: 30px;
    color: white;
    font-size: 40px;
    font-weight: bold;
    cursor: pointer;
    line-height: 1;
  }
  
  @media (max-width: 1400px) { .gallery-grid { grid-template-columns: repeat(3, 1fr); } }
  @media (max-width: 1000px) { .gallery-grid { grid-template-columns: repeat(2, 1fr); } }
  @media (max-width: 650px) { .gallery-grid { grid-template-columns: repeat(1, 1fr); } }
  
  @media (max-width: 768px) {
    .sidebar-filters {
      position: static;
      flex: 1 1 100%;
      margin-bottom: 1rem;
      margin-left: 0;
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
    <div class="gallery-grid">
      {% for work in site.data.technical_works %}
      <div class="project-card {{ work.software | downcase }}" style="border: 1px solid var(--border-color, #333); border-radius: 6px; overflow: hidden; background: var(--card-bg, #1e1e1e); display: flex; flex-direction: column;">
        <div style="height: 240px; background: var(--bg-color, #121212); display: flex; align-items: center; justify-content: center; border-bottom: 1px solid var(--border-color, #333); overflow: hidden; padding: 0.5rem;">
          <a href="{{ work.image_path | relative_url }}" onclick="openLightbox('{{ work.image_path | relative_url }}'); return false;" style="display: flex; align-items: center; justify-content: center; width: 100%; height: 100%;" title="Click to view full size">
            <img src="{{ work.image_path | relative_url }}" alt="{{ work.title }}" style="max-width: 100%; max-height: 100%; object-fit: contain; border-radius: 4px;">
          </a>
        </div>
        
        <div style="padding: 1.2rem; flex-grow: 1; display: flex; flex-direction: column;">
          <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
            <h3 style="margin: 0; font-size: 1.05rem; color: var(--text-color, #fff);">{{ work.title }}</h3>
            <span style="background: rgba(30, 66, 159, 0.3); color: #8bb4f7; font-size: 0.7rem; font-weight: bold; padding: 2px 6px; border-radius: 4px; margin-left: 8px;">{{ work.software }}</span>
          </div>
          
          {% if work.engineering_intent %}
          <p style="color: var(--text-muted, #aaa); font-size: 0.85rem; line-height: 1.5; margin-bottom: 1rem; flex-grow: 1;">{{ work.engineering_intent }}</p>
          {% endif %}
          
          {% if work.technical_skills %}
          <div style="display: flex; flex-wrap: wrap; gap: 4px; margin-top: auto;">
            {% for skill in work.technical_skills %}
              <span style="background: rgba(255,255,255,0.1); color: var(--text-muted, #ddd); font-size: 0.75rem; padding: 3px 8px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.2);">{{ skill }}</span>
            {% endfor %}
          </div>
          {% endif %}
        </div>
      </div>
      {% endfor %}
    </div>
  </main>
</div>

<!-- Lightbox Modal -->
<div id="lightbox" onclick="closeLightbox(event)">
  <span class="close-btn" onclick="closeLightbox(event)">&times;</span>
  <img id="lightbox-img" src="" alt="Full Screen CAD Drawing">
</div>

<script>
  function openLightbox(imgSrc) {
    document.getElementById('lightbox-img').src = imgSrc;
    document.getElementById('lightbox').classList.add('active');
  }
  function closeLightbox(e) {
    if (e.target.id === 'lightbox' || e.target.classList.contains('close-btn')) {
      document.getElementById('lightbox').classList.remove('active');
    }
  }
</script>
