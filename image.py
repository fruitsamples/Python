
from CoreGraphics import *
import sys

if len (sys.argv) >= 2:
  inputFile = sys.argv[1];
else:
  inputFile = "out.png"
outputFile = "out.pdf"


i = CGImageImport (CGDataProviderCreateWithFilename (inputFile))

print "Image \'%s\' size is (%d,%d)" % (inputFile, i.getWidth(), i.getHeight())

# create an output document to draw the image into

pageRect = CGRectMake (0, 0, 612, 792)

c = CGPDFContextCreateWithFilename (outputFile, pageRect)

c.beginPage (pageRect)
c.drawImage (pageRect.inset (72, 72), i)
c.endPage ()
c.finish ()

print "Output PDF file created at \'%s\' " % outputFile
