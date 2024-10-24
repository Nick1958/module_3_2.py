 ## Домашняя работа по уроку "Способы вызова функции", модуль 3_2

def func_send_email(message, recipient, *, sender="university.help@gmail.com"):
    variants = ('.com', '.ru', '.net')
    if not (recipient.endswith(variants) and sender.endswith(variants) and recipient.count('@') == 1 and sender.count('@') == 1):
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)

func_send_email(message='Это сообщение для проверки связи', recipient = 'vasyok1337@gmail.com')
func_send_email(message='Вы видите это сообщение как лучший студент курса!', recipient = 'urban.fan@mail.ru', sender='urban.info@gmail.com')
func_send_email(message='Пожалуйста, исправьте задание', recipient = 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
func_send_email(message='Напоминаю самому себе о вебинаре', recipient = 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
