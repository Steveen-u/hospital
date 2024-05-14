from doctores import Doctor

class Hospital:
    def __init__(self, name, doctores):
        self.__hospitalName = name
        self.__doctores = doctores

    def getHospitalName(self):
        return self.__hospitalName
    
    def setHospitalName(self, name):
        self.__hospitalName = name

    def getDoctores(self):
        return self.__doctores
    
    def setDoctores(self, doctores):
        self.__doctores = doctores

