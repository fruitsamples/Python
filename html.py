#!/usr/bin/python

from CoreGraphics import *
import sys, getopt

default_html = '''
<font face="Helvetica" size="36">
 <b>
   Hello, world
 </b>
</font>'''

def usage ():
  print '''
usage: python html.py [OPTION]... [HTML-FILE]

Convert HTML text to a PDF document.

  -f, --font-size=SIZE
  -o, --output=PDF-FILE
'''

def main ():
  output_file = 'html.pdf'
  font_size = 12.0

  try:
    opts,args = getopt.getopt (sys.argv[1:], 'o:f:', ['output=', 'font-size='])
  except getopt.GetoptError:
    usage ()
    sys.exit (1)

  for (o,a) in opts:
    if o in ('-o', '--output'):
      output_file = a
    elif o in ('-f', '--font-size'):
      font_size = float (a)

  if len (args) >= 1:
    html = CGDataProviderCreateWithFilename (args[0])
  else:
    html = CGDataProviderCreateWithString (default_html)

  pageRect = CGRectMake (0, 0, 612, 792)
  c = CGPDFContextCreateWithFilename (output_file, pageRect)
  c.beginPage(pageRect)

  tr = c.drawHTMLTextInRect (html, pageRect, font_size)

  c.endPage()
  c.finish()


if __name__ == '__main__':
  main ()
