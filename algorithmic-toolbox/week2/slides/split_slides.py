from PyPDF2 import PdfFileReader, PdfFileWriter


def split_slides(
    input_slides: str,
    output_directory: str,
    pages_to_keep: list = None,
    remove_pages: list = None,
):
    file_base_name = input_slides.replace(".pdf", "")
    pdf = PdfFileReader(input_slides)
    pdfWriter = PdfFileWriter()

    if pages_to_keep is None and remove_pages is None:
        raise ValueError("One of `pages_to_keep` or `remove_pages` must be populated")
    if pages_to_keep is not None and remove_pages is not None:
        raise ValueError(
            "Either `pages_to_keep` or `remove_pages` should be submitted. Not both."
        )

    if pages_to_keep is not None:
        pages = pages_to_keep

    if remove_pages is not None:
        pages = [
            page for page in range(1, pdf.getNumPages() + 1) if page not in remove_pages
        ]

    print(f"File: {input_slides}; {len(pages)} Pages: {pages}")

    # PdfFileReader reads/writes 0-indexed
    pages = [page - 1 for page in pages]

    for page_num in pages:
        pdfWriter.addPage(pdf.getPage(page_num))

    with open(f"{output_directory}/{file_base_name}.pdf", "wb") as f:
        pdfWriter.write(f)
        f.close()


# 1-intro-2-fibonaccinumbers.pdf
# These pages numbers are the displayed page numbers
split_slides(
    "1-intro-2-fibonaccinumbers.pdf",
    "reduced-slides",
    remove_pages=[
        4,
        *range(7, 10),
        *range(12, 15),
        18,
        21,
        23,
        24,
        *range(26, 29),
        *range(35, 39),
        41,
        43,
    ],
)

# 1-intro-3-GCD1.pdf
# These pages numbers are the displayed page numbers
split_slides("1-intro-3-GCD1.pdf", "reduced-slides", remove_pages=[3, 4, 7, 8, 10])

# 1-intro-3-GCD2.pdf
# These pages numbers are the displayed page numbers
split_slides(
    "1-intro-3-GCD2.pdf", "reduced-slides", remove_pages=[3, 7, *range(9, 15), 16],
)

# 1-intro-4-1-runtimes.pdf
# These pages numbers are the displayed page numbers
split_slides("1-intro-4-1-runtimes.pdf", "reduced-slides", remove_pages=[4, 18])

# 1-intro-4-2-asymptoticnotation1.pdf
# These pages numbers are the displayed page numbers
split_slides(
    "1-intro-4-2-asymptoticnotation1.pdf", "reduced-slides", remove_pages=[4, 9, 10]
)

# 1-intro-4-2-asymptoticnotation2.pdf
# These pages numbers are the displayed page numbers
split_slides(
    "1-intro-4-2-asymptoticnotation2.pdf", "reduced-slides", remove_pages=[3, 9, 10]
)

# 1-intro-4-2-asymptoticnotation3.pdf
# These pages numbers are the displayed page numbers
split_slides(
    "1-intro-4-2-asymptoticnotation3.pdf",
    "reduced-slides",
    remove_pages=[*range(4, 8), *range(10, 17)],
)

# 1-intro-5-courseoverview.pdf
# These pages numbers are the displayed page numbers
split_slides(
    "1-intro-5-courseoverview.pdf", "reduced-slides", remove_pages=[6, *range(8, 11)],
)
