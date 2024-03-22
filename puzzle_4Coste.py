# Puzle Lineal con búsqueda en profundidad
from arbol import Nodo

#Calcular cuantos numeros estan en la posicion correcta
def calcular_costo(nodo):
    costo = 0
    datos = nodo.get_datos()
    
    for i in range(0, len(datos)):
        #print("i:",i)
        if datos[i] == (i+1):
            costo += 1
    #print("Costo:",costo)
    return costo

def buscar_solucion_DFS(estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)
    
    while (not solucionado) and len(nodos_frontera) != 0 :        
        nodo = nodos_frontera.pop()
        print("Actual:" ,nodo.get_datos())   
        # extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodo)
        #for l in nodos_visitados:
        #    print("VISITADOS:",l.get_datos())

        if nodo.get_datos() == solucion:
            # solución encontrada
            solucionado = True
            return nodo
        else:
            
            
            # expandir nodos hijo
            dato_nodo = nodo.get_datos()
            # operador derecho
            hijo = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2],]
            hijo_derecho = Nodo(hijo)
            hijo_derecho.set_coste(calcular_costo(hijo_derecho))
            if not hijo_derecho.en_lista(nodos_visitados) \
                    and not hijo_derecho.en_lista(nodos_frontera):                
                nodos_frontera.append(hijo_derecho)      
            
                
            # operador central
            hijo = [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]
            hijo_central = Nodo(hijo)
            hijo_central.set_coste(calcular_costo(hijo_central))
            if not hijo_central.en_lista(nodos_visitados) \
                    and not hijo_central.en_lista(nodos_frontera):                
                nodos_frontera.append(hijo_central)

            # operador izquierdo
            hijo = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
            hijo_izquierdo = Nodo(hijo)
            hijo_izquierdo.set_coste(calcular_costo(hijo_izquierdo))    
            if not hijo_izquierdo.en_lista(nodos_visitados) \
                    and not hijo_izquierdo.en_lista(nodos_frontera):                
                nodos_frontera.append(hijo_izquierdo)


            nodo.set_hijos([hijo_izquierdo, hijo_central, hijo_derecho])
            
            print("frontera sin ordenar: ", [h.get_datos() for h in nodos_frontera])
            # Ordenar los nodos frontera según la heurística (número de fichas en posición correcta)
            nodos_frontera.sort(key=lambda x: x.get_coste(), reverse=False)
            
            #hijos.sort(key=lambda x: x.get_coste(), reverse=True)
            print("frontera ordenados: ", [h.get_datos() for h in nodos_frontera]) 



if __name__ == "__main__":
    estado_inicial=[4,3,2,1]
    solucion=[1,2,3,4]
    nodo_solucion = buscar_solucion_DFS(estado_inicial, solucion)
    # mostrar resultado
    resultado=[]
    nodo=nodo_solucion
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()
    print("Estado Inicial: ",estado_inicial)
    print("Estado objetivo: ",solucion)
    print("Solucion: ",resultado)