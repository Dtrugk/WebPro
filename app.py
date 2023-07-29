from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def Landing():
    if request.method == "POST":
        # Get the user input from the form data
        username = request.form["username"]

        # Redirect to the /home route with the username as a parameter in the URL
        return redirect(url_for("home", username=username))

    return render_template("index.html")

@app.route("/home/<username>")
def home(username):
    return render_template("home.html", username=username)

@app.route("/getsgurl")
def getsgurl():
    return render_template("getsgurl.html")

@app.route("/Chatbot")
def Chatbot():
    return render_template("Chatbot.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5005)
