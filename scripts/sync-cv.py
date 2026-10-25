"""Keep both older CV download paths identical to the rendered PDF."""

from pathlib import Path
import os
import shutil

project = Path(__file__).resolve().parent.parent
output = Path(os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "docs"))
if not output.is_absolute():
    output = project / output

source = output / "cv-pdf.pdf"
if source.is_file():
    for destination in (project / "files/cv.pdf", output / "files/cv.pdf"):
        destination.parent.mkdir(parents=True, exist_ok=True)
        if not destination.exists() or source.read_bytes() != destination.read_bytes():
            shutil.copy2(source, destination)
