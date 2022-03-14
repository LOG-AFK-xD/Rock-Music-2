# @xmartperson

from pyrogram.types import InlineKeyboardButton


def song_markup(_, vidid):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["SG_B_2"],
                callback_data=f"song_helper audio|{vidid}",
            ),
            InlineKeyboardButton(
                text=_["SG_B_3"],
                callback_data=f"song_helper video|{vidid}",
            ),
        ],
        [
                InlineKeyboardButton("📨 Support", url=f"https://t.me/bLAZE_SUPPORT"),
                InlineKeyboardButton(
                    "Updates 📨", url=f"https://t.me/THE_BLAZE_NETWORK"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data="close"
            ),
        ],
    ]
    return buttons
