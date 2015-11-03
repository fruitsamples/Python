# ps-to-cmyk.py -- script to convert files from [E]PS to CMYK TIFFs
# $Id: ps-to-cmyk.py,v 1.3 2003/06/19 22:44:47 jharper Exp $

from CoreGraphics import *
import sys, os

if len (sys.argv) != 3:
  print "usage: %s PS-FILE OUTPUT-FILE" % sys.argv[0]
  sys.exit (1)

in_file = sys.argv[1]
out_file = sys.argv[2]

pdf_file = "/tmp/ps-to-cmyk." + str (os.getpid ()) + ".pdf"

# Create a PostScript converter and use it to generate a PDF
# document for our input file

if not CGPSConverterCreateWithoutCallbacks ().convert (
        CGDataProviderCreateWithFilename (in_file),
        CGDataConsumerCreateWithFilename (pdf_file)):
  print "Error while converting %s" % in_file
  sys.exit (1)

# Open the PDF we just created and delete the temp. file

pdf = CGPDFDocumentCreateWithProvider (
        CGDataProviderCreateWithFilename (pdf_file))
os.unlink (pdf_file)

# Get the bounding box of the content, create a CMYK bitmap context
# of the same size with a white background, and draw the PDF into
# the context

r = pdf.getMediaBox (1)
cs = CGColorSpaceCreateWithName (kCGColorSpaceUserCMYK)
ctx = CGBitmapContextCreateWithColor (r.size.width, r.size.height,
                                      cs, (0, 0, 0, 0, 1))
ctx.drawPDFDocument (r, pdf, 1)

# Output everything to the TIFF file

ctx.writeToFile (out_file, kCGImageFormatTIFF)
