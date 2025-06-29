import os

def recuperar_nombres(ruta_principal_train):
    nombres_famosos = []
    for elemento in os.listdir(ruta_principal_train):
        ruta_completa_famoso = os.path.join(ruta_principal_train, elemento)
        if os.path.isdir(ruta_completa_famoso):
            nombres_famosos.append(elemento)
    return nombres_famosos

def obtener_nombres_imagenes(ruta_principal_train):
    todos_los_nombres_imagenes = []
    
    nombres_famosos = recuperar_nombres(ruta_principal_train)
    
    for famoso in nombres_famosos:
        ruta_carpeta_famoso = os.path.join(ruta_principal_train, famoso)
        nombres_imagenes_por_famoso = []
        
        for archivo in os.listdir(ruta_carpeta_famoso):
            if os.path.isfile(os.path.join(ruta_carpeta_famoso, archivo)) and \
               archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                nombres_imagenes_por_famoso.append(archivo)
        todos_los_nombres_imagenes.append(nombres_imagenes_por_famoso)
        
    return todos_los_nombres_imagenes

ruta_a_la_carpeta_train = "C:/Users/Bautista/Desktop/BASEDEDATOS/train"

nombres_famosos_encontrados = recuperar_nombres(ruta_a_la_carpeta_train)
nombres_de_fotos_encontrados = obtener_nombres_imagenes(ruta_a_la_carpeta_train)

print(f"Los nombres de los famosos encontrados son: {nombres_famosos_encontrados}")
print(f"Los nombres de las imagenes encontradas son: {nombres_de_fotos_encontrados}")
