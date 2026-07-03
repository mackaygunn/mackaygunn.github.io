# Automated Portfolio Project Generator

This repository features a custom Python automation script that completely eliminates the need to write Markdown or handle HTML/Liquid tags. 

To add or update a project on the portfolio, follow this simple 3-step guide:

---

## 1. Create the Project Data File
All project data is permanently stored in the **`_project_data`** folder. 

**To add a new project:**
1. Navigate to the `_project_data` folder.
2. Duplicate the `template.json` file and rename it to your project name (e.g., `drone-arm.json`).
3. Open the file and fill in your project details.

**Important Rule:** The `project_folder` field in your JSON file is critical. It determines the URL of the project and where the Python script looks for your images. (e.g., `"project_folder": "my-drone-project"`).

**Pro-Tip (Auto-Sorting):** The `template.json` file has `"date": "TODAY"`. If you leave it as `"TODAY"`, the script will automatically assign today's exact date to the project when you run it, guaranteeing your brand new project appears at the very top of your homepage! If you ever want to bump an older project back to the top of the homepage, just change its date back to `"TODAY"` and re-run the script.

---

## 2. Prepare Your Images
You must place all images for your project in the exact folder specified by the `project_folder` JSON field.
*Example Path:* `assets/images/projects/my-drone-project/`

### Image Naming Rules:
The Python script is designed to automatically detect and format images based purely on their filenames:

1. **The Cover Image**
   * **Name it:** `cover.jpg`
   * **Result:** The script automatically applies this as the small project card thumbnail on the homepage, and as the large hero image at the top of the project page. *(Must be a .jpg)*

2. **CAD Gallery Images**
   * **Name them:** Start the filename with `cad` (e.g., `cad-1.jpg`, `cad-front.png`, `cad_assembly.webp`).
   * **Result:** The script automatically scoops up all files starting with "cad", sorts them alphabetically, and builds a small CAD component CSS grid gallery. You **do not** need to type these names into your JSON file!

3. **All Other Images (Diagrams, Prototypes, Results)**
   * **Name them:** Anything you want (e.g., `circuit.jpg`, `final-prototype.png`).
   * **Result:** Because these images require custom captions, they are the **only** images you must explicitly list inside the `"diagrams"` array in your JSON file.
   ```json
   "diagrams": [
     {
       "file": "final-prototype.png",
       "caption": "The completed physical build."
     }
   ]
   ```

---

## 3. Generate and Publish!
Once your JSON file is filled out and your images are in the correct folder, you are ready to publish!

1. Open your terminal (PowerShell, Command Prompt, or VS Code Terminal) in the root of the repository.
2. Run the generator script:
   ```bash
   python generate_project.py
   ```

**The script will automatically:**
* Scan the `_project_data` folder and read all JSON files.
* Format the complex Industry-Standard Markdown layouts (Overview, Problem Statement, Technical Details, etc.).
* Build the responsive CSS image grids.
* Save the finalized files into the `_projects` folder.
* **Run `git add`, `git commit`, and `git push` to instantly publish the site to GitHub Pages!**
