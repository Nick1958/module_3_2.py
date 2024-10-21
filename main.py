 ## Домашняя работа по уроку "Способы вызова функции", модуль 3_2

# 3.	Проверка на отправителя по умолчанию.

# def func_send_email(message, recipient, *, sender="university.help@gmail.com"):
#     print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
#
# # 2.	Проверка на отправку самому себе
#
#     if recipient != sender:
#         print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)
#
#     else:
#         print("Нельзя отправить письмо самому себе!")
#
# func_send_email(message=input("Введите сообщение"), recipient = str(input("Введите адрес")))
# func_send_email(message=input("Введите сообщение"), recipient=str(input("Введите адрес")), sender=str(input("Введите адрес")))


# # 1b. 	Проверка на корректность e-mail отправителя и получателя, содержание '.com' or '.ru' or '.net'
#
# def func_send_email(message, recipient, sender="university.help@gmail.com"):
#
#         if recipient.count('.com') and sender.count('.com') == 1 \
#             or recipient.count('.com') and sender.count('.ru')== 1 \
#             or recipient.count('.com') and sender.count('.net') \
#             or recipient.count('.ru') and sender.count('.com') == 1 \
#             or recipient.count('.ru') and sender.count('.ru') == 1 \
#             or recipient.count('.ru') and sender.count('.net') == 1 \
#             or recipient.count('.ru') and sender.count('.com') == 1 \
#             or recipient.count('.net') and sender.count('.ru') == 1 \
#             or recipient.count('.net') and sender.count('.net') == 1:
#         #    or recipient.count('@') and sender.count('@') == 1:
#
#             print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)
#
#         else:
#             print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
#
# func_send_email(message=input("Введите сообщение"), recipient=str(input("Введите адрес")), sender=str(input("Введите адрес")))

#  # вывод на консоль:
# Введите сообщение Пожалуйста, исправьте задание
# Введите адрес urban.student@mail.ru
# Введите адрес urban.teacher@mail.uk
# Невозможно отправить письмо с адреса  urban.teacher@mail.uk на адрес  urban.student@mail.ru
#
# Process finished with exit code 0


# # 1a. 	Проверка на корректность e-mail отправителя и получателя, на содержание "@"

# def func_send_email(message, recipient, sender="university.help@gmail.com"):
#
#        if recipient.count('@') and sender.count('@') == 1:
#           print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)
#
#        else:
#           print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
#
# func_send_email(message=input("Введите сообщение"), recipient=str(input("Введите адрес")), sender=str(input("Введите адрес")))

#  # вывод на консоль_1:
# Введите сообщение Пожалуйста, исправьте задание
# Введите адрес urban.student@mail.ru
# Введите адрес urban.teacher@mail.ru
# НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса  urban.teacher@mail.ru на адрес  urban.student@mail.ru
#
# Process finished with exit code 0

#  # вывод на консоль_2_без @  у отправителя:
# Введите сообщение Пожалуйста, исправьте задание
# Введите адрес urban.student@mail.ru
# Введите адрес urban.teacher.mail.ru
# Невозможно отправить письмо с адреса  urban.teacher.mail.ru на адрес  urban.student@mail.ru
#
# Process finished with exit code 0


