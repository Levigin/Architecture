from .Polygonal_Model import PolygonalModel
from .Flash import Flash
from .Camera import Camera


class Scene:
    """
    class Scene:

    Attributes:
        i: int
        models: list[PolygonalModel]
        cameras: list[Camera]
        flashes: list[Flash]

    Methods:
        get_models:
            get model from scene
        get_flashes:
            return obj witch using flash
    """

    def __init__(self, i: int, models: list[PolygonalModel], cameras: list[Camera], flashes=None):
        if flashes is not None and type(flashes) is not list:
            raise Exception('Type is wrong!')
        if flashes is not None:
            for flash in flashes:
                if type(flash) is not Flash:
                    raise Exception('Type is wrong!')

        if len(models) == 0 and len(cameras) == 0:
            raise Exception('Must be one models or cameras')

        self.i = i
        self.models = models
        self.cameras = cameras

    def get_models(self, something):
        ...

    def get_flashes(self, something1, something2):
        if type(something1) != type(something2):
            raise Exception("Type param one is not equal param two")
        ...
