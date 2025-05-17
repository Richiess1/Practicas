import AbstractNotification

class SmsNotification(AbstractNotification.AbstractNotification):
    def _init_(self, name, phone,area_code ):
        super()._init_(name)
        self.phone = phone
<<<<<<< HEAD
        self.area_code = area_code
        

=======
        self.area = area

    def send(self, message):
        print(f"Enviado a {name} con telefono {phone} y codigo de area {area} (SMS)")
>>>>>>> 5e05b5c3483c7e2d05bb3855cca252d4f20da8c6
