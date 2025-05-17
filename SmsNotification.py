import AbstractNotification

class SmsNotification(AbstractNotification):
    def _init_(self, name, phone, area):
        super()._init(name)
        self.phone = phone
        self.area = area

    def send(self, message):
        print(f"Enviado a {name} con telefono {phone} y codigo de area {area} (SMS)")