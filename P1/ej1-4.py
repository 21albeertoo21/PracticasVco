from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

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