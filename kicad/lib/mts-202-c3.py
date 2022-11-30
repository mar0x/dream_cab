import cadquery as cq

e = cq.Workplane("XZ") \
        .center(0, 12.7 / 2) \
        .rarray(1, 12.7 - 0.5, 1, 2) \
        .rect(10, 0.5) \
        .extrude(10) \
        .translate((0, 10 / 2, 0))

b = cq.Workplane("XY") \
    .rect(13.2, 10 - 0.5 * 2) \
    .extrude(12.7) \
    .edges("|Y").fillet(0.5) \
    .faces(">Y").workplane(centerOption="CenterOfBoundBox") \
        .rarray(4.7, 12.7 - 0.5, 2, 2) \
        .hole(1.2, 4) \
    .cut(e)

b1 = cq.Workplane("XY") \
    .rect(13.2, 10 - 0.5 * 2 - 3) \
    .extrude(12.7) \
    .edges("|Y or |X").fillet(0.5) \
    .translate((0, -3 / 2 - 0.5, 0)) \
    .faces("<Y").workplane(centerOption="CenterOfBoundBox") \
        .rect(8, 12.7) \
        .extrude(0.5) \
    .faces("<Y").workplane(centerOption="CenterOfBoundBox") \
        .circle(6 / 2) \
        .extrude(7.1) \
    .faces("<Y").fillet(0.5) \
    .faces("<Y").workplane(centerOption="CenterOfBoundBox") \
        .hole(4, 7.1) \
    .union(
        cq.Workplane("XY") \
            .rarray(5, 1, 2, 1) \
            .rect(1.2, 0.5) \
            .extrude(3.2) \
        .translate((0, -5.25, -3.2)) \
        .edges("|Y and <Z").fillet(0.5)
    ) \
    .cut(b)

l1 = cq.Workplane("YZ") \
    .moveTo(1.2 / 2, -3.2) \
    .vLine(8).hLine(-5) \
    .vLine(-1.2).hLine(5 - 1.2) \
    .vLine(-8 + 1.2).close() \
    .extrude(0.8) \
    .edges("|X and <Z").fillet(0.5) \
    .edges(">Y and >Z").fillet(1) \
    .translate((-0.4, 12.95 - 5.25, 0))

l2 = cq.Workplane("YZ") \
    .moveTo(1.2 / 2, -3.2) \
    .vLine(13).hLine(-5 - 3.8) \
    .vLine(-1.2).hLine(5 + 3.8 - 1.2) \
    .vLine(-13 + 1.2).close() \
    .extrude(0.8) \
    .edges("|X and <Z").fillet(0.5) \
    .edges(">Y and >Z").fillet(1) \
    .translate((-0.4, 12.95 - 5.25 + 3.8, 0))

s = cq.Workplane("XZ") \
    .sphere(5 / 2) \
    .union(
        cq.Workplane("XZ") \
            .circle(2 / 2) \
            .workplane(offset=7) \
            .circle(3 / 2) \
            .loft(combine=True)
    ) \
    .union(
        cq.Workplane("XZ").workplane(offset=7) \
            .sphere(3 / 2)
    ) \
    .rotate((0, 0, 0), (0, 0, 1), 20) \
    .translate((0, -5.5 - 7.1 - 6.9 + 7 + 3/2, 12.7 / 2))

body_color = (0, 122, 170, 0)
body_options = {"rgba": body_color}

metal_color = (200, 200, 200, 0)
metal_options = {"rgba": metal_color}

if __name__ == '__cqgi__':
    show_object(b, options=body_options)
    show_object(b1, options=metal_options)
    show_object(l1.translate((-4.7, 0)), options=metal_options)
    show_object(l1, options=metal_options)
    show_object(l1.translate((4.7, 0)), options=metal_options)
    show_object(l2.translate((-4.7, 0)), options=metal_options)
    show_object(l2, options=metal_options)
    show_object(l2.translate((4.7, 0)), options=metal_options)
    show_object(s, options=metal_options)
