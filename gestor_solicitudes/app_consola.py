
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



def deshacer_ultima_atencion():
    if not pila_historial:
        return None

    solicitud = pila_historial.pop()
    solicitud["estado"] = "pendiente"
    cola_pendientes.insert(0, solicitud)

    return solicitud


def ejecutar_menu():
    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Registrar solicitud")
        print("2. Atender siguiente")
        print("3. Consultar siguiente")
        print("4. Deshacer última atención")
        print("5. Mostrar estado")
        print("6. Salir")
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
            resultado = deshacer_ultima_atencion()

            if resultado:
                print("\nÚltima atención deshecha correctamente.")
                print("ID:", resultado["id"])
                print("Cliente:", resultado["cliente"])
                print("La solicitud volvió al inicio de la cola.")
            else:
                print("\nNo hay atenciones para deshacer.")

        elif opcion == "5":
            mostrar_estado()

        elif opcion == "6":
            print("\nSaliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("\nOpción inválida. Seleccione un número del 1 al 5.")


if __name__ == "__main__":
    ejecutar_menu()
