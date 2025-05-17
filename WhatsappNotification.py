import AbstractNotification;


class WhatsappNotification(AbstractNotification.AbstractNotification):
    def __init__(self, name, phone_number, area_code):
        super().__init__(name)
        self.phone_number = phone_number
        self.area_code = area_code


    