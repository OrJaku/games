from flask import Flask
from flask import render_template, request
# from board_structure import get_structure

app = Flask(__name__)

def differenc(lista_1, lista_2):
    return (list(list(set(lista_1)-set(lista_2))))


@app.route('/', methods=["GET", "POST"])
def board_game():
    if request.method == "POST":
        # numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        # elements_get = request.form.items()
        # print(request.form)
        # elements = [x for x in elements_get]
        # structure = get_structure(elements)
        # elem_call = structure['elem_call']
        # elem_vertical = structure['elem_vertical']
        # elem_horizontal = structure['elem_horizontal']
        # elem_vertical_list = list(elem_vertical.values())
        # elem_horizontal_list = list(elem_horizontal.values())
        # elem_call_list = list(elem_call.values())

        # c = 1
        # # print(elem_horizontal_list)
        # # print(elem_vertical_list)
        # # print(elem_call_list)

        # for row in elem_horizontal_list:
        #     i = 0
        #     current_numbers = numbers.copy()
        #     print(current_numbers)
        #     list_without_horizontal = differenc(current_numbers, row)
        #     list_without_vertical = differenc(list_without_horizontal, elem_vertical_list[i])
        #     # if i <= 2 :
        #     #     c = 0
            
        #     # list_without_cell = differenc(list_without_vertical, elem_call_list[c])
        #     print(list_without_vertical)
        return render_template("board.html")

    return render_template("board.html")

if __name__ == '__main__':
    app.run()