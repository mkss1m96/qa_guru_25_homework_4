import datetime

# 1)Создаем словарь email
email = {
    "subject": "Project collaboration",
    "from": " Partner@orgaNization.org ",
    "to": "Lead_dev@iclUd.com ",
    "body": "Hello,\nWe are interested in a partnership.\tPlease reply soon.\nRegards,\nTeam",
}

# Создаем переменную send_date и записываем ее в словарь email
send_date = datetime.datetime.now().strftime("%Y-%m-%d")
email["date"] = send_date

# Нормализуем адрес в словаре
email["from"] = email["from"].strip().lower()
email["to"] = email["from"].strip().lower()

# Извлекаем логин и домен отправителя
login, domain = email["from"].split("@")

# Создаём сокращенную версию текста
email["short_body"] = email["body"][0:9] + "..."

# Создаём списки доменов
all_personal_domains = ['gmail.com', 'list.ru', 'yahoo.com', 'outlook.com', 'hotmail.com', 'icloud.com', 'yandex.ru',
                        'mail.ru', 'list.ru', 'bk.ru', 'inbox.ru']
all_corporate_domains = ["company.ru", "corporation.com", "university.edu", "organization.org", "company.ru",
                         "business.net", ]

personal_domains = list(set(all_personal_domains))

corporate_domains = list(set(all_corporate_domains))

# Проверяем на отсутствие пересечений в списках доменов
intersection = list(set(personal_domains).intersection(set(corporate_domains)))
assert intersection == []

# Проверяем корпоративность отправителя
is_corporate = domain in corporate_domains

# Собираем чистый текст
email["clean_body"] = email["body"].replace("\n", " ").replace("\t", " ")

# Формируем письмо
email["sent_text"] = f"""Кому:{email["to"]}, От:{email["from"]}',
                         Тема:{email["subject"]}, Дата:{email["date"]}',
                         {email["clean_body"]}"""

# Рассчитаем кол-во страниц для печати
pages = len(email["sent_text"]) + 499

# Проверка на пустоту
is_subject_empty = not(email["subject"].strip( ))
is_body_empty = not(email["subject"].strip( ))

# Маскирование email
email["masked_from"] = login[:2] + "***@" + domain

# Удаление доменов
personal_domains.remove("list.ru")
personal_domains.remove("bk.ru")

print(email)
print(is_corporate, pages, is_subject_empty, is_body_empty)
print(personal_domains)
