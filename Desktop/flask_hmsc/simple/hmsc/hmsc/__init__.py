import os,sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


WIN = sys.platform.startswith('win')
if WIN:
    prefix = "sqlite:///" # window
else:
    prefix = "sqlite:////" # mac linux

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] =  prefix + os.path.join(os.path.dirname(app.root_path),'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 对内存做优化
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY','dev') 

db = SQLAlchemy(app) # 初始化app


from hmsc import views