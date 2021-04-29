class Proyecto:
    __id = ''
    __titulo = ''
    __palabras = []
    __integrantes = []
    __puntaje = 0

    def __init__(self,id = '', tit = '', palab = ''):
        self.__id = id
        self.__titulo = tit
        self.__palabras = palab



    def getpuntaje(self):
        return self.__puntaje

    def getId(self):
        return self.__id

    def getTitulo(self):
        return self.__titulo

    def cargarIntegrantes(self,integrantes=[]):
        self.__integrantes=integrantes

    def CalcularPuntos(self):
        direc = False
        codirec = False
        continte = 0
        catdirec = ''
        catcodirec = ''
        for integrante in self.__integrantes:
            continte += 1
            if not direc:
                if integrante.getRol() =="director":
                    direc = True
                    catdirec = integrante.getCat()
            if not codirec:
                if integrante.getRol() =="codirector":
                    codirec = True
                    catcodirec = integrante.getCat()
        if continte < 3:
            self.__puntaje -= 20
            print("El proyecto debe tener como minimo 3 integrantes.")
        else: self.__puntaje += 10
        if not direc: print("El proyecto debe tener Director.")
        else:
            if catdirec =="I" or catdirec =="II":
                self.__puntaje += 10
            else:
                self.__puntaje -= 5
                print("El Director del Proyecto debe tener categoría I o II.")
        if not codirec:
            print("El proyecto debe tener Codirector.")
        else:
            if catcodirec == "I" or catcodirec == "II" or catcodirec == "III":
                self.__puntaje += 10
            else:
                self.__puntaje -= 5
                print("El Codirector del Proyecto debe tener como mínimo categoría III")
        if not direc and not codirec:
            self.__puntaje -= 10

    def __str__(self):
        return f"ID:{self.__id} Titulo:{self.__titulo} Palabras Clave:{self.__palabras}"

    def __gt__(self,otro):
        return self.__puntaje>otro.getpuntaje()




