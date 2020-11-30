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
                dict_elem_c[cell].append(i[0+(3*n):3+(3*n)])
            else:
                dict_elem_c[cell]=[i[0+(3*n):3+(3*n)]]

    for n in [3, 4, 5]:
        for i in list(dict_elem_h.values())[3:6]:
            cell = f"cell_{n+1}"
            if cell in dict_elem_c:
                dict_elem_c[cell].append(i[0+(3*(n-3)):3+(3*(n-3))])
            else:
                dict_elem_c[cell]=[i[0+(3*(n-3)):3+(3*(n-3))]]

    for n in [6, 7, 8]:
        for i in list(dict_elem_h.values())[6:9]:
            cell = f"cell_{n+1}"
            if cell in dict_elem_c:
                dict_elem_c[cell].append(i[0+(3*(n-6)):3+(3*(6-3))])
            else:
                dict_elem_c[cell]=[i[0+(3*(n-3)):3+(3*(n-3))]]
    context = {
        "elem_call": dict_elem_c, 
        "elem_vertical": dict_elem_v,
        "elem_horizontal": dict_elem_h
    }

    return context
