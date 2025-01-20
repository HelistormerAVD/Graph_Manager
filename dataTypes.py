import re
from PIL import Image as PILImage, ImageEnhance, ImageFilter
import matplotlib.pyplot as plt



#---------IDs for DataTypes------------
#   0 = BDInteger
#   1 = BDFloat
#   2 = BDString
#   3 = BDList (falls wir list machen wollen)
#   4 = BDGraph
#   5 = BDImage
#--------------------------------------

class BDString:
    """ Klasse BDString """
    data = ""  # Sinnhaftigkeit?

    def __init__(self, text=""):  # default-Wert = leerer String
        """ Konstruktor der BDString-Klasse """
        self.data = str(text)

    def replace(self, to_be_replaced, replace_with, case_sensitive=True):
        """ Ersetze alle Vorkommen von `to_be_replaced` mit `replace_with`, optional case-insensitiv """
        to_be_replaced = str(to_be_replaced)
        replace_with = str(replace_with)
        if case_sensitive:
            return self.data.replace(to_be_replaced, replace_with)
        else:
            return re.sub(re.escape(to_be_replaced), replace_with, self.data, flags=re.IGNORECASE)

    def replace_in_range(self, to_be_replaced, replace_with, start=0, end=None, case_sensitive=True):
        """ Ersetze alle Vorkommen von `to_be_replaced` mit `replace_with` zwischen `start` und `end`, optional case-insensitiv """
        to_be_replaced = str(to_be_replaced)
        replace_with = str(replace_with)
        end = end if end is not None else len(self.data)
        sub_content = BDString(self.data[start:end])
        replaced_sub = sub_content.replace(to_be_replaced, replace_with, case_sensitive)
        return self.data[:start] + replaced_sub + self.data[end:]

    def replace_word(self, to_be_replaced, replace_with, case_sensitive=True):
        """ Ersetze alle alleinstehenden Vorkommen von to_be_replaced (die nicht an alphanumerische Zeichen grenzen, sondern an Leerzeichen oder Sonderzeichen), optional case-insensitiv """
        to_be_replaced = str(to_be_replaced)
        replace_with = str(replace_with)
        pattern = r'\b' + re.escape(to_be_replaced) + r'\b'
        if case_sensitive:
            return re.sub(pattern, replace_with, self.data)
        else:
            return re.sub(pattern, replace_with, self.data, flags=re.IGNORECASE)

    def concat(self, s):
        """ konkateniert den BDString mit s """
        return self.data + str(s)

    def find(self, s):
        """ gibt den Start-Index des ersten Vorkommens von s im BDString zurück """
        return BDInteger(self.data.find(str(s)))

    def split(self, s):
        """ splittet den BDString an allen Vorkommen von s und gibt eine BDList zurück """
        return BDList(self.data.split(str(s)))

    def trim(self):
        """ trimmt den BDString """
        return self.data.strip()

    def set_text(self, text):
        """ Text setzen/überschreiben """
        self.data = BDString(text)

    def get_text(self):
        """ BDString zurückgeben """
        return self.__getstate__()

    def __str__(self):
        """ print-Methode/Text (auf der Konsole mit print()) ausgeben """
        return self.data

    # TODO: Unterschied __getstate__ und __str__ ???
    def __getstate__(self):
        return self.data


class BDFloat:  # umbenannt, da es double in (Standard-)Python nicht gibt
    """ Klasse BDFloat """

    def __init__(self, data=1.0):
        """ Konstruktor der Klasse BDFloat """
        self.data = float(data)

    def add(self, summand):
        self.data += summand
        return self.data

    def subtract(self, subtrahend):
        self.data -= subtrahend
        return self.data

    def multiply(self, factor):
        self.data *= factor
        return factor

    def divide(self, divisor):
        try:
            self.data /= divisor
            return self.data
        except ZeroDivisionError:
            return self.data  # TODO: welchen Wert sinnvoll zurückgeben?

    def pow(self, exponent):
        self.data **= exponent
        return self.data

    def to_bd_string(self):
        return BDString(self.data.__str__())

    def __getstate__(self):
        return self.data

    def __str__(self):
        return str(self.data)


class BDInteger:
    """ Klasse BDInteger """

    def __init__(self, data : int):
        """ Konstruktor der Klasse BDInteger """
        self.data = int(data)

    def add(self, summand : int):
        self.data += summand
        return self.data

    def subtract(self, subtrahend=0):
        self.data -= int(subtrahend)
        return self.data    # int(BDFloat.subtract(self, subtrahend))

    def multiply(self, factor=1):
        self.data *= int(factor)
        return self.data    # int(BDFloat.multiply(self, factor))

    def divide(self, divisor=1):
        try:
            quotient = self.data // int(divisor)
            self.data = quotient
            return self.data
        except ZeroDivisionError:
            return 0

    def pow(self, exponent=1):
        self.data **= exponent
        return self.data    # int(BDFloat.pow(self, exponent))

    def modulo(self, num=0):
        self.data %= int(num)
        return self.data

    def to_bd_string(self):
        return BDFloat.to_bd_string(self)

    def __getstate__(self):
        return self.data

    def __str__(self):
        return str(self.data)


