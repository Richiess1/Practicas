from NotificationInterface import NotificationInterface

class AbstractNotification(NotificationInterface):
    def __init__(self, name):
        self.name = name

