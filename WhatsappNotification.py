import AbstractNotification

class WhatsappNotification(AbstractNotification.AbstractNotification):
    def _init_(self, name, phone, area):
        super()._init_(name)
        self.name = name
        self.phone = phone
        self.area

    def send(self, message):
        print(f"Enviado a {name} con telefono {phone} y codigo de area {area} (WhatsApp)")
