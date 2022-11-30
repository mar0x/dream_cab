# This is a CadQuery script template
# Add your script code below
import cadquery as cq
import math

side_panel_width = 130
side_panel_length = 178
side_panel_thickness = 2.5
side_panel_clearance = 0.5

face_thickness = 3
#face_depth = 90 - face_thickness
face_depth = side_panel_length / 2 + side_panel_clearance
face_width = 136
face_height = 136

outer_edge_thickness = 2

edge_width = 12
edge_height = 12
edge_depth = 15
edge_gap = 3.3
edge_bottom_gap = 2.3

iedge_width = 11
iedge_height = 11
iedge_depth = 15
iedge_thickness = 3

dpanel_thickness = 4

hole_tolerance = 1
gap_tolerance = 0.5
dpanel_clearance = 0.2

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
        ) \
        .union(
            cq.Workplane("XY") \
            .rect(face_width + edge_gap * 2 + outer_edge_thickness, face_depth + face_thickness) \
            .extrude(edge_gap - edge_bottom_gap) \
            .translate((0, -(face_depth + face_thickness) / 2, -face_height / 2 - edge_gap))
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
            .rect(side_panel_width + 2 * side_panel_clearance, face_height + edge_gap * 2) \
            .extrude(face_depth)
        ) \
        .cut(
            cq.Workplane("XZ") \
            .rect(face_width + edge_gap * 2, side_panel_width + 2 * side_panel_clearance) \
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

back = face.rotate((0, 0, 0), (0, 1, 0), 0)


# making 5 holes 11mm for buttons
face = face.faces("<Y").workplane(centerOption="CenterOfBoundBox") \
        .center(14, face_height / 2 - 34) \
        .rarray(14, 1, 5, 1, True) \
        .hole(11 + hole_tolerance)

# making 5 small holes 3mm
face = face.faces("<Y").workplane(centerOption="CenterOfBoundBox") \
        .center(- face_width / 2 + 24, 0) \
        .rarray(1, 6, 1, 5, True) \
        .hole(3 + hole_tolerance)

# making 2 holes 9mm
face = face.faces("<Y").workplane(centerOption="CenterOfBoundBox") \
        .center(- face_width / 2 + 25 + 24, - face_height / 2 + 25) \
        .rarray(25 * 2, 1, 2, 1, True) \
        .hole(9 + hole_tolerance)

# making hole 6mm
face = face.faces("<Y").workplane(centerOption="CenterOfBoundBox") \
        .center(- face_width / 2 + 25 + 24, - face_height / 2 + 25) \
        .hole(6 + hole_tolerance)

# making 2 small holes 3mm
face = face.faces("<Y").workplane(centerOption="CenterOfBoundBox") \
        .center(- face_width / 2 + 44, - face_height / 2 + 25) \
        .rarray(1, 26, 1, 2, True) \
        .hole(3 + hole_tolerance)

# making top left hole 16mm
face = face.faces("<Y").workplane(centerOption="CenterOfBoundBox") \
        .center(- face_width / 2 + 24, face_height / 2 - 25) \
        .hole(16 + hole_tolerance)

# making center hole 7mm
face = face.faces("<Y").workplane(centerOption="CenterOfBoundBox") \
        .center(- face_width / 2 + 49, 0) \
        .hole(7 + hole_tolerance)

# making large hole at the right bottom corner
face = face.faces("<Y").workplane(centerOption="CenterOfBoundBox") \
        .center(face_width / 2 - 24, - face_height / 2 + 25) \
        .hole(16 + hole_tolerance)

# making 2 small holes at the right bottom corner
face = face.faces("<Y").workplane(centerOption="CenterOfBoundBox") \
        .center(face_width / 2 - 24, - face_height / 2 + 25) \
        .rarray(1, 26.4, 1, 2, True) \
        .hole(3.5 + hole_tolerance)

stand_centers = [
      (face_width / 2 - 13, 17.5),
      (face_width / 2 - 13, 1.5) ]

# extrude stands
face = face.faces("<Y[-2]").workplane(centerOption="CenterOfBoundBox") \
        .pushPoints(stand_centers) \
        .circle(6 / 2).circle(1).extrude(10)

t_width = 8
t_height = 6
t_clearance = 0.3

t_slot = cq.Workplane("XY") \
        .moveTo(0, t_height + t_clearance) \
        .polyline( [
            (t_width / 2 + t_clearance, t_height + t_clearance),
            (t_width / 2 + t_clearance, t_height - 2 - t_clearance),
            (2 / 2 + t_clearance, t_height - 2 - t_clearance),
            (2 / 2 + t_clearance, 0),
            (0, 0) ] ) \
        .mirrorY() \
        .extrude(dpanel_thickness)

t_edge = cq.Workplane("YZ") \
        .moveTo(0, 0) \
        .polyline( [ (10, 0), (0, 3), (0, 0) ] ) \
        .close() \
        .extrude(2) \
        .translate((-2 / 2, t_height + t_clearance, dpanel_thickness))

#        .translate((- 20 - 4 + 1.5 - 3, -16 + 3, 3))

dpanel_test = cq.Workplane("XY") \
        .rect(60, 20).extrude(dpanel_thickness) \
        .cut( t_slot.translate((48 / 2, -20 / 2, 0)) ) \
        .cut( t_slot.translate((-48 / 2, -20 / 2, 0)) ) \
        .union( t_edge.translate((48 / 2, -20 / 2, 0)) ) \
        .union( t_edge.translate((-48 / 2, -20 / 2, 0)) )

dpanel = cq.Workplane("XY") \
        .moveTo(0, face_height / 2 - dpanel_clearance) \
        .polyline( [
            (face_width / 2 - iedge_width - dpanel_clearance, face_height / 2 - dpanel_clearance),
            (face_width / 2 - iedge_width - dpanel_clearance, face_height / 2 - iedge_thickness - dpanel_clearance),
            (face_width / 2 - iedge_thickness - dpanel_clearance, face_height / 2 - iedge_thickness - dpanel_clearance),
            (face_width / 2 - iedge_thickness - dpanel_clearance, face_height / 2 - iedge_height - dpanel_clearance),
            (face_width / 2 - dpanel_clearance, face_height / 2 - iedge_height - dpanel_clearance),
            (face_width / 2 - dpanel_clearance, 0),
            (face_width / 2 - dpanel_clearance, -face_height / 2 + iedge_height + dpanel_clearance),
            (face_width / 2 - iedge_thickness - dpanel_clearance, -face_height / 2 + iedge_height + dpanel_clearance),
            (face_width / 2 - iedge_thickness - dpanel_clearance, -face_height / 2 + iedge_thickness + dpanel_clearance),
            (face_width / 2 - iedge_width - dpanel_clearance, -face_height / 2 + iedge_thickness + dpanel_clearance),
            (face_width / 2 - iedge_width - dpanel_clearance, -face_height / 2 + dpanel_clearance),
            (0, -face_height / 2 + dpanel_clearance),
        ] ) \
        .mirrorY() \
        .extrude(dpanel_thickness) \
        .faces("<Z").workplane(centerOption="CenterOfBoundBox") \
            .rarray(100, 100, 2, 2, True) \
            .hole(4 + hole_tolerance) \
        .faces("<Z").workplane(centerOption="CenterOfBoundBox") \
            .rarray(121, 121, 2, 2, True) \
            .hole(3.5 + hole_tolerance) \
        .faces("<Z").workplane(centerOption="CenterOfBoundBox") \
            .hole(112 + hole_tolerance) \
        .cut( t_slot.translate((48 / 2, -face_height / 2 + dpanel_clearance, 0)) ) \
        .cut( t_slot.translate((-48 / 2, -face_height / 2 + dpanel_clearance, 0)) ) \
        .union( t_edge.translate((48 / 2, -face_height / 2 + dpanel_clearance, 0)) ) \
        .union( t_edge.translate((-48 / 2, -face_height / 2 + dpanel_clearance, 0)) ) \
        .rotate((0, 0, 0), (1, 0, 0), 90) \
        .translate((0, 30, 0))

dpanel_mount_width = 11
dpanel_mount_height = 11
dpanel_mount_thickness = 6

dpanel_mount = cq.Workplane("XZ") \
        .rect(dpanel_mount_width, dpanel_mount_height) \
        .extrude(dpanel_mount_thickness) \
        .union(
            cq.Workplane("XY") \
            .moveTo(-dpanel_mount_width / 2, -dpanel_mount_thickness) \
            .polyline( [ (dpanel_mount_width / 2, -22), (dpanel_mount_width / 2, -dpanel_mount_thickness) ] ) \
            .close() \
            .extrude(dpanel_mount_height) \
            .translate(( 0, 0, -dpanel_mount_height / 2))
        ) \
        .union(
            cq.Workplane("ZY") \
            .moveTo(-dpanel_mount_height / 2, -dpanel_mount_thickness) \
            .polyline( [ (dpanel_mount_height / 2, -22), (dpanel_mount_height / 2, -dpanel_mount_thickness) ] ) \
            .close() \
            .extrude(dpanel_mount_width) \
            .translate((dpanel_mount_width / 2, 0, 0))
        ) \
        .faces(">Y").workplane(centerOption="CenterOfBoundBox") \
            .center(- dpanel_mount_width / 2 + 7.5, dpanel_mount_height / 2 - 7.5) \
            .hole(2.5 + hole_tolerance) \
        .translate((face_width / 2 - dpanel_mount_width / 2, -face_depth + 3 + 49, face_height / 2 - dpanel_mount_height / 2))

back = back.union(dpanel_mount) \
        .union(dpanel_mount.rotate((0, 0, 0), (0, 1, 0), 90)) \
        .union(dpanel_mount.rotate((0, 0, 0), (0, 1, 0), 180)) \
        .union(dpanel_mount.rotate((0, 0, 0), (0, 1, 0), -90))

back = back.rotate((0, 0, 0), (0, 0, 1), 180) \
        .translate((0, 5, 0))

import mic_mount

mm = mic_mount.create() \
        .rotate((0, 0, 0), (1, 0, 0), 90) \
        .translate((0, -10, 0))

import servo_mount

sm = servo_mount.create() \
        .translate((0, -40, -41))

if __name__ == '__cqgi__':
    show_object(face)
    show_object(dpanel)
    show_object(dpanel_test)
    show_object(back)
    show_object(mm)
    show_object(sm)
else:
    from cadquery import exporters

    box = face # cover.union(base)

    name = 'box_%dx%d' % (midi_sock_count, midi_sock_count)
    exporters.export(box, name + '.step')
    exporters.export(box, name + '.stl')
    exporters.export(box, name + '.vrml')
