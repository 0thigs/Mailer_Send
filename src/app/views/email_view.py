from flask import render_template
from werkzeug.utils import secure_filename
from app.forms.email_form import EmailForm
from app.controllers.email_controller import EmailController
import os


class EmailView:
    def index(self):
        email_form = EmailForm()

        is_validated_form = email_form.validate_on_submit()

        print(is_validated_form)

        if not is_validated_form:
            return render_template("index.html", form=email_form)

        file = email_form.attachment.data

        filename = secure_filename(file.filename)

        path = os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            "..",
            "..",
            "static/tmp",
            filename,
        )

        file.save(path)

        payload = {
            "email": email_form.email.data,
            "password": email_form.password.data,
            "subject": email_form.subject.data,
            "body": email_form.body.data,
            "attachment": path,
        }

        emailController = EmailController()

        emailController.send(payload)

        return render_template("index.html", form=email_form)
