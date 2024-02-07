from data_manage import manageDataRegion, manageDataCategory
from keyboards import regions_inline_keyboard
from strings import category_string


def region_func(bot, call, name, tag):
    bot.answer_callback_query(call.id, name)
    user_id = call.from_user.id
    manageDataRegion(user_id, tag)


def category_self_func(bot, call, name, tag):
    bot.answer_callback_query(call.id, name)
    user_id = call.from_user.id
    manageDataCategory(user_id, tag)
    bot.send_message(call.message.chat.id,
                     category_string,
                     parse_mode='Markdown',
                     reply_markup=regions_inline_keyboard())
