from flask import Flask
app = Flask(__name__)

password = "xyz"

@app.route("/")
def hello():
    print(password)
    return "hello world!"

if __name__ == "__main__":
    app.run()
