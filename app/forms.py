from flask_wtf import FlaskForm  
## de what the forms. fields las formas
from wtforms.fields import StringField, PasswordField, SubmitField
### importar de wtf valodators
from wtforms.validators import DataRequired
### importar unitest para testear las rutas

class LoginForm(FlaskForm):
    '''clase  login form 
        en esta clase se guardan las formas de wtf
    '''
    username = StringField("user name",validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    submit = SubmitField("send")