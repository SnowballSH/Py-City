from ursina import *
from ursina import camera


def display(data):
    app = Ursina()

    data.add_text()

    camera.orthographic = True
    camera.fov = 10
    EditorCamera()

    app.run()
