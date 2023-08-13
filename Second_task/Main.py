from Note import Note
import functions

list_notes = {}

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
        list_notes[note.id] = note
        save = input('Сохранить заметку? (Y/N)')
        if save.lower().startswith('y'):
            list_notes[note.id].save_note()
            print("\n-----------------------")
            print("Заметка успешно создана")
            print("-----------------------")
        else:
            del list_notes[note.id]

    elif (select == 2):
        functions.show_notes(list_notes)

    elif select == 3:
        break
    else:
        print('Выберите корректное действие')
