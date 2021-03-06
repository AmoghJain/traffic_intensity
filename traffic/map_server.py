from flask import Flask, request
# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def root():
    return app.send_static_file('get_traffic_map.html')

if __name__ == "__main__":
    app.run(port=7001)
