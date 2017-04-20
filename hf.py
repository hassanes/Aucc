from reportlab.pdfgen.canvas import Canvas
from pdfrw import PdfReader
from pdfrw.toreportlab import makerl
from pdfrw.buildxobj import pagexobj

input_file = "30-22-camera-ready.pdf"
output_file = "test_header_footer.pdf"

# Get pages
reader = PdfReader(input_file)
pages = [pagexobj(p) for p in reader.pages]


# Compose new pdf
canvas = Canvas(output_file)

for page_num, page in enumerate(pages, start=1):

    # Add page
    canvas.setPageSize((page.BBox[2], page.BBox[3]))
    canvas.doForm(makerl(canvas, page))

    # Draw footer
    footer_text = "BI, Page %s " % (page_num)
    x = 97
    x_offset = 40
    canvas.saveState()
    canvas.setStrokeColorRGB(0, 0, 0)
    canvas.setLineWidth(0.5)
    canvas.line(56, 67, page.BBox[2] - 56, 67)
    canvas.setFont('Times-Italic', 10)
    canvas.setFont('Times-Italic', 8)
    canvas.setFont('Times-Roman', 10)
    canvas.drawString(page.BBox[2]-x, 55, footer_text)
    canvas.restoreState()

    canvas.showPage()

canvas.save()
