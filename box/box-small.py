# This is a CadQuery script template
# Add your script code below
import cadquery as cq
import math

face_thickness = 3
face_depth = 30 - face_thickness
face_width = 35
face_height = 35

outer_edge_thickness = 2

edge_width = 10
edge_height = 10
edge_depth = 7
edge_thickness = 3
edge_gap = 3.3

iedge_width = 9
iedge_height = 9
iedge_depth = 7
iedge_thickness = 3

dpanel_thickness = 4

hole_tolerance = 1
gap_tolerance = 0.5
dpanel_tolerance = 0.2

# make the box
face = cq.Workplane("XZ") \
        .rect(face_width + edge_gap * 2, face_height + edge_gap * 2) \
        .extrude(face_depth + face_thickness - outer_edge_thickness) \
        .faces(">Y").shell(outer_edge_thickness) \
        .union(
            cq.Workplane("XZ") \
            .rect(face_width + edge_gap * 2, face_height + edge_gap * 2) \
            .extrude(face_thickness - outer_edge_thickness) \
            .translate((0, -face_depth))
        )

# make the inner box
iface = cq.Workplane("XZ").rect(face_width, face_height) \
        .extrude(face_depth + iedge_thickness) \
        .faces(">Y").shell(-iedge_thickness) \
        .cut(
            cq.Workplane("XZ") \
            .rect(face_width - iedge_width * 2, face_height) \
            .extrude(face_depth + face_thickness - edge_depth)
        ) \
        .cut(
            cq.Workplane("XZ") \
            .rect(face_width, face_height - iedge_height * 2) \
            .extrude(face_depth + face_thickness - edge_depth)
        )


# make the inner enforcements
ienf = cq.Workplane("XZ") \
        .rect(face_width + edge_gap * 2, face_height + edge_gap * 2) \
        .extrude(face_depth + face_thickness - outer_edge_thickness) \
        .faces(">Y").shell(-edge_gap - iedge_thickness) \
        .cut(
            cq.Workplane("XZ") \
            .rect(face_width - iedge_thickness * 2 + gap_tolerance + 2, face_height + edge_gap * 2) \
            .extrude(face_depth)
        ) \
        .cut(
            cq.Workplane("XZ") \
            .rect(face_width + edge_gap * 2, face_height - iedge_thickness * 2 + gap_tolerance * 2) \
            .extrude(face_depth)
        )

face = face \
        .cut(
            cq.Workplane("XZ") \
            .rect(face_width + edge_gap * 2 - edge_width * 2, face_height + edge_gap * 2 + outer_edge_thickness * 2) \
            .extrude(face_depth + face_thickness - edge_depth)
        ) \
        .cut(
            cq.Workplane("XZ") \
            .rect(face_width + edge_gap * 2 + outer_edge_thickness * 2, face_height + edge_gap * 2 - edge_height * 2) \
            .extrude(face_depth + face_thickness - edge_depth)
        ) \
        .union(iface) \
        .union(ienf)

# making 5 small holes
face = face.faces("<Y").workplane(centerOption="CenterOfBoundBox") \
        .center(- face_width / 2 + 25, 0) \
        .rarray(1, 6, 1, 4, True) \
        .hole(3 + hole_tolerance)

# making hole 7mm
face = face.faces("<Y").workplane(centerOption="CenterOfBoundBox") \
        .center(- face_width / 2 + 10, - face_height / 2 + 15) \
        .hole(7 + hole_tolerance)


if __name__ == '__cqgi__':
    show_object(face)
else:
    from cadquery import exporters

    box = face # cover.union(base)

    name = 'box_%dx%d' % (midi_sock_count, midi_sock_count)
    exporters.export(box, name + '.step')
    exporters.export(box, name + '.stl')
    exporters.export(box, name + '.vrml')
