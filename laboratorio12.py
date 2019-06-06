#Esteban Cabrera Arevalo
#17781

import psycopg2
from psycopg2 import Error

#Funcion para el QUERY 1
def buscarPCPrecio(precio):
    if precio >= 0:
        try:
            precio = float(precio)
            try:
                conexion = psycopg2.connect("dbname=laboratorio12 user=postgres password=Sonic53176340")
                cursor = conexion.cursor()
                cursor.execute("BEGIN TRANSACTION READ ONLY ISOLATION LEVEL READ COMMITTED;")
                cursor.execute('''
                            SELECT pc.modelo, pc.velocidad, pc.ram, pc.disco, pc.precio
                            FROM pc
                            ORDER BY (ABS(%s - pc.precio)) ASC LIMIT 1;''', (precio,))
                result = cursor.fetchall()
                print("\n")
                print(" MODELO  VEL    RAM   DISCO  PRECIO ")
                print("------------------------------------")
                for i in result:
                    print i
                print("")

                conexion.commit()
                print("Transaccion Completada")
        
            except (Exception, psycopg2.DatabaseError) as error:
                print("Hubo un error en la transaccion")
        
            finally:
                cursor.close()
                conexion.close()
                print("Conexion terminada")
                print("")
                pass
            pass
        except ValueError:
            print("Ha ingresado un dato no numerico en el precio")
    else:
        print("EL precio ingresado no es valido")

#Funcion para el QUERY 2
def buscarPCEspecificacionesMinimas(velocidad, ram, disco):
    if velocidad > 0 and ram > 0 and disco > 0:
        try:
            velocidad = float(velocidad)
            ram = float(ram)
            disco = float(disco)
            try:
                conexion = psycopg2.connect("dbname=laboratorio12 user=postgres password=Sonic53176340")
                cursor = conexion.cursor()
                cursor.execute("BEGIN TRANSACTION READ ONLY ISOLATION LEVEL READ COMMITTED;")
                cursor.execute('''
                            SELECT producto.fabricante, laptop.modelo, laptop.velocidad, laptop.ram, laptop.disco, laptop.screen, laptop.precio
                            FROM laptop
                                JOIN producto ON producto.modelo = laptop.modelo
                            WHERE laptop.velocidad >= %s AND laptop.ram >= %s AND laptop.disco >= %s;''', (velocidad,ram,disco))
                result = cursor.fetchall()
                print("\n")
                print(" FAB  MODELO  VEL    RAM   DISCO  SCREEN  PRECIO ")
                print("-------------------------------------------------")
                for i in result:
                    print i
                print("")

                conexion.commit()
                print("Transaccion Completada")
        
            except (Exception, psycopg2.DatabaseError) as error:
                print("Hubo un error en la transaccion")
        
            finally:
                cursor.close()
                conexion.close()
                print("Conexion terminada")
                print("")
                pass
            pass
        except ValueError:
            print("Ha ingresado un dato no numerico")
    else:
        print("Alguna de las cantidades ingresadas es menor o igual a 0")

