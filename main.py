#controlador general
import WhatsappNotification
import SmsNotification
import EmailNotification 

def controller():
    email = EmailNotification(name="Ricardo",email="ricardo@gmail.com")
    whatsApp = WhatsappNotification(name="Ricardo", phone="5623-5623", area="503")
    sms = SmsNotification(name="Ricardo", phone="5623-5623", area="503")

    email.send("Enviado desde correo")
    whatsApp.send("Enviado desde WhatsApp")
    sms.send("Enviado desde SMS")

controller()

