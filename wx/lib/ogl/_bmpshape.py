# -*- coding: utf-8 -*-
#!/usr/bin/env python
#----------------------------------------------------------------------------
# Name:         bmpshape.py
# Purpose:      Bitmap shape
#
# Author:       Pierre Hjälm (from C++ original by Julian Smart)
#
# Created:      2004-05-08
# Copyright:    (c) 2004 Pierre Hjälm - 1998 Julian Smart
# Licence:      wxWindows license
# Tags:         phoenix-port, unittest, py3-port
#----------------------------------------------------------------------------
"""
The OGL Bitmap shape
"""
from ._basic import RectangleShape


class BitmapShape(RectangleShape):
    """Draws a bitmap (non-resizable)."""
    def __init__(self):
        RectangleShape.__init__(self, 100, 50)
        self._filename = ""

    def OnDraw(self, dc):
        if not self._bitmap.IsOk():
            return

        x = self._xpos - self._bitmap.GetWidth() / 2.0
        y = self._ypos - self._bitmap.GetHeight() / 2.0
        dc.DrawBitmap(self._bitmap, x, y, True)

    def SetSize(self, w, h, recursive = True):
        if self._bitmap.IsOk():
            w = self._bitmap.GetWidth()
            h = self._bitmap.GetHeight()

        self.SetAttachmentSize(w, h)

        self._width = w
        self._height = h

        self.SetDefaultRegionSize()

    def GetBitmap(self):
        """Return a the bitmap associated with this shape."""
        return self._bitmap
    
    def SetBitmap(self, bitmap):
        """Set the bitmap associated with this shape.

        You can delete the bitmap from the calling application, since
        reference counting will take care of holding on to the internal bitmap
        data.
        """
        self._bitmap = bitmap
        if self._bitmap.IsOk():
            self.SetSize(self._bitmap.GetWidth(), self._bitmap.GetHeight())
            
    def SetFilename(self, f):
        """Set the bitmap filename."""
        self._filename = f

    def GetFilename(self):
        """Return the bitmap filename."""
        return self._filename
