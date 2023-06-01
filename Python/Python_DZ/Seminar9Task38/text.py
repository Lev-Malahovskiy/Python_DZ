main_menu = '''\nГлавное меню:
    1. Открыть файл
    2. Сохранить файл
    3. Показать контакты
    4. Добавить контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход\n'''

input_choice = 'Выберите пункт меню: '

load_successful = 'Телефонная книга успешно открыта!'
save_successful = 'Телефонная книга успешно сохранена!'

pb_empty = 'Телефонная книга пуста или не загружена!'

input_new_contact = 'Введите данные нового контакта: '
new_contact = {'name': 'Введите имя: ',
               'phone': 'Введите номер телефона: ',
               'comment': 'Введите комментарий: '}

def new_contact_successful(name: str):
    return f'Контакт {name} успешно добавлен'

input_search = 'Что будем искать: '

def empty_search(word) -> str:
    return f'Контакты содержащие слово "{word}" не найдены'

input_change = 'Какой контакт будем менять: '
input_index = 'Введите индекс контакта: '

change_contact = 'Введите новые данные или оставьте поле пустым, чтоб не менять: '

def change_successful(name: str) -> str:
    return f'Контакт {name} успешно изменен!'

input_delete = 'Какой контакт будем удалять? Введите слово для поиска: '
input_index_delete = 'Ведите индекс контакта для удаления: '

def delete_confirm(name: str):
    return f'\nВы уверены, что хотите удалить контакт "{name}" (Y/N)?: '

def delete_success(name: str):
    return f'Контакт "{name}" успешно удален!'