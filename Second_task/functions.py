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
            del dictionary_of_notes[int(input('Введи id заметки:\n'))]

        elif chose == 3:
            dictionary_of_notes[int(input('Введи id заметки: '))].edit_note()

        else:
            pass
    else:
        print("-------------------")
        print("Заметки отсутствуют")
        print("-------------------")
        