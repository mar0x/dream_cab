hole_tolerance = 0.5

def mirror_x(p):
    return (p[0], -p[1])

def mirror_y(p):
    return (-p[0], p[1])

class side_panel:
    width = 130
    length = 178
    thickness = 2 + 0.8
    clearance = 0.5

class outer_edge:
    thickness = 2
    width = 12  # horizontal (X) dimension
    height = 12 # vertical (Z) dimension
    depth = 15  # Y dimension
    gap = side_panel.thickness + 0.3   # the distance to inner_edge

    @classmethod
    def create(c, cq):
        return cq.Workplane("XZ") \
            .rect(face.width + c.gap * 2 - c.width * 2, face.height + c.gap * 2 + c.thickness * 2) \
            .extrude(face.depth + face.thickness - c.depth) \
            .union(
                cq.Workplane("XZ") \
                .rect(face.width + c.gap * 2 + c.thickness * 2, face.height + c.gap * 2 - c.height * 2) \
                .extrude(face.depth + face.thickness - c.depth)
            )

class face:
    thickness = 3
    depth = side_panel.length / 2 + side_panel.clearance
    outer_width = 144 + (outer_edge.gap - 2.0) * 2   # outer horizontal (X) dimension
    outer_height = 144 + (outer_edge.gap - 2.0) * 2  # outer vertical (Z) dimension

    width = outer_width - 2 * outer_edge.thickness - 2 * outer_edge.gap
    height = outer_height - 2 * outer_edge.thickness - 2 * outer_edge.gap

    @classmethod
    def create_box(c, cq):
        # make the box
        face = cq.Workplane("XZ") \
            .rect(c.width + outer_edge.gap * 2, c.height + outer_edge.gap * 2) \
            .extrude(c.depth + c.thickness - outer_edge.thickness) \
            .faces(">Y").shell(outer_edge.thickness) \
            .union(
                cq.Workplane("XZ") \
                .rect(c.width + outer_edge.gap * 2, c.height + outer_edge.gap * 2) \
                .extrude(c.thickness - outer_edge.thickness) \
                .translate((0, -c.depth))
            ) \
            .cut( outer_edge.create(cq) )

        # make the inner enforcements
        ienf = cq.Workplane("XZ") \
            .rect(c.width + outer_edge.gap * 2, c.height + outer_edge.gap * 2) \
            .extrude(c.depth + c.thickness - outer_edge.thickness) \
            .faces(">Y").shell(-outer_edge.gap - inner_edge.thickness) \
            .cut(
                cq.Workplane("XZ") \
                .rect(side_panel.width + 2 * side_panel.clearance, c.height + outer_edge.gap * 2) \
                .extrude(c.depth)
            ) \
            .cut(
                cq.Workplane("XZ") \
                .rect(c.width + outer_edge.gap * 2, side_panel.width + 2 * side_panel.clearance) \
                .extrude(c.depth)
            )

        return face.union( inner_edge.create(cq) ).union( ienf )

    @classmethod
    def drill(c, f):
        # making 5 small holes 3mm
        f = f.faces("<Y").workplane(centerOption="CenterOfBoundBox") \
                .center(-48, 0) \
                .rarray(1, 6, 1, 5, True) \
                .hole(3 + hole_tolerance)

        # making 4 holes 11mm
        f = f.faces("<Y").workplane(centerOption="CenterOfBoundBox") \
                .center(-24, -47 + 16.5 / 2) \
                .rarray(24 * 2, 16.5, 2, 2, True) \
                .hole(11 + hole_tolerance)

        # making hole 6mm
        f = f.faces("<Y").workplane(centerOption="CenterOfBoundBox") \
                .center(-24, -47) \
                .hole(6 + hole_tolerance)

        # making 2 small holes 3mm
        f = f.faces("<Y").workplane(centerOption="CenterOfBoundBox") \
                .center(-24, -47) \
                .rarray(22, 1, 2, 1, True) \
                .hole(3 + hole_tolerance)

        # making top left hole 16mm
        f = f.faces("<Y").workplane(centerOption="CenterOfBoundBox") \
                .center(-48, 41) \
                .hole(16 + hole_tolerance)

        # making center hole 7mm
        f = f.faces("<Y").workplane(centerOption="CenterOfBoundBox") \
                .center(-24, 0) \
                .hole(7 + hole_tolerance)

        # making 7mm hole at the right
        f = f.faces("<Y").workplane(centerOption="CenterOfBoundBox") \
                .center(36, 0) \
                .hole(7 + hole_tolerance)

        # making rect hole at the right
        f = f.faces("<Y").workplane(centerOption="CenterOfBoundBox") \
                .center(36, 30) \
                .rect(13, 19) \
                .cutThruAll()

        f = f.faces("<Y").workplane(centerOption="CenterOfBoundBox") \
                .center(36, 30) \
                .rect(13 + 4, 19 + 4) \
                .cutBlind(-1)

        # making 2 holes 7mm at the right bottom corner
        f = f.faces("<Y").workplane(centerOption="CenterOfBoundBox") \
                .center(36, -47) \
                .rarray(24, 1, 2, 1, True) \
                .hole(7 + hole_tolerance)

        # making 3 holes 2mm at the top and bottom edges
        f = f.faces(">Z").workplane(centerOption="CenterOfBoundBox") \
            .center(0, - c.depth / 2 + outer_edge.depth - 9) \
            .rarray((c.width - outer_edge.width) / 2 - 3, 1, 3, 1, True) \
            .hole(2)

        return f

    @classmethod
    def create_stands(c, cq):
        stand_centers = [
              (-48 - 11, 17),
              (-48 - 11, 1) ]

        # extrude stands
        s = cq.Workplane("XZ") \
                .pushPoints(stand_centers) \
                .circle(6 / 2).circle(1).extrude(9) \
                .translate((0, -c.depth + 9, 0))

        return s

    @classmethod
    def create(c, cq):
        box = c.create_box(cq)

        dpm = dpanel_mount.create3(cq)

        box = box \
            .union(dpm) \
            .union(dpm.rotate((0, 0, 0), (0, 1, 0), 90)) \
            .union(dpm.rotate((0, 0, 0), (0, 1, 0), 180)) \
            .union(dpm.rotate((0, 0, 0), (0, 1, 0), -90)) \
            .faces(">Y").workplane(centerOption="CenterOfBoundBox") \
                .rarray(c.width + outer_edge.gap, c.height + outer_edge.gap, 2, 2) \
                .hole(4.2, 10) \

        return c.drill(box) \
            .union(c.create_stands(cq)) \
            .cut(connect_rim.create(cq))

