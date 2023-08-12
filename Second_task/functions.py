import Note

def show_notes(dictionary_of_notes: dict) -> None:
    if len(dictionary_of_notes) != 0:
        for n in dictionary_of_notes:
            print(dictionary_of_notes[n])
        chose = int(input(
            '\n1. Открыть заметку'
            '\n2. Удалить заметку'
            '\n3. Редактировать заметку'
            '\n4. На уровень выше\n'))

        if chose == 1:
            dictionary_of_notes[int(
                input('Введи id заметки: '))].display_info()
            print("-------------------")

        elif chose == 2:
            del_id = int(input('Введи id заметки:\n'))
            dictionary_of_notes[del_id].del_note('test.json')
            # del dictionary_of_notes[int(input('Введи id заметки:\n'))]

        elif chose == 3:
            dictionary_of_notes[int(input('Введи id заметки: '))].edit_note()

        else:
            pass
    else:
        print("-------------------")
        print("Заметки отсутствуют")
        print("-------------------")


# def save_note(note):
#     file_name = input("Введите имя файла для сохранения: ") + ".json"
#     with open(file_name, 'a', encoding='utf-8') as outfile:
#             # outfile.seek(0)
#         json.dump(note.to_string(), outfile, ensure_ascii=False)
#         json.dump('\n', outfile)
#           # return note
#     outfile.close
