from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img_fondo1 = Image.open("Fondo1.tif")
img_fondo2 = Image.open("Fondo2.tif")

# Redimensionar las dos imagenes a 256x256 
img_fondo1_resized = img_fondo1.resize((256, 256))
img_fondo2_resized = img_fondo2.resize((256, 256))
#img_fondo1_resized.show()
#img_fondo2_resized.show()