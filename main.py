#controlador general
import WhatsappNotification
import SmsNotification
import EmailNotification 

def controller():
    email = EmailNotification("Ricardo","ricardo@gmail.com")
    whatsApp = WhatsappNotification("Ricardo", "5623-5623","503")
    sms = SmsNotification("Ricardo", "5623-5623", "503")

    email.send("Enviado desde correo")
    whatsApp.send("Enviado desde WhatsApp")
    sms.send("Enviado desde SMS")

controller()

