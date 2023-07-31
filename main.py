from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "your_secret_key"  

@app.route("/",methods =["GET","POST"])
def landing():
    if request.method == "POST":
        username = request.form.get("username")
        # Store the username in the session
        session["username"] = username
        return redirect(url_for("home"))
    return render_template("index.html")

@app.route("/home")
def home():
    username = session.get("username")
    return render_template("home.html",username=username)

@app.route("/Chatbot")
def chat():
    return render_template("Chatbot.html")

@app.route("/getsgurl")
def getgirl():
    return render_template("getsgurl.html")


if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    app.run(host="127.0.0.1", port=8080, debug=True)
