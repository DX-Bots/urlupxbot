from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
👋 Hᴇʏ {}🙋

I ᴀᴍ Tᴇʟᴇɢʀᴀᴍ Mᴏsᴛ Pᴏᴡᴇʀғᴜʟ Uʀʟ Uᴘʟᴏᴀᴅᴇʀ Bᴏᴛ.

Usᴇ /help ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ.

Mᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : [@TeleRoidGroup](https://telegram.me/TeleRoidGroup)
"""
    HELP_TEXT = """
Lɪɴᴋ ᴛᴏ Mᴇᴅɪᴀ ᴏʀ Fɪʟᴇ

➠ Sᴇɴᴅ ᴀ ʟɪɴᴋ ғᴏʀ ᴜᴘʟᴏᴀᴅ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇ ᴏʀ ᴍᴇᴅɪᴀ.

Sᴇᴛ ᴛʜᴜᴍʙɴᴀɪʟ

➠ sᴇɴᴅ ᴀ ᴘʜᴏᴛᴏ ᴛᴏ ᴍᴀᴋᴇ ɪᴛ ᴀs ᴘᴇʀᴍᴀɴᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ.

ᴅᴇʟᴇᴛɪɴɢ ᴛʜᴜᴍʙɴᴀɪʟ

➠ Sᴇɴᴅ /delthumb ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛʜᴜᴍʙɴᴀɪʟ.

Sᴇᴛᴛɪɴɢs

➠ Cᴏɴғɪɢᴜʀᴇ ᴍʏ Sᴇᴛᴛɪɴɢs ᴛᴏ ᴄʜᴀɴɢᴇ ᴜᴘʟᴏᴀᴅ ᴍᴏᴅᴇ

sʜᴏᴡ ᴛʜᴜᴍʙɴᴀɪʟ

➠ Sᴇɴᴅ /showthumb ᴛᴏ ᴠɪᴇᴡ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ.

ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : [@TheTeleRoid](https://telegram.me/TheTeleRoid)
 
"""
    ABOUT_TEXT = """
**Mʏ ɴᴀᴍᴇ** : [ᴜᴘʟᴏᴀᴅᴇʀ ʙᴏᴛ](http://t.me/UrlUpxBot)

**Cʜᴀɴɴᴇʟ** : [TᴇʟᴇRᴏɪᴅGʀᴏᴜᴘ](https://t.me/TeleRoidGroup)

**Vᴇʀꜱɪᴏɴ** : [2.0 ʙᴇᴛᴀ](https://t.me/joinchat/t1ko_FOJxhFiOThl)

**Sᴏᴜʀᴄᴇ** : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://github.com/PredatorHackerzZ)

**Sᴇʀᴠᴇʀ** : [ʜᴇʀᴏᴋᴜ](https://heroku.com/)

**Lᴀɴɢᴜᴀɢᴇ :** [Pʏᴛʜᴏɴ 3.10.2](https://www.python.org/)

**Fʀᴀᴍᴇᴡᴏʀᴋ :** [ᴘʏʀᴏɢᴀᴍ 1.3.6](https://docs.pyrogram.org/)

**Dᴇᴠᴇʟᴏᴘᴇʀ :** [TᴇʟᴇRᴏɪᴅGʀᴏᴜᴘ](https://t.me/MoviesFlixers_DL)

**ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ :** [TʜᴇTᴇʟᴇRᴏɪᴅ](https://t.me/TheTeleRoid)

"""


    PROGRESS = """
╭──[🔅Pʀᴏɢʀᴇss Bᴀʀ🔅]──⍟
│
├Sᴘᴇᴇᴅ : {3}/s
│
├Dᴏɴᴇ : {1}
│
├Tᴏᴛᴀʟ sɪᴢᴇ  : {2}
│
├Tɪᴍᴇ ʟᴇғᴛ : {4}
╰─────────────────⍟
"""


    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⚙ Sᴇᴛᴛɪɴɢs', callback_data='OpenSettings')
        ],[
        InlineKeyboardButton('🆘 Hᴇʟᴘ', callback_data='help'),
        InlineKeyboardButton('👤 Aʙᴏᴜᴛ', callback_data='about')
        ],[
        InlineKeyboardButton('🔐 Cʟᴏsᴇ', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 ʜᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton('👤 Aʙᴏᴜᴛ', callback_data='about')
        ],[
        InlineKeyboardButton('🔐 Cʟᴏsᴇ', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Hᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton('🆘 Hᴇʟᴘ', callback_data='help')
        ],[
        InlineKeyboardButton('🔐 Cʟᴏsᴇ', callback_data='close')
        ]]
    )
    BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 ʜᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton('🆘 ʜᴇʟᴘ', callback_data='help')
        ],[
        InlineKeyboardButton('🔐 ᴄʟᴏsᴇ', callback_data='close')
        ]]
    )

    IFLONG_FILE_NAME = " Only 64 characters can be named . "
    RENAME_403_ERR = "Sorry. You are not permitted to rename this file."
    ABS_TEXT = " Please don't be selfish."
    UPGRADE_TEXT = "<b>No preminum plans available in this bot </b>  /help for Details"
    FORMAT_SELECTION = "Nᴏᴡ Sᴇʟᴇᴄᴛ Tʜᴇ Dᴇsɪʀᴇᴅ Fᴏʀᴍᴀᴛ ᴏʀ Fɪʟᴇ 🗄️ Sɪᴢᴇ ᴛᴏ Uᴘʟᴏᴀᴅ"
    SET_CUSTOM_USERNAME_PASSWORD = """"""
    NOYES_URL = "Slow URL detected. Please use https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    DOWNLOAD_FILE = "📥 Downloading  File "
    UPLOAD_FILE = " UploadinG 📤 \n\n To  transfer.sh "
    ANNO_UPLOAD = " UploadinG📤 \n\n To  anonfiles.com "
    BAY_UPLOAD = " UploadinG📤 \n\n To  bayfiles.com "
    GO_FILE_UPLOAD = " 📤UploadinG📤 \n\n To  gofile.io "
    DOWNLOAD_START = "Dᴏᴡɴʟᴏᴀᴅɪɴɢ ᴛᴏ ᴍʏ sᴇʀᴠᴇʀ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ  ⏳"
    UPLOAD_START = "📤 Uᴘʟᴏᴀᴅɪɴɢ Pʟᴇᴀsᴇ Wᴀɪᴛ"
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 2GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG = " JOIN : https://t.me/TGBotsCollection\nFor the List of Telegram Bots"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Dᴏᴡɴʟᴏᴀᴅᴇᴅ ɪɴ {} sᴇᴄᴏɴᴅs.\n\nTʜᴀɴᴋs Fᴏʀ Usɪɴɢ Mᴇ\n\nUᴘʟᴏᴀᴅᴇᴅ ɪɴ {} sᴇᴄᴏɴᴅs"
    NOT_AUTH_USER_TEXT = "Please /upgrade your subscription."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}. Free Users can only upload: {}\nPlease /upgrade your subscription.\nIf you think this is a bug, please contact <a href='https://telegram.dog/TeleRoid14'>@TeleRoid14</a>"
    SAVED_CUSTOM_THUMB_NAIL = "Cᴜsᴛᴏᴍ ᴠɪᴅᴇᴏ / ғɪʟᴇ ᴛʜᴜᴍʙɴᴀɪʟ sᴀᴠᴇᴅ. Tʜɪs ɪᴍᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴜsᴇᴅ ɪɴ ᴛʜᴇ ᴠɪᴅᴇᴏ / ғɪʟᴇ."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Cᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴄʟᴇᴀʀᴇᴅ sᴜᴄᴄᴇsғᴜʟʟʏ"
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    SAVED_RECVD_DOC_FILE = "Document Downloaded Successfully."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_CUSTOM_THUMB_NAIL_FOUND = "Nᴏ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ғᴏᴜɴᴅ"
    NO_VOID_FORMAT_FOUND = "ERROR... <code>{}</code>"
    FILE_NOT_FOUND = "Error, File not Found!!"
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    SOMETHING_WRONG = "<code>Something Wrong. Try again.</code>"
    REPLY_TO_DOC_GET_LINK = "Reply to a Telegram media to get High Speed Direct Download Link"
    REPLY_TO_DOC_FOR_C2V = "Reply to a Telegram media to convert"
    REPLY_TO_DOC_FOR_SCSS = "Reply to a Telegram media to get screenshots"
    REPLY_TO_DOC_FOR_RENAME_FILE = "Reply to a Telegram media to /ren with custom thumbnail support"
    AFTER_GET_LINK = " <b>File Name :</b> <code>{}</code>\n<b>File Size :</b> {}\n\n<b>⚡Link⚡ :</b> <code>{}</code>\n\nJoin : @TeleRoidGroup"
    AFTER_GET_DL_LINK = " <b>File Name :</b> <code>{}</code>\n<b>File Size :</b> {}\n\n<b>⚡Link⚡ :</b> <code>{}</code>\n\nValid for <b>14</b> days.\nJoin : @TeleRoidGroup"
    #AFTER_GET_DL_LINK = " {} valid for 30 or more days.\n\n Join : @Tellybots_4u \n For the list of Telegram bots. "
    AFTER_GET_GOFILE_LINK = " <b>File Name :</b> <code>{}</code>\n<b>File Size :</b> {}\n<b>File MD5 Checksum :</b> <code>{}</code>\n\n<b>⚡Link⚡ :</b> <code>{}</code>\n\n Valid untill 10 days of inactivity\nJoin : @TGRobots_List"
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Syntax: /trim HH:MM:SS for screenshot of that specific time."""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "First send /downloadmedia to any media so that it can be downloaded to my local. \nSend /storageinfo to know the media, that is currently downloaded."
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "Video Duration: {}\nSend /clearffmpegmedia to delete this media, from my storage.\nSend /trim HH:MM:SS [HH:MM:SS] to cu[l]t a small photo / video, from the above media."
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "A saved media already exists. Please send /storageinfo to know the current media details."
    USER_DELETED_FROM_DB = "User <a href='tg://user?id={}'>{}</a> deleted from DataBase."
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "Reply to a Telegram media (MKV), to extract embedded streams"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
    INVALID_UPLOAD_BOT_URL_FORMAT = "URL format is incorrect. make sure your url starts with either http:// or https://. You can set custom file name using the format link | file_name.extension"
    ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction."
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "Join : @TGBotsCollectionbot \n For the list of Telegram bots. "
    EXTRACT_ZIP_INTRO_ONE = "Send a compressed file first, Then reply /unzip command to the file."
    EXTRACT_ZIP_INTRO_THREE = "Analyzing received file. ⚠️ This might take some time. Please be patient. "
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "Sorry. Errors occurred while processing compressed file. Please check everything again twice, and if the issue persists, report this to <a href='https://telegram.dog/TeleRoid14'>@TeleRoid14</a>"
    EXTRACT_ZIP_STEP_TWO = """Select file_name to upload from the below options.
You can use /rename command after receiving file to rename it with custom thumbnail support."""
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    FREE_USER_LIMIT_Q_SZE = """Cannot Process.
Free users only 1 request per 30 minutes.
/upgrade or Try 1800 seconds later."""
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    FORCE_SUBSCRIBE_TEXT = "<code>Sorry Dear You Must Join My Updates Channel for using me 😉....</code>"
    BANNED_USER_TEXT = "<code>You are Banned!</code>"
    CHECK_LINK = "Pʀᴏᴄᴇssɪɴɢ ʏᴏᴜʀ ʟɪɴᴋ ⌛"

