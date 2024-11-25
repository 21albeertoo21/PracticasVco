from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen
img = Image.open("d52.jpg")

#EJERCICIO 1
"""# Mostrar la imagen original
img.show()
"""
# Convertir la imagen a un formato con 16 colores
img_reduced = img.convert("P", palette=Image.ADAPTIVE, colors=4)

# Mostrar la imagen reducida
#img_reduced.show()

####################################################

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
"""r.show()
g.show()
b.show()
"""
####################################################

#EJERCICIO 3

img_fondo1 = Image.open("Fondo1.tif")
img_fondo2 = Image.open("Fondo2.tif")

# Redimensionar las dos imagenes a 256x256 
img_fondo1_resized = img_fondo1.resize((256, 256))
img_fondo2_resized = img_fondo2.resize((256, 256))
#img_fondo1_resized.show()
#img_fondo2_resized.show()

####################################################

#EJERCICIO 4
# Cargar la imagen y convertirla a escala de grises
img = Image.open('d52.jpg').convert('L')

# Convertir la imagen a un array de numpy
img_array = np.array(img)

# Obtener las dimensiones de la imagen
y, x = img_array.shape

# Crear una malla de coordenadas
X, Y = np.meshgrid(np.arange(x), np.arange(y))

# Dibujar la superficie
plt.figure(figsize=(10, 6))
plt.contourf(X, Y, img_array, levels=256, cmap='gray')
plt.colorbar()
plt.title('Representación de la Imagen como Superficie')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.show()


