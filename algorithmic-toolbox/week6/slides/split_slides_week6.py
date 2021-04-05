from pathlib import Path

from PyPDF2 import PdfFileReader, PdfFileWriter


def split_slides(
    input_slides: str,
    output_directory: str,
    pages_to_keep: list = None,
    remove_pages: list = None,
):
    """
    Page numbers are the displayed page numbers.
    """
    input_slides = Path(input_slides)
    output_directory = Path(output_directory)

    pdf = PdfFileReader(str(input_slides))
    pdfWriter = PdfFileWriter()

    if pages_to_keep is None and remove_pages is None:
        raise ValueError("One of `pages_to_keep` or `remove_pages` must be populated")
    if pages_to_keep is not None and remove_pages is not None:
        raise ValueError(
            "Either `pages_to_keep` or `remove_pages` should be submitted. Not both."
        )

    if pages_to_keep is not None:
        pages = [page for page in pages_to_keep]

    if remove_pages is not None:
        pages = [
            page for page in range(1, pdf.getNumPages() + 1) if page not in remove_pages
        ]

    print(f"File: {input_slides.name}; {len(pages)} Pages: {pages}")

    # PdfFileReader reads/writes 0-indexed
    pages = [page - 1 for page in pages]

    for page_num in pages:
        pdfWriter.addPage(pdf.getPage(page_num))

    with open(output_directory / input_slides.name, "wb") as f:
        pdfWriter.write(f)
        f.close()


split_slides(
    "original/04_dynamic_programming_1_changeproblem.pdf",
    "reduced",
    remove_pages=[],
)
