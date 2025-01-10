import graph
import image
import re
from PIL import Image as PILImage, ImageEnhance, ImageFilter
import matplotlib.pyplot as plt


class BDString:
    """ Klasse BDString """
    data = ""  # Sinnhaftigkeit?

    def __init__(self, text=""):  # default-Wert = leerer String
        """ Konstruktor der BDString-Klasse """
        self.data = text

    def replace(self, to_be_replaced, replace_with, case_sensitive=True):
        """ Ersetze alle Vorkommen von `to_be_replaced` mit `replace_with`, optional case-insensitiv """
        if case_sensitive:
            return self.data.replace(to_be_replaced, replace_with)
        else:
            return re.sub(re.escape(to_be_replaced), replace_with, self.data, flags=re.IGNORECASE)

    def replace_in_range(self, to_be_replaced, replace_with, start=0, end=None, case_sensitive=True):
        """ Ersetze alle Vorkommen von `to_be_replaced` mit `replace_with` zwischen `start` und `end`, optional case-insensitiv """
        end = end if end is not None else len(self.data)
        sub_content = BDString(self.data[start:end])
        replaced_sub = sub_content.replace(to_be_replaced, replace_with, case_sensitive)
        return self.data[:start] + replaced_sub + self.data[end:]

    def replace_word(self, to_be_replaced, replace_with, case_sensitive=True):
        """ Ersetze alle alleinstehenden Vorkommen von to_be_replaced (die nicht an alphanumerische Zeichen grenzen, sondern an Leerzeichen oder Sonderzeichen), optional case-insensitiv """
        pattern = r'\b' + re.escape(to_be_replaced) + r'\b'
        if case_sensitive:
            return re.sub(pattern, replace_with, self.data)
        else:
            return re.sub(pattern, replace_with, self.data, flags=re.IGNORECASE)

    def set_text(self, text):
        """ Text setzen/überschreiben """
        self.data = text

    def get_text(self):
        """ BDString zurückgeben """
        return self.__str__()

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
        self.data /= divisor
        return self.data

    def pow(self, exponent):
        self.data **= exponent
        return self.data

    def to_bd_string(self):
        return BDString(self.data.__str__())

    def __getstate__(self):
        return self.data

    def __str__(self):
        return str(self.data)


# TODO: Ergibt es Sinn, dass BDInteger von BDFloat erbt?
class BDInteger(BDFloat):
    """ Klasse BDInteger erbt von BDFloat """

    def __init__(self, data=0):
        """ Konstruktor der Klasse BDInteger """
        super().__init__(data)
        self.data = int(data)

    def add(self, summand=0):
        return int(BDFloat.add(self, summand))

    def subtract(self, subtrahend=0):
        return int(BDFloat.subtract(self, subtrahend))

    def multiply(self, factor=1):
        return int(BDFloat.multiply(self, factor))

    def divide(self, divisor=1):
        try:
            quotient = self.data // int(divisor)
            self.data = quotient
            return self.data
        except ZeroDivisionError:
            return self.data

    def pow(self, exponent=1):
        return int(BDFloat.pow(self, exponent))

    def modulo(self, num=0):
        self.data %= int(num)
        return self.data

    def to_bd_string(self):
        return BDFloat.to_bd_string(self)

    def __getstate__(self):
        return self.data

    def __str__(self):
        return str(self.data)


class BDImage:
    """ Klasse BDImage """
    data = image.Image("assets/moeve.jpg")

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
    data = graph.Graph([0], [0])
    pointsX = []
    pointsY = []
    graph = plt

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_graph(self):
        self.graph.xlabel("x")
        self.graph.ylabel("y")
        self.graph.title("Your Graph")
        self.graph.grid(True)
        self.graph.plot(self.x, self.y, label="first")
        self.graph.legend()
        self.graph.show()

    def get_graph(self):
        result_graph = self.graph.gca()
        return result_graph

    def modify_graph(self, x, y, label, x_label="x", y_label="y", title="Your Graph", grid=None):
        self.x = x
        self.y = y
        self.graph.xlabel(x_label)
        self.graph.ylabel(y_label)
        self.graph.title(title)
        self.graph.grid(grid)
        self.graph.plot(self.x, self.y, label=label)
        self.graph.legend()
        self.graph.show()

    def __getstate__(self):
        return self.data


if __name__ == '__main__':
    i = BDInteger(3)
    i.add(5)
    i.multiply(7)
    print(i)