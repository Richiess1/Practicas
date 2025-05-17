from AbstractNotification import AbstractNotification

class SmsNotification(AbstractNotification):
    def __init__(self, name, phone, area):
        super().__init__(name)
        self.phone = phone
        self.area = area

    def send(self):
        print(f"Enviado a {self.name} con telefono {self.phone} y codigo de area {self.area} (SMS)")
