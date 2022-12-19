from .Polygon import Point3D
from .Flash import Angle


class Camera:
    """
    class Camera:

    Attributes:
        location: Point3D
        angle: Angle

    Methods:
        vRotUte:
            rotate the camera
        move:
            moving camera
    """
    def __init__(self, location: Point3D, angle: 'Angle'):
        self.location = location
        self.angle = angle

    def vRotUte(self, angle: 'Angle'):
        self.angle.flat_angle_x += angle.flat_angle_x
        self.angle.flat_angle_y += angle.flat_angle_y
        self.angle.flat_angle_z += angle.flat_angle_z

    def move(self, point: 'Point3D'):
        self.location = point
