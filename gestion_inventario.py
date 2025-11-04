"""
Examen: Gestión de Inventario con Persistencia JSON y Programación Orientada a Objetos
Autor/a: Alejandro Maya Ureba
Fecha: 04/11/2025

Objetivo:
Desarrollar una aplicación orientada a objetos que gestione un inventario de productos
con persistencia de datos en ficheros JSON y uso de listas y diccionarios anidados.

Clases requeridas:
- Proveedor
- Producto
- Inventario

"""

import json
import os


# ======================================================
# Clase Proveedor
# ======================================================


datos = [
    {
        "codigo": "P001",
        "nombre": "Teclado mecánico RGB",
        "precio": 45.99,
        "stock": 10,
        "proveedor": {
            "codigo": "PR01",
            "nombre": "TechZone",
            "contacto": "ventas@techzone.com"
        }
    },
    {
        "codigo": "P002",
        "nombre": "Ratón óptico inalámbrico",
        "precio": 19.95,
        "stock": 25,
        "proveedor": {
            "codigo": "PR01",
            "nombre": "TechZone",
            "contacto": "ventas@techzone.com"
        }
    },
    {
        "codigo": "P003",
        "nombre": "Monitor LED 24 pulgadas",
        "precio": 139.00,
        "stock": 8,
        "proveedor": {
            "codigo": "PR02",
            "nombre": "VisualTech",
            "contacto": "contacto@visualtech.es"
        }
    },
    {
        "codigo": "P004",
        "nombre": "Disco SSD 1TB NVMe",
        "precio": 89.90,
        "stock": 15,
        "proveedor": {
            "codigo": "PR03",
            "nombre": "DataPlus",
            "contacto": "info@dataplus.com"
        }
    },
    {
        "codigo": "P005",
        "nombre": "Auriculares Bluetooth",
        "precio": 29.50,
        "stock": 30,
        "proveedor": {
            "codigo": "PR02",
            "nombre": "VisualTech",
            "contacto": "contacto@visualtech.es"
        }
    }
]



class Proveedor:
    def __init__(self, codigo, nombre, contacto):
        self.codigo = codigo
        self.nombre = nombre
        self.contacto = contacto

    def __str__(self):
        return f"(Proveedor)Codigo: {self.codigo}, Nombre: {self.nombre}, contacto: {self.contacto}"


# ======================================================
# Clase Producto
# ======================================================

class Producto:
    def __init__(self, codigo, nombre, precio, stock, proveedor:Proveedor):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.proveedor = {"codigo": proveedor.codigo,"nombre":proveedor.nombre,"contacto": proveedor.contacto}

    def __str__(self):
        return f"{self.codigo} {self.nombre} - {self.precio} € ({self.stock} uds.) | {self.proveedor}"
        # Ejemplo: "[P001] Teclado - 45.99 € (10 uds.) | Proveedor: TechZone (ventas@techzone.com)"
        


# ======================================================
# Clase Inventario
# ======================================================

