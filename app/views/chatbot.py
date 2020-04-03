from flask import request, render_template
from .. import app
from ..forms.chat_form import ChatForm

# TODO: Change the chatbot from Gilbert (mock testing bot) to Peggy (actual bot with neural network).
#from ..chatbot import respond
import random
def respond(user_input):
    return random.choice(["H3ll0, 1 4m GI-L83RT, th3 r0b0t.", "H0w c4n 1 h3lp y0u?", "D1d y0u kn0w th4t 1'm 4 r0b0t?", "01001000010001010100110001001100010011110000110100001010", "01001000010010010000110100001010"])


# TODO: Create html for chatbot view.
# TODO: Figure out how to fit chatbot view in base.html and make it work.
# TODO: Figure out how to test TensorFlow 2.x with Flask (TF needs a CPU with AVX instructions and wont install locally).

class Message():
    def __init__(sender, content):
        self.sender = sender
        self.content = content

@app.route("/chatbot", request=["POST"]):
def chatbot(username, botname, user_messages=[], bot_messages=[])    
    form = ChatForm()
    if request() == "POST" and form.validate_on_submit:
        
        user_msg = form.user_response.data

        user_messages.append(Message(username, user_msg))
        bot_messages.append(Message(botname, respond(user_msg)))
        
    render_template("chat.html", user_messages=user_messages, others_messages=bot_messages)
