from flask import Flask, Blueprint, abort, render_template, request
#from regex import P
#from werkzeug.utils import secure_filename
import os

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('/home.html')

@views.route('/lab')
def lab():
    return render_template('/lab.html')

"""@views.errorhandler(404)
#Invalid URL
def page_not_found(e):
    return render_template('404.html'), 404

@views.errorhandler(500)
#Internal Server Error
def Server_Error(e):
    return render_template('500.html'), 500
"""