class back(face):
    thickness = 3

    @classmethod
    def create(c, cq):
        dpm = dpanel_mount.create2a(cq)
        dpm3 = dpanel_mount.create3(cq)

        box = c.create_box(cq) \
            .union(dpm) \
            .union(dpm.rotate((0, 0, 0), (0, 1, 0), 90)) \
            .union(dpm.rotate((0, 0, 0), (0, 1, 0), 180)) \
            .union(dpm.rotate((0, 0, 0), (0, 1, 0), -90)) \
            .union(dpm3) \
            .union(dpm3.rotate((0, 0, 0), (0, 1, 0), 90)) \
            .union(dpm3.rotate((0, 0, 0), (0, 1, 0), 180)) \
            .union(dpm3.rotate((0, 0, 0), (0, 1, 0), -90)) \
            .rotate((0, 0, 0), (0, 0, 1), 180) \
            .faces(">Y").workplane(centerOption="CenterOfBoundBox") \
                .center(52, -55) \
                .hole(11 + hole_tolerance, c.thickness) \
            .faces(">Y").workplane(centerOption="CenterOfBoundBox") \
                .center(-50, -46) \
                .pushPoints([
                    (-mic_socket.hole_x, mic_socket.hole_y),
                    (mic_socket.hole_x, -mic_socket.hole_y)
                    ]) \
                .hole(mic_socket.hole_d + hole_tolerance, c.thickness * 2) \
            .faces(">Y").workplane(centerOption="CenterOfBoundBox") \
                .rarray(c.width + outer_edge.gap, c.height + outer_edge.gap, 2, 2) \
                .cboreHole(3.2, 6, 4) \
            .cut(
                mic_socket.create(cq) \
                .rotate((0,0,0), (1, 0, 0), 90) \
                .translate((50, c.depth + c.thickness, -46))
            ) \
            .faces(">Z").workplane(centerOption="CenterOfBoundBox") \
                .center(0, c.depth / 2 - outer_edge.depth + 9) \
                .rarray((c.width - outer_edge.width) / 2 - 3, 1, 3, 1, True) \
                .hole(2) \
            .cut(connect_rim.create(cq))

        return box

