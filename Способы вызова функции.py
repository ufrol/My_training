a = ('@', '.com', '.ru', '.net')


def send_email(message, recipient, sender="sender = 'urban.info@gmail.com'", sender_u='university.help@gmail.com'):
    global a

    rec_send_0 = "Невозможно отправить письмо с адреса", (sender), "на адрес", (recipient)
    rec_send_1 = "Письмо успешно отправлено с адреса", (sender), "на адрес", (recipient)
    rec_send_2 = "Нельзя отправить письмо самому себе!"
    rec_send_3 = "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", (sender), "на адрес", (recipient)

    if '@' in recipient and '@' in sender:
        print(message)
    else:
        print(message)
        print(*rec_send_0)
        return
    if recipient.endswith(a) and sender.endswith(a):
        print()
    else:
        print(*rec_send_0)
        return
    if (recipient) == (sender):
        print(*rec_send_2)
        return
    if (sender_u) == 'university.help@gmail.com':
        print(*rec_send_1)
    else:
        print(*rec_send_3)
    return

# send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com', sender = 'sender = university.help@gmail.com', sender_u = 'university.help@gmail.com')

# send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender = 'sender = urban.info@gmail.com', sender_u = 'university.help@gmail.com')

# send_email('Пожалуйста, исправьте задание', 'urban.studentп"@"mail.ru', sender = "urban.teacher@mail.uk")

# send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender = 'urban.teacher@mail.ru')
