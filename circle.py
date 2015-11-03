#!/usr/bin/python

#  Simple python example to draw a circle

from CoreGraphics import *
import math   # for pi

pageRect = CGRectMake (0, 0, 612, 792)   #  landscape
c = CGPDFContextCreateWithFilename ("circle.pdf", pageRect)
c.beginPage (pageRect)
c.setRGBFillColor(1.0,0.0,0.0,1.0)
c.addArc(300,300,100,0,2*math.pi,1)
c.fillPath()
c.endPage()
c.finish()
