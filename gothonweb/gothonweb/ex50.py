from flask import Flask

app = Flask(__name__)

@app.route ('/')

def helllo_world ():
    greeting = "world"
    return f"Hello, {greeting}!"

if __name__ == "__main__":
    app.run ()
