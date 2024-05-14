class Doctor:
    def __init__(self, name, specialty, DNi):
        self.__doctorName = name
        self.__doctorSpecialty = specialty
        self.__doctorDNI = DNi

    def getDoctorName(self):
        return self.__doctorName
    
    def setDoctorName(self, name):
        self.__doctorName = name

    def getDoctorSpecialty(self):
        return self.__doctorSpecialty
    
    def setDoctorSpecialty(self, specialty):
        self.__doctorSpecialty = specialty

    def getDoctorDNI(self):
        return self.__doctorDNI
    
    def setDoctorDNI(self, DNi):
        self.__doctorDNI = DNi