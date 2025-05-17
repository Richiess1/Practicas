from AbstractNotification import AbstractNotification

class EmailNotification(AbstractNotification):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

    def send(self):
        print(f"Enviado a {self.name} con correo electronico de {self.email} (Email)")
