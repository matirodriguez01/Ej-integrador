import csv
from IntegrantesProyecto import IntegrantesProyecto


class ManejadorIntegrantesProyecto:
    __listaintegrantes = []

    def __init__(self):
        file = open('integrantesProyecto.csv')
        reader = csv.reader(file, delimiter=';')
        bandera = True
        for fila in reader:
            if bandera == True:
                bandera = False
            else:
                integr = IntegrantesProyecto(fila[0], fila[1], (fila[2]), fila[3], fila[4])
                self.__listaintegrantes.append(integr)

    def integrantesProyectos(self, id):
        inte = []
        for integrante in self.__listaintegrantes:
            if integrante.getid() == id: inte.append(integrante)
        return inte


