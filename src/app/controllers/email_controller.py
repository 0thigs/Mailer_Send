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

        emailsTeste = ["machinimavlogs@gmail.com", "gabrielsoliveira1606@gmail.com"]

        emails = ["teste123456banana@gmail.com",'tadeu.yoshida@55pro.com.br', 'contact@7comm.com.br', 'joao@avionics.com.br', 'srvp@abimaq.org.br', 'lmainardi@acaditi.com.br', 'vendas@acnisdobrasil.com.br', 'contato@adtechsd.com.br', 'douglas.ortlibas@aernnova.com', 'contato@aeroconcepts.com.br', 'dario.cristaldo@aerocris.ind.br', 'contato@aerojr.com', 'leonardo.andrade@aeromot.com.br', 'aeroriver.adm@gmail.com', 'fulvio.delicato@aerospacebrazilcertifications.com', 'alexandra.gioso@agglobal.com.br', 'david@papayacomunicacao.com.br', 'ags@agsholding.com', 'contato@aichico.com', 'contato@adb.ind.br', 'atendimento@aisys.com.br', 'comercial@akaer.com.br', 'nd@aliger.io', 'juliana@allteccomposites.com.br', 'brasil@altair.com', 'contato@altave.com.br', 'contato@alvalavanderia.com', 'pires.anacris@gmail.com', 'souza_anap@yahoo.com.br', 'natani@aortacomunicacao.com.br', 'contato@apimetrology.com', 'info@arable.com', 'vendas@arbonne.com.br', 'alberto.bordonaba@aritex-es.com', 'contato@arqmedes.com', 'comercial.sjc@arquivar.com', 'marcos.bernardes@atimetals.com', 'aerospace@ats4i.com.br', 'contato@autaza.com', 'eduardo.leonetti@eati-avibras.com.br', 'contact@awsgroup.com.br', 'salesbrazil@axon-cable.com', 'contato@baikalsec.com', 'falecom@bestcode.com.br', 'contato@betel.aero', 'comercial@biosind.com.br', 'nondiaye@gmail.com', 'octavio@bizu.space', 'salesbrasil@blueskynetwork.com', 'felipe.mello@bmlaw.com', 'contato@bongoup.com.br', 'helder@bongoup.com.br', 'contato@brengtrein.com.br', 'cristiane.rabello@buenonetworks.com.br', 'calfer@calfer.com.br', 'asbrito@cdatec.com.br', 'contato@cemaden.gov.br', 'demetrius.alexandre@fundhas.org.br', 'carl@agrointeligencia.com.br', 'celia.faria@cgvale.com.br', 'comercial@ciatec.ind.br', 'cassia@cintrarh.com.br', 'contato@cis-erp.com.br', 'cite@cite.org.br', 'gilca@climatempo.com.br', 'jose.henrique@clp.org.br', 'info@clurb.net', 'cristine.menezes@cmgovernanca.com.br', 'daniela@courban.com.br', 'contato@compassnegociosdisruptivos.com.br', 'lucianon@projetosigo.com.br', 'compressorinteligente@gmail.com', 'comercial@compsis.com.br', 'roberto.bonesio@comutensili.it', 'renato@conectadigitalsolutions.com', 'david@agenziamkt.com.br', 'admconsensus4@gmail.com', 'cjefgv@cjefgv.com.br', 'carlosvinicius@companyprogress.com.br', 'comercial@csjsistemas.com.br', 'contato@cstglobal.com.br', 'contato@centrotreinamentos.com.br', 'contato@databot.digital', 'info@datalogix.com.br', 'clientes@deepesg.com', 'daniel.resemini@deltavengenharia.com', 'michel.amaral@designa.com.br', 'comercial@devmaker.com.br', 'lduarte@digicon.com.br', 'atendimento@softcake.com.br', 'vendas@dodesk.com.br', 'contact@domrock.ai', 'contato@drlicita.com', 'drmcro@drmicro.com.br', 'alexandre@dtacargo.com.br', 'wagner@dualsys.com.br', 'fernandes.laerte@e3metais.com', 'leticia@easy2tech.com.br', 'financeiro@electroimpact.com', 'jose.brancalion@embraer.com.br', 'embras@embras.net', 'rpadantas@gmail.com', 'pier@emoov.com.br', 'marcelo.essado@emsisti.com.br', 'endneves.ndt@gmail.com', 'michelle.feierabend@energytelecom.com.br', 'comercial@engtelco.com.br', 'contato@environmentals.com.br', 'vanderlei@edgeofspace.com.br', 'epsoft@epsoft.com.br', 'ccghizoni@equatorialsistemas.com.br', 'juliomoreira@equatorium.com.br', 'contato@ermatech.com.br', 'comercial@ejt.com.br', 'luiz@esss.co', 'contato@estrataxia.com.br', 'comercial@evereste.org.br', 'sergio@explorer.com.br', 'extremussurfaces@gmail.com', 'rubsney.nascimento@fabsolucoes.com.br', 'fabiodossantos77@hotmail.com', 'cia.sjcampos@fsantoantonio.edu.br', 'recanto.bemtevi@hotmail.com', 'everton.mota@fastworkps.com.br', 'secretaria.sjc@fatec.sp.gov.br', 'fernando.vidal@favedigital.com.br', 'nehemias@femtociencias.com.br', 'ferdnan@gamatecnivca.com.br', 'carrasco@fev.com', 'srafgvsp@fgv.br', 'fibraforte@fibraforte.com.br', 'dennis@fieldeyes.com.br', 'contato@findrs.com.br', 'comercial@finetornos.com.br', 'mail@fius.com.br', 'hamiltonfaria@fiscoexpert.com.br', 'mcarneiro@fitec.org.br', 'marcelo.col@flareConsultoria.com.br', 'contato@fleeting.com.br']


        # SALVA A LISTA DE EMAILS
        #with open("emails_list.py", "r") as arquivo:
        #    emails = arquivo.read()

        # LOOP QUE ENVIA OS EMAILS!
        for receiver_email in emails:  # trocar `emailsTeste` pela lista `emails`!
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
