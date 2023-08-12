import datetime
import json


class Note:
    id = 0

    def __init__(self):
        Note.id += 1
        self.id = Note.id
        self.title = self.add_title()
        self.content = self.add_content()
        self.current_date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M") #str(datetime.date.today())

    def display_info(self):
        print(f"\nid: {self.id} title: {self.title}\ncontent: {self.content}\nDate: {self.current_date}")

    def add_title(self):
        title1 = input("Введите заголовок заметки: ")
        return title1

    def add_content(self):
        content1 = input("Введите содержание заметки: ")
        return content1

    # def save_note(note):
    #     file_name = input("Введите имя файла для сохранения: ") + ".json"
    #     with open(file_name, 'w') as outfile:
    #         json.dump(note.__dict__, outfile)
    #     return note

    def save_note(note):
        file_name = input("Введите имя файла для сохранения: ") + ".json"
        with open(file_name, 'a', encoding='utf-8') as outfile:
            # outfile.seek(0)
            # json.dump(note.to_string(), outfile, ensure_ascii=False)
            json.dump(note.__dict__, outfile)
            # json.dump('\n', outfile)
          # return note
        outfile.close
        return file_name  # возвращаем название файла

    def del_note(note, file_name):
        with open(file_name, 'r', encoding='utf-8') as f_json:
            # outfile.seek(0)
            data = json.load(f_json)
            print(data)
            print(note.id)
            # del data[note.id]
        #     with open(file_name, 'w', encoding='utf-8') as f_json:
        #         json.dump(data, f_json)
        # f_json.close


    def edit_note(self):
        self.title = self.add_title()
        self.content = self.add_content()
        self.current_date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

    def __str__(self):
        return 'ID: ' + str(self.id) + ' Title: ' + self.title + ' Date: ' + self.current_date

    def to_string(self):
        return str(self.id) + '; ' + self.title + '; ' + self.content + '; ' + str(self.current_date)

    # def update_note(self, title=None, body=None, created_at=None, updated_at=None):
    #     if title is not None:
    #         self.title = title
    #     if body is not None:
    #         self.body = body
    #     if created_at is not None:
    #         self.created_at = created_at
    #     if updated_at is not None:
    #         self.updated_at = updated_at

    # def save_note():
    #     file_name = input("\nВведите имя файла для сохранения: ") + ".json"
    #     with open(file_name, 'w') as file:
    #         file.write(json.dump(Note))

    # data = list()
    # data.append(self.title, self.id, self.content, self.data)
    # with open('note.txt', 'w') as outfile:
    #     json.dump(data, outfile)
