from reportlab.pdfgen.canvas import Canvas
from pdfrw import PdfReader
from pdfrw.toreportlab import makerl
from pdfrw.buildxobj import pagexobj
import glob
import csv
from pandas import DataFrame, read_csv
import pandas as pd
#Get all pages.

directoryCat = ["BI","CE","CI","CSN","DSA","IoT","IT","KDM","MCG","SE"]
listOfFiles = glob.glob('pdfFile/*/*.pdf')

LocationCSV = r'ListOfFile.csv'
df = pd.read_csv(LocationCSV)
dfFilePath = df['filepath_camera_ready']
df['p0'] = 0
df['p1'] = 0
df['file_path'] = ''
df.loc[416]['p0'] = 1
#df.set_value(416,'p0',1)
print(df.loc[416])
df.index = df['filepath_camera_ready']


for i in directoryCat:
    print(i)

    output_file = 'output/'+i+'/'

    printCountPage = 0

    previousConter = 0
    for row in dfFilePath:
        filePath = row

        for fileName in listOfFiles:
            if i in fileName:
                if len(i) >= 3:
                    fileName = fileName[12:]
                else:
                    fileName = fileName[11:]
                if filePath == fileName:
                    fileNameFull = 'pdfFile/'+i+'/'+fileName
                    print(fileNameFull)

                    reader = PdfReader(fileNameFull)
                    pages = [pagexobj(p) for p in reader.pages]

                    #previousConter = previousConter + 1
                    #print("previousConter is" +str(previousConter))

                    # Compose new pdf

                    #print(str(printCountPage + 1))

                    df.set_value(filePath,'p0',str(printCountPage + 1))

                    for page_num, page in enumerate(pages, start=1):
                        printCountPage = printCountPage + 1
                        #print(printCountPage)


                    #print(str(printCountPage))
                    df.set_value(filePath,'p1',str(printCountPage))
                    df.set_value(filePath,'file_path',str(fileNameFull))
                    df.to_csv('births.csv')


'''
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

                        for page_num, page in enumerate(pages, start=1):
                            printCountPage = printCountPage + 1
                            print(printCountPage)
                            fileWrite.write(i+str(printCountPage)+'\n')
'''
