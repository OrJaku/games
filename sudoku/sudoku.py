from flask import Flask
from flask import render_template, request
from board_structure import get_structure

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def board_game():
    if request.method == "POST":
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        elements_get = request.form.items()
        elements = [x for x in elements_get]
        structure = get_structure(elements)
        elem_call = structure['elem_call']
        elem_vertical = structure['elem_vertical']
        elem_horizontal = structure['elem_horizontal']
        elem_vertical_list = list(elem_vertical.values())
        elem_horizontal_list = list(elem_horizontal.values())
        elem_call_list = list(elem_call.values())

        c = 1
        # print(elem_horizontal_list)
        # print(elem_vertical_list)
        # print(elem_call_list)

        for row in elem_horizontal_list:
            
            i = 0
            for value in row:
                if value == "":
                    for n in numbers:
                        if n in row or n in elem_call_list[0] or n in elem_vertical_list[0] :
                           continue
                        else:
                            row[i] = n
                i += 1
            row_number = str(c)
            elem_horizontal[row_number] = row
            c += 1
        print(elem_horizontal)







        return render_template("board.html")

    return render_template("board.html")

if __name__ == '__main__':
    app.run()