from google.cloud import aiplatform
from vertexai.preview.language_models import ChatModel, InputOutputTextPair,ChatSession
import colorama
import sys

# Run these command first to start the environment 
# python3 -m venv env
# source env/bin/activate

def main(temperature: float = 0.5):
    chat_model = ChatModel.from_pretrained("chat-bison@001")
    chat = ChatSession(chat_model)

    # TODO developer - override these parameters as needed:
    parameters = {
        "temperature": temperature,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": 256,  # Token limit determines the maximum amount of text output.
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


    user_inp = input("[User] ")
    

    response = chat.send_message(
        user_inp, **parameters
    )
    print("[Model] "+colorama.Fore.GREEN+ f"{response.text}"+colorama.Fore.RESET)
    # [END aiplatform_sdk_chat]
    if user_inp == "OUT":
        sys.exit()

    return response

while True:
    if __name__ == "__main__":
        main()