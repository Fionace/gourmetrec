#-*-coding:utf-8-*-
from flask import Flask
from gourmetrec.app import gourmetrec


app=Flask(__name__,static_folder='gourmetrec/static',template_folder='gourmetrec/templates')
app.config.from_object(__name__)
app.register_blueprint(gourmetrec)

if __name__=='__main__':
    app.debug=True
    app.run()

