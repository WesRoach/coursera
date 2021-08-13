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
    "original/2-greedy-1-intro.pdf",
    "reduced",
    pages_to_keep=[
        *range(1, 3 + 1),
        9,
        14,
        19,
        23,
        27,
        31,
        35,
        38,
        *range(42, 44 + 1),
        *range(45, 47 + 1),
        52,
        53,
        59,
        60,
        61,
        67,
        68,
        71,
        72,
        73,
        79,
        80,
        81,
        85,
        86,
        87,
        90,
        95,
    ],
)

split_slides(
    "original/2-greedy-2-groupingchildren.pdf",
    "reduced",
    remove_pages=[
        *range(7, 14),
        *range(15, 17),
        *range(20, 22),
        *range(23, 26),
        *range(28, 31),
        *range(32, 35),
        *range(36, 40),
    ],
)

split_slides(
    "original/2-greedy-3-fractionalknapsack.pdf",
    "reduced",
    remove_pages=[*range(3, 5), 14, *range(18, 22), *range(26, 29), 30,],
)

split_slides(
    "original/2-greedy-4-review.pdf", "reduced", remove_pages=[*range(5, 9)],
)
