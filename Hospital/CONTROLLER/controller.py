from MODEL.doctores import Doctor
class Controller:
    def __init__(self, hospital, view):
        self.hospital = hospital  # Instancia de Hospital
        self.view = view

        self.view.register_event_handler(self.handle_event)

    def handle_event(self, event, data):
        if event == "agregar_doctor":
            doctor_info = data  # {'name': name, 'specialty': specialty, 'DNI': dni}
            new_doctor = Doctor(doctor_info["name"], doctor_info["specialty"], doctor_info["DNI"])
            self.hospital.getDoctores().append(new_doctor)  # Agregar doctor a la lista
            self.view.actualizar_vista(self.hospital.getDoctores())
        elif event == "editar_doctor":
            doctor_id = data["id"]
            doctor_info = data["nueva_informacion"]
            self.hospital.getDoctores()[doctor_id] = Doctor(doctor_info["name"], doctor_info["specialty"], doctor_info["DNI"])
            # Alternativa: usar metodo actualizar_doctor en Hospital (si existe)
            self.view.actualizar_vista(self.hospital.getDoctores())
        elif event == "eliminar_doctor":
            doctor_id = data
            del self.hospital.getDoctores()[doctor_id]
            self.view.actualizar_vista(self.hospital.getDoctores())

    def buscarHospital(self):
        return self.hospital.getNombre()

    def buscarDoctores(self):
        return self.hospital.getDoctores()  
    
    
