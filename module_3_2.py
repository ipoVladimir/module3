# Задача "Рассылка писем":
# Часто при разработке и работе с рассылками писем(e-mail) они отправляются от одного и того же пользователя(администрации или службы поддержки). Тем не менее должна быть возможность сменить его в редких случаях.
# Попробуем реализовать функцию с подробной логикой.
#
# Создайте функцию send_email, которая принимает 2 обычных аргумента: сообщение и получатель и 1 обязательно именованный аргумент со значением по умолчанию - отправитель.
# Внутри функции реализовать следующую логику:
#
#     Проверка на корректность e-mail отправителя и получателя.
#     Проверка на отправку самому себе.
#     Проверка на отправителя по умолчанию.
#
# Пункты задачи:
#
#     Создайте функцию send_email, которая принимает 2 обычных аргумента: message(сообщение), recipient(получатель) и 1 обязательно именованный аргумент со значением по умолчанию sender = "university.help@gmail.com".
#     Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net", то вывести на экран(в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
#     Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"
#     Если же отправитель по умолчанию - university.help@gmail.com, то вывести сообщение: "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
#     В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>."
#     Здесь <sender> и <recipient> - значения хранящиеся в этих переменных.
#     За один вызов функции выводится только одно и перечисленных уведомлений! Проверки перечислены по мере выполнения.
#
#
# Пример результата выполнения программы:
# Пример выполняемого кода (тесты):
# send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
# send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
# send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
# send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
# Вывод на консоль:
# Письмо успешно отправлено с адреса university.help@gmail.com на адрес vasyok1337@gmail.com
# НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса urban.info@gmail.com на адрес urban.fan@mail.ru
# Невозможно отправить письмо с адреса urban.teacher@mail.uk на адрес urban.student@mail.ru
# Нельзя отправить письмо самому себе!
#
# Примечания:
#
#     Обязательно именованные аргументы отделяются от остальных символом "*" перед ними.
#     Именованные аргументы всегда идут после позиционных.

def send_email(message='', recipient='', *, sender = "university.help@gmail.com"):
    # Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net",
    # то вывести на экран(в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
    email_symbol = '@'
    email_postfix = {'.com', '.ru', '.net'}
    email_postfix_delim = '.'
    recipient.lower()
    sender.lower()
    recipient_end, sender_end = '', ''
    if recipient.rfind(email_postfix_delim)>-1:
        recipient_end = recipient[recipient.rfind(email_postfix_delim):]
    if sender.rfind(email_postfix_delim)>-1:
        sender_end = sender[sender.rfind(email_postfix_delim):]

    if (email_symbol not in recipient or email_symbol not in sender or recipient_end not in email_postfix or
            sender_end not in email_postfix):
        print(f"Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}>")
    # Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    # Если же отправитель по умолчанию - university.help@gmail.com, то вывести сообщение: "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса <{sender}> на адрес <{recipient}>")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <{sender}> на адрес <{recipient}>")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')


