from flask import Flask, request, jsonify

from main import chatWithBot

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('index.html')

@app.route('/chat', methods=['GET', 'POST'])
def chatBot():
    chatInput = request.form['chatInput']
   
     chatBotReply=chatWithBot(chatInput)
     return render_template('reply.html',chatBotReply)


if __name__ == '__main__':
    app.run(debug=True)