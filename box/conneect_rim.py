import cadquery as cq

from importlib import reload 
import gcab
gcab = reload(gcab)

from gcab import connect_rim
from gcab import face

body_color = (103, 103, 103, 0)
body_options = {"rgba": body_color}

if __name__ == '__cqgi__':
    b = connect_rim.create(cq).translate((0, 8, 0))

    f = face.create(cq).cut(b)

#    b = cq.Workplane("XZ").sphere(60) \
#        .translate((-back.width / 2, back.depth, -back.height / 2)) \
#        .intersect(b)

    show_object(b, options=body_options)

    show_object(f, options=body_options)
