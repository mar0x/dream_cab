import cadquery as cq

c1 = cq.Workplane("XY") \
    .rarray(11.7, 6.35, 2, 3) \
      .rect(0.4, 1.5) \
    .extrude(8.5) \
    .edges("|X").chamfer(0.5) \
    .translate((0, -21.5 / 2 + 4.25 + 6.35, -3.3))

c2 = cq.Workplane("XY") \
    .rarray(13.1, 6.35, 2, 3) \
        .rect(1.5, 0.4) \
    .extrude(25) \
    .edges("|Y").chamfer(0.5) \
    .translate((0, -21.5 / 2 + 4.25 + 3.25 + 6.35, -3.3))

d1 = cq.Workplane("XY") \
    .rect(16, 21.5) \
    .extrude(12.9) \
    .faces("<Y").workplane(centerOption="CenterOfBoundBox") \
        .circle(10.7 / 2) \
        .extrude(9.5) \
    .faces("<Y").chamfer(1) \
    .faces("<Y").workplane(centerOption="CenterOfBoundBox") \
        .hole(7.5) \
    .faces(">Y").workplane(centerOption="CenterOfBoundBox") \
        .circle(9 / 2) \
        .extrude(3) \
    .faces(">Y").chamfer(2.1) \
    .faces("|Z").chamfer(0.1) \
    .cut(
        cq.Workplane("XY") \
          .rect(4.5, 5.3) \
          .extrude(6.5) \
          .translate((0, 5.3 / 2 - 21.5 / 2, 0))
     ) \
    .cut(
        cq.Workplane("XY") \
          .rect(7.9, 12.2) \
          .extrude(3.5) \
          .translate((0, 12.2 / 2 + 21.5 / 2 - 1 - 12.2, 0))
     ) \
    .cut(
        cq.Workplane("XY") \
          .rarray(16 - 2.7, 6.35, 2, 3) \
              .rect(2.7, 1.7) \
          .extrude(4.5) \
          .translate((0, -21.5 / 2 + 4.25 + 6.35, 0))
    )


s = cq.Workplane("XY") \
    .rect(16, 21.5) \
    .extrude(3.9) \
    .faces("|Z").chamfer(0.1) \
    .translate((0, 0, 12.9))

d2 = d1.translate((0, 0, 12.9 + 3.9))

body_color = (103, 103, 103, 0)
body_options = {"rgba": body_color}

leg_color = (200, 200, 200, 0)
leg_options = {"rgba": leg_color}

if __name__ == '__cqgi__':
    show_object(d1, options=body_options)
    show_object(s, options=body_options)
    show_object(d2, options=body_options)

    show_object(c1, options=leg_options)
    show_object(c2, options=leg_options)
