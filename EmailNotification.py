import AbstractNotification

class EmailNotification(AbstractNotification.AbstractNotification):
    def _init_(self, name, email):
        super()._init(name)
        self.email = email
