class EmailNotification(AbstractNotification):
    def _init_(self, name, email):
        super()._init(name)
        self.email = email