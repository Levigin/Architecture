import math

from .Polygon import Point3D
import numpy as np


class Flash:
    """
    class Flash:

    Attributes:
        location: Point3D
        angle: Angle
        colour: Colour
        power: float

    Methods:
        vRotUte:
            rotate the camera
        move:
            moving camera
    """

    def __init__(self, location: Point3D, angle: 'Angle', colour: 'Colour', power: float):
        self.location = location
        self.angle = angle
        self.colour = colour
        self.power = power

    def vRotUte(self, angle: 'Angle'):
        self.angle.flat_angle_x += angle.flat_angle_x
        self.angle.flat_angle_y += angle.flat_angle_y
        self.angle.flat_angle_z += angle.flat_angle_z

    def move(self, point: 'Point3D'):
        self.location = point


class Angle:

    def __init__(self, flat_angle_x: float, flat_angle_y: float, flat_angle_z: float):
        self.flat_angle_x = flat_angle_x
        self.flat_angle_y = flat_angle_y
        self.flat_angle_z = flat_angle_z
        self.rotations_matrix = np.array([],
                                         [],
                                         [])

    def __str__(self):
        return f'{self.flat_angle_x, self.flat_angle_y, self.flat_angle_z}'

    def __repr__(self):
        return str(self)


class Colour:

    def __init__(self, name_color):
        self.name_color = name_color