class Inventario:
    def __init__(self, nombre_fichero):
        self.nombre_fichero = nombre_fichero
        self.productos = [] #type: list[Producto]

    def cargar(self, nombre_fichero):
        """
        Carga los datos del fichero JSON si existe y crea los objetos Producto y Proveedor.
        Si el fichero no existe, crea un inventario vacío.
        """
        # TODO: implementar la lectura del fichero JSON y la creación de objetos
        try:
            with open(nombre_fichero, 'r') as f:
                productos_cargados = json.load(f)
                self.productos = []
                for p in productos_cargados:
                    producto = Producto(p["codigo"],p["nombre"], p["precio"], p["stock"],
                                        Proveedor(p["proveedor"]["codigo"]
                                                   , p["proveedor"]["nombre"]
                                                   , p["proveedor"]["contacto"]))
                    self.productos.append(producto)
        except ValueError:
            print("Error al cargar los datos")


    def guardar(self,nombre_fichero):
        with open (nombre_fichero, 'w') as f:
            json.dump([p.__dict__ for p in self.productos], f, default=str)

    def anadir_producto(self, producto):
        self.productos.append(producto)

    def mostrar(self):
        """
        Muestra todos los productos del inventario.
        """
        for p in self.productos:
            print(p)

    def buscar(self, codigo):

        for p in self.productos:
            if p.codigo == codigo:
                return f"\n{p}"
            else:
                return f"None"

    def modificar(self, codigo, nombre=None, precio=None, stock=None):
        """
        Permite modificar los datos de un producto existente.
        """
        # TODO: buscar el producto y actualizar sus atributos
        for p in self.productos:
            if p.codigo == codigo:
                if nombre:
                    p.nombre = nombre
                
                if precio:
                    p.precio = precio

                if stock:
                    p.stock = stock
            
            else:
                return f"Producto no existente"

    def eliminar(self, codigo):
        """
        Elimina un producto del inventario según su código.
        """
        # TODO: eliminar el producto de la lista
        nueva_lista = [p for p in self.productos if p.codigo != codigo]
        self.productos = nueva_lista
        print("Lista actualizada")

    def valor_total(self):
        """
        Calcula y devuelve el valor total del inventario (precio * stock).
        """
        # TODO: devolver la suma total del valor del stock
        total = 0
        for p in self.productos:
            total += float(p.precio) * float(p.stock)

        return total

    def mostrar_por_proveedor(self, nombre_proveedor):
        """
        Muestra todos los productos de un proveedor determinado.
        Si no existen productos de ese proveedor, mostrar un mensaje.
        """
        # TODO: filtrar y mostrar los productos de un proveedor concreto
        pass


# ======================================================
# Función principal (menú de la aplicación)
# ======================================================

def main():

    gestor  = Inventario("inventario.json")
    gestor.cargar("inventario.json")

    #gestor.cargar()
    #gestor.mostrar()

    # TODO: crear el objeto Inventario y llamar a los métodos según la opción elegida
    while True:
        print("\n=== GESTIÓN DE INVENTARIO ===")
        print("1. Añadir producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Modificar producto")
        print("5. Eliminar producto")
        print("6. Calcular valor total")
        print("7. Mostrar productos de un proveedor")
        print("8. Guardar y salir")

        opcion = input("Seleccione una opción: ")

        # TODO: implementar las acciones correspondientes a cada opción del menú
        if opcion == '1':
            #Este apartado está mal
            nombre = input("Nombre: ")
            precio = input("Precio: ")
            stock = input("Stock: ")
            cProveedor = input("Codigo de proveedor: " )

            for pr in datos:
                if pr["proveedor"]["codigo"] == cProveedor:
                    cProveedor = pr



            producto = Producto(nombre,precio,stock, cProveedor )
            gestor.anadir_producto(producto)
            #proveedor = input("Código proveedor: ")

        elif opcion == '2':
            print(gestor.mostrar())

        elif opcion == '3':
            codigo = input("Código: ")
            print(gestor.buscar(codigo))

        elif opcion == '4':
            codigo = input("Codigo: ")

            for p in gestor.productos:
                if p.codigo == codigo:
                    nNombre = input("Nuevo nombre: ")
                    nPrecio = input("Nuevo precio: ")
                    nStock = input("Nuevo stock: ")

                    gestor.modificar(codigo,nNombre,nPrecio,nStock)
                    print("Producto actualizado")
                    break
                
                else:
                    print("Producto no existente")
                    break


        elif opcion == '5':
            codigo = input("Codigo: ")
            gestor.eliminar(codigo)
            print("--->Mostrando la nueva lista...")
            gestor.mostrar()

        elif opcion == '6':
            print(f"El precio total del inventario es: {gestor.valor_total()}")


        elif opcion == '7':
            pass

        elif opcion == '8':
            gestor.guardar("inventario.json")
            print("---> Saliendo del programa...")
            break

        else:
            print(f"---> Opción inválida. Intentalo de nuevo.")

if __name__ == "__main__":
    main()

