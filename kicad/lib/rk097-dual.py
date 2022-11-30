import cadquery as cq
import math

e = cq.Workplane("XY") \
    .rect(9.5, 2) \
    .extrude(1) \
    .translate((0, 2, 0.35))

b = cq.Workplane("XY") \
    .rect(9.5, 7.5) \
    .extrude(6.5 + 4.85 - 0.35) \
    .edges("|Y and >Z").fillet(0.5) \
    .translate((0, 2 + 7.5 / 2, 0.35)) \
    .cut(e) \
    .faces("<Z").workplane(centerOption="CenterOfBoundBox") \
        .rarray(9.5 - 1, 7.5 - 1 - 0.7, 2, 2) \
        .rect(1, 0.7) \
        .extrude(0.35)

e2 = cq.Workplane("XZ") \
    .pushPoints([(-8.5/2, 7.5/2), (8.5/2, -7.5/2)]) \
    .rect(3, 3) \
    .extrude(0.5) \
    .edges("|Y").fillet(0.5) \
    .translate((0, 0.5, 6.5))

n = 18
r1 = 6 / 2
r2 = 5.3 / 2
shaft = []
for i in range(n):
    a = 2 * math.pi / n * i
    shaft.append((r1 * math.sin(a), r1 * math.cos(a)))

    a += math.pi / n
    shaft.append((r2 * math.sin(a), r2 * math.cos(a)))

shaft0 = shaft.pop(0)

L = 15
F = 8.5
W = 5

c = cq.Workplane("XZ") \
    .circle(r1 * 2) \
    .extrude(F) \
    .cut(
        cq.Workplane("XZ") \
          .circle(r1) \
          .extrude(F) \
          .faces("<Y").chamfer(0.5) \
    ) \
    .union(
        cq.Workplane("XZ") \
        .rect(r1 * 2, 1) \
        .extrude(F) \
        .rotate((0, 0, 0), (0, 1, 0), 90 - 3 * 360 / 18)
    ) \
    .translate((0, -W - (L - F - W), 6.5))

b1 = cq.Workplane("XY") \
    .rect(9.5, 2) \
    .extrude(6.5 + 4.85 - 0.35) \
    .edges("|Y").fillet(0.5) \
    .translate((0, 2 / 2, 0.35)) \
    .cut(e) \
    .faces("<Y").workplane(centerOption="CenterOfBoundBox") \
        .center(0, 1 - 0.35) \
        .circle(6.7 / 2) \
        .extrude(W) \
    .faces("<Y").chamfer(0.5) \
    .faces("<Y").workplane(centerOption="CenterOfBoundBox") \
        .circle(6 / 2) \
        .extrude(L - F - W) \
    .faces("<Y").workplane(centerOption="CenterOfBoundBox") \
        .moveTo(*shaft0) \
        .polyline(shaft) \
        .close() \
        .extrude(F) \
    .cut(c) \
    .cut(e2)

l = cq.Workplane("XY") \
    .rarray(2.5, 2.5, 3, 2) \
    .rect(0.8, 0.3) \
    .extrude(-3.5 - 0.35) \
    .edges("|Y and <Z").chamfer(0.2) \
    .translate((0, 5 + 2.5 / 2, 0.35))

body_color = (0, 131, 107, 0)
body_options = {"rgba": body_color}

metal_color = (200, 200, 200, 0)
metal_options = {"rgba": metal_color}

if __name__ == '__cqgi__':
    show_object(b, options=body_options)
    show_object(b1, options=metal_options)
    show_object(l, options=metal_options)
