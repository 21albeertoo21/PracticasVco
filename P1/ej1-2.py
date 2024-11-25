from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#EJERCICIO 2
# Imagen con rotación de 90 grados y volteada horizontalmente
img_transformed = img_reduced.rotate(90).transpose(Image.FLIP_LEFT_RIGHT)
#img_transformed.show()

# Convertir imagen de color a grises
img_2 = Image.open("cartas_4.jpg")
img_gray = img_2.convert("L")
#img_2.show()
#img_gray.show()

# Mostrar los tres componentes RGB de la imagen como imágenes de gris por separado
img_aloe = Image.open("AloeVera.jpg")
r, g, b = img_aloe.split()
r.show()
g.show()
b.show()