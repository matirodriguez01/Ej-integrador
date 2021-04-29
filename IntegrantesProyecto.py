class IntegrantesProyecto:
    __idproy = ''
    __nombre = ''
    __dni = ''
    __cat = ''
    __rol = ''

    def __init__(self, idp='', nom='', dni='', cat='', rol=''):
        self.__idproy = idp
        self.__nombre = nom
        self.__dni = dni
        self.__cat = cat
        self.__rol = rol

    def getid(self):
        return self.__idproy

    def getCat(self):
        return self.__cat

    def getRol(self):
        return self.__rol

