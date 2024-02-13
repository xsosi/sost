@Client.on_message(
    filters.command(["ping"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def pingme(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xx = await message.reply_text("**0% ▒▒▒▒▒▒▒▒▒▒**")
    try:
       await message.delete()
    except:
       pass
    await xx.edit("**20% ██▒▒▒▒▒▒▒▒ 🚩😈ᴘᴏɪsᴏɴ ᴏᴘ ʙᴏʟᴛᴇ🚩😈**")
    await xx.edit("**40% ████▒▒▒▒▒▒ 🚩😈ᴊᴀɪ sʜʀᴇᴇ ʀᴀᴍ**")
    await xx.edit("**60% ██████▒▒▒▒ 🚩😈ʀᴀᴅʜᴇ ᴋʀɪsʜɴᴀ**")
    await xx.edit("**80% ████████▒▒ 🚩😈Hᴀʀ ʜᴀʀ ᴍᴀʜᴀᴅᴇᴠ**")
    await xx.edit("**100% ████████▒▒ 🚩Jᴀɪ sʜʀᴇᴇ ʀᴀᴍ🚩**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await xx.edit(
        f"🚩🕉️ **🔥🖤ᴘᴏɪsᴏɴ ᴛᴏxɪᴄ ᴅᴏ ᴅɪʟ ᴇᴋ ᴊᴀᴀɴ🔥🖤**\n"
        f"❏ **🚩😈ᴘᴏɪsᴏɴ ʙᴏᴛ ғɪʀᴇ ᴏɴ😈🚩**\n"
        f"├• **🚩🕉️** - `%sms`\n"
        f"├• **🚩🕉️ -** `{uptime}` \n"
        f"└• **🚩🕉️:** {client.me.mention}" % (duration)
    )


add_command_help(
    "ping",
    [
        ["ping", "Check bot alive or not."],
    ],
)
