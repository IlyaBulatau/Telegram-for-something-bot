from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def keyboard_for_some_choose() -> InlineKeyboardMarkup:
    callback_data_set = {
        "data1": "option1",
        "data2": "option2",
        "data3": "option3",
    }

    keyboard = [
        [
            InlineKeyboardButton(
                text="Option 1", callback_data=callback_data_set["data1"]
            ),
            InlineKeyboardButton(
                text="Option 2", callback_data=callback_data_set["data2"]
            ),
        ],
        [
            InlineKeyboardButton(
                text="Option 3", callback_data=callback_data_set["data3"]
            ),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup
