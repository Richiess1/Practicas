import AbstractNotification

class SmsNotification(AbstractNotification.AbstractNotification):
    def _init_(self, name, phone,area_code ):
        super()._init_(name)
        self.phone = phone
        self.area_code = area_code
        

