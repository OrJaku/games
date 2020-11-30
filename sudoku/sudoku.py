from flask import Flask
from flask import render_template, request
from board_structure import get_structure

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def board_game():
    if request.method == "POST":
        elements_get = request.form.items()
        elements = [x for x in elements_get]
        structure = get_structure(elements)
        elem_call = structure['elem_call']
        elem_vertical = structure['elem_vertical']
        elem_horizontal = structure['elem_horizontal']
        # print(elem_call)
        # print(elem_vertical)
        # print(elem_horizontal)
        
            
        return render_template("board.html")

    return render_template("board.html")

if __name__ == '__main__':
    app.run()