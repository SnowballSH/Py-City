from ursina import *
from ursina import camera


def display(data):
    app = Ursina()

    # e = Entity(model='cube', color=color.orange, scale_y=2)

    data.add_text()

    camera.orthographic = True
    camera.fov = 8
    EditorCamera()

    app.run()
