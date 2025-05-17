from NotificationInterface import NotificationInterface

class AbstractNotification(NotificationInterface):
    def __init__(self, name:str):
        self.name = name

