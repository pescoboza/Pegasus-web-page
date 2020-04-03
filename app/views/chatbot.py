from flask import request, render_template
from .. import app
from ..forms.chat_form import ChatForm

# TODO: Change the chatbot from Gilbert (mock testing bot) to Peggy (actual bot with neural network).
#from ..chatbot import respond
import random


def respond(user_input):
    return random.choice(
        ["H3ll0, 1 4m GI-L83RT, th3 r0b0t.",
         "H0w c4n 1 h3lp y0u?", "D1d y0u kn0w th4t 1'm 4 r0b0t?",
         "01001000010001010100110001001100010011110000110100001010",
         "01001000010010010000110100001010"])


# TODO: Create html for chatbot view.
# TODO: Figure out how to fit chatbot view in base.html and make it work.
# TODO: Figure out how to test TensorFlow 2.x with Flask (TF needs a CPU with AVX instructions and wont install locally).

class ChatMessage():
    def __init__(self, sender, content, from_you=False):
        self.sender = sender
        self.content = content
        self.from_you = from_you


@app.route("/chatbot", methods=["GET", "POST"])
def chatbot(username="You", botname="Gilbert", chat_messages=[]):
    form = ChatForm()
    if request.method == "POST" and form.validate_on_submit:

        user_msg = form.user_response.data
        bot_msg = respond(user_msg)
        msg = ChatMessage(username, user_msg, True)
        chat_messages.append(msg)
        chat_messages.append(ChatMessage(botname, bot_msg, False))

    return render_template("chat.html", chat_messages=chat_messages, form=form)
