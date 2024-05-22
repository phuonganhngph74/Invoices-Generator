import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# Read all txt files in the folder
filepaths = glob.glob('Text_Files/*.txt')
pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    pdf.add_page()

    filename = Path(filepath).stem
    name = filename.title()

    pdf.set_font("Times", size=16, style='B')
    pdf.cell(w=50, h=8, txt=f"File Name: {name}")

    with open(filepath, 'r') as file:
        content = file.read()

    pdf.set_font("Times", size=12)
    pdf.multi_cell(w=0, h=10, txt=content)

pdf.output(f"Text_Files/PDFs/output.pdf")