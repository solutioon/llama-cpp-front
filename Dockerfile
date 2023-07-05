# Usa una imagen base de Python
FROM python:3.11

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de requerimientos (requirements.txt) al contenedor
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos de la aplicación al contenedor
COPY . .

# Expone el puerto 5001 (el puerto por defecto de Flask mencionado)
EXPOSE 5001

# Comando por defecto para ejecutar la aplicación Flask
CMD ["python", "app.py"]
