from flask import Flask, request, jsonify
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

app = Flask(__name__)

def send_test_mail(body):
    sender_email = "erikdhv@gmail.com"
    receiver_email = "erikdhv@gmail.com"

    msg = MIMEMultipart()
    msg['Subject'] = '[Email Test]'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    msgText = MIMEText('<b>%s</b>' % (body), 'html')
    msg.attach(msgText)

    filename = "/home/erik/Escritorio/PandoraSoft_Logo.png"
    f = open(filename, mode='r')
    print("Hola mundo", f)
    msg.attach(MIMEText(f))

    with open('/home/erik/Escritorio/PandoraSoft_Logo.png', 'rb') as fp:
        img = MIMEImage(fp.read())
        img.add_header('Content-Disposition', 'attachment', filename="PandoraSoft_Logo.png")
        msg.attach(img)
        
    pdf = MIMEApplication(open("/home/erik/Escritorio/PandoraSoft_Logo.png", 'rb').read())
    pdf.add_header('Content-Disposition', 'attachment', filename= "PandoraSoft_Logo.png")
    msg.attach(pdf)

    try:
        with smtplib.SMTP('localhost') as smtpObj:
            smtpObj.ehlo()
            smtpObj.starttls()
            #smtpObj.login("sender@email.com", "password")
            smtpObj.sendmail(sender_email, receiver_email, msg.as_string())
    except Exception as e:
        print(e)
        
@app.route('/')
def hello_world():
    return "Hello world!"

if __name__ == "__main__":
    send_test_mail("Welcome to Medium!")
    app.run('0.0.0.0',port=5000)