class dpanel_mount:
    width = 11
    height = 11
    thickness = 5
    hole_d = 3.2
    threaded_hole_d = 4.2

    @classmethod
    def create(c, cq):
        return cq.Workplane("XZ") \
            .rect(c.width, c.height) \
            .extrude(c.thickness) \
            .faces(">Y").workplane(centerOption="CenterOfBoundBox") \
                .center(- c.width / 2 + 7.5, c.height / 2 - 7.5) \
                .hole(c.hole_d + hole_tolerance) \
            .translate((face.width / 2 - c.width / 2, -face.depth + 3 + 49, face.height / 2 - c.height / 2))

    @classmethod
    def create2(c, cq):
        return cq.Workplane("XZ") \
            .rect(c.width, c.height) \
            .extrude(c.thickness) \
            .union(
                cq.Workplane("XY") \
                    .moveTo(-c.width / 2, -c.thickness) \
                    .polyline( [ (c.width / 2, -22), (c.width / 2, -c.thickness) ] ) \
                    .close() \
                .extrude(c.height) \
                .translate(( 0, 0, -c.height / 2))
            ) \
            .union(
                cq.Workplane("ZY") \
                    .moveTo(-c.height / 2, -c.thickness) \
                    .polyline( [ (c.height / 2, -22), (c.height / 2, -c.thickness) ] ) \
                    .close() \
                .extrude(c.width) \
                .translate((c.width / 2, 0, 0))
            ) \
            .faces(">Y").workplane(centerOption="CenterOfBoundBox") \
                .center(- c.width / 2 + 7.5, c.height / 2 - 7.5) \
                .hole(c.hole_d + hole_tolerance) \
            .cut(
                square_nut.create(cq) \
                .rotate((0, 0, 0), (1, 0, 0), 90) \
                .translate((c.width / 2 - 7.5, -4, c.height / 2 - 7.5))
            ) \
            .cut(
                square_nut.create(cq) \
                .rotate((0, 0, 0), (1, 0, 0), 90) \
                .translate((c.width / 2 - 7.5 - 1, -4, c.height / 2 - 7.5))
            ) \
            .translate((face.width / 2 - c.width / 2, -face.depth + 3 + 49, face.height / 2 - c.height / 2)) \

    @classmethod
    def create2a(c, cq):
        return cq.Workplane("XZ") \
            .rect(c.width, c.height) \
            .extrude(c.thickness) \
            .union(
                cq.Workplane("XY") \
                    .moveTo(-c.width / 2, -c.thickness) \
                    .polyline( [ (c.width / 2, -22), (c.width / 2, -c.thickness) ] ) \
                    .close() \
                .extrude(c.height) \
                .translate(( 0, 0, -c.height / 2))
            ) \
            .union(
                cq.Workplane("ZY") \
                    .moveTo(-c.height / 2, -c.thickness) \
                    .polyline( [ (c.height / 2, -22), (c.height / 2, -c.thickness) ] ) \
                    .close() \
                .extrude(c.width) \
                .translate((c.width / 2, 0, 0))
            ) \
            .faces(">Y").workplane(centerOption="CenterOfBoundBox") \
                .center(- c.width / 2 + 7.5, c.height / 2 - 7.5) \
                .hole(c.threaded_hole_d + hole_tolerance) \
            .translate((face.width / 2 - c.width / 2, -face.depth + 3 + 49, face.height / 2 - c.height / 2)) \

    @classmethod
    def create3(c, cq):
        return cq.Workplane("XZ") \
            .rect(c.width, c.height) \
            .extrude(c.thickness) \
            .union(
                cq.Workplane("XY") \
                    .moveTo(-c.width / 2, -c.thickness) \
                    .polyline( [ (c.width / 2, -22), (c.width / 2, -c.thickness) ] ) \
                    .close() \
                .extrude(c.height) \
                .translate(( 0, 0, -c.height / 2))
            ) \
            .union(
                cq.Workplane("ZY") \
                    .moveTo(-c.height / 2, -c.thickness) \
                    .polyline( [ (c.height / 2, -22), (c.height / 2, -c.thickness) ] ) \
                    .close() \
                .extrude(c.width) \
                .translate((c.width / 2, 0, 0))
            ) \
            .faces(">Y").workplane(centerOption="CenterOfBoundBox") \
                .center(- c.width / 2 + 7.5 + 2, c.height / 2 - 7.5 - 2) \
                .hole(c.hole_d + 2 * 2 + hole_tolerance) \
            .translate((face.width / 2 - c.width / 2, 0, face.height / 2 - c.height / 2)) \

