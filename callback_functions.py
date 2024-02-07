from data_manage import manage_data_region, manage_data_category, manage_data_category_org
from keyboards import regions_inline_keyboard, organized_inline_keyboard
from strings import category_string, regions_string


def region_func(bot, call, name, tag):
    bot.answer_callback_query(call.id, name)
    user_id = call.from_user.id
    manage_data_region(user_id, tag)


def category_self_func(bot, call, name, tag):
    bot.answer_callback_query(call.id, name)
    user_id = call.from_user.id
    manage_data_category(user_id, tag)
    bot.send_message(call.message.chat.id,
                     regions_string,
                     parse_mode='Markdown',
                     reply_markup=regions_inline_keyboard())


def category_org_func(bot, call, name, tag):
    bot.answer_callback_query(call.id, name)
    user_id = call.from_user.id
    manage_data_category_org(user_id, tag)
    bot.send_message(call.message.chat.id,
                     category_string,
                     parse_mode='Markdown',
                     reply_markup=organized_inline_keyboard())
