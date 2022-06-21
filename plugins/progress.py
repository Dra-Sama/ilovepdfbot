# fileName : plugins/progress.py
# copyright ©️ 2021 nabilanavab

import time, math
from pyrogram.types import Message
from pyrogram import Client, filters
from plugins.fileSize import get_size_format as gSF
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

#--------------->
#--------> DOWNLOAD PROGRESS
#------------------->

reply_markup = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton("⟨ Cancel ⟩", callback_data="closeme")
        ]]
    )

# Here t = 0; cauz downloading using bot.downlod_media cant fetch
# total file size, so sharing file_size as function para.
async def progress(current, t, total, message, start):
    now = time.time()
    diff = now - start

    if round(diff % 10) in [0, 8] or current == total:
        # if round(current / total * 100, 0) % 10 == 0:
        percentage = current * 100 / total
        speed = current / diff
        time_to_completion = round((total - current)/speed)*1000
        progress="[{0}{1}] \n".format(
            ''.join(["●" for _ in range(math.floor(percentage / 5))]),
            ''.join(["○" for _ in range(20 - math.floor(percentage / 5))])
        )
        estimated_total_time = TimeFormatter(time_to_completion)
        tmp = progress + "**\nDone ✅ : **{0}/{1}\n**Speed 🚀:** {2}/s\n**Estimated Time ⏳:** {3}".format(
            await gSF(current), await gSF(total), await gSF(speed),
            estimated_total_time if estimated_total_time != '' else "0 s"
        )

        await message.edit_text(
            text=f"DOWNLOADING.. 📥\n{tmp}", reply_markup=reply_markup
        )


async def uploadProgress(current, total, message, start):
    now = time.time()
    diff = now - start

    if round(diff % 10) in [0, 8] or current == total:
        # if round(current / total * 100, 0) % 10 == 0:
        percentage = current * 100 / total
        speed = current / diff
        time_to_completion = round((total - current)/speed)*1000
        progress="[{0}{1}] \n".format(
            ''.join(["●" for _ in range(math.floor(percentage / 5))]),
            ''.join(["○" for _ in range(20 - math.floor(percentage / 5))])
        )
        estimated_total_time = TimeFormatter(time_to_completion)
        tmp = progress + "**\nDone ✅ : **{0}/{1}\n**Speed 🚀:** {2}/s\n**Estimated Time ⏳:** {3}".format(
            await gSF(current), await gSF(total), await gSF(speed),
            estimated_total_time if estimated_total_time != '' else "0 s"
        )

        await message.edit_text(
            text=f"UPLOADING.. 📤\n{tmp}", reply_markup=reply_markup
        )

#--------------->
#--------> TIME FORMATTER
#------------------->

def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds=divmod(seconds, 60)
    hours, minutes=divmod(minutes, 60)
    days, hours=divmod(hours, 24)
    tmp = (
        (f"{str(days)}d, " if days else "")
        + (f"{str(hours)}h, " if hours else "")
        + (f"{str(minutes)}m, " if minutes else "")
        + (f"{str(seconds)}s, " if seconds else "")
        + (f"{str(milliseconds)}ms, " if milliseconds else "")
    )

    return tmp[:-2]

#                                                                                  Telegram: @nabilanavab
