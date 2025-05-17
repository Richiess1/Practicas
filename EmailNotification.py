import AbstractNotification

class EmailNotification(AbstractNotification.AbstractNotification):
    def __init__(self, name, email):  
        super().__init__(name)        
        self.email = email
<<<<<<< HEAD
        print(f"Enviado a {name} con correo electrónico de {email} (Email)")
        
=======

    def send(self, message):
        print(f"Enviado a {name} con correo electronico de {email} (Email)")
>>>>>>> 5e05b5c3483c7e2d05bb3855cca252d4f20da8c6
