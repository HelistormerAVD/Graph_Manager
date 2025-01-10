import re


class Text:
    def __init__(self, content=""):
        self.content = content

    def replace(self, to_be_replaced, replace_with, case_sensitive=True):
        """ Ersetze alle Vorkommen von to_be_replaced mit replace_with, optional case-insensitiv """
        if case_sensitive:
            return self.content.replace(to_be_replaced, replace_with)
        else:
            return re.sub(re.escape(to_be_replaced), replace_with, self.content, flags=re.IGNORECASE)

    def replace_in_range(self, to_be_replaced, replace_with, start=0, end=None, case_sensitive=True):
        """ Ersetze alle Vorkommen von `to_be_replaced` mit `replace_with` zwischen `start` und `end`, optional case-insensitiv """
        end = end if end is not None else len(self.content)
        sub_content = Text(self.content[start:end])
        replaced_sub = sub_content.replace(to_be_replaced, replace_with, case_sensitive)
        return self.content[:start] + replaced_sub + self.content[end:]

    def replace_word(self, to_be_replaced, replace_with, case_sensitive=True):
        """ Ersetze alle alleinstehenden Vorkommen von to_be_replaced (die nicht an alphanumerische Zeichen grenzen, sondern an Leerzeichen oder Sonderzeichen), optional case-insensitiv """
        pattern = r'\b' + re.escape(to_be_replaced) + r'\b'
        if case_sensitive:
            return re.sub(pattern, replace_with, self.content)
        else:
            return re.sub(pattern, replace_with, self.content, flags=re.IGNORECASE)

    def set_content(self, content):
        """ Text setzen/überschreiben """
        self.content = content

    def get_content(self):
        """ Text zurückgeben """
        return self.__str__()

    def __str__(self):
        """ Text (auf der Konsole mit print()) ausgeben """
        return self.content


if __name__ == '__main__':
    bsp = "Hat hatte Hat-Trick hattrick that hat's hat hat."
    to_be_replaced = "hat"
    replace_with = "_"
    text = Text(bsp)
    # text.get_content()
    print(text)
    print(text.replace(to_be_replaced, replace_with))  # correcto
    print(text.replace_in_range(to_be_replaced, replace_with))  # falso
    print(text.replace_in_range(to_be_replaced, replace_with, case_sensitive=False))  # falso
    print(text.replace(to_be_replaced, replace_with, case_sensitive=False))  # correcto
    print(text.replace_in_range(to_be_replaced, replace_with, start=15, end=None, case_sensitive=False))  # falso
    print(text.replace_word(to_be_replaced, replace_with))  # correcto
    print(text.replace_word(to_be_replaced, replace_with, case_sensitive=False))  # correcto
