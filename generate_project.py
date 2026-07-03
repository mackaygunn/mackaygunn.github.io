import json
import os
import glob
import subprocess

def build_markdown(data):
    # Extract Data
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
    
    cover_image = data.get("cover_image", "cover.jpg")
    
    # Start building MD
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
"""

    # Overview
    md += f"\n## Overview\n"
    if p_type: md += f"**Project Type:** {p_type}<br>\n"
    if duration: md += f"**Duration:** {duration}<br>\n"
    if team: md += f"**Team:** {team}<br>\n"
    if role: md += f"**My Role:** {role}\n\n"
    
    overview_text = data.get("overview_text", "")
    if overview_text:
        md += f"{overview_text}\n"

    # Dynamic Sections
    sections = [
        ("Problem Statement", "problem_statement", False),
        ("Objectives", "objectives", True),
        ("Engineering Process", "engineering_process", False),
        ("Technical Details", "technical_details", False),
        ("Design Decisions", "design_decisions", False),
        ("Tools & Software", "tools_and_software", True),
        ("Engineering Skills Demonstrated", "engineering_skills", True),
        ("Challenges", "challenges", False),
        ("Results", "results", False),
        ("Key Learning", "key_learning", False)
    ]

    for title_header, key, is_list in sections:
        val = data.get(key)
        if val:
            md += f"\n## {title_header}\n"
            if is_list and isinstance(val, list):
                for item in val:
                    md += f"* {item}\n"
            else:
                md += f"{val}\n"

    # Gallery
    cad_gallery = data.get("cad_gallery", [])
    diagrams = data.get("diagrams", [])
    
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

    return md, filename_date_prefix(date, folder)

def filename_date_prefix(date, folder):
    return f"{date}-{folder}.md"

def main():
    data_dir = '_project_data'
    projects_dir = '_projects'
    
    if not os.path.exists(data_dir):
        print(f"Directory {data_dir} not found. Please create it and add JSON files.")
        return
        
    if not os.path.exists(projects_dir):
        os.makedirs(projects_dir)

    json_files = glob.glob(os.path.join(data_dir, '*.json'))
    
    if not json_files:
        print(f"No JSON files found in {data_dir}")
        return

    print(f"Found {len(json_files)} project files. Generating markdown...")
    
    for json_path in json_files:
        with open(json_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                md_content, filename = build_markdown(data)
                
                filepath = os.path.join(projects_dir, filename)
                with open(filepath, 'w', encoding='utf-8') as out_f:
                    out_f.write(md_content)
                print(f" -> Generated: {filename}")
                
            except json.JSONDecodeError as e:
                print(f"Error parsing JSON in {json_path}: {e}")
            except Exception as e:
                print(f"Error processing {json_path}: {e}")

    # Git Operations
    print("\nPushing updates to GitHub...")
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Auto-publish updated projects database"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Successfully published to GitHub Pages!")
    except subprocess.CalledProcessError as e:
        print(f"Git push failed or nothing to commit. {e}")

if __name__ == "__main__":
    main()
