import NotificationInterface;

class AbstractNotification(NotificationInterface.NotificationInterface):

    name = None
    def __init__(self, name):
       self.name = name

       