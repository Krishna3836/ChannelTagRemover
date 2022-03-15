from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):



    START_TEXT = """
Hey {} 

I am Instant Forward Tag Remover Bot

Made With 💕 By @NaysaBots
"""
    HELP_TEXT = """
Recommended
➠ Just Make Me admin in that Channel Where you want to remove tag and see magic
"""
    ABOUT_TEXT = """
 **🤖 Bot :** Instant-Tag-Remover\n
 **👲 Developer :** [Tellybots](https://telegram.me/tellybots)\n
 **👥 Channel :** [Tellybots](https://telegram.me/tellybots)\n
 **❄️ Credits :** Everyone in this journey\n
 **🍴 Source :** [Click here](https://t.me/tellybots_digital)\n
 **📝 Language :** [Python3](https://python.org)\n
 **📚 Library :** [Pyrogram v1.2.20](https://pyrogram.org)\n
 **🌟 Server :** [Heroku](https://heroku.com)\n
"""
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('❔ Help', callback_data='help'),
        InlineKeyboardButton('👲 About', callback_data='about')
        ],[
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('👲 About', callback_data='about'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('❔ Help', callback_data='help'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
