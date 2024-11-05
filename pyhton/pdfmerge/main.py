import os
from pypdf import PdfWriter

merger = PdfWriter()
pdfs = [file for file in os.listdir() if file.endswith("pdf")]

for pdf in pdfs:
    print(f"New pdf Made {pdf}")
    merger.append(pdf)

merger.write("merged.pdf") 
print("New pdf Made")
merger.close()