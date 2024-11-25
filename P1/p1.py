from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen
img = Image.open("d52.jpg")
"""
#EJERCICIO 1
# Mostrar la imagen original
img.show()

# Convertir la imagen a un formato con 16 colores
img_reduced = img.convert("P", palette=Image.ADAPTIVE, colors=4)

# Mostrar la imagen reducida
img_reduced.show()


#EJERCICIO 2
img_reduced = img.convert("P", palette=Image.ADAPTIVE, colors=4)

# Imagen con rotación de 90 grados y volteada horizontalmente
img_transformed = img_reduced.rotate(90).transpose(Image.FLIP_LEFT_RIGHT)
img_transformed.show()

# Convertir imagen de color a grises
img_2 = Image.open("cartas_4.jpg")
img_gray = img_2.convert("L")
img_2.show()
img_gray.show()
"""
# Mostrar los tres componentes RGB de la imagen como imágenes de gris por separado
img_aloe = Image.open("AloeVera.jpg")
r, g, b = img_aloe.split()
r.show()
g.show()
b.show()
