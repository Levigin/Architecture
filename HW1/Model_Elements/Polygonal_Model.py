from .Polygon import Polygon
from .Texture import Texture


class PolygonalModel:
    """
    class PolygonalModel:

    Attributes:
        polygons: list[Polygon]
        textures: list[Texture]
    """

    def __init__(self, polygons: list[Polygon], textures=None):
        if textures is not None and type(textures) is not list:
            raise Exception('Type is wrong!')
        if textures is not None:
            for i in textures:
                if type(i) is not Texture:
                    raise Exception('Type is wrong!')

        if len(polygons) == 0:
            raise Exception('Must be one polygon')

        self.polygons = polygons
        self.textures = textures
