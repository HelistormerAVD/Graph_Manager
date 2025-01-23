# nützliche Hilfs-Funktionen.

def h_get_next_empty_dictionary(dictionary):
    a = dictionary.items().__len__()
    b = 0
    if a == 0:
        return 0
    for i in range(a):
        # print(a)
        b = i
        if not dictionary.get(i):
            return b
    return b + 1


def h_get_vector_between_points(x1, y1, x2, y2):
    return (x2 - x1), (y2 - y1)


def h_find_from_canvas_dict_obj(canvas_obj_id, dictionary, is_component):
    length = dictionary.__len__()


def h_convert_to_data_types_from_string(input_string: str):
    if str.isdigit(input_string):
        if input_string.find(".") > -1:
            return float(input_string)
        else:
            return int(input_string)
    else:
        return input_string


if __name__ == "__main__":
    print("Test einer Hilfs-Funktion")
    # ------------------

    werte = {}
    werte[0] = {"test": True, "zahl": 1, "vals": {}}
    werte[1] = {"test": True, "zahl": 1, "vals": {}}
    werte[2] = {"test": True, "zahl": 1, "vals": {}}
    werte[3] = {"test": True, "zahl": 1, "vals": {}}
    werte[4] = {"test": True, "zahl": 1, "vals": {}}
    # werte[5] = {"test": True, "zahl": 1, "vals": {}}
    # werte[6] = {"test": True, "zahl": 1, "vals": {}}
    out = h_get_next_empty_dictionary(werte)
    print(out)
