



def send_email(message, recipient, sender = "university.help@gmail.com"):
    if "@" not in (recipient or sender):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        exit()
    if recipient.endswith('.ru') + recipient.endswith('.com') + recipient.endswith('.net') != True:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        exit()
    if sender.endswith('.ru') + sender.endswith('.com') + sender.endswith('.net') != True:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        exit()
    else:
        if recipient == sender:
                print("Нельзя отправить письмо самому себе!")
                exit()
        if sender == "university.help@gmail.com":
                print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
                exit()
        if sender != "university.help@gmail.com":
            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
            exit()



send_email('hi', 'university.help@gmail.com')



