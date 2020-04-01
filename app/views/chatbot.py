from flask import request, render_template
from .. import app
from ..forms.chat_form import ChatForm
from ..chatbot import respond


# TODO: Create html for chatbot view.
# TODO: Figure out how to fit chatbot view in base.html and make it work.
# TODO: Figure out how to test out TensorFlow 2.x with Flask.

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
