import csv
import os
misLibros=[['ID       ','Título   ','Género(s)','ISBN     ','Editorial','Autor(es)']]
os.system("cls")

def seleccionar_menu(a):
    if a==1:
        print("leer archivo")
    elif a==2:
        print("listar libro")
    elif a==3:
        print("Agregar libro")
    elif a==4:
        print("Eliminar libro")
    elif a==5:
        print("Buscar por isbn o titulo")
    elif a==6:
        print("ordenar por titulo")
    elif a==7:
        print("buscar_autor_editorial_genero")
    elif a==8:
        print("editar libro")
    elif a==9:
        print("guardar libros")
    else:
        print("Opción no disponible")
    