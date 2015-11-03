# watermark.py -- add a "watermark" to each page of a pdf document
# $Id: watermark.py,v 1.1 2003/06/19 19:39:53 jharper Exp $

from CoreGraphics import *
import sys, os, math, getopt, string

def usage ():
  print '''
usage: python watermark.py [OPTION]... INPUT-PDF OUTPUT-PDF

Add a "watermark" to a PDF document.

  -t, --text=STRING
  -f, --font-name=FONTNAME
  -F, --font-size=SIZE
  -c, --color=R,G,B
'''

def main ():

  text = 'CONFIDENTIAL'
  color = (1, 0, 0)
  font_name = 'Gill Sans Bold'
  font_size = 36
  page_rect = CGRectMake (0, 0, 612, 792)

  try:
    opts,args = getopt.getopt (sys.argv[1:], 't:f:F:c:',
			       ['text=', 'font-name=', 'font-size=', 'color='])
  except getopt.GetoptError:
    usage ()
    sys.exit (1)

  if len (args) != 2:
    usage ()
    sys.exit (1)

  for o,a in opts:
    if o in ('-t', '--text'):
      text = a
    elif o in ('-f', '--font-name'):
      font_name = a
    elif o in ('-F', '--font-size'):
      font_size = float (a)
    elif o in ('-c', '--color'):
      color = map (float, string.split (a, ','))

  c = CGPDFContextCreateWithFilename (args[1], page_rect)
  pdf = CGPDFDocumentCreateWithProvider (CGDataProviderCreateWithFilename (args[0]))

  for p in range (1, pdf.getNumberOfPages () + 1):
    r = pdf.getMediaBox (p)
    c.beginPage (r)
    c.saveGState ()
    c.drawPDFDocument (r, pdf, p)
    c.restoreGState ()
    c.saveGState ()
    c.setRGBFillColor (color[0], color[1], color[2], 1)
    c.setTextDrawingMode (kCGTextFill)
    c.setTextMatrix (CGAffineTransformIdentity)
    c.selectFont (font_name, font_size, kCGEncodingMacRoman)
    c.translateCTM (r.size.width - font_size, r.size.height - font_size)
    c.rotateCTM (-90.0 / 180 * math.pi)
    c.showTextAtPoint (0, 0, text, len (text))
    c.restoreGState ()
    c.endPage ()
  c.finish ()


if __name__ == '__main__':
  main ()
