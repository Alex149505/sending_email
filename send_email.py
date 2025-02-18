import logging
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()
LOGIN=os.getenv('LOGIN')
PASSWORD=os.getenv('PASSWORD')
recipient_name = "Петр"
sender_name = "Александр"
website_link = "https://dvmn.org/profession-ref-program/id507018210/DLO5k/"
sender_email = "alexandarvarfolomeev@yandex.ru"
recipient_email = "alex1995599105@gmail.com"

letter = """From: {sender_email}
To: {recipient_email} 
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

Привет, {0}! {1} приглашает тебя на сайт {2}!

{2} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {2}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 

Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {2}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл""".format(recipient_name, sender_name, website_link, sender_email = sender_email, recipient_email = recipient_email)
letter = letter.encode("UTF-8")
server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(LOGIN, PASSWORD)
server.sendmail(sender_email, recipient_email, letter)
server.quit()


