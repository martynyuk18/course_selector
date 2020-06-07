from time import sleep
import datetime
import requests
import algorithm
import pandas as pd

university_data = pd.read_csv('data.csv')

token = "1222655206:AAHVwvTlOofqmGjwxuMDwFuUbSPxc1Sym78"
url = "https://api.telegram.org/bot%s/"%(token)

def get_updates(request):
    params = {'timeout':100, 'offset':None}
    response = requests.get(request + 'getUpdates', data=params)
    return response.json()

def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def get_username(update):
    username = update['message']['chat']['username']
    return username

def get_first_name(update):
    first_name = update['message']['chat']['first_name']
    return first_name

def get_text(update):
    text = update['message']['text']
    return text

def send_mess(chat, text):
    params = {'chat_id':chat, 'text':text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

def greeting(name):
    now = datetime.datetime.now()
    hour = now.hour
    if 6 <= hour < 12:
        return 'Доброе утро, %s!'%(name)
    elif 12 <= hour < 17:
        return 'Добрый день, %s!'%(name)
    elif 17 <= hour < 23:
        return 'Добрый вечер, %s!'%(name)
    else:
        return 'Доброй ночи, %s!'%(name)

def main():
    update_id = last_update(get_updates(url))['update_id']
    while True:
        if update_id == last_update(get_updates(url))['update_id']:
            update = last_update(get_updates(url))
            chat_id = get_chat_id(last_update(get_updates(url))) 
            user_querry = get_text(update)
            rule = "\nВведите Ваши результаты как на примере снизу:\nматематика 70 русский язык 70 физика 70"
            if user_querry == "/start":
                try:
                    username = get_username(update)
                    greeting_message = greeting(username)
                    send_mess(chat_id, greeting_message + rule)
                except KeyError:
                    first_name = get_first_name(update)
                    greeting_message = greeting(first_name)
                    send_mess(chat_id, greeting_message + rule)
            else:
                # обрабатываем запрос
                output_result = algorithm.output(user_querry, university_data)
                if len(output_result) != 0:
                    for output_subject in output_result:
                        query = university_data.loc[university_data.program_spec == output_subject]
                        result_message = "%s\nСсылка: %s\nСтоимость - %s руб."%(output_subject, str(query.iloc[0, 6]), str(query.iloc[0, 7]))
                        send_mess(chat_id, result_message)
                else:
                    send_mess(chat_id, 'К сожалению по Вашим результатам нет подходящих направлений.')
            update_id += 1
        sleep(1)

if __name__ == '__main__':
    main()


