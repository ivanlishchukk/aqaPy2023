# Task0
my_note = ['add', 'earliest', 'latest', 'longest', 'shortest', 'Exit']
typo = 'add'
notes_list = []

for typo in my_note:
      print('Оберіть та напишіть потрібну команду із запропонованих: \n\t- add \n\t- earliest \n\t- latest '
            '\n\t- longest \n\t- shortest \n\t- Exit')
      typo = input()

      if typo == 'add':
            new_note = input('Введіть нотатку: ')
            notes_list.append(new_note)
            print(notes_list)

      elif typo == 'earliest':
            indexes_for_earliest_notes = sorted(range(len(notes_list)), key=lambda index: notes_list[index])
            earliest_notes_list = [notes_list[index] for index in indexes_for_earliest_notes]
            print(f"Від найновішої до найпізнішої: {earliest_notes_list}")

      elif typo == 'latest':
            indexes_for_earliest_notes = sorted(range(len(notes_list)), key=lambda index: notes_list[index])
            latest_notes_list = [notes_list[index] for index in indexes_for_earliest_notes]
            latest_notes_list.reverse()
            print(f"Від найпізнішої до найновішої: {latest_notes_list}")

      elif typo == 'longest':
            notes_list.sort(key=len, reverse = True)
            print(f"Від найдовшої до найкоротшоЇ: {notes_list}")

      elif typo == 'shortest':
            notes_list.sort(key=len)
            print(f"Від найкоротшої до найдовшої: {notes_list}")

      elif typo == 'Exit':
            print('Дкуємо, що обрали нашу програму')
            break

      else:
            print('Будь ласка, введіть коректну команду!')
