
from CoreGraphics import *
import math

# Create an RGB bitmap context, transparent black background, 256x256

cs = CGColorSpaceCreateDeviceRGB ()
c = CGBitmapContextCreateWithColor (256, 256, cs, (0,0,0,0))

# Draw a yellow square with a red outline in the center

c.saveGState ()
c.setRGBStrokeColor (1,0,0,1)			# red
c.setRGBFillColor (1,1,0,1)			# yellow
c.setLineWidth (3)
c.setLineJoin (kCGLineJoinBevel)
c.addRect (CGRectMake (32.5, 32.5, 191, 191))
c.drawPath (kCGPathFillStroke);
c.restoreGState ()

# Draw some text at an angle

c.saveGState ()
c.translateCTM (128, 128)
c.rotateCTM ((-30.0 / 360) * (2 * math.pi))
c.translateCTM (-128, -128)
c.setRGBStrokeColor (0,0,0,1)
c.setRGBFillColor (1,1,1,1)
c.selectFont ("Helvetica", 36, kCGEncodingMacRoman)
c.setTextPosition (40, 118)
c.setTextDrawingMode (kCGTextFillStroke)
c.setShadow (CGSizeMake (0,-10), 2)
c.showText ("hello, world", 12)
c.restoreGState ()

# Write the bitmap to disk in PNG format

c.writeToFile ("out.png", kCGImageFormatPNG)

