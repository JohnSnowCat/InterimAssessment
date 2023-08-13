import datetime
import json


class Note:
    id = 0

    def __init__(self):
        Note.id += 1
        self.id = Note.id
        self.title = self.add_title()
        self.content = self.add_content()
        self.current_date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

    def display_info(self):
        print(f"\nid: {self.id} title: {self.title}\ncontent: {self.content}\nDate: {self.current_date}")

    def add_title(self):
        title1 = input("Введите заголовок заметки: ")
        return title1

    def add_content(self):
        content1 = input("Введите содержание заметки: ")
        return content1

    def save_note(note):
        file_name = input("Введите имя файла для сохранения: ") + ".json"
        with open(file_name, 'a', encoding='utf-8') as outfile:
            json.dump(note.to_string(), outfile, ensure_ascii=False)
            json.dump('\n', outfile)
        outfile.close

    def edit_note(self):
        self.title = self.add_title()
        self.content = self.add_content()
        self.current_date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

    def __str__(self):
        return 'ID: ' + str(self.id) + ' Title: ' + self.title + ' Date: ' + self.current_date

    def to_string(self):
        return str(self.id) + '; ' + self.title + '; ' + self.content + '; ' + str(self.current_date)
