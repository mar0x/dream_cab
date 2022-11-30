# This is a CadQuery script template
# Add your script code below
import cadquery as cq

from importlib import reload 
import gcab
gcab = reload(gcab)

from gcab import dpanel
from gcab import servo_mount

if __name__ == '__cqgi__':
    show_object( dpanel.create(cq).translate((0, 40, 0)) )
    show_object( servo_mount.create(cq) \
        .translate((0, -40, -40.8))
    )
