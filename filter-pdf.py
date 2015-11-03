# filter-pdf.py -- apply a ColorSync Filter to each page of a pdf document
# $Id: filter-pdf.py,v 1.1 2003/07/22 01:00:46 jharper Exp $

from CoreGraphics import *
import sys, os, math, getopt, string

def usage ():
  print '''
usage: python filter-pdf.py FILTER INPUT-PDF OUTPUT-PDF

Apply a ColorSync Filter to a PDF document.
'''

def main ():

  page_rect = CGRectMake (0, 0, 612, 792)

  try:
    opts,args = getopt.getopt (sys.argv[1:], '', [])
  except getopt.GetoptError:
    usage ()
    sys.exit (1)

  if len (args) != 3:
    usage ()
    sys.exit (1)

  filter = CGContextFilterCreateDictionary (args[0])
  if not filter:
    print 'Unable to create context filter'
    sys.exit (1)

  pdf = CGPDFDocumentCreateWithProvider (CGDataProviderCreateWithFilename (args[1]))
  if not pdf:
    print 'Unable to open input file'
    sys.exit (1)

  c = CGPDFContextCreateWithFilename (args[2], page_rect, filter)
  if not c:
    print 'Unable to create output context'
    sys.exit (1)

  for p in range (1, pdf.getNumberOfPages () + 1):
    r = pdf.getMediaBox (p)
    c.beginPage (r)
    c.drawPDFDocument (r, pdf, p)
    c.endPage ()

  c.finish ()


if __name__ == '__main__':
  main ()
