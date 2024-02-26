import smtplib
import ssl
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class EmailController:
    def send(self, payload: dict) -> None:
        """Send an email to somebody
        Args:
            payload (dict): data of the sender
            - 'email': Email of the sender
            - 'password': Password of the sender
            - 'subject': Subject of the email
            - 'body': Body of the email
            - 'attachment': File in attachment of the email
        """

        def adicionar_anexo(message, filename):
            with open(payload["attachment"], "rb") as attachment:  # NOME DO PDF
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
            )
            message.attach(part)

        emailsTeste = [
            "silva.faelm@gmail.com",
            "machinimavlogs@gmail.com",
            "joaopcarvalho.cds@gmail.com",
        ]

        # SALVA A LISTA DE EMAILS
        # with open("emails_list.py", "r") as arquivo:
        #     emails = arquivo.read()

        # LOOP QUE ENVIA OS EMAILS!
        for receiver_email in emailsTeste:  # trocar `emailsTeste` pela lista `emails`!
            message = MIMEMultipart()
            message["From"] = payload["email"]
            message["To"] = receiver_email
            message["Subject"] = payload["subject"]

            message.attach(MIMEText(payload["body"], "html"))

            # Adicionar anexo ao e-mail
            # filename = "curriculo.pdf"  # Nome do arquivo P DF a ser anexado
            adicionar_anexo(message, payload["attachment"])

            # Converter a mensagem para string
            text = message.as_string()

            # Login no servidor usando contexto seguro e envio de e-mail
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(payload["email"], payload["password"])
                server.sendmail(payload["email"], receiver_email, text)

        os.remove(payload["attachment"])
        print(payload)
        print("E-mails enviados com sucesso!")