#Funcion para el QUERY 3
def buscarPC_ImpresoraPresupuesto(presupuesto, velocidad, color):
    color = color.upper()
    if color == "S":
        color = True
    else:
        color = False
        
    if presupuesto > 0 and velocidad > 0 and color == True:
        try:
            presupuesto = float(presupuesto)
            velocidad = float(velocidad)
            try:
                conexion = psycopg2.connect("dbname=laboratorio12 user=postgres password=Sonic53176340")
                cursor = conexion.cursor()
                cursor.execute("BEGIN TRANSACTION READ ONLY ISOLATION LEVEL READ COMMITTED;")
                cursor.execute('''
                            SELECT pc.modelo AS ModeloPC, printer.modelo AS ModeloPrinter, (pc.precio + printer.precio) AS precio_Total, pc.velocidad AS PCVelocidad, pc.ram AS PCRAM, pc.disco AS PCDisco, printer.color AS PrintColor, printer.type AS PrintType
                            FROM pc, printer
                            WHERE pc.velocidad >= %s AND (pc.precio + printer.precio) <= %s AND printer.color = true;''', (velocidad,presupuesto))
                result = cursor.fetchall()
                print("\n")
                print(" MODPC   MODPRI  TOTAL  VEL   RAM    DISC  COLOR  TYPE ")
                print("-------------------------------------------------------")
                for i in result:
                    print i
                print("")

                conexion.commit()
                print("Transaccion Completada")
        
            except (Exception, psycopg2.DatabaseError) as error:
                print("Hubo un error en la transaccion")
        
            finally:
                cursor.close()
                conexion.close()
                print("Conexion terminada")
                print("")
                pass
            pass
        except ValueError:
            print("Ha ingresado un dato no numerico en un parametro numerico")
    elif presupuesto > 0 and velocidad > 0 and color == False:
        try:
            presupuesto = float(presupuesto)
            velocidad = float(velocidad)
            try:
                conexion = psycopg2.connect("dbname=laboratorio12 user=postgres password=Sonic53176340")
                cursor = conexion.cursor()
                cursor.execute("BEGIN TRANSACTION READ ONLY ISOLATION LEVEL READ COMMITTED;")
                cursor.execute('''
                            SELECT pc.modelo AS ModeloPC, printer.modelo AS ModeloPrinter, (pc.precio + printer.precio) AS precio_Total, pc.velocidad AS PCVelocidad, pc.ram AS PCRAM, pc.disco AS PCDisco, printer.color AS PrintColor, printer.type AS PrintType
                            FROM pc, printer
                            WHERE pc.velocidad >= %s AND (pc.precio + printer.precio) <= %s;''', (velocidad,presupuesto))
                result = cursor.fetchall()
                print("\n")
                print(" MODPC   MODPRI  TOTAL  VEL   RAM    DISC  COLOR  TYPE ")
                print("-------------------------------------------------------")
                for i in result:
                    print i
                print("")

                conexion.commit()
                print("Transaccion Completada")
        
            except (Exception, psycopg2.DatabaseError) as error:
                print("Hubo un error en la transaccion")
        
            finally:
                cursor.close()
                conexion.close()
                print("Conexion terminada")
                print("")
                pass
            pass
        except ValueError:
            print("Ha ingresado un dato no numerico en un parametro numerico")        
    else:
        print("Alguna de las cantidades ingresadas es menor o igual a 0")

#Funcion para el QUERY 4
def insertarNuevoModeloPC(fabricante, modelo, velocidad, ram, disco, precio):
    if modelo > 0 and velocidad > 0 and ram > 0 and disco > 0 and precio > 0:
        try:
            velocidad = float(velocidad)
            ram = float(ram)
            disco = float(disco)
            precio = float(precio)
            try:
                conexion = psycopg2.connect("dbname=laboratorio12 user=postgres password=Sonic53176340")
                cursor = conexion.cursor()
                cursor.execute("BEGIN TRANSACTION READ WRITE ISOLATION LEVEL READ COMMITTED;")
                cursor.execute("SELECT * FROM insercion(%s, %s, %s, %s, %s, %s);", (fabricante, modelo, velocidad, ram, disco, precio))
                result = cursor.fetchall()
                print("\n")
                print("La nueva PC fue ingresada con exito")
                print("\n")
                print(" FAB  MODELO   VEL    RAM   DISCO  PRECIO ")
                print("------------------------------------------")
                for i in result:
                    print i
                print("")

                conexion.commit()
                print("Transaccion Completada")
        
            except (Exception, psycopg2.DatabaseError) as error:
                print("Hubo un error en la transaccion")
        
            finally:
                cursor.close()
                conexion.close()
                print("Conexion terminada")
                print("")
                pass
            pass
        except ValueError:
            print("Ha ingresado un dato no numerico")
    else:
        print("Alguna de las cantidades ingresadas es menor o igual a 0")

#QUERY PARA CREAR EL PROCEDIMIENTO ALMACENADO UTILIZADO PARA LA FUNCION 4
'''CREATE OR REPLACE FUNCTION insercion(fab VARCHAR, model INT, speed REAL, ra REAL, hd REAL, price REAL) 
RETURNS TABLE(
	fabricante VARCHAR,
	modelor VARCHAR,
	velocidad REAL,
	ram REAL,
	disco REAL,
	precio REAL
) AS $$
DECLARE
numeroModelo INTEGER := model;
validador BOOLEAN := FALSE;
BEGIN
	-- Verificacion de Existencia
	WHILE validador != TRUE LOOP
		PERFORM *
		FROM producto
		WHERE producto.modelo = CAST (numeroModelo AS VARCHAR);
	
		IF NOT FOUND THEN
			validador := TRUE;
		ELSE
			numeroModelo := numeroModelo + 1;
		END IF; 
	
   	END LOOP;
	
	INSERT INTO producto(fabricante, modelo, tipo) VALUES(fab, CAST (numeroModelo AS VARCHAR), 'pc');
	INSERT INTO pc(modelo, velocidad, ram, disco, precio) VALUES(CAST (numeroModelo AS VARCHAR), speed, ra, hd, price);	
	
	-- Query
	RETURN QUERY
	SELECT producto.fabricante, pc.modelo, pc.velocidad, pc.ram, pc.disco, pc.precio
    FROM pc
		JOIN producto ON producto.modelo = pc.modelo
	WHERE producto.fabricante = fab AND pc.modelo = CAST (numeroModelo AS VARCHAR) AND pc.velocidad = speed AND pc.ram = ra AND pc.disco = hd AND pc.precio = price;

END;
$$ LANGUAGE plpgsql;

-- QUERY DE PRUEBA PARA EL PROCEDIMIENTO ALMACENADO EN POSTGRES
SELECT * FROM insercion('Z', 1001, 200, 300, 400, 500);'''

