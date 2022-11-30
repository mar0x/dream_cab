import cadquery as cq

from importlib import reload
import gcab
gcab = reload(gcab)

from gcab import face

f = face.create(cq)
s1 = cq.Workplane("XZ").sphere(45) \
    .translate((face.width / 2, -face.depth, -face.height / 2)) \
    .intersect(f)

s2 = cq.Workplane("XZ").box(45, 45, 45) \
    .edges("|Y").fillet(6) \
    .translate((-47 - 5.5, -face.depth, 0)) \
    .intersect(f)

# f2 = f2.intersect(s2)

if __name__ == '__cqgi__':
    show_object(s1)
    show_object(s2)
