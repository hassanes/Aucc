from reportlab.pdfgen.canvas import Canvas
from pdfrw import PdfReader
from pdfrw.toreportlab import makerl
from pdfrw.buildxobj import pagexobj
import glob
import csv

#Get all pages.

#List document list in each directory
directoryCat = ["BI","CE","CI","CSN","DSA","IoT","IT","KDM","MCG","SE"]
listOfFiles = glob.glob('pdfFile/*/*.pdf')
directoryCat.sort()
for i in directoryCat:
    print(i)

    output_file = 'output/'+i+'/'

    printCountPage = 0

    fileWrite = open("test.txt", "w")

    with open('ListOfFile.csv') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            filePath = row['filepath_camera_ready']
            for fileName in listOfFiles:
                if i in fileName:
                    if len(i) >= 3:
                        fileName = fileName[12:]
                    else:
                        fileName = fileName[11:]
                    if filePath == fileName:
                        fileNameFull = 'pdfFile/'+i+'/'+fileName
                        print(fileNameFull)

                        # Get pages
                        reader = PdfReader(fileNameFull)
                        pages = [pagexobj(p) for p in reader.pages]

                        # Compose new pdf
                        canvas = Canvas(output_file+fileName)

                        for page_num, page in enumerate(pages, start=1):
                            printCountPage = printCountPage + 1
                            print(printCountPage)
                            fileWrite.write(i+str(printCountPage)+'\n')

                            # Add page
                            canvas.setPageSize((page.BBox[2], page.BBox[3]))
                            canvas.doForm(makerl(canvas, page))

                            # Draw footer
                            #footer_text = "Page BI%s of %s" % (page_num, len(pages))
                            footer_text = i+ ", Page %s " % (printCountPage)
                            #header_text = "The 5    ASEAN Undergraduate Conference in Computing"
                            x = 97
                            x_offset = 40
                            canvas.saveState()
                            canvas.setStrokeColorRGB(0, 0, 0)
                            canvas.setLineWidth(0.5)
                            canvas.line(56, 67, page.BBox[2] - 56, 67)
                            canvas.setFont('Times-Italic', 10)
                            #canvas.drawString(page.BBox[0] + x_offset, page.BBox[3] - 25, header_text)
                            canvas.setFont('Times-Italic', 8)
                            #canvas.drawString(page.BBox[0] + x_offset +25, page.BBox[3] - 20, "th")
                            canvas.setFont('Times-Roman', 10)
                            canvas.drawString(page.BBox[2]-x, 55, footer_text)

                            canvas.restoreState()

                            canvas.showPage()
                        canvas.save()

"""
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
    footer_text = "Page BI%s of %s" % (page_num, len(pages))
    header_text = "The 5    ASEAN Undergraduate Conference in Computing"
    x = 128
    x_offset = 40
    canvas.saveState()
    canvas.setStrokeColorRGB(0, 0, 0)
    canvas.setLineWidth(0.5)
    canvas.line(66, 78, page.BBox[2] - 66, 78)
    canvas.setFont('Times-Italic', 10)
    canvas.drawString(page.BBox[0] + x_offset, page.BBox[3] - 25, header_text)
    canvas.setFont('Times-Italic', 8)
    canvas.drawString(page.BBox[0] + x_offset +25, page.BBox[3] - 20, "th")
    canvas.setFont('Times-Roman', 10)
    canvas.drawString(page.BBox[2]-x, 65, footer_text)
    canvas.restoreState()

    canvas.showPage()

canvas.save()


#print(type(listOfFiles))
"""
"""
countPage = 0
for num in range(len(listOfFilesBI)):
    reader = PdfReader(listOfFilesBI[num])
    pages = [pagexobj(p) for p in reader.pages]
    for page_num, page in enumerate(pages, start=1):
        countPage = countPage + 1
print(countPage)

printCountPage = 0
for num in range(len(listOfFilesBI)):
    reader = PdfReader(listOfFilesBI[num])
    pages = [pagexobj(p) for p in reader.pages]
    canvas = Canvas(output_file+str(num)+".pdf")
    for page_num, page in enumerate(pages, start=1):
        printCountPage = printCountPage + 1
        print(printCountPage)
        # Add page
        canvas.setPageSize((page.BBox[2], page.BBox[3]))
        canvas.doForm(makerl(canvas, page))

        # Draw footer
        #This footer include page of
        #footer_text = "Categoty BI, Page %s of %s" % (printCountPage, countPage)
        #this footer not include page of
        footer_text = "Categoty BI, Page %s " % (printCountPage)
        #header_text = "The 5    ASEAN Undergraduate Conference in Computing"
        x = 128
        x_offset = 40
        canvas.saveState()
        canvas.setStrokeColorRGB(0, 0, 0)
        canvas.setLineWidth(0.5)
        canvas.line(66, 78, page.BBox[2] - 66, 78)
        canvas.setFont('Times-Italic', 10)
        #canvas.drawString(page.BBox[0] + x_offset, page.BBox[3] - 25, header_text)
        canvas.setFont('Times-Italic', 8)
        #canvas.drawString(page.BBox[0] + x_offset +25, page.BBox[3] - 20, "th")
        canvas.setFont('Times-Roman', 10)
        canvas.drawString(page.BBox[2]-x, 65, footer_text)
        canvas.restoreState()

        canvas.showPage()
    canvas.save()
"""
