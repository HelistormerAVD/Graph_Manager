from PIL import Image as PILImage, ImageEnhance, ImageFilter

# TODO: Docstrings, (noch mehr) Inhalte (?)
'''
    - rotate, putalpha, paste (siehe Vorlesung 11 pillow)
    - "Strg+Z"-Funktion? "Strg+Y"-Operation?
        - vor/nach jeder Operation Bild in einer Liste speichern
        - `modified_image` und `history`-Liste aktualisieren
        - evtl. `history`-Liste ersetzen
'''


class Image:
    """ Klasse Image """

    def __init__(self, file_path):
        """ Konstruktor der Image-Klasse """
        self.file_path = file_path
        self.image = PILImage.open(file_path)  # Original-Version des Bildes
        self.modified_image = self.image.copy()  # Kopie des Bildes zum Bearbeiten
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
        self.update_history("brightness", factor)
        image_enhancer = ImageEnhance.Brightness(self.modified_image)
        self.modified_image = image_enhancer.enhance(factor)

    def reset(self):
        """ Bild auf Anfang/Original zurücksetzen """
        self.modified_image = self.image.copy()
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
    def set_image(self, image):
        """ bearbeitetes Bild 'überschreiben' """
        self.modified_image = image

    def get_image(self):
        """ bearbeitetes Bild zurückgeben """
        return self.modified_image

    # andere Funktionen bieten Möglichkeit zum Modifizieren des Bildes (Zuschneiden, Helligkeit, Filter, Größe)
    def modify_image(self, image):
        """ Sinnhaftigkeit der Funktion? """
        pass


if __name__ == "__main__":
    """ Beispiel zur Anwendung der Funktionen """
    img = Image("assets/moeve.jpg")
    img.resize(400, 400)
    img.adjust_brightness(1.5)
    img.apply_filter("SHARPEN")
    img.save("assets/moeve-modified.jpg")
    img.show()
