import csv
import os
misLibros=[['ID       ','Título   ','Género(s)','ISBN     ','Editorial','Autor(es)']]
os.system("cls")

def mostrar_menu():
    print("Seleccione una opción")

def leer_archivo():
    print("Carga de archivo con éxito")

def listar_libros():
    print("Listado de libros")

def agregar_libro():
    print("Libro agregado")

def eliminar_libro():
    print("Libro eliminado")

def buscar_isbn_titulo():
    print("Buscar por ISBN o TITULO")

def ordenar_titulo():
    print("Libros ordenados por titulo")

def buscar_autor_editorial_genero():
    print("Buscar por Autor, Editorial o Género")

def editar_libro():
    print("Libro editado")

def guardar_libros():
    print("Libro guardado")

def salir_menu():
    print("Vuelva pronto")

def seleccionar_menu(a):
    if a==1:
        leer_archivo()
    elif a==2:
        listar_libros()
    elif a==3:
        agregar_libro()
    elif a==4:
        eliminar_libro()
    elif a==5:
        buscar_isbn_titulo()
    elif a==6:
        ordenar_titulo()
    elif a==7:
        buscar_autor_editorial_genero()
    elif a==8:
        editar_libro()
    elif a==9:
        guardar_libros()
    elif a==10:
        salir_menu()
    else:
        print("Opción no disponible")
    