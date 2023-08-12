from Note import Note
import functions

# list_notes = []
list_notes = {}
file_path = ''

while True:
    print(
        '\nВыберите желаемое действие:\n'
        '1. Добавить заметку\n'
        '2. Посмотреть все заметки\n'
        '3. Выход')
    select = int(input('\nВаш выбор: '))
    print()
    if select == 1:
        note = Note()
        # list_notes.append(note)
        list_notes[note.id] = note
        # first.save_note()
        save = input('Сохранить заметку? (Y/N)')
        if save.lower().startswith('y'):
            print('Yes!')
            file_path = list_notes[note.id].save_note()
            print("\n-----------------------")
            print("Заметка успешно создана")
            print("-----------------------")
        else:
            del list_notes[note.id]

    elif (select == 2):
        ## for n in list_notes:  //list
        ##     n.display_info()  //list
        # if len(list_notes) != 0:
        #     for n in list_notes:
        #         print(list_notes[n])
        #     chose = int(input("\n1. Открыть заметку, 2. Удалить заметку, 3.Редактировать заметку, 4. На уровень выше\n"))
        #     if chose == 1:
        #         list_notes[int(input('Введи id заметки: '))].display_info()
        #         print("-------------------")
        #     elif chose == 2:
        #         del list_notes[int(input('Введи id заметки:\n'))]
        #     elif chose == 3:
        #         list_notes[int(input('Введи id заметки: '))].edit_note()
        #     else:
        #         pass
        # else:
        #     print("-------------------")
        #     print("Заметки отсутствуют")
        #     print("-------------------")
        functions.show_notes(list_notes)

    elif select == 3:
        break
    else:  # (select == 4):
        break
