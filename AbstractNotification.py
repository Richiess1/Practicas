import NotificationInterface

class AbstractNotification(NotificationInterface):
    def _init_(self, name:str):
        self.name = name