class square_nut:
    width = 5.5
    height = 1.8

    clearance = 0.3
    hclearance = 0.3

    @classmethod
    def create(c, cq):
        return cq.Workplane("XY") \
            .rect(c.width + 2 * c.clearance, c.width + 2 * c.clearance) \
            .extrude(c.height + 2 * c.hclearance)

class inner_edge:
    thickness = 3
    width = 11  # horizontal (X) dimension
    height = 11 # vertical (Z) dimension
    depth = 15  # Y dimension

    @classmethod
    def create(c, cq):
        return cq.Workplane("XZ") \
            .rect(face.width, face.height) \
            .extrude(face.depth + c.thickness) \
            .faces(">Y").shell(-c.thickness) \
            .cut(
                cq.Workplane("XZ") \
                .rect(face.width - c.width * 2, face.height) \
                .extrude(face.depth + face.thickness - c.depth)
            ) \
            .cut(
                cq.Workplane("XZ") \
                .rect(face.width, face.height - c.height * 2) \
                .extrude(face.depth + face.thickness - c.depth)
            )

class connect_rim:
    depth = 8

    @classmethod
    def create(c, cq):
        return cq.Workplane("XZ") \
            .rect(face.width, face.height) \
            .rect(face.width - 2 * inner_edge.thickness, face.height - 2 * inner_edge.thickness) \
            .extrude(c.depth) \
            .edges("|Y").fillet(3) \
            .translate((0, c.depth / 2, 0))

class T_bar:
    width = 8
    height = 6
    thickness = 2

    polyline_r = [
        (width / 2, height),
        (width / 2, height - thickness),
        (thickness / 2, height - thickness),
        (thickness / 2, 0)
    ]

    @classmethod
    def start(c):
        return c.polyline_r[0]

    @classmethod
    def polyline(c):
        r = list(c.polyline_r)
        l = list(map(mirror_y, r))
        l.reverse()

        r.extend(l)
        r.pop(0)

        return r

    @classmethod
    def create(c, cq, length):
        return cq.Workplane("XY") \
            .moveTo(*c.start()) \
            .polyline( c.polyline() ) \
            .close() \
            .extrude(length)

class T_slot:
    clearance = 0.2
    width = T_bar.width + 2 * clearance
    height = T_bar.height + clearance
    thickness = T_bar.thickness + 2 * clearance

    polyline_r = [
        (width / 2, height),
        (width / 2, height - thickness),
        (thickness / 2, height - thickness),
        (thickness / 2, 0)
    ]

    @classmethod
    def start(c):
        return c.polyline_r[0]

    @classmethod
    def polyline(c):
        r = list(c.polyline_r)
        l = list(map(mirror_y, r))
        l.reverse()

        r.extend(l)
        r.pop(0)

        return r

    @classmethod
    def create(c, cq, thk):
        return cq.Workplane("XY") \
            .moveTo( *c.start() ) \
            .polyline( c.polyline() ) \
                .close() \
            .extrude( thk )

