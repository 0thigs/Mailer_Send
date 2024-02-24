import email, smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def adicionar_anexo(message, filename):
    with open("NOME DO PDF", "rb") as attachment: #NOME DO PDF
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    message.attach(part)

emailsTeste = ['silva.faelm@gmail.com', 'machinimavlogs@gmail.com', 'joaopcarvalho.cds@gmail.com']

#SALVA A LISTA DE EMAILS
with open('listaEmails.py', 'r') as arquivo:
    emails = arquivo.read()

# EMAIL CONTENT!
subject = "Sample Subject"
body = "Sample Text"

# INFO-SENDER!
sender_email = "EMAIL DO PROPRIETARIO" # EMAIL DO SENDER
password = "EMAIL RECEPTOR" # SUA SENHA DO APP PASSWORD/2-step verification

# LOOP QUE ENVIA OS EMAILS!
for receiver_email in emailsTeste: # trocar `emailsTeste` pela lista `emails`!
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))
    
    # Adicionar anexo ao e-mail
    filename = "curriculo.pdf"  # Nome do arquivo PDF a ser anexado
    adicionar_anexo(message, filename)

    # Converter a mensagem para string
    text = message.as_string()

    # Login no servidor usando contexto seguro e envio de e-mail
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

print("E-mails enviados com sucesso!")