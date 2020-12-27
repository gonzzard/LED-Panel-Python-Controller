import numpy as np

class PanelsControl:

    PANELS = {
        'LEFT_PANEL': {
            'ID': "LP",
            'SHAPE': (32, 64, 3)
        },
        'RIGHT_PANEL': {
            'ID': "RP",
            'SHAPE': (32, 64, 3)
        },
        'UPPER_PANEL': {
            'ID': "UP",
            'SHAPE': (16, 16, 3)
        }
    }

    def __valid_panel_shape(self, matrix, panel, shape):
        if matrix.shape != shape:
            return False
        elif shape == (32, 64, 3) and (panel != "RP" or panel != "LP"):
            return False
        elif shape == (16, 16, 3) and panel != "UP" :
            return False
        else:
            return True

    def write_on_64x32(self, matrix, panel):
        if self.__valid_panel_shape(matrix, panel, (32, 64, 3)) == True:
            # TODO Llamar al interfaz para rellenar los pixeles.
            pass
        else:
            raise Exception("Parámetros incorrectos")

    def write_on_16x16(self, matrix, panel):
        if self.__valid_panel_shape(matrix, panel, (16, 16, 3)) == True:
            # TODO Llamar al interfaz para rellenar los pixeles.
            pass
        else:
            raise Exception("Parámetros incorrectos")