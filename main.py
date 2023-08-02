from flask import Flask, render_template, request, session, redirect, url_for
# If i added this line, the webpage won't be loaded. The website would work just fine if it removed it
from vertexai.preview.language_models import ChatModel, InputOutputTextPair,ChatSession
from google.cloud import aiplatform

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
    # username = chatbot.chat()
    return render_template("home.html",username=username)

@app.route("/Chatbot",methods =["GET","POST"])
def chat():
    chat_model = ChatModel.from_pretrained("chat-bison@001")
    chat = ChatSession(chat_model)

    # TODO developer - override these parameters as needed:
    parameters = {
        "temperature": 0.5,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": 1000,  # Token limit determines the maximum amount of text output.
        "top_p": 0.95,  # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
        "top_k": 40,  # A top_k of 1 means the selected token is the most probable among all tokens.
    }

    Example = InputOutputTextPair(
        input_text="What are you?",
        output_text="I'm a AI language model"
    )

    Example2 = InputOutputTextPair(
        input_text="How to crack an eggs",
        output_text="To crack an egg, gently tap the egg on a hard surface, such as the counter or a bowl. Then, using your fingers, gently spread the shell apart and open the egg.",
    )
    render_template("Chatbot.html")
    usr = "Hello"  # Assign a default value for usr

    if request.method == "POST":
        usr = request.form.get("userinput")

    response = chat.send_message(
        usr, **parameters
    )

    return render_template("Chatbot.html",response = response)

@app.route("/getsgurl")
def getgirl():
    return render_template("getsgurl.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

