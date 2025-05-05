# Plant Breeding Data Analysis Course - Baku

This repository contains the Quarto project for the plant breeding data analysis course materials, specifically designed for breeders in Baku, in collaboration with ICARDA.

## Project Structure

- **\`_quarto.yml\`**: Main configuration file for the Quarto project (defines book structure, output formats including slides).
- **\`index.qmd\`**: The main landing page/introduction chapter for the book format.
- **\`00_Setup_Intro/\` to \`06_GIGWA_AI/\`**: Folders containing course modules as Quarto (\`.qmd\`) files.
- **\`code/\`**: R scripts.
- **\`data/\`**: Datasets (\`raw/\`, \`example/\`, \`processed/\`).
- **\`figures/\`**: Saved plots.
- **\`output/\`**: Location for rendered outputs (HTML book, PDF book, slides).
  - **\`pdfs/\`**: Placeholder for final PDFs.
- **\`resources/\`**: Supplementary materials.
- **\`assets/\`**: Contains shared assets like logos.
  - **\`icarda_logo.png\`**: **IMPORTANT: Replace this placeholder with the actual logo file.**
- **\`custom.css\`**: Custom CSS rules, including adding the ICARDA logo to \`revealjs\` slides.
- **\`README.md\`**: This file.
- **\`gitignore\`**: Specifies files/directories for Git to ignore.

## How to Use and Render

1.  **Prerequisites:** R, RStudio, Quarto, LaTeX (e.g., run \`tinytex::install_tinytex()\` in R console).
2.  **Replace Logo:** Put the actual \`icarda_logo.png\` file into the \`assets/\` directory. Adjust size/position in \`custom.css\` if needed.
3.  **Open Project:** Open in RStudio (use \`File > New Project > Existing Directory...\`).
4.  **Install R Packages:** Add necessary package installation commands (e.g., \`install.packages(c("tidyverse", "rrBLUP", "qqman", "readxl", "writexl"))\`) to \`00_Setup_Intro/01_Setup_R_RStudio.qmd\` and run them in the R console.
5.  **Render Specific Formats:** Use the Terminal in RStudio:
    *   **HTML Book:** \`quarto render\` (Default based on \`project: type: book\`) -> output in \`output/_book/\`
    *   **PDF Book:** \`quarto render --to pdf\` -> output PDF in \`output/\`
    *   **HTML Slides (revealjs):** \`quarto render <filename>.qmd --to revealjs\` (e.g., \`quarto render 01_R_Basics/01_Intro_To_R.qmd --to revealjs\`) -> output as \`<filename>.html\` in the source directory.
    *   **PDF Slides (beamer):** \`quarto render <filename>.qmd --to beamer\` (e.g., \`quarto render 01_R_Basics/01_Intro_To_R.qmd --to beamer\`) -> output as \`<filename>.pdf\` in the source directory.
    *   *Note on Slide Warnings:* The warnings "revealjs/beamer format is not supported by book projects" appear when rendering the *whole book*. They mean these formats are ignored for the *book build*, but you can still render *individual files* to these formats using the commands above.

## Course Content Overview

See the \`_quarto.yml\` file or the rendered book's Table of Contents for module details. The \`.qmd\` files contain skeletal content that needs further development.
