from flask import Flask, render_template
from google.cloud import aiplatform
from vertexai.preview.language_models import ChatModel, InputOutputTextPair,ChatSession

app = Flask(__name__)

@app.route("/")
def home():
    chat_model = ChatModel.from_pretrained("chat-bison@001")
    chat = ChatSession(chat_model)
    parameters = {
        "max_output_tokens": 256,  # Token limit determines the maximum amount of text output.
        "top_p": 0.95,  # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
        "top_k": 40,  # A top_k of 1 means the selected token is the most probable among all tokens.
    }
    Example = InputOutputTextPair(
        input_text="What are you?",
        output_text="I'm a AI language model"
    )
    usr_input = "Hello Chatbot,What are you ? answer me "
    response = chat.send_message(
        usr_input, **parameters
    )
    res = response.text
    return f"<p>{res}<p>"


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=4000)






























