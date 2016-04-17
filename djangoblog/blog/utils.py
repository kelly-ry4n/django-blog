from __future__ import division 

import colorsys
import webcolors

class SNormalizer(object):


    def __init__(self, s,v):
        self.s = s
        self.v = v

    def __or__(self, col):

        return (col*self.s) / 100

class VNormalizer(object):

    def __init__(self, s,v):
        self.s = s
        self.v = v
        
    def __or__(self, col):

        print self.s, self.v, col

        return col*self.v/100

def get_colors_for_base(base):
    ''' returns a color pallet of the form

            colors = {
                'base':'#7F2900',
                'light':'#FF864C',
                'bright':'#FF5200',
                'dark':'#7F4326',
                'saturated':'#CC4200',
            }

    '''

    r,g,b = webcolors.hex_to_rgb('#' + base)
    h,s,v = colorsys.rgb_to_hsv(r/255,g/255,b/255)

    colors = {} 

    old_s = s

    s = SNormalizer(old_s,v)
    v = VNormalizer(old_s,v)


    colors['light'] = colorsys.hsv_to_rgb(h,s|70,v|100) 
    print colors['light']
    colors['bright'] = colorsys.hsv_to_rgb(h,s|100,v|100)
    colors['dark'] = colorsys.hsv_to_rgb(h,s|70,v|50)
    colors['saturated'] = colorsys.hsv_to_rgb(h,s|100,v|80)


    for name, col in colors.iteritems():
        base_255 = [i*255 for i in col]
        hex = webcolors.rgb_to_hex(base_255)
        colors[name] = hex
        

    return colors

