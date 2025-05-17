#controlador general
from EmailNotification import EmailNotification 
from SmsNotification import SmsNotification
from WhatsappNotification import WhatsappNotification

def controller():
    email = EmailNotification("ricardo", "ricardo.com")
    sms = SmsNotification("ricardo", "56895689", "503")
    wha = WhatsappNotification("ricardo", "56895689", "503")
    email.send()
    sms.send()
    wha.send()

controller()

