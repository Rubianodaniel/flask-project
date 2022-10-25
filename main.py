### importar de flask todos los metodos necesarios para crear la app
from flask import (Flask, request,make_response,
                    redirect, render_template,session,
                    url_for,flash)  
### importar bootstrap
from flask_bootstrap import Bootstrap
### importar what the forms de flask  
from flask_wtf import FlaskForm  
## de what the forms. fields las formas
from wtforms.fields import StringField, PasswordField, SubmitField
### importar de wtf valodators
from wtforms.validators import DataRequired
### importar unitest para testear las rutas
import unittest

## iniciar el servidor con el nombre del archivo
app = Flask(__name__)
## configuracion flask
app.config["SECRET_KEY"]= "SUPER SECRETO"




tasks = ["buy coffe", "send puchase request", "send product to costumer"]
bootstrap = Bootstrap(app)

class LoginForm(FlaskForm):
    '''clase  login form 
        en esta clase se guardan las formas de wtf
    '''
    username = StringField("user name",validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    submit = SubmitField("send")

### comandos de cli
@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

### rutas o path or endpoints
@app.errorhandler(404)
def not_found(error):
    return render_template("404.html", error = error)


@app.route("/")
def index():
    user_ip = request.remote_addr
    response = make_response(redirect("/hello")) ## reddireccionar a otra ruta
    #response.set_cookie("user_ip", user_ip)##crear una cookie
    session["user_ip"]=user_ip ## user secret key
    return response


@app.route('/hello',methods = ["GET","POST"])
def hello():
    ##user_ip = request.cookies.get("user_ip")#obtener el valor de la cookie
    user_ip = session.get("user_ip") ## obtener valor de la session
    login_form = LoginForm()
    username = session.get("username")
    context = {
        'user_ip':user_ip,
        'tasks':tasks,
        'login_form':login_form,
        "username":username
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        session["username"] = username
        flash ("user name registered succesfuly")
        return redirect(url_for('index'))
    return (render_template("hello.html", **context))


if __name__ == '__main__':
    app.run(debug=True)
    