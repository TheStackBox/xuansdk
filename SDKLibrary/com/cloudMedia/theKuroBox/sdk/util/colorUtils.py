##############################################################################################
# Copyright 2014-2015 Cloud Media Sdn. Bhd.
#
# This file is part of Xuan Application Development SDK.
#
# Xuan Application Development SDK is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Xuan Application Development SDK is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Xuan Application Development SDK.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################################

import math
import struct
import binascii
from com.cloudMedia.theKuroBox.sdk.util.mathUtils import MathUtils

class ColorUtils(object):
    '''
    Utility methods for manipulating with colors value
    '''

    @staticmethod
    def rgb_to_cie(r, g, b, colorPoints={"r":(1.0, 0), "g":(0.0, 1.0), "b":(0.0, 0.0)}):
        '''
        Function : Convert RGB to CIE XYB value
        1. r:Number       - r value [0-255]
        2. g:Number       - g value [0-255]
        3. b:Number       - b value [0-255]
        4. colorPoints:Dictionary       - color gamut triangle to limit the color conversion
        
        return : A dictionary object with key "x", "y", "b", None if invalid input
        '''
        pass

    @staticmethod
    def cie_to_rgb(x, y, b=1.0, colorPoints={"r":(1.0, 0), "g":(0.0, 1.0), "b":(0.0, 0.0)}):
        '''
        Function : Convert CIE XYB to RGB value
        1. x:Number       - x value [0-1]
        2. y:Number       - y value [0-1]
        3. b:Number       - b value [0-1]
        4. colorPoints:Dictionary       - color gamut triangle to limit the color conversion
         
        return : A dictionary object with key "r", "g", "b", None if invalid input
        '''
        pass

    @staticmethod
    def hex_to_rgb(hexString):
        '''
        Function : Convert Hex value to RGB
        1. hexString:String / List       - The hex value
        
        return: A dictionary object with key "r", "g", "b" [0-255], None if invalid input 
        '''
        pass

    @staticmethod
    def rgb_to_hex(r, g, b):
        '''
        Function : Convert RGB to hex string
        1. r:Number       - r value [0-255]
        2. g:Number       - g value [0-255]
        3. b:Number       - b value [0-255]
        
        return : Hex string representation, None if invalid input
        '''
        pass

    @staticmethod
    def hex_to_cie(hexString, colorPoints={"r":(1.0, 0), "g":(0.0, 1.0), "b":(0.0, 0.0)}):
        '''
        Function : Convert Hex value to CIE XYB
        1. hexString:String / List       - The hex value
        2. colorPoints:Dictionary        - color gamut triangle to limit the color conversion
         
        return : A dictionary object with key "x", "y", "b", None if invalid input
        '''
        pass

    @staticmethod
    def cie_to_hex(x, y, b=1.0, colorPoints={"r":(1.0, 0), "g":(0.0, 1.0), "b":(0.0, 0.0)}):
        '''
        Function : Convert CIE to hex string
        1. x:Number       - x value [0-0.8]
        2. y:Number       - y value [0-1]
        3. b:Number       - b value [0-1]
        4. colorPoints:Dictionary        - color gamut triangle to limit the color conversion
        
        return : Hex string representation, None if invalid input
        '''
        pass

    @staticmethod
    def rgb_to_hsb(r, g, b):
        '''
        Function : Convert RGB to HSB
        1. r:Number       - r value [0-255]
        2. g:Number       - g value [0-255]
        3. b:Number       - b value [0-255]
        
        return : Dictionary with "h", "s", "b", None if invalid input
        NOTE : "h" may be None if the r = g = b = 0
        '''
        pass

    @staticmethod
    def hsb_to_rgb(h, s, b):
        '''
        Function : Convert HSB to RGB
        1. h:Number       - h value [0-360]
        2. s:Number       - s value [0-1]
        3. b:Number       - b value [0-1]
        
        return : Dictionary with "h", "s", "b", None if invalid input
        '''
        pass

