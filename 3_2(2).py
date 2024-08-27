def send_email(message, recipient, sender="university.help@gmail.com"):
    if "@" not in (recipient or sender):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

    elif recipient.endswith('.ru') + recipient.endswith('.com') + recipient.endswith('.net') != True:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

    elif sender.endswith('.ru') + sender.endswith('.com') + sender.endswith('.net') != True:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

    else:
        if recipient == sender:
            print("Нельзя отправить письмо самому себе!")

        elif sender == "university.help@gmail.com":
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")

        elif sender != "university.help@gmail.com":
            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")



send_email('hi', 'university.help@gmail.com')