class dpanel:
    thickness = 4
    clearance = 0.2

    width = face.width
    height = face.height

    polyline_tr = [
        (width / 2 - inner_edge.width, height / 2),
        (width / 2 - inner_edge.width, height / 2 - inner_edge.thickness),
        (width / 2 - inner_edge.thickness, height / 2 - inner_edge.thickness),
        (width / 2 - inner_edge.thickness, height / 2 - inner_edge.height),
        (width / 2, height / 2 - inner_edge.height)
    ]

    @classmethod
    def clear(c, p):
        return (p[0] - c.clearance, p[1] - c.clearance)

    @classmethod
    def start(c):
        return c.clear(c.polyline_tr[0])

    @classmethod
    def polyline(c):
        tr = list(map(c.clear, c.polyline_tr))
        br = list(map(mirror_x, tr))
        br.reverse()
        tr.extend(br)

        l = list(map(mirror_y, tr))
        l.reverse()

        tr.extend(l)
        tr.pop(0)

        return tr

    @classmethod
    def create(c, cq):
        t_slot = T_slot.create(cq, c.thickness) \
            .translate((0, -c.height / 2 + c.clearance, 0))

        t_edge = cq.Workplane("YZ") \
            .polyline( [ (8, 0), (0, 9), (0, 0) ] ) \
                .close() \
            .extrude( T_slot.width ) \
            .translate((-T_slot.width / 2, T_slot.height - c.height / 2 + c.clearance, c.thickness))

        return cq.Workplane("XY") \
            .moveTo(*c.start()) \
                .polyline( c.polyline() ) \
                .close() \
            .extrude( c.thickness ) \
            .faces("<Z").workplane(centerOption="CenterOfBoundBox") \
                .rarray(100, 100, 2, 2, True) \
                .hole(4 + hole_tolerance) \
            .faces("<Z").workplane(centerOption="CenterOfBoundBox") \
                .rarray(121, 121, 2, 2, True) \
                .hole(3.5 + hole_tolerance) \
            .faces("<Z").workplane(centerOption="CenterOfBoundBox") \
                .hole(112 + hole_tolerance) \
            .cut( t_slot.translate((48 / 2, 0, 0)) ) \
            .cut( t_slot.translate((-48 / 2, 0, 0)) ) \
            .union( t_edge.translate((48 / 2, 0, 0)) ) \
            .union( t_edge.translate((-48 / 2, 0, 0)) ) \
            .rotate((0, 0, 0), (1, 0, 0), 90)

class servo:
    width = 40
    height = 20
    clearance = 0.2

class servo_mount:
    hole_distance_x = 48
    hole_distance_y = 10
    bar_width = 8

    height = 34 - 4 - 2
    width = servo.width + 2 * bar_width
    thickness = 3

    @classmethod
    def create(c, cq):
        # make the box
        mount = cq.Workplane("XY").rect(c.width, c.height) \
                .extrude(c.thickness)

        # making 4 holes 4mm
        mount = mount.faces(">Z").workplane(centerOption="CenterOfBoundBox") \
                .center(0, c.height / 2 - servo.height / 2) \
                .rarray(c.hole_distance_x, c.hole_distance_y, 2, 2, True) \
                .hole(4 + hole_tolerance)

        mount = mount.cut(
                    cq.Workplane("XY") \
                    .rect(servo.width + servo.clearance * 2, servo.height + servo.clearance) \
                    .extrude(c.thickness) \
                    .translate((0, (c.height - servo.height) / 2, 0))
                )

        pin_height = 6

        pin = cq.Workplane("XY") \
              .rect(c.thickness, pin_height) \
              .extrude(c.thickness) \
              .translate((0, -c.height / 2 - pin_height / 2, 0))

        t_bar = T_bar.create(cq, 75) \
                .translate((0, - T_bar.height - c.height / 2, 0)) \
                .cut(pin)

        mount = mount \
                .union( t_bar.translate((c.hole_distance_x / 2, -7, 0)) ) \
                .union( t_bar.translate((-c.hole_distance_x / 2, -7, 0)) )

        edge = cq.Workplane("YZ") \
                    .moveTo(8, 0) \
                    .polyline( [ (0, 0), (0, 10) ] ) \
                    .close() \
                .extrude(c.bar_width) \
                .translate((-c.bar_width / 2, -c.height / 2, c.thickness)) \
                .union(pin)

        return mount \
                .union(edge.translate((c.hole_distance_x / 2, 0, 0))) \
                .union(edge.translate((-c.hole_distance_x / 2, 0, 0))) \
                .rotate((0, 0, 0), (1, 0, 0), 90) \
                .rotate((0, 0, 0), (0, 0, 1), 180)

class servo_arm2:
    clearance = 0.1
    thickness = 2.5 + 0.2
    r1 = 11.2 / 2
    r2 = 2.5
    length = 39.2
    width = 7.9
    wlen = 18.5

    @classmethod
    def create(c, cq):
        return cq.Workplane("XY") \
            .circle(c.r1 + c.clearance) \
            .extrude(c.thickness) \
            .union(
                cq.Workplane("XY") \
                .moveTo(c.width / 2 + c.clearance, 0) \
                .lineTo(c.width / 2 + c.clearance, - c.wlen / 2 - c.clearance) \
                .lineTo(c.r2 + c.clearance, - c.length / 2 + c.r2 - c.clearance) \
                .radiusArc((-c.r2 - c.clearance, -c.length / 2 + c.r2 - c.clearance), c.r2 + c.clearance) \
                .lineTo(-c.width / 2 - c.clearance, - c.wlen / 2 - c.clearance) \
                .lineTo(-c.width / 2 - c.clearance, 0) \
                .mirrorX() \
                .extrude(c.thickness)
            ) \
            .union(
                cq.Workplane("XY") \
                .circle(8.6 / 2 + c.clearance) \
                .extrude(6) \
                .translate((0, 0, -0.5)) \
                .faces("<Z").workplane(centerOption="CenterOfBoundBox") \
                .hole(5.8 - c.clearance, 1.5)
            )

