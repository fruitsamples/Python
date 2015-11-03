#!/usr/bin/python
from CoreGraphics import *
import math

#  For old times sake -- the PostScript cookbook wedge example in python...

def inch(x):
	return 72*x

def rad(angle):
	return angle*math.pi/180.0

def wedge(c):
	c.beginPath()
	c.moveToPoint(0,0)
	c.translateCTM(1,0)
	c.rotateCTM(rad(16))
	c.translateCTM(0, math.sin(rad(15)))
	c.addArc(0,0, math.sin(rad(15)), rad(-90), rad(90), 0)
	c.closePath()

pageRect = CGRectMake (0, 0, 612, 792)   #  landscape
c = CGPDFContextCreateWithFilename ("wedge.pdf", pageRect)
c.beginPage(pageRect)
c.saveGState()
c.translateCTM(inch(4.25), inch(4.25))
c.scaleCTM(inch(1.75), inch(1.75))
c.setLineWidth(.02)
for i in range(1,13):
	c.setGrayFillColor(i/12.0,1.0)
	c.saveGState()
	wedge(c)
	c.fillPath()
	c.restoreGState()
	c.saveGState()
	c.setGrayStrokeColor(0,1)
	wedge(c)
	c.strokePath()
	c.restoreGState()
	c.rotateCTM(rad(30))
c.restoreGState()
c.endPage()
c.finish()
