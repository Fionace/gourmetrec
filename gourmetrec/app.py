#-*-coding:utf-8-*-

from flask import redirect,render_template,Blueprint,url_for

gourmetrec=Blueprint('gourmetrec',__name__,static_folder='static',template_folder='templates')

@gourmetrec.route("/")
def login():
    #return render_template("index.html")
    return str(url_for('.templates',filename='jquery-1.9.1.js'))

@gourmetrec.route("/register")
def register():
    return render_template("register.html")

@gourmetrec.route("/tmptest")
def tmp():
    return render_template("tmp.html")

@gourmetrec.route("/test")
def test():
    return str(url_for('.templates',filename='jquery-1.9.1.js'))