class servo_arm:
    clearance = 0.1
    thickness = 2.4 + 0.2
    r1 = 12.1 / 2
    r2 = 2.5
    length = 38.2
    width = 8.7
    wlen = 8.6

    @classmethod
    def create(c, cq):
        return cq.Workplane("XY") \
            .circle(c.r1 + c.clearance) \
            .extrude(c.thickness) \
            .union(
                cq.Workplane("XY") \
                .moveTo(c.width / 2 + c.clearance, 0) \
                .lineTo(c.width / 2 + c.clearance, - c.wlen / 2 - c.clearance) \
                .lineTo(c.r2 + c.clearance, - c.length / 2 + c.r2 - c.clearance) \
                .radiusArc((-c.r2 - c.clearance, -c.length / 2 + c.r2 - c.clearance), c.r2 + c.clearance) \
                .lineTo(-c.width / 2 - c.clearance, - c.wlen / 2 - c.clearance) \
                .lineTo(-c.width / 2 - c.clearance, 0) \
                .mirrorX() \
                .extrude(c.thickness)
            ) \
            .union(
                cq.Workplane("XY") \
                .circle(8.5 / 2 + c.clearance) \
                .extrude(5.5) \
                .translate((0, 0, -0.1)) \
                .faces("<Z").workplane(centerOption="CenterOfBoundBox") \
                .hole(5.8 - c.clearance, 1.5)
            )

class mic_mount:
    hole_distance = 6

    inner_r = 29 / 2
    outer_r = 33 / 2

    height = 45 - inner_r
    width = 2 * (servo_arm.r1 + servo_arm.clearance + 1)
    thickness = 2.5

    @classmethod
    def create(c, cq):
        # make the box
        mount = cq.Workplane("XY").rect(c.width, c.height) \
                .extrude(c.thickness) \
                .translate((0, - c.inner_r - c.height / 2, 0))

        # making 2 holes 2.5mm
        mount = mount.faces(">Z").workplane(centerOption="CenterOfBoundBox") \
                .center(0, c.height / 2 - 10 - c.hole_distance / 2) \
                .rarray(1, c.hole_distance, 1, 2, True) \
                .hole(2.5 + hole_tolerance)

        ears = cq.Workplane("XY").rect(4 + 2 * 2, 10 + 2) \
                .extrude(10) \
                .faces(">Y").edges("|X").fillet(3) \
                .translate((0, c.inner_r + (10 + 2) / 2, 0)) \
                .faces(">X").workplane(centerOption="CenterOfBoundBox") \
                  .center(1, 0) \
                  .hole(3 + hole_tolerance)

        ring = cq.Workplane("XY").center(0, 0) \
                .circle(c.outer_r).circle(c.inner_r) \
                .extrude(10) \
                .union(ears) \
                .cut(
                  cq.Workplane("XY").rect(4, 10 + 4) \
                  .extrude(10) \
                  .translate((0, c.inner_r + (10 + 2) / 2, 0))
                ) \
                .faces("<Z").fillet(0.5)

        edge = cq.Workplane("YZ") \
                  .moveTo(-c.height, 0) \
                  .hLine(c.height) \
                  .vLine(10 - c.thickness) \
                  .hLine(-c.height) \
                  .close() \
                .extrude(1) \
                .translate((-0.5, -c.inner_r, c.thickness))

        edge2 = cq.Workplane("XY") \
                  .rect(c.width, 1) \
                  .extrude(10)

        mount = mount \
                .union(edge.translate((-c.width / 2 + 0.5, 0, 0))) \
                .union(edge.translate((c.width / 2 - 0.5, 0, 0))) \
                .union(edge2.translate((0, -28, 0))) \
                .union(edge2.translate((0, -33, 0))) \
                .union(edge2.translate((0, -38, 0))) \
                .faces("<Z").workplane(centerOption="CenterOfBoundBox") \
                .center(0, c.height / 2) \
                .cboreHole(3 + hole_tolerance, 5.5 + hole_tolerance, 4) \
                .faces("<Z").fillet(0.5)

        clutch = cq.Workplane("XY") \
                .circle(15 / 2) \
                .extrude(10) \
                .faces("<Z").workplane(centerOption="CenterOfBoundBox") \
                .cboreHole(3 + hole_tolerance, 5.5 + hole_tolerance, 4) \
                .translate((0, -45, 0)) \
                .faces("<Z").fillet(0.5)

        return ring.union(mount) \
                .union(clutch) \
                .cut(
                    servo_arm.create(cq).translate((0, -45, 10 - servo_arm.thickness))
                )