class BDList:

    """ Klasse BDList """
    data = list()

    def __init__(self, data=None):  # default-Wert = leerer String
        """ Konstruktor der BDList-Klasse """
        if data is None:
            data = list()
        self.data = list(data)

    def append(self, elem):
        """ fügt elem an das Ende der BDList an """
        return self.data.append(elem)

    def clear(self):
        """ entfernt alle Elemente der BDList """
        return self.data.clear()

    def copy(self):
        """ gibt eine Kopie der BDList zurück """
        return self.data.copy()

    def count(self, elem):
        """ zählt die Vorkommen von elem in der BDList """
        return self.data.count(elem)

    def extend(self, data):
        """ hängt die Elemente der BDList data an self.data an """
        return self.data.extend(data)

    def index(self, elem):
        """ gibt den Index des ersten Vorkommens von elem in der BDList aus """
        return self.data.index(elem)

    def insert(self, pos, elem):
        """ fügt elem an der Position pos in die BDList ein """
        return self.data.insert(pos, elem)

    def pop(self, pos):
        """ entfernt das Element an Position pos aus der BDList und gibt es aus """
        return self.data.pop(pos)

    def remove(self, elem):
        """ entfernt das erste Vorkommen von elem aus der BDList """
        return self.data.remove(elem)

    def reverse(self):
        """ stellt die BDList auf den Kopf """
        return self.data.reverse()

    def sort(self):
        return self.data.sort()

    def set_list(self, data):
        """ Liste setzen/überschreiben """
        self.data = BDList(data)

    def get_list(self):
        """ BDList zurückgeben """
        return self.__getstate__()

    def __str__(self):
        """ print-Methode/Text (auf der Konsole mit print()) ausgeben """
        return self.data

    def __getstate__(self):
        return self.data


class BDImage:
    """ Klasse BDImage """

    def __init__(self, file_path):
        """ Konstruktor der Image-Klasse """
        self.file_path = file_path
        self.data = PILImage.open(file_path)  # Original-Version des Bildes
        self.modified_image = self.data.copy()  # Kopie des Bildes zum Bearbeiten
        self.history = []  # Liste angewandter Operationen

    def save(self, file_path):
        """ Bild unter {file_path} speichern """
        self.modified_image.save(file_path)

    def resize(self, width, height):
        """ Größe des Bildes verändern """
        self.update_history("resize", (width, height))
        self.modified_image = self.modified_image.resize((width, height))

    def crop(self, left, top, right, bottom):
        """ Bild zuschneiden """
        self.update_history("crop", (left, top, right, bottom))
        self.modified_image = self.modified_image.crop((left, top, right, bottom))

    def apply_filter(self, filter_type):
        """ Filter auf das Bild anwenden (BLUR, CONTOUR, SHARPEN) """
        self.update_history("filter", filter_type)
        match filter_type:
            case "BLUR":
                self.modified_image = self.modified_image.filter(ImageFilter.BLUR)
            case "CONTOUR":
                self.modified_image = self.modified_image.filter(ImageFilter.CONTOUR)
            case "SHARPEN":
                self.modified_image = self.modified_image.filter(ImageFilter.SHARPEN)
            case _:
                self.history.pop()  # zuvor in `history`-Liste eingefügten Eintrag wieder entfernen
                raise ValueError(f"Filter-Typ {filter_type} nicht bekannt")

    def adjust_brightness(self, factor):
        """ Helligkeit um `factor` anpassen """
        self.update_history("brightness", factor)
        image_enhancer = ImageEnhance.Brightness(self.modified_image)
        self.modified_image = image_enhancer.enhance(factor)

    def reset(self):
        """ Bild auf Anfang/Original zurücksetzen """
        self.modified_image = self.data.copy()
        self.history.clear()  # Einträge der `history`-Liste löschen

    def get_size(self):
        """ Höhe und Breite des Bildes ausgeben """
        return self.modified_image.size

    def show(self):
        """ Bild anzeigen """
        self.modified_image.show()

    def update_history(self, operation, arguments):
        """ Fügt einen Tupel-Eintrag der angewandten Operation + Argumente in die `history`-Liste ein """
        self.history.append((operation, arguments))

    # die nachfolgenden Funktionen sind evtl. überflüssig
    def set_image(self, data):
        """ bearbeitetes Bild 'überschreiben' """
        self.modified_image = data

    def get_image(self):
        """ bearbeitetes Bild zurückgeben """
        return self.modified_image

    def __getstate__(self):
        return self.data


class BDGraph:
    """ Klasse BDGraph """
    points_x = []
    points_y = []
    graph = plt

    def __init__(self):
        self.points_x = []
        self.points_y = []

    def insert_lists(self, x, y):
        self.points_x = x
        self.points_y = y

    def set_graph(self):
        self.graph.xlabel('x')
        self.graph.ylabel('y')
        self.graph.title('Your Graph')
        self.graph.grid(True)
        self.graph.plot(self.points_x, self.points_y, label="first")
        self.graph.legend()
        self.graph.show()

    def get_graph(self):
        get_graph = self.graph.gca()
        return get_graph

    def modify_graph(self, x, y, xlabel, ylabel, title, grid, label):
        self.points_x = x
        self.points_y = y
        self.graph.xlabel(xlabel if xlabel else "x")
        self.graph.ylabel(ylabel if ylabel else "y")
        self.graph.title(title if title else "Your Graph")
        if grid is not None:
            self.graph.grid(grid)
        self.graph.plot(self.points_x, self.points_y, label=label)
        self.graph.legend()
        self.graph.show()

    def __getstate__(self):
        return self.graph


if __name__ == '__main__':
    i = BDInteger(3)
    i.add(5)
    i.multiply(7)
    print(i)

    number = BDInteger(324732895)
    x = number.__getstate__()
    if isinstance(x, int):
        print(x)
