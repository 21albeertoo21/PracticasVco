from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img_fondo1 = Image.open("azulejo.tif")
img_fondo2 = Image.open("azulejo2.tif")

# Redimensionar las dos imagenes a 256x256 
img_fondo1_resized = img_fondo1.resize((256, 256))
img_fondo2_resized = img_fondo2.resize((256, 256))

# Realización de diferentes operaciones con las imágenes
# Suma de las dos imágenes
#img_suma = Image.blend(img_fondo1_resized, img_fondo1_resized, 0.5)
#img_suma.show()

# Resta de las dos imágenes
#img_resta = Image.blend(img_fondo1_resized, img_fondo2_resized, 0.5)
#img_resta.show()

# Realización de la combinación lineal
# Convertir las imágenes a arrays de NumPy
img_fondo1_array = np.array(img_fondo1_resized, dtype=np.float32)
img_fondo2_array = np.array(img_fondo2_resized, dtype=np.float32)

# Realización de la combinación lineal
# azulejo * 1.8 - azulejo2 * 1.2 + 128
img_combined_array = (img_fondo1_array * 1.8) - (img_fondo2_array * 1.2) + 128

# Asegurarse de que los valores estén en el rango [0, 255]
img_combined_array = np.clip(img_combined_array, 0, 255).astype(np.uint8)

# Convertir el array de vuelta a una imagen
img_combined = Image.fromarray(img_combined_array)

img_combined.show()

