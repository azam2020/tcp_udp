from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
	return render_template('index.html')


@socketio.on('message_from_client')
def handle_message(message):
	print("Received messgae: ",message)
	emit('message_from_server',{'user':message['user'],'message':message['message']},broadcast=True)

if __name__=='__main__':
	socketio.run(app,debug=True,host='0.0.0.0',port=5002)
