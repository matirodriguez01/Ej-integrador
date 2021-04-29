import csv
from Proyecto import Proyecto
from ManejadorIntegrantesProyecto import ManejadorIntegrantesProyecto

class ManejadorProyecto:

    __listaproyectos = []

    def __init__(self):
        file = open('proyectos.csv')
        reader = csv.reader(file, delimiter=';')
        bandera = True
        for fila in reader:
            if bandera == True:
                bandera = False
            else:
                proyecto = Proyecto(fila[0], fila[1], fila[2])
                self.__listaproyectos.append(proyecto)

    def Integrantes(self):
        inte = ManejadorIntegrantesProyecto()
        for proyecto in self.__listaproyectos:
            integrantes = inte.integrantesProyectos(proyecto.getId())
            proyecto.cargarIntegrantes(integrantes)

    def calcularPuntos(self):
        for proyecto in self.__listaproyectos:
            print("Calculando puntaje del proyecto: {}".format(proyecto.getId()))
            proyecto.CalcularPuntos()

    def listar(self):
        self.__listaproyectos.sort(reverse=True)
        print("ID       PROYECTO%72sPUNTAJE" % (" "))
        for proyecto in self.__listaproyectos:
            print("%-8s%-80s  %2i " % (proyecto.getId(), proyecto.getTitulo(), proyecto.getpuntaje()))


    def getlista(self):
        return self.__listaproyectos




