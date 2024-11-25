from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen
img = Image.open("d52.jpg")

#EJERCICIO 1
# Mostrar la imagen original
img.show()

# Convertir la imagen a un formato con 16 colores
img_reduced = img.convert("P", palette=Image.ADAPTIVE, colors=4)

# Mostrar la imagen reducida
img_reduced.show()