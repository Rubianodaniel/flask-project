from app.forms import LoginForm
from . import auth
from flask import render_template

@auth.route('/login')
def login():
    context = {
        'Login_form':LoginForm()
    }
    return render_template(**context)