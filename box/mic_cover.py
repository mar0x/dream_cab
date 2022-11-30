# This is a CadQuery script template
# Add your script code below
import cadquery as cq

from importlib import reload 
import gcab
gcab = reload(gcab)

from gcab import mic_cover

if __name__ == '__cqgi__':
    show_object( mic_cover.create(cq) )
