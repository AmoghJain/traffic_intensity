from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
	payload  = json.loads(request.data)
	# payload is the post parameters passed as json
	# call your python function from here and pass the payload to it as the argument


if __name__ == "__main__":
	app.run(port="5000") # runs on port 5000, feel free change it	
