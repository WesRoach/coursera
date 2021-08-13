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
    "original/3-divideandconquer-1-searcharray.pdf",
    "reduced",
    remove_pages=[
        *range(3, 6),
        *range(11, 15),
        *range(16, 20),
        21,
        *range(23, 27),
        *range(32, 40),
        *range(41, 44),
        *range(45, 47),
        *range(48, 50),
        *range(51, 53),
        *range(55, 58),
        60,
        *range(62, 69),
        *range(70, 75),
        *range(76, 78),
        *range(79, 80),
        *range(81, 83),
        *range(84, 87),
        *range(89, 91),
        *range(92, 94),
        *range(95, 99),
        *range(100, 108),
        109,
    ],
)

split_slides(
    "original/3-divideandconquer-2-karatsuba.pdf",
    "reduced",
    remove_pages=[
        *range(4, 7),
        *range(8, 14),
        *range(15, 19),
        *range(21, 24),
        *range(25, 26),
        *range(28, 33),
        *range(34, 49),
        *range(50, 57),
        *range(58, 72),
        *range(74, 83),
        *range(84, 101),
        *range(102, 116),
    ],
)

split_slides(
    "original/3-divideandconquer-3-mastertheorem.pdf",
    "reduced",
    remove_pages=[
        *range(3, 4),
        *range(5, 6),
        *range(7, 8),
        *range(9, 10),
        *range(11, 16),
        *range(17, 21),
        *range(22, 26),
        *range(27, 31),
        *range(32, 36),
        *range(37, 41),
        *range(44, 52),
        *range(53, 58),
        *range(59, 63),
        *range(64, 65),
        *range(66, 69),
        *range(70, 74),
        75,
    ],
)

split_slides(
    "original/3-divideandconquer-4-sorting.pdf",
    "reduced",
    remove_pages=[
        *range(5, 6),
        *range(8, 10),
        *range(11, 14),
        *range(15, 18),
        *range(19, 23),
        *range(24, 25),
        *range(26, 27),
        *range(28, 30),
        *range(31, 32),
        *range(34, 36),
        *range(38, 41),
        *range(45, 46),
        *range(47, 50),
        *range(52, 53),
        *range(54, 55),
        *range(57, 60),
        *range(63, 65),
        *range(67, 69),
        *range(71, 72),
    ],
)

split_slides(
    "original/3-divideandconquer-5-quicksort.pdf",
    "reduced",
    remove_pages=[
        *range(4, 5),
        *range(9, 11),
        *range(12, 16),
        *range(17, 20),
        *range(21, 26),
        *range(27, 29),
        *range(30, 32),
        *range(37, 38),
        *range(39, 40),
        *range(41, 43),
        *range(46, 47),
        *range(49, 50),
        *range(51, 55),
        *range(56, 58),
        *range(59, 60),
        *range(63, 66),
        *range(72, 73),
        *range(74, 76),
        *range(77, 79),
    ],
)
