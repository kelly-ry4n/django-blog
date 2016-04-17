from __future__ import division 

import colorsys
import webcolors

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


    colors['light'] = colorsys.hsv_to_rgb(h,70/100,100/100) 
    colors['bright'] = colorsys.hsv_to_rgb(h,100/100,100/100)
    colors['dark'] = colorsys.hsv_to_rgb(h,70/100,50/100)
    colors['saturated'] = colorsys.hsv_to_rgb(h,100/100,80/100)


    for name, col in colors.iteritems():
        base_255 = [i*255 for i in col]
        hex = webcolors.rgb_to_hex(base_255)
        colors[name] = hex
        

    return colors

