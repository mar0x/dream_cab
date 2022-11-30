import cadquery as cq

from importlib import reload 
import gcab
gcab = reload(gcab)


from gcab import back

if __name__ == '__cqgi__':
    b = back.create(cq)

#    b = cq.Workplane("XZ").sphere(60) \
#        .translate((-back.width / 2, back.depth, -back.height / 2)) \
#        .intersect(b)

    show_object(b)