#Funcion para el QUERY 5
def buscarCantidadPCLaptopPrinterPrecioMayor(precio):
    if precio >= 0:
        try:
            precio = float(precio)
            try:
                conexion = psycopg2.connect("dbname=laboratorio12 user=postgres password=Sonic53176340")
                cursor = conexion.cursor()
                cursor.execute("BEGIN TRANSACTION READ ONLY ISOLATION LEVEL READ COMMITTED;")
                cursor.execute('''
                            SELECT COUNT(DISTINCT pc.modelo) AS Numero_PC, (SELECT COUNT(*) 
									    FROM laptop
									    WHERE laptop.precio > %s) AS Numero_Laptop, (SELECT COUNT(*) 
															   FROM printer
											     				   WHERE printer.precio > %s) AS Numero_Printer
                            FROM pc
                            WHERE pc.precio > %s;''', (precio,precio,precio))
                count2 = cursor.fetchone()
                result = "      "+str(count2[0])+"                   "+str(count2[1])+"                  "+str(count2[2])
                print("\n")
                print(" Cantidad PC's    Cantidad Laptop's    Cantidad Printer's ")
                print("----------------------------------------------------------")
                print(result)
                print("")

                conexion.commit()
                print("Transaccion Completada")
        
            except (Exception, psycopg2.DatabaseError) as error:
                print("Hubo un error en la transaccion")
        
            finally:
                cursor.close()
                conexion.close()
                print("Conexion terminada")
                print("")
                pass
            pass
        except ValueError:
            print("Ha ingresado un dato no numerico en el precio")
    else:
        print("EL precio ingresado no es valido")

        
#Menu para Interaccion
opcion = 1
while opcion != 6: 
        print("Bienvenido al Laboratorio 12\nElija un numero de opcion a realizar:\n1. Buscar PC por precio cercano\n2. Buscar laptop por requisitos minimos\n3. PC + Laptop Bajo presupuesto\n4. Ingresar nueva PC en tablas Producto y PC\n5. Cantidad de PCs, Laptops y Printers arriba de un precio\n6. Salir")
        opcion = input("Ingrese la opcion que desea renderizar: ")
        try:
                opcion = int(opcion)
                if opcion == 1:
                    opcion11 = input("Ingrese el precio del PC: ")
                    buscarPCPrecio(opcion11)
                    pass
                elif opcion == 2:
                    opcion21 = input("Ingrese la velocidad minima: ")
                    opcion22 = input("Ingrese la RAM minima: ")
                    opcion23 = input("Ingrese el tamanio de disco minimo: ")
                    buscarPCEspecificacionesMinimas(opcion21,opcion22,opcion23)
                    pass
                elif opcion == 3:
                    opcion31 = input("Ingrese su presupuesto: ")
                    opcion32 = input("Ingrese la velocidad minima: ")
                    opcion33 = raw_input("Le importa que la impresora imprima a color (S/N) (Ingresar sin comillas la letra): ")
                    buscarPC_ImpresoraPresupuesto(opcion31, opcion32, opcion33)
                    pass
                elif opcion == 4:
                    opcion41 = raw_input("Ingrese el fabricante (Sin comillas): ")
                    opcion42 = input("Ingrese el numero de modelo: ")
                    opcion43 = input("Ingrese la velocidad de procesador: ")
                    opcion44 = input("Ingrese el tamanio de RAM: ")
                    opcion45 = input("Ingrese el tamanio de disco: ")
                    opcion46 = input("Ingrese el precio: ")
                    insertarNuevoModeloPC(opcion41, opcion42, opcion43, opcion44, opcion45, opcion46)
                    pass
                elif opcion == 5:
                    opcion51 = input("Ingrese el precio a superar: ")
                    buscarCantidadPCLaptopPrinterPrecioMayor(opcion51)
                    pass
                else: 
                        print("Ha ingresado una opcion invalida")
        except ValueError:
                print("El dato que ingreso no es valido")
print("Hasta Pronto\n")
