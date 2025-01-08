import json


class FileIO:
    def __init__(self, file=None):
        self.file = file

    def load_file(self, file_path):
        """ Lädt eine Datei """
        try:
            with open(self.file, 'r') as f:
                if file_path.endswith('.json'):
                    data = json.load(f)
                else:
                    data = f.read()
                return data
        except Exception as e:
            print(f"Fehler beim Laden der Datei: {e}")
            return None

    @staticmethod
    def save_file(data, file_path):
        """ Speichert Daten in einer Datei """
        try:
            with open(file_path, 'w') as f:
                if isinstance(data, dict):
                    json.dump(data, f, indent=4)
                else:
                    f.write(data)
            print(f"Datei gespeichert unter: {file_path}")
        except Exception as e:
            print(f"Fehler beim Speichern der Datei: {e}")


if __name__ == '__main__':
    file_io = FileIO()
    data = file_io.load_file("assets/hallo.txt")
    print(data)
    file_io.save_file("adflasdfhldfdlkf", "assets/hallo.txt")
