
cola_pendientes = []
pila_historial = []
siguiente_id = 1


def mostrar_estado():
    print("\n========== ESTADO DEL SISTEMA ==========")

    print("\nCola de pendientes:")
    if cola_pendientes:
        for solicitud in cola_pendientes:
            print(
                f"ID: {solicitud['id']} | "
                f"Cliente: {solicitud['cliente']} | "
                f"Asunto: {solicitud['asunto']} | "
                f"Estado: {solicitud['estado']}"
            )
    else:
        print("No hay solicitudes pendientes.")

    print("\nPila de historial (última atención primero):")
    if pila_historial:
        for solicitud in reversed(pila_historial):
            print(
                f"ID: {solicitud['id']} | "
                f"Cliente: {solicitud['cliente']} | "
                f"Asunto: {solicitud['asunto']} | "
                f"Estado: {solicitud['estado']}"
            )
    else:
        print("No hay solicitudes atendidas.")

    print("========================================")


def registrar_solicitud(cliente, asunto):
    global siguiente_id

    if not cliente.strip() or not asunto.strip():
        return None

    solicitud = {
        "id": siguiente_id,
        "cliente": cliente.strip(),
        "asunto": asunto.strip(),
        "estado": "pendiente"
    }

    cola_pendientes.append(solicitud)
    siguiente_id += 1

    return solicitud


def atender_siguiente():
    if not cola_pendientes:
        return None

    solicitud = cola_pendientes.pop(0)
    solicitud["estado"] = "atendida"
    pila_historial.append(solicitud)

    return solicitud

def consultar_siguiente():
    if cola_pendientes:
        return cola_pendientes[0]
    else:
        return None

def buscar_solicitud(id_solicitud):
    for solicitud in cola_pendientes:
        if solicitud["id"] == id_solicitud:
            return solicitud, "pendientes"

    for solicitud in pila_historial:
        if solicitud["id"] == id_solicitud:
            return solicitud, "historial"

    return None

def cancelar_solicitud(id_solicitud):
        for solicitud in cola_pendientes:
            if solicitud["id"] == id_solicitud:
                cola_pendientes.remove(solicitud)
                return solicitud
        return None
        



def deshacer_ultima_atencion():
    if not pila_historial:
        return None

    solicitud = pila_historial.pop()
    solicitud["estado"] = "pendiente"
    cola_pendientes.insert(0, solicitud)

    return solicitud


def deshacer_varias(cantidad):
    if cantidad <= 0:
        print("\nError: debe ingresar una cantidad mayor que cero.")
        return 0

    recuperadas = 0

    for i in range(cantidad):
        resultado = deshacer_ultima_atencion()

        if resultado:
            recuperadas += 1
        else:
            break

    if recuperadas == cantidad:
        print(f"\nSe deshicieron correctamente {recuperadas} atenciones.")
    elif recuperadas > 0:
        print(f"\nSolo había {recuperadas} atenciones disponibles para deshacer.")
    else:
        print("\nNo hay atenciones disponibles para deshacer.")

    return recuperadas



def ejecutar_menu():
    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Registrar solicitud")
        print("2. Atender siguiente")
        print("3. Consultar siguiente")
        print("4. Buscar Solicitud")
        print("5. Cancelar solicitud")
        print("6. Deshacer última atención")
        print("7. Deshacer varias atenciones")
        print("8. Mostrar estado")
        print("9. Salir")
        print("====================================")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            cliente = input("Nombre del cliente: ").strip()
            asunto = input("Asunto de la solicitud: ").strip()

            resultado = registrar_solicitud(cliente, asunto)

            if resultado:
                print("\nSolicitud registrada correctamente.")
                print("ID asignado:", resultado["id"])
            else:
                print("\nError: el cliente y el asunto son obligatorios.")

        elif opcion == "2":
            resultado = atender_siguiente()

            if resultado:
                print("\nSolicitud atendida correctamente:")
                print("ID:", resultado["id"])
                print("Cliente:", resultado["cliente"])
                print("Asunto:", resultado["asunto"])
            else:
                print("\nNo hay solicitudes pendientes para atender.")

        elif opcion == "3":
            resultado = consultar_siguiente()

            if resultado:
                print("\nEl siguiente en consultar:")
                print("ID:",resultado["id"])
                print("Cliente:",resultado["cliente"])
                print("Estado: ",resultado["estado"])
                print("Asunto:",resultado["asunto"])
            else:
                print("\nNo hay solicitudes restantes")

        elif opcion == "4":
            resultado = buscar_solicitud(int(input("Ingrese el id de la solicitud: ")))
            if resultado:
                solicitud, ubicacion = resultado
                print("\nLa solicitud buscada es:")
                print("ID:",solicitud["id"])
                print("Cliente:",solicitud["cliente"])
                print("Estado: ",solicitud["estado"])
                print("Asunto:",solicitud["asunto"])
                print("Ubicacion",ubicacion)
            else:
                print("\nNo existe esa solicitud")   

        elif opcion == "5":
            resultado = cancelar_solicitud(int(input("Ingrese el ID de la solicitud que desea cancelar: "))) 
            if resultado:
                print("\nSolicitud cancelada correctamente")
                print("ID:",resultado["id"])
                print("CLiente:",resultado["cliente"])
                print("Estado:",resultado["estado"])
                print("Asunto:",resultado["asunto"])
            else:
                print("Esa solicitud no se encuentra entre los pendientes")


        elif opcion == "6":
            resultado = deshacer_ultima_atencion()

            if resultado:
                print("\nÚltima atención deshecha correctamente.")
                print("ID:", resultado["id"])
                print("Cliente:", resultado["cliente"])
                print("La solicitud volvió al inicio de la cola.")
            else:
                print("\nNo hay atenciones para deshacer.")

        elif opcion == "7":
            try:
             cantidad = int(input("Ingrese cuántas atenciones desea deshacer: "))
             deshacer_varias(cantidad)
            except ValueError:
             print("\nError: debe ingresar un número entero válido.")


        elif opcion == "8":
            mostrar_estado()

        elif opcion == "9":
            print("\nSaliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("\nOpción inválida. Seleccione un número del 1 al 5.")


if __name__ == "__main__":
    ejecutar_menu()
