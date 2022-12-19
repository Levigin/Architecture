from HW1.Model_Elements.Polygonal_Model import PolygonalModel
from HW1.Model_Elements.Flash import Flash
from HW1.Model_Elements.Scene import Scene
from HW1.Model_Elements.Camera import Camera
from .IModelChanger import IModelChanger
from .IModelChangedObserver import IModelChangedObserver


class ModelStore:
    """
    class ModelStore:
        some models

    :argument
    models: list[PolygonalModel]
    scenes: list[Scene]
    flashes: list[Flash]
    cameras: list[Camera]
    change_observers: list[IModelChangedObserver]

    Methods:
        get_scene:
            get scene and return the scene
        notify_change:
            notifies about changes in model
    """
    def __init__(self, models: list[PolygonalModel], scenes: list[Scene], flashes: list[Flash], cameras: list[Camera],
                 change_observers=None):

        if change_observers is not None and type(change_observers) is not list:
            raise Exception('Type is wrong!')
        if change_observers is not None:
            for change_observer in change_observers:
                if type(change_observer) is not IModelChangedObserver:
                    raise Exception('Type is wrong!')

        if len(models) == 0 and len(cameras) == 0 and len(scenes) == 0 and len(flashes) == 0:
            raise Exception('Must be one models or cameras or flashes or scenes')

        self.models = models
        self.scene = scenes
        self.flashes = flashes
        self.cameras = cameras
        self._change_observer = change_observer

    def get_scene(self, i: int):
        pass

    def notify_change(self, obj: IModelChanger):
        pass