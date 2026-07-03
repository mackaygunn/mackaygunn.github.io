# How to Create a New Project

To ensure all future projects match the exact layout, image scaling, and formatting of your "Thermo-Electrical Lunchbox" case study, follow these steps:

## 1. Prepare Your Images
1. **Create a Folder:** Create a new folder for your project under `assets/images/projects/` (e.g., `assets/images/projects/my-new-project/`).
2. **Upload Images:** Place all your images inside this folder.
3. **Cover Image:** Ensure you have a main cover image (e.g., `cover.jpg`) that will be used for both the homepage card and the top of the project page.

## 2. Create the Markdown File
1. Go to the `_projects/` directory.
2. Create a new markdown file. **CRITICAL:** Name the file with a date in the **past** or **present**, otherwise GitHub Pages will skip it! (e.g., `2025-11-20-my-new-project.md`).

## 3. Copy & Paste the Template
Paste the following template into your new file, and replace the bracketed `[DATA]` with your actual project details. 

> [!WARNING]  
> Be extremely careful with the Liquid image paths `{{ '/assets/images/...' | relative_url }}`. Do **not** add `/ramiruliyanage.github.io` to the paths, the `relative_url` filter handles it automatically!

```markdown
---
layout: project
title: "[Your Project Title]"
date: 2025-11-20
categories: [design-simulation, physical-projects]
tags: [Tag-1, Tag-2, Tag-3]
duration: "[e.g., June - October 2025]"
image: "/assets/images/projects/[project-folder]/cover.jpg"
thumbnail: "/assets/images/projects/[project-folder]/cover.jpg"
---

<img src="{{ '/assets/images/projects/[project-folder]/cover.jpg' | relative_url }}" alt="Project Cover" style="width: 250px; height: auto; display: block; margin: 0 auto 2rem auto; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">

## Overview
**Project Type:** [Type 1] • [Type 2] • [Type 3]<br>
**Duration:** [Duration]<br>
**Team:** [Team Size]<br>
**My Role:** [Your Role]

[Write a 2-3 sentence overview of the project here.]

## Problem Statement
[Describe the problem you were trying to solve.]

## Project Objectives
* [Objective 1]
* [Objective 2]
* [Objective 3]

## Gallery

### CAD Component Geometry
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 10px; margin-bottom: 15px;">
  <img src="{{ '/assets/images/projects/[project-folder]/cad-1.jpg' | relative_url }}" alt="CAD View 1" style="width:100%; border-radius: 4px; border: 1px solid #eee;">
  <img src="{{ '/assets/images/projects/[project-folder]/cad-2.jpg' | relative_url }}" alt="CAD View 2" style="width:100%; border-radius: 4px; border: 1px solid #eee;">
  <img src="{{ '/assets/images/projects/[project-folder]/cad-3.jpg' | relative_url }}" alt="CAD View 3" style="width:100%; border-radius: 4px; border: 1px solid #eee;">
</div>
*Caption: Orthographic profiles and individual component geometries.*

### System Integration & Prototyping

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin-bottom: 2rem; text-align: center;">
  <div>
    <img src="{{ '/assets/images/projects/[project-folder]/diagram-1.jpg' | relative_url }}" alt="Exploded Diagram" style="width: 100%; border-radius: 6px; border: 1px solid #ddd; margin-bottom: 5px;">
    <p style="font-size: 0.85em; color: #666; line-height: 1.4;"><em>[Diagram 1 Caption]</em></p>
  </div>
  <div>
    <img src="{{ '/assets/images/projects/[project-folder]/diagram-2.jpg' | relative_url }}" alt="Circuit Diagram" style="width: 100%; border-radius: 6px; border: 1px solid #ddd; margin-bottom: 5px;">
    <p style="font-size: 0.85em; color: #666; line-height: 1.4;"><em>[Diagram 2 Caption]</em></p>
  </div>
  <div>
    <img src="{{ '/assets/images/projects/[project-folder]/diagram-3.jpg' | relative_url }}" alt="Physical Prototype" style="width: 100%; border-radius: 6px; border: 1px solid #ddd; margin-bottom: 5px;">
    <p style="font-size: 0.85em; color: #666; line-height: 1.4;"><em>[Diagram 3 Caption]</em></p>
  </div>
</div>
```

## Important Rules to Remember
1. **Line Breaks:** Notice the `<br>` tags at the end of the lines in the `## Overview` section? You **must** include those, or Markdown will merge all the metadata into one massive paragraph!
2. **Categories:** The `categories` array in the front matter must only contain `design-simulation` or `physical-projects`. This is how the homepage filter buttons know where to sort your project!
3. **No HTML in YAML:** Never put the `{{ ... | relative_url }}` Liquid tags inside the YAML front matter at the very top. Only use them in the actual markdown body.
