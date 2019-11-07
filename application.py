from cs50 import SQL
from flask import Flask, redirect, render_template, request
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename


app = Flask(__name__);

@app.route("/")
def index():
  return render_template("index.html", author="Doctor Vee")