from flask import Flask,url_for,render_template,request,flash,redirect
from hmsc.models import *
from hmsc import db,app


@app.route('/')
def index():
    return 'flask run'


