import json
import os
import glob
import subprocess
import datetime

def build_markdown(data):
    # Extract Data
    folder = data.get("project_folder", "new-project").strip().replace(' ', '-')
    title = data.get("title", "Untitled Project")
    date = data.get("date", "TODAY")
    
    if date == "TODAY" or not date:
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        data['date'] = date

    categories = data.get("categories", [])
    tags = data.get("tags", [])
    
    meta = data.get("overview_metadata", {})
    p_type = meta.get("project_type", "")
    duration = meta.get("duration", "")
    team = meta.get("team", "")
    role = meta.get("my_role", "")
    
    cover_image = "cover.jpg" # Fallback
    image_dir = os.path.join('assets', 'images', 'projects', folder)
    if os.path.exists(image_dir):
        for f in os.listdir(image_dir):
            if f.lower().startswith("cover."):
                cover_image = f
                break
    
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

    # GitHub Code Link
    github_link = data.get("github_link", "")
    if github_link:
        md += f'\n<div style="text-align: center; margin: 3rem 0;">\n'
        md += f'  <a href="{github_link}" target="_blank" class="btn btn-secondary" style="display: inline-flex; align-items: center; gap: 10px; background: #24292e; color: #fff; border: none; padding: 0.8rem 1.5rem;">\n'
        md += f'    <svg viewBox="0 0 24 24" width="22" height="22" fill="currentColor"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>\n'
        md += f'    View Source Code\n'
        md += f'  </a>\n'
        md += f'</div>\n'

    # Gallery
    diagrams = data.get("diagrams", [])
    
    # Automatically find CAD images
    cad_gallery = []
    image_dir = os.path.join('assets', 'images', 'projects', folder)
    if os.path.exists(image_dir):
        for f in os.listdir(image_dir):
            if f.lower().startswith("cad") and f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                cad_gallery.append(f)
    cad_gallery.sort()
    
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

    return md, filename_date_prefix(date, folder), data

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

    # Get all json files in _project_data directory
    json_files = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith('.json') and f != 'template.json']
    
    if not json_files:
        print(f"No JSON files found in {data_dir}")
        return

    print(f"Found {len(json_files)} project files. Generating markdown...")
    
    for json_path in json_files:
        with open(json_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                md_content, filename, updated_data = build_markdown(data)
                
                # Delete any old markdown files for this project to prevent duplicates
                folder = updated_data.get("project_folder", "")
                if folder:
                    old_files = glob.glob(os.path.join(projects_dir, f"*-{folder}.md"))
                    for old in old_files:
                        os.remove(old)
                
                filepath = os.path.join(projects_dir, filename)
                with open(filepath, 'w', encoding='utf-8') as out_f:
                    out_f.write(md_content)
                    
                # Save the JSON back in case the date was updated from "TODAY"
                with open(json_path, 'w', encoding='utf-8') as json_out:
                    json.dump(updated_data, json_out, indent=2)
                    
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
