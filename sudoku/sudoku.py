from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def board_game():
    if request.method == "POST":
        elements = request.form
        print("Elements", elements)
        for i in elements:
            
        
    return render_template("board.html")

if __name__ == '__main__':
    app.run()