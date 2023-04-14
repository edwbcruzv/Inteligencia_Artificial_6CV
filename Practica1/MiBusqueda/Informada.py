from .NoInformada import *


# Busqueda Voras (F(n)= H(n)) sin el costo de camino recorrido,
# Busqueda con Costo Uniforme
def UCS_V(problema: Problema, info: bool = False):  # Listo
    raiz = nodoRaiz(problema)
    # la frontera almacena nodos
    frontera = [raiz, ]

    # explorados almacena estados
    explorados = set()  # un set tiene elementos unicos sin repetirse
    ruta = []
    if info:
        print("=======================UCS===========================")
    while True:
        if info:
            # print("Explorados:", [estado.__str__() for estado in explorados])
            print("Frontera(PRIORY-LIFO):<=IN==", [(nodo.__str__(), nodo.Heuristica)
                                                   for nodo in frontera], "<====")

        # hasta que se quede vacia la frontera, si eso pasa no hay solucion.
        if len(frontera) == 0:
            if info:
                print("Frontera vacia, no se encontro el objetivo")
                print("=====================================================")
            return None
        nodo = frontera.pop(0)
        ruta.append(nodo)
        if problema.testObjetivo(nodo.Estado):
            if info:
                print("Se encontro el objetivo:", nodo)
                print("=====================================================")
            return nodo, ruta
        explorados.add(nodo.Estado)
        if info:
            print("Pop:", nodo)
            print("=====================================================")
        if not nodo.Acciones:
            if info:
                print("no hay acciones")
            continue

        # validacion de acciones que podemos realizar
        for accion in nodo.Acciones.keys():
            hijo = nodoHijo(problema, nodo, accion)

            estados_frontera = [nodo.Estado for nodo in frontera]
            if hijo.Estado not in explorados and hijo.Estado not in estados_frontera:
                frontera.append(hijo)
            else:
                buscar = [nodo for nodo in frontera
                          if nodo.Estado == hijo.Estado]

                if buscar:
                    if hijo.Heuristica < buscar[0].Heuristica:
                        indice = frontera.index(buscar[0])
                        frontera[indice] = hijo
            frontera.sort(key=lambda nodo: nodo.Heuristica)


# Busqueda A* (F(n)= H(n) +  G(n))
# Busqueda con Costo Uniforme
def UCS_A(problema: Problema, info: bool = False):  # Listo
    raiz = nodoRaiz(problema)
    # la frontera almacena nodos
    frontera = [raiz, ]

    # explorados almacena estados
    explorados = set()  # un set tiene elementos unicos sin repetirse
    ruta = []
    if info:
        print("=======================UCS===========================")
    while True:
        if info:
            # print("Explorados:", [estado.__str__() for estado in explorados])
            print("Frontera(PRIORY-LIFO):<=IN==", [(nodo.__str__(), nodo.FNValor)
                                                   for nodo in frontera], "<====")

        # hasta que se quede vacia la frontera, si eso pasa no hay solucion.
        if len(frontera) == 0:
            if info:
                print("Frontera vacia, no se encontro el objetivo")
                print("=====================================================")
            return None
        nodo = frontera.pop(0)
        ruta.append(nodo)
        if problema.testObjetivo(nodo.Estado):
            if info:
                print("Se encontro el objetivo:", nodo)
                print("=====================================================")
            return nodo, ruta
        explorados.add(nodo.Estado)
        if info:
            print("Pop:", nodo)
            print("=====================================================")
        if not nodo.Acciones:
            if info:
                print("no hay acciones")
            continue

        # validacion de acciones que podemos realizar
        for accion in nodo.Acciones.keys():
            hijo = nodoHijo(problema, nodo, accion)

            estados_frontera = [nodo.Estado for nodo in frontera]
            if hijo.Estado not in explorados and hijo.Estado not in estados_frontera:
                frontera.append(hijo)
            else:
                buscar = [nodo for nodo in frontera
                          if nodo.Estado == hijo.Estado]

                if buscar:
                    if hijo.FNValor < buscar[0].FNValor:
                        indice = frontera.index(buscar[0])
                        frontera[indice] = hijo
            frontera.sort(key=lambda nodo: nodo.FNValor)