class mic_socket:

    bar_thickness = 3
    bar_width = 26
    bar_length = 32
    bar_fillet_r = 3

    face_r = 23.5 / 2
    face_height = 1.8 + 0.2

    body_r = 21.5 / 2
    body_height = 22 + bar_thickness + face_height

    hole_d = 3
    hole_stand_r = 5.6 / 2
    hole_stand_h = 2.7
    hole_x = bar_width / 2 - 1.4 - hole_stand_r
    hole_y = bar_length / 2 - 1.4 - hole_stand_r

    clearance = 0.3


    @classmethod
    def create(c, cq, clearance=None, holes=False):
        if clearance == None:
            clearance = c.clearance

        bar = cq.Workplane("XY") \
            .rect(c.bar_width + 2 * clearance, c.bar_length + 2 * clearance) \
            .extrude(c.bar_thickness + 2 * clearance) \
            .edges("|Z").fillet(c.bar_fillet_r + clearance) \
            .translate((0, 0, c.face_height + clearance)) \
            .faces(">Z").workplane(centerOption="CenterOfBoundBox") \
                .pushPoints([
                    (c.hole_x, c.hole_y),
                    (-c.hole_x, -c.hole_y)
                    ]) \
                .circle(c.hole_stand_r + clearance) \
                .extrude(c.hole_stand_h + clearance)

        if holes:
            bar = bar.faces("<Z").workplane(centerOption="CenterOfBoundBox") \
                .pushPoints([
                    (-c.hole_x, c.hole_y),
                    (c.hole_x, -c.hole_y)
                    ]) \
                .hole(c.hole_d)

        return cq.Workplane("XY") \
            .circle(c.body_r + clearance) \
            .extrude(c.body_height + 2 * clearance) \
            .union(
                cq.Workplane("XY") \
                .circle(c.face_r + clearance) \
                .extrude(c.face_height + clearance)
            ) \
            .union(bar) \
            .translate((0, 0, -clearance)) \

class mic_cover:
    base_d = 27
    inner_d = 24
    top_d = 29
    top_inner_d = 27
    height = 37

    hole_d = 4.2
    hole_x = 7.5

    @classmethod
    def create(c, cq, clearance=None, holes=False):
        if clearance == None:
            clearance = 0.2

        return cq.Workplane("XY") \
            .circle(c.base_d / 2) \
            .workplane(offset=c.height) \
            .circle(c.top_d / 2) \
            .loft(combine=True) \
            .faces(">Z").workplane(centerOption="CenterOfBoundBox") \
                .hole(c.top_inner_d + 2 * clearance, 5) \
            .faces(">Z[-2]").workplane(centerOption="CenterOfBoundBox") \
                .cskHole(c.inner_d + 2 * clearance,
                    c.top_inner_d + 2 * clearance, 82, c.height - 5 - 2 - clearance) \
            .faces("<Z") \
                .chamfer(0.5) \
            .faces("<Z").workplane(centerOption="CenterOfBoundBox") \
                .rarray(c.hole_x, 1, 3, 1) \
                .hole(c.hole_d + hole_tolerance) \


if __name__ == '__cqgi__':
    import cadquery as cq

    show_object( face.create(cq) )
    show_object( connect_rim.create(cq).translate((0, 8, 0)) )
    show_object( back.create(cq).translate((0, 16, 0)) )
    show_object( dpanel.create(cq).translate((0, 40, 0)) )

    show_object( mic_mount.create(cq) \
        .rotate((0, 0, 0), (1, 0, 0), 90) \
        .translate((0, -10, 0))
    )

    show_object( servo_mount.create(cq) \
        .translate((0, -40, -40.8))
    )
