from app import app
from flask import Flask, redirect, render_template

@app.route('/')
def index():
    return render_template('main.html')
