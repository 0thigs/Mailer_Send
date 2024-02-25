from flask_wtf import FlaskForm
from wtforms import FileField, PasswordField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email


class EmailForm(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = PasswordField("Senha", validators=[DataRequired()])
    subject = StringField("Assunto", validators=[DataRequired()])
    body = TextAreaField("Corpo", validators=[DataRequired()])
    attachment = FileField("Anexo", validators=[DataRequired()])
    submit_button = SubmitField("Enviar")
