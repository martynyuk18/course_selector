import telegram

def display_buttons():
    buttons_list = [[telegram.InlineKeyboardButton(text='Скидка 70%', callback_data='disc70'),
                    telegram.InlineKeyboardButton(text='Скидка 50%', callback_data='disc50'),
                    telegram.InlineKeyboardButton(text='Скидка 25%', callback_data='disc25')]]
    telegram.ReplyKeyboardMarkup(buttons_list)

def apply_discount(cost, size):
    #size = update.callbabck_query.data
    if size == 'disc70':
        return cost*0.7
    if size == 'disc50':
        return cost*0.5
    if size == 'disc25':
        return cost*0.25

def buttons_info():
    return """Вы можете выбрать размер скидки при определенных условиях:
    ?0% скидка предоставляется призерам и победителям олимпиады 'Высшая проба', по предметам не входящие в Перечень Минобрнауки.
    50% скидка предоставляется участникам заключительного этапа Всероссийской олимпиады школьников.
    25% скидка предоставляется победителям и призерам региональных этапов Всероссийской олимпиады школьников.
    Если любое из условий соблюдается кликните на соотвествующую кнопу со скидкой, и цена за направления будет перерасчитана."""
