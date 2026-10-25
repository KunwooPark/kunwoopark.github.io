# Academic Website

This project is my academic homepage, developed using **Quarto**.

## Update and publish

1. Edit `index.qmd` or `research.qmd` for the corresponding content. Update `cv-pdf.qmd` for education, funding, and teaching; keep `cv.qmd` as a download-only page.
2. Update the shared `_preprints.qmd`, `_journal-articles.qmd`, `_international-conferences.qmd`, and `_domestic-conferences.qmd` lists. Both Publications and the PDF CV include these files.
3. Run `quarto render`. PDF generation requires LuaLaTeX (for example, via `quarto install tinytex`) and either Malgun Gothic or Noto Sans CJK KR for the Korean grant name. Python 3 is used by the post-render hook to keep the older CV URLs current automatically.
4. Commit the source changes and rendered `docs/` files to `main`. GitHub Pages publishes the rendered site.

The CV page links to `cv-pdf.pdf`; the older `files/cv.pdf` path is kept as a compatible copy.
