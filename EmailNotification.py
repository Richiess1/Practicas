import AbstractNotification

class EmailNotification(AbstractNotification.AbstractNotification):
    def __init__(self, name, email):  
        super().__init__(name)        
        self.email = email
        print(f"Enviado a {name} con correo electrónico de {email} (Email)")
        
