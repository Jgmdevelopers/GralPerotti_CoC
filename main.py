from flask import Flask, request, make_response, redirect, render_template, session
from app import create_app

app = create_app()

items= ["Arroz", "Cafe", "Leche", "Yerba"]


@app.errorhandler(404)
def not_found_endpoint(error):
    return render_template('404.html', error=error)

@app.route("/")
def index():
    user_ip_information = request.remote_addr
    session["user_ip_information"] = user_ip_information
    
    return render_template("base.html")

@app.route("/show_information_address")
def show_information():
    user_ip = session.get("user_ip_information")
    context = {
        "user_ip":user_ip,
        "items":items
    }
    return render_template("ip_information.html", **context)

app.run(host='0.0.0.0', port=81, debug=True)