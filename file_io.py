from tkinter import filedialog, messagebox
import tkinter as tk
import json


class FileIO:
    def __init__(self, root):
        """ Konstruktor der Klasse FileIO """
        self.root = root
        self.file_path = None

    def load_file(self):
        """ Öffnet den Dateiexplorer, um eine Datei zu laden und sie zu lesen """
        self.file_path = filedialog.askopenfilename(
            title="Datei laden",
            filetypes=[("Alle Dateien", "*.*"), ("JSON", "*.json"), ("Textdateien", "*.txt")]
        )

        if not self.file_path:
            return None  # wenn der Benutzer abbricht

        try:
            with open(self.file_path, "r") as file:
                if self.file_path.endswith(".json"):
                    data = json.load(file)
                else:
                    data = file.read()
            messagebox.showinfo("Erfolgreich geladen", f"Datei {self.file_path} wurde geladen")
            return data
        except FileNotFoundError as e:
            messagebox.showerror("Fehler", f"Datei konnte nicht gefunden werden")
            return None
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler beim Laden der Datei: {e}")
            return None

    @staticmethod
    def save_file(data):
        """ Öffnet den Dateiexplorer, um eine Datei mit dem Inhalt `data` zu speichern, ohne die geladene Datei zu überschreiben """
        save_path = filedialog.asksaveasfilename(
            title="Speichern unter",
            defaultextension=".txt",
            filetypes=[("Alle Dateien", "*.*"), ("JSON", "*.json"), ("Textdateien", "*.txt")]
        )

        if not save_path:
            return  # wenn der Benutzer abbricht, abbrechen

        try:
            with open(save_path, 'w') as file:
                if isinstance(data, dict):
                    json.dump(data, file, indent=4)
                else:
                    file.write(data)
            messagebox.showinfo("Erfolg", f"Datei gespeichert unter {save_path}")
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler beim Speichern der Datei: {e}")


if __name__ == '__main__':
    """ Anwendungsbeispiel für load_file und save_file Methoden """
    root = tk.Tk()
    root.withdraw()

    file_io = FileIO(root)

    content = file_io.load_file()
    if content:
        print(content)

    file_io.save_file("Test")  # öffnet den Dateiexplorer um eine Datei mit dem Inhalt "Test" zu speichern
