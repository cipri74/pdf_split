import pathlib as pl
from PyPDF2 import PdfFileWriter, PdfFileReader

REL_INPUT_DIR = pl.Path("input")
REL_OUTPUT_DIR = pl.Path("output")


def read_pdf(pdf_path: pl.Path):
    return PdfFileReader(open(pdf_path, "rb"))


def main():
    file_name = "file.pdf"
    pdf_path = REL_INPUT_DIR / file_name
    input_pdf = read_pdf(pdf_path)
    for nr_page in range(input_pdf.numPages):
        output = PdfFileWriter()
        output.addPage(input_pdf.getPage(nr_page))
        output_dir = REL_OUTPUT_DIR / file_name
        output_dir.mkdir(parents=True, exist_ok=True)
        output_file = output_dir / f"document-page{nr_page+1}.pdf"
        with open(output_file, "wb") as outputStream:
            output.write(outputStream)


if __name__ == "__main__":
    main()
