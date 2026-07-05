# Engineering Portfolio Automation Guide

Welcome to your automated portfolio! I have designed this codebase to completely separate **Data** from **Design**. This means you never have to write HTML or CSS again. 

When you want to add new projects or CAD drawings, you simply fill out a JSON template, drop in your images, and the system automatically generates the beautiful webpages for you.

There are **two** distinct systems in this portfolio:
1. **The Main Projects Page** (In-depth engineering case studies)
2. **The CAD Gallery** (Quick-view grid of technical drawings)

---

## 1. How to Upload a Main Project

The Main Projects Page (`/projects`) is for full engineering case studies. The system automatically creates a dedicated webpage for the project based on a JSON file.

**Step 1: Prepare your Images**
1. Create a new folder inside `assets/images/projects/` named after your project (e.g., `my-new-drone`).
2. Inside that folder, save your main cover image as `cover.jpg` (or `cover.png`).
3. Add any other diagrams or CAD images you want to show on the project page into this folder.

**Step 2: Fill out the Data**
1. Go to the `_project_data/` folder.
2. Copy the `template.json` file and rename it to your project name (e.g., `my-new-drone.json`).
3. Open your new JSON file and fill in the text fields (title, overview, problem statement, etc.).
4. *Important:* Make sure the `"project_folder"` field exactly matches the folder name you created in Step 1 (e.g., `"my-new-drone"`).

**Step 3: Publish to GitHub!**
1. Open your terminal or command prompt.
2. Run this single command:
   ```bash
   python generate_project.py
   ```
3. **You're done!** The Python script will automatically generate the HTML webpage and instantly push your changes to GitHub. Your new project will be live in 30 seconds.

---

## 2. How to Upload a CAD Drawing (Gallery)

The CAD Gallery (`/cad-gallery/`) is a quick-view grid. It does not create separate pages; it just adds a new card to the existing grid.

**Step 1: Save the Image**
1. Export your drawing from AutoCAD, SolidWorks, or MATLAB.
2. Save the image directly into the `assets/images/projects/cad/` folder (or `matlab/`, etc.). 

**Step 2: Add the Data**
1. Open the `_data/technical_works.json` file.
2. Paste a new JSON block at the very top of the file. It should look like this:
   ```json
   {
     "title": "My New Suspension System",
     "software": "SolidWorks",
     "image_path": "/assets/images/projects/cad/suspension-drawing.jpg",
     "engineering_intent": "Designed a double-wishbone suspension...",
     "technical_skills": ["FEA", "Kinematics", "Assemblies"]
   }
   ```
   *(Note: `engineering_intent` and `technical_skills` are completely optional! If you leave them out, the card will automatically shrink into a clean, image-only card).*

**Step 3: Publish to GitHub!**
1. You can either use standard Git commands (`git add .`, `git commit`, `git push`)...
2. **OR** you can just run `python generate_project.py`! Even if you didn't add a main project, the python script will automatically commit and push your CAD Gallery changes to the internet for you.

---

## Troubleshooting

* **My images are broken (404 Error):** Double check that the file name in your JSON exactly matches the file name in your `assets/` folder (watch out for `.jpg` vs `.png`!).
* **My site didn't update:** GitHub Pages takes about 30–60 seconds to build. Wait a minute, then do a "Hard Refresh" on your browser (`Ctrl + F5` on Windows, or `Cmd + Shift + R` on Mac).
* **Syntax Error:** JSON is very strict about commas. Make sure every line (except the last one in a block) ends with a comma `,`.
