import json
import os
import subprocess

def main():
    json_path = 'new_project.json'
    
    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found.")
        return
        
    with open(json_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
            return
            
    # Extract data
    folder = data.get("project_folder", "new-project").strip().replace(' ', '-')
    title = data.get("title", "Untitled Project")
    date = data.get("date", "2025-01-01")
    categories = data.get("categories", [])
    tags = data.get("tags", [])
    
    meta = data.get("overview_metadata", {})
    p_type = meta.get("project_type", "")
    duration = meta.get("duration", "")
    team = meta.get("team", "")
    role = meta.get("my_role", "")
    
    overview_text = data.get("overview_text", "")
    problem = data.get("problem_statement", "")
    objectives = data.get("objectives", [])
    cover_image = data.get("cover_image", "cover.jpg")
    cad_gallery = data.get("cad_gallery", [])
    diagrams = data.get("diagrams", [])
    
    # Build Markdown Content
    md = f"""---
layout: project
title: "{title}"
date: {date}
categories: {json.dumps(categories)}
tags: {json.dumps(tags)}
duration: "{duration}"
image: "/assets/images/projects/{folder}/{cover_image}"
thumbnail: "/assets/images/projects/{folder}/{cover_image}"
---

<img src="{{{{ '/assets/images/projects/{folder}/{cover_image}' | relative_url }}}}" alt="Project Cover" style="width: 250px; height: auto; display: block; margin: 0 auto 2rem auto; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">

## Overview
**Project Type:** {p_type}<br>
**Duration:** {duration}<br>
**Team:** {team}<br>
**My Role:** {role}

{overview_text}

## Problem Statement
{problem}

## Project Objectives
"""
    for obj in objectives:
        md += f"* {obj}\n"
        
    if cad_gallery or diagrams:
        md += "\n## Gallery\n"
        
    if cad_gallery:
        md += "\n### CAD Component Geometry\n"
        md += '<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 10px; margin-bottom: 15px;">\n'
        for cad in cad_gallery:
            md += f'  <img src="{{{{ \'/assets/images/projects/{folder}/{cad}\' | relative_url }}}}" alt="CAD View" style="width:100%; border-radius: 4px; border: 1px solid #eee;">\n'
        md += '</div>\n*Caption: Orthographic profiles and individual component geometries.*\n'
        
    if diagrams:
        md += "\n### System Integration & Prototyping\n\n"
        md += '<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin-bottom: 2rem; text-align: center;">\n'
        for d in diagrams:
            img = d.get("file", "")
            cap = d.get("caption", "")
            md += f'  <div>\n'
            md += f'    <img src="{{{{ \'/assets/images/projects/{folder}/{img}\' | relative_url }}}}" alt="Diagram" style="width: 100%; border-radius: 6px; border: 1px solid #ddd; margin-bottom: 5px;">\n'
            md += f'    <p style="font-size: 0.85em; color: #666; line-height: 1.4;"><em>{cap}</em></p>\n'
            md += f'  </div>\n'
        md += '</div>\n'
        
    # Write to file
    filename = f"{date}-{folder}.md"
    projects_dir = "_projects"
    if not os.path.exists(projects_dir):
        os.makedirs(projects_dir)
        
    filepath = os.path.join(projects_dir, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(md)
        
    print(f"Successfully generated markdown file: {filepath}")
    
    # Automatically Git Add, Commit, Push
    print("Pushing to GitHub...")
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"Auto-publish project: {title}"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Successfully published to GitHub Pages!")
    except subprocess.CalledProcessError as e:
        print(f"Error during Git push: {e}")

if __name__ == "__main__":
    main()
