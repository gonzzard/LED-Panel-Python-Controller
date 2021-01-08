import numpy as np
import spidev
import bitarray
import time as t

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


    def __init__(self):
        #SPI port init for the 16x16 display
        self.spi1 = spidev.SpiDev()
        self.spi1.open(0, 0)		#The 16x16 display will be connected to the spi1 port, CS0 (not used)
        self.spi1.max_speed_hz=6400000	#Speed: 6.4MHz
        self.spi1.no_cs = True


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
        if self.__valid_panel_shape(matrix, panel, (16, 16, 3)) == False:

            raise Exception("Parámetros incorrectos: invalid matrix shape, must be 16x16x3")

            return

        elif matrix.dtype != np.uint8:

            raise Exception("Invalid matrix dtype, must be: np.unin8")

            return

        else:

            #First, we will get the frame to update the led matrix
            frame = self.get_frame_from_matrix_16x16(matrix)

            #Second, we send the frame over the SPI port
            self.spi1.writebytes2(frame)

            #Third, we wait 51us to finish the actual refresh data cycle
            t.sleep(50*10**(-6))


    def get_frame_from_matrix_16x16(self, matrix):
        #The led possitions form a zig-zag pattern, therefore, we will have
        #send the frame in the same order

        frame = []

        for idx, line in enumerate(matrix):

            if(idx%2==0):

                for pixel in line:
                    frame = self.write_frame_buffer_WS2812B(frame, pixel)

            else:
                reverse_line = line[::-1]

                for pixel in reverse_line:
                    frame = self.write_frame_buffer_WS2812B(frame, pixel)

        return frame



    #pixelColor: it's a numpy array which contains the RGB values of the pixel
    def write_frame_buffer_WS2812B(self, frameBuffer, pixelColor):
        #The WS2812B led expect a frame which follows the GRB order:
        return frameBuffer + self.convert_byte_to_frame_WS2812B(pixelColor[1].tobytes()) + self.convert_byte_to_frame_WS2812B(pixelColor[0].tobytes()) + self.convert_byte_to_frame_WS2812B(pixelColor[2].tobytes())


    def convert_byte_to_frame_WS2812B(self, byteToConvert):

        b = bitarray.bitarray(endian='big')
        b.frombytes(byteToConvert)

        byteToFrame = []

        for idx, bit in enumerate(b):

            if(bit == True):
                byteToFrame.append(int.from_bytes(b'\xf8', 'big')) # b'11111000'
            else:
                byteToFrame.append(int.from_bytes(b'\xe0', 'big')) # b'11100000' 

        return byteToFrame
