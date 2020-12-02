elem = [('a1', '7'), ('b1', '2'), ('c1', ''), ('a2', ''), ('b2', ''), ('c2', '9'), ('a3', '8'), ('b3', ''), ('c3', ''), ('d1', ''), ('e1', '6'), ('f1', '9'), ('d2', ''), ('e2', '3'), ('f2', ''), ('d3', '4'), ('e3', ''), ('f3', ''), ('g1', ''), ('h1', ''), ('i1', '4'), ('g2', ''), ('h2', 
'5'), ('i2', ''), ('g3', '2'), ('h3', '6'), ('i3', ''), ('a4', ''), ('b4', '6'), ('c4', ''), ('a5', ''), ('b5', '3'), ('c5', ''), ('a6', '5'), ('b6', 
''), ('c6', ''), ('d4', '9'), ('e4', ''), ('f4', ''), ('d5', ''), ('e5', '8'), ('f5', ''), ('d6', ''), ('e6', ''), ('f6', '2'), ('g4', ''), ('h4', ''), ('i4', '8'), ('g5', ''), ('h5', '1'), ('i5', ''), ('g6', ''), ('h6', '4'), ('i6', ''), ('a7', ''), ('b7', '5'), ('c7', '1'), ('a8', ''), ('b8', '8'), ('c8', ''), ('a9', '4'), ('b9', ''), ('c9', ''), ('d7', ''), ('e7', ''), ('f7', '4'), ('d8', ''), ('e8', '2'), ('f8', ''), ('d9', '3'), ('e9', '7'), ('f9', ''), ('g7', ''), ('h7', ''), ('i7', '6'), ('g8', '4'), ('h8', ''), ('i8', ''), ('g9', ''), ('h9', '2'), ('i9', '5')]

def differenc(lista_1, lista_2):
    return (list(list(set(lista_1)-set(lista_2)) + list(set(lista_2)-set(lista_1))))
def differenc_2(lista_1, lista_2):
    return (list(list(set(lista_1)-set(lista_2))))
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]



def get_structure(elem):
    all_vertical = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    all_horizontal = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    dict_elem_v = {}
    dict_elem_h = {}
    dict_elem_c = {}
    for i in elem:
        for v in all_vertical:
            if v in i[0]:
                if v in dict_elem_v:
                    dict_elem_v[v].append(i[1])
                else:
                    dict_elem_v[v]=[i[1]]
                
    for i in elem:
        for h in all_horizontal:
            h = str(h)
            if h in i[0]:
                if h in dict_elem_h:
                    dict_elem_h[h].append(i[1])
                else:
                    dict_elem_h[h]=[i[1]]

    for n in [0, 1, 2]:
        for i in list(dict_elem_h.values())[0:3]:
            cell = f"cell_{n+1}"
            if cell in dict_elem_c:
                dict_elem_c[cell] = dict_elem_c[cell] + i[0+(3*n):3+(3*n)]
            else:
                dict_elem_c[cell]=i[0+(3*n):3+(3*n)]

    for n in [3, 4, 5]:
        for i in list(dict_elem_h.values())[3:6]:
            cell = f"cell_{n+1}"
            if cell in dict_elem_c:
                dict_elem_c[cell] = dict_elem_c[cell] + i[0+(3*(n-3)):3+(3*(n-3))]
            else:
                dict_elem_c[cell]=i[0+(3*(n-3)):3+(3*(n-3))]

    for n in [6, 7, 8]:
        for i in list(dict_elem_h.values())[6:9]:
            cell = f"cell_{n+1}"
            if cell in dict_elem_c:
                dict_elem_c[cell] = dict_elem_c[cell] + i[0+(3*(n-6)):3+(3*(n-6))]
            else:
                dict_elem_c[cell]=i[0+(3*(n-6)):3+(3*(n-6))]
    context = {
        "elem_call": dict_elem_c, 
        "elem_vertical": dict_elem_v,
        "elem_horizontal": dict_elem_h
    }

    return context

structure = get_structure(elem)
elem_call = structure['elem_call']
elem_vertical = structure['elem_vertical']
elem_horizontal = structure['elem_horizontal']
elem_vertical_list = list(elem_vertical.values())
elem_horizontal_list = list(elem_horizontal.values())
elem_call_list = list(elem_call.values())

# print(elem_vertical_list)
# print(elem_horizontal_list)
# print(elem_call_list)
h_index = 0
for row in elem_horizontal_list:
    current_numbers = numbers.copy()
    list_without_horizontal = differenc(current_numbers, row)
    list_without_vertical = differenc_2(list_without_horizontal, elem_vertical_list[h_index])
    list_without_cell = ""
    v_index = 0
    for value in row:
        if value == "":
            if h_index <= 2 and v_index <= 2:
                c =0
                print(c)
            elif h_index <= 2 and v_index <= 5:
                c =1
                print(c)
            elif h_index <= 2 and v_index <= 8:
                c =2
                print(c)

            elif h_index <= 5 and v_index <= 2:
                c =3
                print(c)
            elif h_index <= 5 and v_index <= 5:
                c =4
                print(c)
            elif h_index <= 5 and v_index <= 8:
                c =5
                print(c)
            elif h_index <= 8 and v_index <= 2:
                c =6
                print(c)
            elif h_index <= 8 and v_index <= 5:
                c =7
                print(c)
            elif h_index <= 8 and v_index <= 8:
                c =8
                print(c)
            list_without_cell = differenc_2(list_without_vertical, elem_call_list[c])
        v_index += 1
    h_index += 1

    print(list_without_cell)





