#controlador general
<<<<<<< HEAD
=======
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

>>>>>>> 5e05b5c3483c7e2d05bb3855cca252d4f20da8c6
