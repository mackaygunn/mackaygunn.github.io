---
layout: page
title: Design & Simulation Gallery
permalink: /cad-gallery/
---

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2rem;">
  {% for work in site.data.technical_works %}
  <div style="border: 1px solid #eaeaea; border-radius: 6px; overflow: hidden; background: #fff; display: flex; flex-direction: column;">
    <div style="height: 220px; background: #f4f4f5; display: flex; align-items: center; justify-content: center; border-bottom: 1px solid #eaeaea; overflow: hidden;">
      <img src="{{ work.image_path | relative_url }}" alt="{{ work.title }}" style="width: 100%; height: 100%; object-fit: cover;">
    </div>
    
    <div style="padding: 1.5rem; flex-grow: 1; display: flex; flex-direction: column;">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
        <h3 style="margin: 0; font-size: 1.2rem; color: #111;">{{ work.title }}</h3>
        <span style="background: #e1effe; color: #1e429f; font-size: 0.75rem; font-weight: bold; padding: 3px 8px; border-radius: 4px;">{{ work.software }}</span>
      </div>
      
      <p style="color: #555; font-size: 0.95rem; line-height: 1.6; margin-bottom: 1.5rem; flex-grow: 1;">{{ work.engineering_intent }}</p>
      
      <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: auto;">
        {% for skill in work.technical_skills %}
          <span style="background: #f3f4f6; color: #374151; font-size: 0.8rem; padding: 4px 10px; border-radius: 12px; border: 1px solid #e5e7eb;">{{ skill }}</span>
        {% endfor %}
      </div>
    </div>
  </div>
  {% endfor %}
</div>
