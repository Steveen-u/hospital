from MODEL.hospital import Hospital as hospital
from ICrud import ICrud

class ImpCrudHospital ( ICrud .ICrud ) :

 def crear ( self , ** kwargs ) :
     return hospital.Hospital(kwargs ["hospitalName"])

 def relacion ( self , ** kwargs ) :
    hospital.doctores = kwargs [ "doctores"]
    return hospital
 
 def buscar ( self , ** kwargs ) :
    return hospital.hospitalName