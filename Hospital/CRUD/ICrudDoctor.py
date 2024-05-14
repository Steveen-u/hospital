from MODEL.doctores import Doctor as doctor
from ICrud import ICrud


class ImpCrudDoctor ( ICrud .ICrud ) :

 def crear ( self , ** kwargs ) :
        return doctor.Doctor(kwargs ["doctorName"], kwargs ["doctorSpecialty"], kwargs ["doctorDNI"])
 
def buscarPorDni ( self , ** kwargs ) :
        return doctor.Doctor(kwargs ["doctorDNI"])
     