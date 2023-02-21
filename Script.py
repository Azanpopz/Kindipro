class script(object):
    START_TXT = """𝗛ᴇʟʟᴏ {},

 𝗠ʏ 𝗡ᴀᴍᴇ ɪ𝘀  ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ

𝖨'𝗆 𝖺 𝖴𝗌𝖾𝗋-𝖥𝗋𝗂𝖾𝗇𝖽𝗅𝗒 𝗀𝗋𝗈𝗎𝗉 𝖬𝖺𝗇𝖺𝗀𝖾𝗋 
➢ <b>Build Version</b>: <code>V2.1.0 [BETA]</code>
➢ <b>Speciality</b>: <code>Movie Provider</code>
𝖢𝗅𝗂𝖼𝗄 <b>𝖧𝖾𝗅𝗉</b> 𝗍𝗈 𝗆𝗒 𝖥𝗎𝗇𝖼𝗍𝗂𝗈𝗇𝗌<a href='https://telegra.ph/file/eaf97e4782f05b667e551.jpg'>.</a>"""
   
    PM_TXT = "<a href='https://telegra.ph/file/eaf97e4782f05b667e551.jpg'>.</a> \n <b>Message from:</b> {}\n<b>Name:</b> {}\n\n{}"
    CP_TXT = """𝗛ᴇʟʟᴏ {},

 FILE : <code>{file_name}</code>\nSize : <i>{file_size}</i>\n\nHello {message.from_user.first_name} \n\n⚠️ കോപ്പി റൈറ്റ് ഉള്ളത് കൊണ്ട് ഈ ഒരു ഫയൽ 1 മണിക്കൂർകൊണ്ട് ഇവിടെ നിന്നും ഡിലേറ്റാവും...!!!\n\nഇവിടെ നിന്നും വേറെ എവിടേലും മാറ്റിയതിന് ശേഷം ഡൗൺലോഡ് ചെയ്യുക...!!!\n\nFILES FORWARD TO YOUR SAVED MESSAGES\n\nAll files here Gets Deleted With in 1 hour.  
"""
       

  

    HELP_TXT = """<b>𝖧𝖾𝗋𝖾 𝗂𝗌 𝗍𝗁𝖾 𝖴𝗌𝗎𝖺𝗅 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌:</b>
"""
    GTRANS_TXT = """<b>𝖳𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝗈𝗋</b>
- 𝖳𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾 𝗍𝖾𝗑𝗍𝗌 𝗍𝗈 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝗂𝖼 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾!
<b>𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖺𝗇𝖽 𝖴𝗌𝖺𝗀𝖾:</b>
- /tr [language code][reply] - 𝖳𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾 𝗋𝖾𝗉𝗅𝗂𝖾𝖽 𝗆𝖾𝗌𝗌𝖺𝗀𝖾 𝗍𝗈 𝗌𝗉𝖾𝖼𝗂𝖿𝗂𝖼 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾.
"""
    PASTE_TXT = """<b>𝖯𝖺𝗌𝗍𝖾</b>
- 𝖯𝖺𝗌𝗍𝖾 𝗌𝗈𝗆𝖾 𝗍𝖾𝗑𝗍𝗌 𝗈𝗋 𝖽𝗈𝖼𝗎𝗆𝖾𝗇𝗍𝗌 𝗈𝗇 𝖺 𝗐𝖾𝖻𝗌𝗂𝗍𝖾!
<b>𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖺𝗇𝖽 𝖴𝗌𝖺𝗀𝖾:</b>
- /paste [text] - 𝖯𝖺𝗌𝗍𝖾 𝗍𝗁𝖾 𝗀𝗂𝗏𝖾𝗇 𝗍𝖾𝗑𝗍 𝗈𝗇 𝗉𝖺𝗌𝗍𝗒
- /paste [reply] - 𝖯𝖺𝗌𝗍𝖾 𝗍𝗁𝖾 𝗋𝖾𝗉𝗅𝗂𝖾𝖽 𝗍𝖾𝗑𝗍 𝗈𝗇 𝗉𝖺𝗌𝗍𝗒
"""
    STICK_TXT = """<b>𝖲𝗍𝗂𝖼𝗄𝖾𝗋 𝖨𝖣</b>
- 𝖳𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗂𝗌 𝗎𝗌𝖾𝖽 𝗍𝗈 𝗀𝖾𝗍 𝖺 𝖨𝖣 𝗈𝖿 𝖺𝗇 𝗌𝗍𝗂𝖼𝗄𝖾𝗋

<b>Command</b>
- /stickerid - 𝖦𝖾𝗍 𝖨𝖣
"""
    ABOUT_TXT = """
𝐌𝐲 𝐍𝐚𝐦𝐞 :ᴏʙᴀɴᴀɪ ɪɢᴜʀᴏ 🐍

🦁 𝐂𝐫𝐞𝐚𝐭𝐨𝐫 :ʙʟᴇssᴏɴ[TG]🍷

🐍𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞 : 𝐏𝐲𝐭𝐡𝐨𝐧

🐍𝐋𝐢𝐛𝐫𝐚𝐫𝐲 : 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝐚𝐬𝐲𝐧𝐜𝐢𝐨 

🐍𝐒𝐮𝐩𝐩𝐨𝐫𝐭𝐞𝐝 𝐒𝐢𝐭𝐞 : 𝐎𝐧𝐥𝐲 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦

🐍𝐒𝐞𝐫𝐯𝐞𝐫 : 𝐇𝐞𝐫𝐨𝐤U

🐍𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞 : 𝐌𝐨𝐧𝐠𝐨𝐃𝐁

🐍𝐁𝐮𝐢𝐥𝐝 s𝐭𝐚𝐭𝐮𝐬 : 𝐕2.1 [𝐁𝐄𝐓𝐀]
"""
    SOURCE_TXT = """<b>NOTE:</b>
- This is a closed source project.   

CODES:
1. Auto Filter
2. Group Managing  
"""
    TTS_TXT = """<b>TEXT TO SPEACH</b>
Simple Telegram Text-To-Speech Module.
It can use the following as speech synthesis engines:

Amazon's Polly engine
Google's TTS engine by way of the gTTS library
"""
    COVID_TXT = """<b><u>𝖢𝗈𝗏𝗂𝖽 19 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇</u><b/>
𝖢𝗈𝗋𝗈𝗇𝖺 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇 𝗈𝖿 𝗒𝗈𝗎𝗋 𝖼𝗈𝗎𝗇𝗍𝗋𝗒 / 𝖳𝗈 𝗄𝗇𝗈𝗐 𝗍𝗁𝖾 𝖼𝗈𝗏𝗂𝖽 𝗂𝗇𝖿𝗈 𝗈𝖿 𝖺𝗇𝗒 𝖼𝗈𝗎𝗇𝗍𝗋𝗒            
<b>𝖢𝗈𝗆𝗆𝖺𝗇𝖽:</b>
/covid [country name] - 𝖦𝖾𝗍 𝗂𝗇𝖿𝗈 𝖺𝖻𝗈𝗎𝗍 𝖼𝗈𝗏𝗂𝖽 𝖼𝖺𝗌𝖾𝗌 𝗂𝗇 𝗒𝗈𝗎𝗋 𝖼𝗈𝗎𝗇𝗍𝗋𝗒
<b>𝖴𝗌𝖺𝗀𝖾</b>
- 𝖢𝗈𝗎𝗅𝖽 𝖻𝖾 𝗎𝗌𝖾𝖽 𝗂𝗇 𝗉𝗆 𝖺𝗇𝖽 𝗀𝗋𝗈𝗎𝗉𝗌
    """
    BAN_TXT = """<b>𝖡𝖺𝗇𝗌:</b>
𝖲𝗈𝗆𝖾 𝗉𝖾𝗈𝗉𝗅𝖾 𝗇𝖾𝖾𝖽 𝗍𝗈 𝖻𝖾 𝗉𝗎𝖻𝗅𝗂𝖼𝗅𝗒 𝖻𝖺𝗇𝗇𝖾𝖽; 𝗌𝗉𝖺𝗆𝗆𝖾𝗋𝗌, 𝖺𝗇𝗇𝗈𝗒𝖺𝗇𝖼𝖾𝗌, 𝗈𝗋 𝗃𝗎𝗌𝗍 𝗍𝗋𝗈𝗅𝗅𝗌.  
𝖳𝗁𝗂𝗌 𝗆𝗈𝖽𝗎𝗅𝖾 𝖺𝗅𝗅𝗈𝗐𝗌 𝗒𝗈𝗎 𝗍𝗈 𝖽𝗈 𝗍𝗁𝖺𝗍 𝖾𝖺𝗌𝗂𝗅𝗒, 𝖻𝗒 𝖾𝗑𝗉𝗈𝗌𝗂𝗇𝗀 𝗌𝗈𝗆𝖾 𝖼𝗈𝗆𝗆𝗈𝗇 𝖺𝖼𝗍𝗂𝗈𝗇𝗌, 𝗌𝗈 𝖾𝗏𝖾𝗋𝗒𝗈𝗇𝖾 𝗐𝗂𝗅𝗅 𝗌𝖾𝖾!

<b>𝖠𝖽𝗆𝗂𝗇 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌:</b>
- /ban - 𝖡𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋
- /tban - 𝖳𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋. 𝖤𝗑𝖺𝗆𝗉𝗅𝖾 𝗍𝗂𝗆𝖾 𝗏𝖺𝗅𝗎𝖾𝗌: 𝟦𝗆 = 𝟦 𝗆𝗂𝗇𝗎𝗍𝖾𝗌, 𝟥𝗁 = 𝟥 𝗁𝗈𝗎𝗋𝗌, 𝟨𝖽 = 𝟨 𝖽𝖺𝗒𝗌, 𝟧𝗐 = 𝟧 𝗐𝖾𝖾𝗄𝗌.
- /unban - 𝖴𝗇𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋

<b>𝖤𝗑𝖺𝗆𝗉𝗅𝖾𝗌:</b>
- 𝖡𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋 𝖿𝗈𝗋 𝗍𝗐𝗈 𝗁𝗈𝗎𝗋𝗌. 
-> /tban @𝗎𝗌𝖾𝗋𝗇𝖺𝗆𝖾 𝟤𝗁
"""
    PING_TXT= """<b>𝖯𝗂𝗇𝗀:</b>

𝖧𝖾𝗅𝗉𝗌 𝗒𝗈𝗎 𝗍𝗈 𝗄𝗇𝗈𝗐 𝗒𝗈𝗎𝗋 𝗉𝗂𝗇𝗀, 𝖨𝗇 𝗌𝗁𝗈𝗋𝗍-𝗍𝖾𝗋𝗆𝗌 '𝗆𝗌'.

<b>𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌:</b>

- /alive - 𝖳𝗈 𝖼𝗁𝖾𝖼𝗄 𝗐𝗁𝖾𝗍𝗁𝖾𝗋 𝗒𝗈𝗎 𝖺𝗋𝖾 𝖺𝗅𝗂𝗏𝖾
- /hi - 𝖭𝗈 𝗁𝗂, 𝖡𝗈𝗍 𝗁𝖺𝗍𝖾𝗌 𝗁𝗂
- /ping - 𝖳𝗈 𝖪𝗇𝗈𝗐 𝗒𝗈𝗎𝗋 𝗉𝗂𝗇𝗀 

<b>𝖴𝗌𝖺𝗀𝖾:</b>

• 𝖳𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝖼𝖺𝗇 𝖻𝖾 𝗎𝗌𝖾𝖽 𝗂𝗇 𝗉𝗆𝗌 𝖺𝗇𝖽 𝗀𝗋𝗈𝗎𝗉𝗌.
• 𝖳𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝖼𝖺𝗇 𝖻𝖾 𝗎𝗌𝖾𝖽 𝖻𝗎𝗒 𝖾𝗏𝖾𝗋𝗒𝗈𝗇𝖾 𝗂𝗇 𝗀𝗋𝗈𝗎𝗉𝗌 𝖺𝗇𝖽 𝖻𝗈𝗍𝗌 𝗉𝗆.
"""
    JSON_TXT = """<b>𝖩𝗌𝗈𝗇:</b>
𝖡𝗈𝗍 𝗋𝖾𝗍𝗎𝗋𝗇𝗌 𝗃𝗌𝗈𝗇 𝖿𝗈𝗋 𝖺𝗅𝗅 𝗋𝖾𝗉𝗅𝗂𝖾𝖽 𝗆𝖾𝗌𝗌𝖺𝗀𝖾𝗌 𝗐𝗂𝗍𝗁 /json. 
<b>𝖥𝖾𝖺𝗍𝗎𝗋𝖾𝗌:</b>
𝖬𝖾𝗌𝗌𝖺𝗀𝖾 𝖤𝖽𝗂𝗍𝗍𝗂𝗇𝗀 JSON
𝖯𝗆 𝖲𝗎𝗉𝗉𝗈𝗋𝗍 
𝖦𝗋𝗈𝗎𝗉 𝖲𝗎𝗉𝗉𝗈𝗋𝗍
"""
    FUN_TXT ="""<b>𝖥𝗎𝗇 𝖬𝗈𝖽𝗎𝗅𝖾𝗌</b> 
    
<b>🎲 𝖭𝗈𝗍𝗁𝗂𝗇𝗀 𝗆𝗎𝖼𝗁 𝗃𝗎𝗌𝗍 𝗌𝗈𝗆𝖾 𝖿𝗎𝗇 𝗌𝗍𝗎𝖿𝖿𝗌</b>
𝗍𝗋𝗒 𝗍𝗁𝖾𝗌𝖾 𝗈𝗎𝗍: 
𝟣. /dice - 𝖱𝗈𝗅𝗅 𝗍𝗁𝖾 𝖽𝗂𝖼𝖾
𝟤. /Throw 𝗈𝗋 /Dart - 𝖳𝗈 𝗍𝗁𝗋𝗈𝗐 𝖺 𝖽𝖺𝗋𝗍
3. /Runs - 𝖩𝗎𝗌𝗍 𝗌𝗈𝗆𝖾 𝗋𝖺𝗇𝖽𝗈𝗆 𝖽𝖺𝗂𝗅𝗈𝗎𝗀𝖾𝗌
4. /Goal or /Shoot - 𝖳𝗈 𝗀𝗈𝖺𝗅 𝗈𝗋 𝗌𝗁𝗈𝗈𝗍 𝖺 𝖻𝖺𝗅𝗅
"""
    PURGE_TXT ="""<b>𝖯𝗎𝗋𝗀𝖾</b>
- 𝖣𝖾𝗅𝖾𝗍𝖾 𝖺 𝗅𝗈𝗍𝗌 𝗈𝖿 𝗆𝖾𝗌𝗌𝖺𝗀𝖾𝗌 𝖿𝗋𝗈𝗆 𝖺 𝗀𝗋𝗈𝗎𝗉!
    
 <b>𝖠𝖽𝗆𝗂𝗇</b> 
◉ /purge :- 𝖣𝖾𝗅𝖾𝗍𝖾 𝖺𝗅𝗅 𝗆𝖾𝗌𝗌𝖺𝗀𝖾𝗌 𝖿𝗋𝗈𝗆 𝗍𝗁𝖾 𝗋𝖾𝗉𝗅𝗂𝖾𝖽 𝗆𝖾𝗌𝗌𝖺𝗀𝖾 𝗍𝗈, 𝖳𝗁𝖾 𝖼𝗎𝗋𝗋𝖾𝗇𝗍 𝗆𝖾𝗌𝗌𝖺𝗀𝖾
    """
    MANUELFILTER_TXT = """<b>𝖥𝗂𝗅𝗍𝖾𝗋𝗌</b>
𝖥𝗂𝗅𝗍𝖾𝗋 𝗂𝗌 𝗍𝗁𝖾 𝖿𝖾𝖺𝗍𝗎𝗋𝖾 𝗐𝖾𝗋𝖾 𝗎𝗌𝖾𝗋𝗌 𝖼𝖺𝗇 𝗌𝖾𝗍 𝖺𝗎𝗍𝗈𝗆𝖺𝗍𝖾𝖽 𝗋𝖾𝗉𝗅𝗂𝖾𝗌 𝖿𝗈𝗋 𝖺 𝗉𝖺𝗋𝗍𝗂𝖼𝗎𝗅𝖺𝗋 𝗄𝖾𝗒𝗐𝗈𝗋𝖽 𝖺𝗇𝖽 𝗍𝗁𝖾 𝖻𝗈𝗍 𝗐𝗂𝗅𝗅 𝗋𝖾𝗌𝗉𝗈𝗇𝖽 𝗐𝗁𝖾𝗇𝖾𝗏𝖾𝗋 𝖺 𝗄𝖾𝗒𝗐𝗈𝗋𝖽 𝗂𝗌 𝖿𝗈𝗎𝗇𝖽 𝗍𝗁𝖾 𝗆𝖾𝗌𝗌𝖺𝗀𝖾 
<b>𝖭𝖮𝖳𝖤:</b>
𝟣. 𝖻𝗈𝗍 𝗌𝗁𝗈𝗎𝗅𝖽 𝗁𝖺𝗏𝖾 𝖺𝖽𝗆𝗂𝗇 𝗉𝗋𝗂𝗏𝗂𝗅𝗅𝖺𝗀𝖾 𝗂𝗇 𝗈𝗋𝖽𝖾𝗋 𝗍𝗈 𝗋𝖾𝗉𝗅𝗒 𝖿𝗂𝗅𝗍𝖾𝗋𝗌 𝗂𝗇 𝖺 𝖼𝗁𝖺𝗍. 
𝟤. 𝗈𝗇𝗅𝗒 𝖺𝖽𝗆𝗂𝗇𝗌 𝖼𝖺𝗇 𝖺𝖽𝖽 𝖿𝗂𝗅𝗍𝖾𝗋𝗌 𝗂𝗇 𝖺 𝖼𝗁𝖺𝗍. 
𝟥. 𝖿𝗂𝗅𝗍𝖾𝗋𝗌 𝖽𝗈𝖾𝗌 𝗌𝗎𝗉𝗉𝗈𝗋𝗍 𝖺𝗅𝗅 𝗍𝗁𝖾 𝗍𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝗆𝖺𝗋𝗄𝖽𝗈𝗐𝗇𝗌, 𝗆𝖾𝖽𝗂𝖺𝗌 𝖺𝗇𝖽 𝖻𝗎𝗍𝗍𝗈𝗇𝗌. 
𝟦. 𝖺𝗅𝖾𝗋𝗍 𝖻𝗎𝗍𝗍𝗈𝗇𝗌 𝖺𝗋𝖾 𝖺𝗅𝗌𝗈 𝗌𝗎𝗉𝗉𝗈𝗋𝗍𝖾𝖽 𝗐𝗂𝗍𝗁 𝖺 𝗅𝗂𝗆𝗂𝗍 𝗈𝖿 𝟨𝟦 𝖼𝗁𝖺𝗋𝖺𝖼𝗍𝖾𝗋𝗌. 
𝟧. 𝗍𝗁𝖾𝗋𝖾 𝖺𝗋𝖾 𝗌𝗈𝗆𝖾 𝖾𝖺𝗌𝗍𝖾𝗋 𝖾𝗀𝗀𝗌, 𝗍𝗋𝗒 𝗍𝗈 𝖿𝗂𝗇𝖽 𝗂𝗍 𝗈𝗎𝗍. 
<b>𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖺𝗇𝖽 𝖴𝗌𝖺𝗀𝖾:</b>
/filter  𝗈𝗋 /add - 𝖺𝖽𝖽 𝖺 𝖿𝗂𝗅𝗍𝖾𝗋
/filters 𝗈𝗋 /viewfilters - 𝗅𝗂𝗌𝗍 𝖺𝗅𝗅 𝗍𝗁𝖾 𝖿𝗂𝗅𝗍𝖾𝗋𝗌 𝗈𝖿 𝖺 𝖼𝗁𝖺𝗍 
/stop 𝗈𝗋 /del - 𝖽𝖾𝗅𝖾𝗍𝖾 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝗂𝖼 𝖿𝗂𝗅𝗍𝖾𝗋 (𝗌𝖾𝗉𝖺𝗋𝖺𝗍𝖾 𝗄𝖾𝗒𝗐𝗈𝗋𝖽𝗌 𝗐𝗂𝗍𝗁 𝗌𝗉𝖺𝖼𝖾𝗌 𝖿𝗈𝗋 𝖽𝖾𝗅𝖾𝗍𝗂𝗇𝗀 𝗆𝗎𝗅𝗍𝗂𝗉𝗅𝖾 𝖿𝗂𝗅𝗍𝖾𝗋𝗌 𝖺𝗍 𝖺 𝗍𝗂𝗆𝖾) 
/stopall 𝗈𝗋 /delall - 𝖽𝖾𝗅𝖾𝗍𝖾 𝗍𝗁𝖾 𝗐𝗁𝗈𝗅𝖾 𝖿𝗂𝗅𝗍𝖾𝗋𝗌 𝗂𝗇 𝖺 𝖼𝗁𝖺𝗍 (𝖼𝗁𝖺𝗍 𝗈𝗐𝗇𝖾𝗋 𝗈𝗇𝗅𝗒)
"""
    SONG_TXT = """<b>𝖲𝗈𝗇𝗀 𝖣𝗈𝗐𝗇𝗅𝗈𝖺𝖽 𝖬𝗈𝖽𝗎𝗅𝖾</b>
- 𝖨𝖿 𝗒𝗈𝗎 𝗐𝖺𝗇𝗍 𝗍𝗈 𝖽𝗈𝗐𝗇𝗅𝗈𝖺𝖽 𝖺 𝗌𝗈𝗇𝗀, 𝖽𝗈𝗇'𝗍 𝗌𝖾𝖺𝗋𝖼𝗁 𝖿𝗈𝗋 𝗈𝗍𝗁𝖾𝗋 𝖻𝗈𝗍 𝗁𝖾𝗋𝖾 𝗂𝗌 𝗍𝗁𝖾 𝖺𝗅𝗅 𝗂𝗇 𝗈𝗇𝖾 𝖻𝗈𝗍
<b>𝖢𝗈𝗆𝗆𝖺𝗇𝖽</b>
- /song [Song Name] - 𝖳𝗈 𝗀𝖾𝗍 𝗍𝗁𝖾 𝗌𝗈𝗇𝗀
<b>Usage</b>
- 𝖢𝖺𝗇 𝖻𝖾 𝗎𝗌𝖾𝖽 𝖻𝗒 𝖾𝗏𝖾𝗋𝗒 𝗈𝗇𝖾
- 𝖶𝗈𝗋𝗄𝗌 𝗈𝗇𝗅𝗒 𝗂𝗇 𝖻𝗈𝗍𝗌 𝗉𝗆
<b>𝖡𝗎𝗀</b>
𝖲𝗈𝗆𝖾𝗍𝗂𝗆𝖾𝗌 𝗂𝗍 𝗐𝗂𝗅𝗅 𝗌𝗁𝗈𝗐 𝖺𝗇 𝖾𝗋𝗋𝗈𝗋!
"""
    MUTE_TXT = """<b>𝖬𝗎𝗍𝖾:</b>

𝖲𝗈𝗆𝖾 𝗉𝖾𝗈𝗉𝗅𝖾 𝗇𝖾𝖾𝖽 𝗍𝗈 𝖻𝖾 𝗉𝗎𝖻𝗅𝗂𝖼𝗅𝗒 Muted; 𝗌𝗉𝖺𝗆𝗆𝖾𝗋𝗌, 𝖺𝗇𝗇𝗈𝗒𝖺𝗇𝖼𝖾𝗌, 𝗈𝗋 𝗃𝗎𝗌𝗍 𝗍𝗋𝗈𝗅𝗅𝗌.  
𝖳𝗁𝗂𝗌 𝗆𝗈𝖽𝗎𝗅𝖾 𝖺𝗅𝗅𝗈𝗐𝗌 𝗒𝗈𝗎 𝗍𝗈 𝖽𝗈 𝗍𝗁𝖺𝗍 𝖾𝖺𝗌𝗂𝗅𝗒, 𝖻𝗒 𝖾𝗑𝗉𝗈𝗌𝗂𝗇𝗀 𝗌𝗈𝗆𝖾 𝖼𝗈𝗆𝗆𝗈𝗇 𝖺𝖼𝗍𝗂𝗈𝗇𝗌, 𝗌𝗈 𝖾𝗏𝖾𝗋𝗒𝗈𝗇𝖾 𝗐𝗂𝗅𝗅 𝗌𝖾𝖾!   

<b>🔞 𝖠𝖽𝗆𝗂𝗇 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌:</b>

- /mute - 𝖬𝗎𝗍𝖾 𝖠 𝖴𝗌𝖾𝗋 
- /tmute - 𝖳𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝖬𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋. 𝖤𝗑𝖺𝗆𝗉𝗅𝖾 𝗍𝗂𝗆𝖾 𝗏𝖺𝗅𝗎𝖾𝗌: 𝟦𝗆 = 𝟦 𝗆𝗂𝗇𝗎𝗍𝖾𝗌, 𝟥𝗁 = 𝟥 𝗁𝗈𝗎𝗋𝗌, 𝟨𝖽 = 𝟨 𝖽𝖺𝗒𝗌, 𝟧𝗐 = 𝟧 𝗐𝖾𝖾𝗄𝗌. 
- /unmute - 𝖴𝗇mute 𝖺 𝗎𝗌𝖾𝗋.  
𝖤𝗑𝖺𝗆𝗉𝗅𝖾𝗌:
- 𝖬𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝖿𝗈𝗋 𝗍𝗐𝗈 𝗁𝗈𝗎𝗋𝗌. 
-> /tmute @𝗎𝗌𝖾𝗋𝗇𝖺𝗆𝖾 𝟤𝗁
"""
    CNTRY_TXT = """Use /Country (Country name)
- Get info about Country 
"""
    TRNT_TXT = """This feature will be added soon"""
    SHORT_TXT = """To Short your big urls
- Command /Short Link 
"""
    WEATHER_TXT = """Under development"""
    BUTTON_TXT = """Help: <b>𝖡𝗎𝗍𝗍𝗈𝗇𝗌</b>
@The_obanai_bot 𝗌𝗎𝗉𝗉𝗈𝗋𝗍𝗌 𝖻𝗈𝗍𝗁 𝗎𝗋𝗅 𝖺𝗇𝖽 𝖺𝗅𝖾𝗋𝗍 𝗂𝗇𝗅𝗂𝗇𝖾 𝖻𝗎𝗍𝗍𝗈𝗇𝗌, 𝗇𝗈𝗐 𝗅𝖾𝗍𝗌 𝗌𝖾𝖾 𝗁𝗈𝗐 𝗍𝗈 𝗂𝗆𝗉𝗅𝖾𝗆𝖾𝗇𝗍 𝗂𝗍. 
<b>𝖭𝖡:</b>
𝟣. 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝗐𝗂𝗅𝗅 𝗇𝗈𝗍 𝖺𝗅𝗅𝗈𝗐𝗌 𝗒𝗈𝗎 𝗍𝗈 𝗌𝖾𝗇𝖽 𝖻𝗎𝗍𝗍𝗈𝗇𝗌 𝗐𝗂𝗍𝗁𝗈𝗎𝗍 𝖺𝗇𝗒 𝖼𝗈𝗇𝗍𝖾𝗇𝗍, 𝗌𝗈 𝖼𝗈𝗇𝗍𝖾𝗇𝗍 𝗂𝗌 𝗆𝖺𝗇𝖽𝖺𝗍𝗈𝗋𝗒. 
𝟤. 𝖳𝗁𝗂𝗌 𝖻𝗈𝗍 𝗌𝗎𝗉𝗉𝗈𝗋𝗍𝗌 𝖻𝗎𝗍𝗍𝗈𝗇𝗌 𝗐𝗂𝗍𝗁 𝖺𝗇𝗒 𝗍𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝗆𝖾𝖽𝗂𝖺 𝗍𝗒𝗉𝖾. 
𝟥. 𝖡𝗎𝗍𝗍𝗈𝗇𝗌 𝗌𝗁𝗈𝗎𝗅𝖽 𝖻𝖾 𝗉𝗋𝗈𝗉𝖾𝗋𝗅𝗒 𝖿𝗈𝗋𝗆𝖺𝗍𝗍𝖾𝖽 𝖺𝗌 𝖻𝖾𝗅𝗈𝗐 𝗈𝗋 𝖾𝗅𝗌𝖾 𝗋𝖾𝗌𝗎𝗅𝗍 𝗐𝗂𝗅𝗅 𝖻𝖾 𝗆𝖺𝗅𝖿𝗈𝗋𝗆𝖾𝖽. 
<b>𝖴𝖱𝖫 𝖻𝗎𝗍𝗍𝗈𝗇𝗌:</b>
- 𝗌𝗂𝗇𝗀𝗅𝖾 𝖻𝗎𝗍𝗍𝗈𝗇 
<code>[𝖡𝗎𝗍𝗍𝗈𝗇](𝖻𝗎𝗍𝗍𝗈𝗇𝗎𝗋𝗅://𝗍.𝗆𝖾/𝗌𝖺𝗄𝗎𝗋𝖺𝖻𝗈𝗍𝗎𝗉𝖽𝖺𝗍𝖾𝗌)</code>
- 𝖣𝗈𝗎𝖻𝗅𝖾 𝖻𝗎𝗍𝗍𝗈𝗇 
<code>[𝖡𝗎𝗍𝗍𝗈𝗇𝟣](𝖻𝗎𝗍𝗍𝗈𝗇𝗎𝗋𝗅://𝗍.𝗆𝖾/telegram)
[𝖡𝗎𝗍𝗍𝗈𝗇𝟤](𝖻𝗎𝗍𝗍𝗈𝗇𝗎𝗋𝗅://𝗍.𝗆𝖾/telegram)</code>
- 𝖣𝗈𝗎𝖻𝗅𝖾 𝖻𝗎𝗍𝗍𝗈𝗇𝗌 𝗂𝗇 𝖲𝖺𝗆𝖾 𝖱𝖺𝗐 
<code>[𝖡𝗎𝗍𝗍𝗈𝗇𝟣](𝖻𝗎𝗍𝗍𝗈𝗇𝗎𝗋𝗅://𝗍.𝗆𝖾/𝗌𝖺𝗄𝗎𝗋𝖺𝖻𝗈𝗍𝗎𝗉𝖽𝖺𝗍𝖾𝗌)
[𝖡𝗎𝗍𝗍𝗈𝗇𝟤](𝖻𝗎𝗍𝗍𝗈𝗇𝗎𝗋𝗅://𝗍.𝗆𝖾/𝗌𝖺𝗆𝗂𝗇𝗌𝗎𝗆𝖾𝗌𝗁:𝗌𝖺𝗆𝖾)</code>
<b>𝖠𝗅𝖾𝗋𝗍 𝖻𝗎𝗍𝗍𝗈𝗇𝗌:</b>
<code>[𝖡𝗎𝗍𝗍𝗈𝗇](𝖻𝗎𝗍𝗍𝗈𝗇𝖺𝗅𝖾𝗋𝗍:𝗍𝗁𝗂𝗌 𝗂𝗌 𝖺𝗇 𝖺𝗅𝖾𝗋𝗍!)</code>
"""
    AUTOFILTER_TXT = """<b>Auto Filter</b>
<b>𝖭𝗈𝗍𝖾:</b>
𝟣. 𝖬𝖺𝗄𝖾 𝗆𝖾 𝗍𝗁𝖾 𝖺𝖽𝗆𝗂𝗇 𝗈𝖿 𝗒𝗈𝗎𝗋 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 𝗂𝖿 𝗂𝗍'𝗌 𝗉𝗋𝗂𝗏𝖺𝗍𝖾. 
𝟤. 𝗆𝖺𝗄𝖾 𝗌𝗎𝗋𝖾 𝗍𝗁𝖺𝗍 𝗒𝗈𝗎𝗋 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 𝖽𝗈𝖾𝗌 𝗇𝗈𝗍 𝖼𝗈𝗇𝗍𝖺𝗂𝗇𝗌 𝖼𝖺𝗆 𝗋𝗂𝗉, 𝗉𝗈𝗋𝗇 𝖺𝗇𝖽 𝖿𝖺𝗄𝖾 𝖿𝗂𝗅𝖾𝗌. 
𝟥. 𝖥𝗈𝗋𝗐𝖺𝗋𝖽 𝗍𝗁𝖾 𝗅𝖺𝗌𝗍 𝗆𝖾𝗌𝗌𝖺𝗀𝖾 𝗍𝗈 𝗆𝖾 𝗐𝗂𝗍𝗁 𝗊𝗎𝗈𝗍𝖾𝗌.  𝖨'𝗅𝗅 𝖺𝖽𝖽 𝖺𝗅𝗅 𝗍𝗁𝖾 𝖿𝗂𝗅𝖾𝗌 𝗂𝗇 𝗍𝗁𝖺𝗍 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 𝗍𝗈 𝗆𝗒 𝖽𝖻.
"""
    CONNECTION_TXT = """<b>𝖢𝗈𝗇𝗇𝖾𝖼𝗍𝗂𝗈𝗇𝗌</b>
𝖴𝗌𝖾𝖽 𝗍𝗈 𝖼𝗈𝗇𝗇𝖾𝖼𝗍 𝖻𝗈𝗍 𝗍𝗈 𝖯𝖬 𝗐𝗁𝗂𝖼𝗁 𝗅𝖾𝗍 𝗐𝗂𝗅𝗅 𝗒𝗈𝗎 𝗍𝗈 𝖾𝗑𝖾𝖼𝗎𝗍𝖾 𝖻𝗈𝗍𝗁 𝗇𝗈𝗋𝗆𝖺𝗅 𝖿𝗂𝗅𝗍𝖾𝗋 𝗋𝖾𝗅𝖺𝗍𝖾𝖽 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖺𝗇𝖽 𝗌𝗈𝗆𝖾 𝗈𝗍𝗁𝖾𝗋 𝗌𝖾𝗇𝗌𝗂𝗍𝗂𝗏𝖾 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝗋𝗂𝗀𝗁𝗍 𝖿𝗋𝗈𝗆 𝗍𝗁𝖾 𝖯𝖬 𝗍𝗁𝖺𝗍 𝗐𝗂𝗅𝗅 𝗋𝖾𝖿𝗅𝖾𝖼𝗍 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉 𝗐𝗁𝗂𝖼𝗁 𝗁𝖾𝗅𝗉𝗌 𝗒𝗈𝗎 𝗍𝗈 𝗄𝖾𝖾𝗉 𝗍𝗁𝖾 𝖿𝗂𝗅𝗍𝖾𝗋 𝖺𝖽𝖽𝗂𝗍𝗂𝗈𝗇𝗌 𝖺𝗇𝖽 𝗈𝗍𝗁𝖾𝗋 𝗌𝗍𝗎𝖿𝖿𝗌 𝗉𝗋𝗂𝗏𝖺𝗍𝖾 𝖺𝗇𝖽 𝗁𝖾𝗅𝗉𝗌 𝗍𝗈 𝗉𝗋𝖾𝗏𝖾𝗇𝗍 𝖿𝗅𝗈𝗈𝖽𝗂𝗇𝗀. 
𝖭𝖮𝖳𝖤:
𝟣. 𝖮𝗇𝗅𝗒 𝖺𝖽𝗆𝗂𝗇𝗌 𝖼𝖺𝗇 𝖺𝖽𝖽 𝖺 𝖼𝗈𝗇𝗇𝖾𝖼𝗍𝗂𝗈𝗇. 
𝟤. 𝖨𝗇 𝖺 𝖼𝗁𝖺𝗍 𝗒𝗈𝗎 𝖼𝖺𝗇 𝗌𝗂𝗆𝗉𝗅𝗒 𝗎𝗌𝖾 𝗍𝗁𝖾 /connect 𝖿𝗈𝗋 𝗌𝗍𝖺𝗋𝗍𝗂𝗇𝗀 𝖺 𝖼𝗈𝗇𝗇𝖾𝖼𝗍𝗂𝗈𝗇  
𝟥. 𝖨𝗇 𝖯𝖬 𝗒𝗈𝗎 𝗆𝗎𝗌𝗍 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝖼𝗁𝖺𝗍 𝗂𝖽 𝗋𝗂𝗀𝗁𝗍 𝖺𝖿𝗍𝖾𝗋 𝗍𝗁𝖾 𝖼𝗈𝗆𝗆𝖺𝗇𝖽. 
𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖺𝗇𝖽 𝖴𝗌𝖺𝗀𝖾: 
/connect - 𝖼𝗈𝗇𝗇𝖾𝖼𝗍 𝖺 𝗉𝖺𝗋𝗍𝗂𝖼𝗎𝗅𝖺𝗋 𝖼𝗁𝖺𝗍 𝗍𝗈 𝗒𝗈𝗎𝗋 𝖯𝖬 
/disconnect  - 𝖽𝗂𝗌𝖼𝗈𝗇𝗇𝖾𝖼𝗍 𝖿𝗋𝗈𝗆 𝖺 𝖼𝗁𝖺𝗍 
/connections - 𝗅𝗂𝗌𝗍 𝖺𝗅𝗅 𝗒𝗈𝗎𝗋 𝖼𝗈𝗇𝗇𝖾𝖼𝗍𝗂𝗈𝗇𝗌

"""
    FILTER_TXT ="""𝖲𝖾𝗅𝖾𝖼𝗍 𝖺 𝖿𝗂𝗅𝗍𝖾𝗋 𝗍𝗒𝗉𝖾 𝖻𝖾𝗅𝗈𝗐:"""
    PIN_TXT = """<b>𝖯𝖨𝖭:</b>
𝖠𝗅𝗅 𝗍𝗁𝖾 𝗉𝗂𝗇 𝗋𝖾𝗅𝖺𝗍𝖾𝖽 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖼𝖺𝗇 𝖻𝖾 𝖿𝗈𝗎𝗇𝖽 𝗁𝖾𝗋𝖾; 𝗄𝖾𝖾𝗉 𝗒𝗈𝗎𝗋 𝖼𝗁𝖺𝗍 𝗎𝗉 𝗍𝗈 𝖽𝖺𝗍𝖾 𝗈𝗇 𝗍𝗁𝖾 𝗅𝖺𝗍𝖾𝗌𝗍 𝗇𝖾𝗐𝗌 𝗐𝗂𝗍𝗁 𝖺 𝗌𝗂𝗆𝗉𝗅𝖾 𝗉𝗂𝗇𝗇𝖾𝖽 𝗆𝖾𝗌𝗌𝖺𝗀𝖾!  

<b>𝖠𝖽𝗆𝗂𝗇 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌:</b> 
- /pin: 𝖯𝗂𝗇 𝗍𝗁𝖾 𝗆𝖾𝗌𝗌𝖺𝗀𝖾 𝗒𝗈𝗎 𝗋𝖾𝗉𝗅𝗂𝖾𝖽 𝗍𝗈 𝖬𝖾𝗌𝗌𝖺𝗀𝖾 𝗍𝗈 𝗌𝖾𝗇𝖽 𝖺 𝗇𝗈𝗍𝗂𝖿𝗂𝖼𝖺𝗍𝗂𝗈𝗇 𝗍𝗈 𝗀𝗋𝗈𝗎𝗉 𝗆𝖾𝗆𝖻𝖾𝗋𝗌. 
- /unpin: 𝖴𝗇𝗉𝗂𝗇 𝗍𝗁𝖾 𝖼𝗎𝗋𝗋𝖾𝗇𝗍 𝗉𝗂𝗇𝗇𝖾𝖽 𝗆𝖾𝗌𝗌𝖺𝗀𝖾. 𝖨𝖿 𝗎𝗌𝖾𝖽 𝖺𝗌 𝖺 𝗋𝖾𝗉𝗅𝗒, 𝗎𝗇𝗉𝗂𝗇𝗌 𝗍𝗁𝖾 𝗋𝖾𝗉𝗅𝗂𝖾𝖽 𝗍𝗈 𝗆𝖾𝗌𝗌𝖺𝗀𝖾.
"""
    TGRAPH_TXT ="""<b>𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗉𝗁</b>
𝖣𝗈 𝖺𝗌 𝗒𝗈𝗎 𝗐𝗂𝗌𝗁 𝗐𝗂𝗍𝗁 telegra.ph 𝗆𝗈𝖽𝗎𝗅𝖾!
<b>𝖴𝗌𝖺𝗀𝖾:</b>

- /telegraph - 𝖲𝖾𝗇𝖽 𝗆𝖾 𝖯𝗂𝖼𝗍𝗎𝗋𝖾 𝗈𝗋 𝖵𝗂𝖽𝖾 𝖴𝗇𝖽𝖾𝗋 (𝟧𝖬𝖡)

<b>𝖭𝖮𝖳𝖤:</b>
• 𝖲𝖺𝗄𝗎𝗋𝖺 𝗌𝗁𝗈𝗎𝗅𝖽 𝗁𝖺𝗏𝖾 𝖺𝖽𝗆𝗂𝗇 𝗉𝗋𝗂𝗏𝗂𝗅𝗅𝖺𝗀𝖾.
• 𝖳𝗁𝗂𝗌 𝖢𝗈𝗆𝗆𝖺𝗇𝖽 𝖨𝗌 𝖠𝗏𝖺𝗂𝗅𝖺𝖻𝗅𝖾 𝗂𝗇 𝗀𝗈𝗎𝗉𝗌 𝖺𝗇𝖽 𝗉𝗆𝗌
• 𝖳𝗁𝗂𝗌 𝖢𝗈𝗆𝗆𝖺𝗇𝖽 𝖢𝖺𝗇 𝖻𝖾 𝗎𝗌𝖾𝖽 𝖻𝗒 𝖾𝗏𝖾𝗋𝗒𝗈𝗇𝖾
"""
    IMBD_TXT ="""<b>Search</b>
- 𝖲𝖾𝖺𝗋𝖼𝗁 𝖿𝗂𝗅𝗆 𝖽𝖾𝗍𝖺𝗂𝗅𝗌 𝗐𝗂𝗍𝗁𝗈𝗎𝗍 𝗅𝖾𝖺𝗏𝗂𝗇𝗀 𝗍𝖾𝗅𝖾𝗀𝗋𝖺𝗆
- 𝖲𝖾𝖺𝗋𝖼𝗁 𝖺𝗇𝗒𝗍𝗁𝗂𝗇𝗀 𝗐𝗂𝗍𝗁𝗈𝗎𝗍 𝗅𝖾𝖺𝗏𝗂𝗇𝗀 𝗍𝖾𝗅𝖾𝗀𝗋𝖺𝗆
<b>U𝗌𝖺𝗀𝖾:</b>
- /imdb - 𝗀𝖾𝗍 𝗍𝗁𝖾 𝖿𝗂𝗅𝗆 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇 𝖿𝗋𝗈𝗆 𝖨𝖬𝖣𝖻 𝗌𝗈𝗎𝗋𝖼𝖾
- /search - 𝗀𝖾𝗍 𝗍𝗁𝖾 𝖿𝗂𝗅𝗆 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇 𝖿𝗋𝗈𝗆 𝗏𝖺𝗋𝗂𝗈𝗎𝗌 𝗌𝗈𝗎𝗋𝖼𝖾𝗌
"""
    INFO_TXT ="""<b>𝖨𝗇𝖿𝗈</b>
𝖦𝖾𝗍 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇 𝖺𝖻𝗈𝗎𝗍 𝗌𝗈𝗆𝖾𝗍𝗁𝗂𝗇𝗀!
<b>𝖴𝗌𝖺𝗀𝖾:</b>
➥ /id - 𝗀𝖾𝗍 𝗍𝗁𝖾 𝗂𝖽 𝗈𝖿 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝖾𝖽 𝗎𝗌𝖾𝗋
➥ /info - 𝗀𝖾𝗍 𝗍𝗁𝖾 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇 𝖺𝖻𝗈𝗎𝗍 𝖺 𝗎𝗌𝖾𝗋
"""
    EXTRAMOD_TXT = """<b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of tessa

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>
"""
    ADMIN_TXT = """
<b>🤖Bot Commands and Usage</b>

• /filter 𝗈𝗋 /add <code>𝖺𝖽𝖽 𝖺 𝖿𝗂𝗅𝗍𝖾𝗋</code>
• /filters 𝗈𝗋 /viewfilters <code>𝗅𝗂𝗌𝗍 𝖺𝗅𝗅 𝗍𝗁𝖾 𝖿𝗂𝗅𝗍𝖾𝗋𝗌 𝗈𝖿 𝖺 𝖼𝗁𝖺𝗍</code>
• /stop 𝗈𝗋 /del <code>𝖽𝖾𝗅𝖾𝗍𝖾 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝗂𝖼 𝖿𝗂𝗅𝗍𝖾𝗋</code>
• /stopall 𝗈𝗋 /delall <code>𝖽𝖾𝗅𝖾𝗍𝖾 𝗍𝗁𝖾 𝗐𝗁𝗈𝗅𝖾 𝖿𝗂𝗅𝗍𝖾𝗋𝗌 𝗂𝗇 𝖺 𝖼𝗁𝖺𝗍</code>
• /imdb <code>𝗀𝖾𝗍 𝗍𝗁𝖾 𝖿𝗂𝗅𝗆 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇 𝖿𝗋𝗈𝗆 𝖨𝖬𝖣𝖻 𝗌𝗈𝗎𝗋𝖼𝖾</code>
• /search <code>𝗀𝖾𝗍 𝗍𝗁𝖾 𝖿𝗂𝗅𝗆 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇 𝖿𝗋𝗈𝗆 𝗏𝖺𝗋𝗂𝗈𝗎𝗌 𝗌𝗈𝗎𝗋𝖼𝖾𝗌</code>
• /purge <code>𝖣𝖾𝗅𝖾𝗍𝖾 𝖺𝗅𝗅 𝗆𝖾𝗌𝗌𝖺𝗀𝖾𝗌 Of Groups</code>
• /telegraph <code>𝖲𝖾𝗇𝖽 𝗆𝖾 𝖯𝗂𝖼𝗍𝗎𝗋𝖾 𝗈𝗋 𝖵𝗂𝖽𝖾 𝖴𝗇𝖽𝖾𝗋 (𝟧𝖬𝖡)</code>
• /pin <code>𝖯𝗂𝗇 𝗍𝗁𝖾 𝗆𝖾𝗌𝗌𝖺𝗀𝖾 𝗒𝗈𝗎 𝗋𝖾𝗉𝗅𝗂𝖾𝖽 𝗍𝗈 𝖬𝖾𝗌𝗌𝖺𝗀𝖾 𝗍𝗈 𝗌𝖾𝗇𝖽 𝖺 𝗇𝗈𝗍𝗂𝖿𝗂𝖼𝖺𝗍𝗂𝗈𝗇 𝗍𝗈 𝗀𝗋𝗈𝗎𝗉 𝗆𝖾𝗆𝖻𝖾𝗋𝗌</code>
• /unpin <code>𝖴𝗇𝗉𝗂𝗇 𝗍𝗁𝖾 𝖼𝗎𝗋𝗋𝖾𝗇𝗍 𝗉𝗂𝗇𝗇𝖾𝖽 𝗆𝖾𝗌𝗌𝖺𝗀𝖾</code>
• /id <code>𝗀𝖾𝗍 𝗍𝗁𝖾 𝗂𝖽 𝗈𝖿 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝖾𝖽 𝗎𝗌𝖾𝗋</code>
• /info <code>𝗀𝖾𝗍 𝗍𝗁𝖾 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇 𝖺𝖻𝗈𝗎𝗍 𝖺 𝗎𝗌𝖾𝗋</code>
• /covid [country name] <code>𝖦𝖾𝗍 𝗂𝗇𝖿𝗈 𝖺𝖻𝗈𝗎𝗍 𝖼𝗈𝗏𝗂𝖽 𝖼𝖺𝗌𝖾𝗌 𝗂𝗇 𝗒𝗈𝗎𝗋 𝖼𝗈𝗎𝗇𝗍𝗋𝗒</code>
• /song [Song Name] <code>𝖳𝗈 𝗀𝖾𝗍 𝗍𝗁𝖾 𝗌𝗈𝗇𝗀</code>
• /tr [language code][reply] <code>𝖳𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾 𝗋𝖾𝗉𝗅𝗂𝖾𝖽 𝗆𝖾𝗌𝗌𝖺𝗀𝖾 𝗍𝗈 𝗌𝗉𝖾𝖼𝗂𝖿𝗂𝖼 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾.</code>
• /Country (Country name) <code>Get info about Country</code>
• /stats <code>Get Activities Of Bots</code>
"""
    STATUS_TXT = """𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌: <code>{}</code>
𝖳𝗈𝗍𝖺𝗅 𝖬𝖾𝗆𝖻𝖾𝗋𝗌: <code>{}</code>
𝖳𝗈𝗍𝖺𝗅 𝖢𝗁𝖺𝗍𝗌: <code>{}</code>
𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾: <code>{}</code> 𝙼𝚒𝙱
"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""



    USER_DETAILS = "<b>PM FROM:</b>\nName: {} {}\nId: {}\nUname: @{}\nScam: {}\nRestricted: {}\nStatus: {}\nDc Id: {}"
    PM_TXT_ATT = "<b>Message from:</b> {}\n<b>Name:</b> {}\n\n{}"
    PM_MED_ATT = "<b>Message from:</b> {} \n<b>Name:</b> {}"

    MY_CAPTION = "FILE : <code>{file_name}</code> \nSize : <i>{file_size}</i>\n\n Hello {message.from_user.first_name} \n\n⚠️ കോപ്പി റൈറ്റ് ഉള്ളത് കൊണ്ട് ഈ ഒരു ഫയൽ 1 മണിക്കൂർകൊണ്ട് ഇവിടെ നിന്നും ഡിലേറ്റാവും...!!!\n\nഇവിടെ നിന്നും വേറെ എവിടേലും മാറ്റിയതിന് ശേഷം ഡൗൺലോഡ് ചെയ്യുക...!!!\n\nFILES FORWARD TO YOUR SAVED MESSAGES\n\nAll files here Gets Deleted With in 1 hour."
 




    START_TXT = """
<b>ʜᴇʏ, {}

ɪ ᴀᴍ ᴀ ᴘᴏᴡᴇʀꜰᴜʟ ᴀᴜᴛᴏꜰɪʟᴛᴇʀ + ᴍᴀɴᴜᴀʟꜰɪʟᴛᴇʀ + ꜰɪʟᴇsᴛᴏʀᴇ ʙᴏᴛ.
ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ɪ ᴡɪʟʟ ɢɪᴠᴇ ᴍᴏᴠɪᴇs ᴏʀ sᴇʀɪᴇs ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴘᴍ !!

🌿 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/TGxFOXY'>ꜰᴏxʏ ᴛɢ</a></b>"""
    HELP_TXT = """
<b>Hᴇʏ {}

ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴꜱ ʙᴇʟᴏᴡ ᴛᴏ ɢᴇᴛ ᴅᴏᴄᴜᴍᴇɴᴛᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ꜱᴘᴇᴄɪꜰɪᴄ ᴍᴏᴅᴜʟᴇꜱ..

🧨 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/TGxFOXY'>ꜰᴏxʏ ᴛɢ</a></b>"""

    HELPER_TXT = """
<b>ʜᴇy {}

ʜᴇʀᴇ ɪꜱ ᴛʜᴇ ʜᴇʟᴩ ꜰᴏʀ ᴍy ᴄᴏᴍᴍᴀɴᴅꜱ.

💞 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/TGxFOXY'>ꜰᴏxʏ ᴛɢ</a></b>"""

    ABOUT_TXT = """<b>
‣ ᴍʏ ɴᴀᴍᴇ : <a href='https://t.me/at3moviesofficalbot'>ᴍᴀsᴛᴇʀ​​​</a>
‣ ᴄʀᴇᴀᴛᴏʀ : <a href='tg://settings'>ᴛʜɪs ᴘᴇʀsᴏɴ​</a>
‣ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/TGxFOXY'>ꜰᴏxʏ ᴛɢ​​</a>
‣ ʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢʀᴀᴍ</a>
‣ ʟᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org/download/releases/3.0/'>ᴘʏᴛʜᴏɴ 3</a>
‣ ᴅᴀᴛᴀ ʙᴀsᴇ : <a href='https://www.mongodb.com/'>ᴍᴏɴɢᴏ ᴅʙ</a>
‣ ʙᴏᴛ sᴇʀᴠᴇʀ : <a href='https://t.me/quickfastt'>ǫᴜɪᴄᴋ ꜰᴀsᴛ​</a>
‣ ʙᴜɪʟᴅ sᴛᴀᴛᴜs : ᴠ2.7.1 [sᴛᴀʙʟᴇ​]</b>"""
    SOURCE_TXT = """<b>NOTE:
⚠️ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ᴀɴ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ
◆ ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : <a href='https://t.me/MLZ_BOTZ_SUPPORT'>ᴍʟᴢ ʙᴏᴛᴢ​</a>

◆ ᴅᴇᴠs ​1 : <a href='https://t.me/Autofilter_vipBot'>ʟɪsᴀ</a>
◆ ᴅᴇᴠs 2​ : <a href='https://t.me/crazyspiderr'>ꜱᴘɪᴅᴇʀ</a></b>"""
    MANUELFILTER_TXT = """ʜᴇʟᴘ: <b>ꜰɪʟᴛᴇʀꜱ</b>
- ꜰɪʟᴛᴇʀ ɪꜱ ᴀ ꜰᴇᴀᴛᴜʀᴇ ᴡᴇʀᴇ ᴜꜱᴇʀꜱ ᴄᴀɴ ꜱᴇᴛ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ʀᴇᴘʟɪᴇꜱ ꜰᴏʀ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴋᴇʏᴡᴏʀᴅ ᴀɴᴅ ɪ ᴡɪʟʟ ʀᴇꜱᴘᴏɴᴅ ᴡʜᴇɴᴇᴠᴇʀ ᴀ ᴋᴇʏᴡᴏʀᴅ ɪꜱ ꜰᴏᴜɴᴅ ɪɴ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ
<b>ɴᴏᴛᴇ:</b>
1. ᴛʜɪꜱ ʙᴏᴛ ꜱʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟᴇɢᴇ.
2. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ.
3. ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ ʜᴀᴠᴇ ᴀ ʟɪᴍɪᴛ ᴏꜰ 64 ᴄʜᴀʀᴀᴄᴛᴇʀꜱ.
Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:
• /filter - <code>ᴀᴅᴅ ᴀ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ</code>
• /filters - <code>ʟɪꜱᴛ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴛᴇʀꜱ ᴏꜰ ᴀ ᴄʜᴀᴛ</code>
• /del - <code>ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ</code>
• /delall - <code>ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡʜᴏʟᴇ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ (ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)</code>"""

    BUTTON_TXT = """ʜᴇʟᴘ: <b>ʙᴜᴛᴛᴏɴꜱ</b>
- ᴛʜɪꜱ ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛꜱ ʙᴏᴛʜ ᴜʀʟ ᴀɴᴅ ᴀʟᴇʀᴛ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴꜱ.
<b>ɴᴏᴛᴇ:</b>
1. ᴛᴇʟᴇɢʀᴀᴍ ᴡɪʟʟ ɴᴏᴛ ᴀʟʟᴏᴡꜱ ʏᴏᴜ ᴛᴏ ꜱᴇɴᴅ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴄᴏɴᴛᴇɴᴛ, ꜱᴏ ᴄᴏɴᴛᴇɴᴛ ɪꜱ ᴍᴀɴᴅᴀᴛᴏʀʏ.
2. ᴛʜɪꜱ ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛꜱ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ.
3. ʙᴜᴛᴛᴏɴꜱ ꜱʜᴏᴜʟᴅ ʙᴇ ᴘʀᴏᴘᴇʀʟʏ ᴘᴀʀꜱᴇᴅ ᴀꜱ ᴍᴀʀᴋᴅᴏᴡɴ ꜰᴏʀᴍᴀᴛ
<b>ᴜʀʟ ʙᴜᴛᴛᴏɴꜱ:</b>
<code>[Button Text](buttonurl:https://t.me/MLZ_BOTZ)</code>
<b>ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ:</b>
<code>[Button Text](buttonalert:ᴛʜɪꜱ ɪꜱ ᴀɴ ᴀʟᴇʀᴛ ᴍᴇꜱꜱᴀɢᴇ)</code>"""

    AUTOFILTER_TXT = """ʜᴇʟᴘ: <b>ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ</b>
<b>ɴᴏᴛᴇ: Fɪʟᴇ Iɴᴅᴇx</b>
1. ᴍᴀᴋᴇ ᴍᴇ ᴛʜᴇ ᴀᴅᴍɪɴ ᴏꜰ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪꜰ ɪᴛ'ꜱ ᴘʀɪᴠᴀᴛᴇ.
2. ᴍᴀᴋᴇ ꜱᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴅᴏᴇꜱ ɴᴏᴛ ᴄᴏɴᴛᴀɪɴꜱ ᴄᴀᴍʀɪᴘꜱ, ᴘᴏʀɴ ᴀɴᴅ ꜰᴀᴋᴇ ꜰɪʟᴇꜱ.
3. ꜰᴏʀᴡᴀʀᴅ ᴛʜᴇ ʟᴀꜱᴛ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴍᴇ ᴡɪᴛʜ Qᴜᴏᴛᴇꜱ. ɪ'ʟʟ ᴀᴅᴅ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇꜱ ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴍʏ ᴅʙ.

<b>Nᴏᴛᴇ: AᴜᴛᴏFɪʟᴛᴇʀ</b>
1. Aᴅᴅ ᴛʜᴇ ʙᴏᴛ ᴀs ᴀᴅᴍɪɴ ᴏɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
2. Usᴇ /connect ᴀɴᴅ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ ᴛʜᴇ ʙᴏᴛ.
3. Usᴇ /settings ᴏɴ ʙᴏᴛ's PM ᴀɴᴅ ᴛᴜʀɴ ᴏɴ AᴜᴛᴏFɪʟᴛᴇʀ ᴏɴ ᴛʜᴇ sᴇᴛᴛɪɴɢs ᴍᴇɴᴜ."""

    CONNECTION_TXT = """ʜᴇʟᴘ: <b>ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ</b>
- ᴜꜱᴇᴅ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʙᴏᴛ ᴛᴏ ᴘᴍ ꜰᴏʀ ᴍᴀɴᴀɢɪɴɢ ꜰɪʟᴛᴇʀꜱ 
- ɪᴛ ʜᴇʟᴘꜱ ᴛᴏ ᴀᴠᴏɪᴅ ꜱᴘᴀᴍᴍɪɴɢ ɪɴ ɢʀᴏᴜᴘꜱ.
<b>ɴᴏᴛᴇ:</b>
1. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ᴀ ᴄᴏɴɴᴇᴄᴛɪᴏɴ.
2. ꜱᴇɴᴅ <code>/ᴄᴏɴɴᴇᴄᴛ</code> ꜰᴏʀ ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴘᴍ
Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:
• /connect  - <code>ᴄᴏɴɴᴇᴄᴛ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴛᴏ ʏᴏᴜʀ ᴘᴍ</code>
• /disconnect  - <code>ᴅɪꜱᴄᴏɴɴᴇᴄᴛ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ</code>
• /connections - <code>ʟɪꜱᴛ ᴀʟʟ ʏᴏᴜʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ</code>"""

    EXTRAMOD_TXT = """ʜᴇʟᴘ: Exᴛʀᴀ Mᴏᴅᴜʟᴇs
<b>ɴᴏᴛᴇ:</b>
ᴛʜᴇꜱᴇ ᴀʀᴇ ᴛʜᴇ ᴇxᴛʀᴀ ꜰᴇᴀᴛᴜʀᴇꜱ ᴏꜰ ᴛʜɪꜱ ʙᴏᴛ
Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:
• /id - <code>ɢᴇᴛ ɪᴅ ᴏꜰ ᴀ ꜱᴘᴇᴄɪꜰɪᴇᴅ ᴜꜱᴇʀ.</code>
• /info  - <code>ɢᴇᴛ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜꜱᴇʀ.</code>
• /imdb  - <code>ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ɪᴍᴅʙ ꜱᴏᴜʀᴄᴇ.</code>
• /search  - <code>ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ᴠᴀʀɪᴏᴜꜱ ꜱᴏᴜʀᴄᴇꜱ.</code>"""

    ADMIN_TXT = """ʜᴇʟᴘ: Aᴅᴍɪɴ Mᴏᴅs
<b>ɴᴏᴛᴇ:</b>
Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋs Fᴏʀ Mʏ Aᴅᴍɪɴs
Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:
• /logs - <code>ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʀᴇᴄᴇɴᴛ ᴇʀʀᴏʀꜱ</code>
• /stats - <code>ᴛᴏ ɢᴇᴛ ꜱᴛᴀᴛᴜꜱ ᴏꜰ ꜰɪʟᴇꜱ ɪɴ ᴅʙ. [Tʜɪs Cᴏᴍᴍᴀɴᴅ Cᴀɴ Bᴇ Usᴇᴅ Bʏ Aɴʏᴏɴᴇ]</code>
• /delete - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.</code>
• /users - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴜꜱᴇʀꜱ ᴀɴᴅ ɪᴅꜱ.</code>
• /chats - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴄʜᴀᴛꜱ ᴀɴᴅ ɪᴅꜱ</code>
• /leave  - <code>ᴛᴏ ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ.</code>
• /disable  -  <code>ᴛᴏ ᴅɪꜱᴀʙʟᴇ ᴀ ᴄʜᴀᴛ.</code>
• /ban  - <code>ᴛᴏ ʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /unban  - <code>ᴛᴏ ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /channel - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴄʜᴀɴɴᴇʟꜱ</code>
• /broadcast - <code>ᴛᴏ ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ</code>
• /grp_broadcast - <code>Tᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs.</code>
• /gfilter - <code>ᴛᴏ ᴀᴅᴅ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs</code>
• /gfilters - <code>ᴛᴏ ᴠɪᴇᴡ ʟɪsᴛ ᴏғ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs</code>
• /delg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ</code>
• /request - <code>Tᴏ sᴇɴᴅ ᴀ Mᴏᴠɪᴇ/Sᴇʀɪᴇs ʀᴇᴏ̨ᴜᴇsᴛ ᴛᴏ ʙᴏᴛ ᴀᴅᴍɪɴs. Oɴʟʏ ᴡᴏʀᴋs ᴏɴ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ. [Tʜɪs Cᴏᴍᴍᴀɴᴅ Cᴀɴ Bᴇ Usᴇᴅ Bʏ Aɴʏᴏɴᴇ]</code>
• /delallg - <code>Tᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ Gғɪʟᴛᴇʀs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.</code>
• /deletefiles - <code>Tᴏ ᴅᴇʟᴇᴛᴇ CᴀᴍRɪᴘ ᴀɴᴅ PʀᴇDVD Fɪʟᴇs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.</code>"""

    STATUS_TXT =  """╔════❰ ꜱᴛᴀᴛᴜꜱ ❱═❍⊱❁۪۪
║┏━━━━━━━━━━━━━━━➣
║┣⪼<b>📂 Tᴏᴛᴀʟ Fɪʟᴇs: <code>{}</code></b>
║┣⪼<b>👤 Tᴏᴛᴀʟ Usᴇʀs: <code>{}</code></b>
║┣⪼<b>♻️ Tᴏᴛᴀʟ Cʜᴀᴛs: <code>{}</code></b>
║┣⪼<b>🗃️ Usᴇᴅ Sᴛᴏʀᴀɢᴇ: <code>{}</code> 𝙼𝚒𝙱</b>
║┣⪼<b>🆓 Fʀᴇᴇ Sᴛᴏʀᴀɢᴇ: <code>{}</code> 𝙼𝚒𝙱</b>
║┗━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁"""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Nᴀᴍᴇ - {}
"""
    ALRT_TXT = """ʜᴇʟʟᴏ {},
ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ʏᴏᴜʀ ᴍᴏᴠɪᴇ ʀᴇQᴜᴇꜱᴛ,
ʀᴇQᴜᴇꜱᴛ ʏᴏᴜʀ'ꜱ..."""

    OLD_ALRT_TXT = """ʜᴇʏ {},
ʏᴏᴜ ᴀʀᴇ ᴜꜱɪɴɢ ᴏɴᴇ ᴏꜰ ᴍʏ ᴏʟᴅ ᴍᴇꜱꜱᴀɢᴇꜱ, 
ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ᴛʜᴇ ʀᴇQᴜᴇꜱᴛ ᴀɢᴀɪɴ."""

    CUDNT_FND = """ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏᴛʜɪɴɢ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ {}
ᴅɪᴅ ʏᴏᴜ ᴍᴇᴀɴ ᴀɴʏ ᴏɴᴇ ᴏꜰ ᴛʜᴇꜱᴇ?"""

    I_CUDNT = """ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏ ᴍᴏᴠɪᴇ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ {}"""

    I_CUD_NT = """ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏ ᴍᴏᴠɪᴇ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ {}.
ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ ꜱᴘᴇʟʟɪɴɢ ᴏɴ ɢᴏᴏɢʟᴇ ᴏʀ ɪᴍᴅʙ..."""

    MVE_NT_FND = """ᴛʜɪꜱ ᴍᴏᴠɪᴇ ɪꜱ ɴᴏᴛ ʏᴇᴛ  ʀᴇʟᴇᴀꜱᴇᴅ ᴏʀ ᴀᴅᴅᴇᴅ ᴛᴏ ᴅᴀᴛᴀʙᴀꜱᴇ"""

    TOP_ALRT_MSG = """ᴄ​ʜᴇᴄᴋɪɴɢ Fᴏʀ Mᴏᴠɪᴇ Iɴ Dᴀᴛᴀʙᴀsᴇ..."""

    MELCOW_ENG = """
👋🏻 ʜᴇʏ {}

          ❤ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ❤
➖➖➖➖➖➖➖➖➖➖➖➖
        ▷  {}  ◁
➖➖➖➖➖➖➖➖➖➖➖➖

🏅 ɪꜰ ʏᴏᴜʀ ᴍᴏᴠɪᴇs ꜱᴘᴇʟʟɪɴɢ ɪꜱ ᴄᴏʀʀᴇᴄᴛ ᴅᴇꜰɪɴᴇᴛʟʏ ɢᴇᴛ ʏᴏᴜʀ ᴍᴏᴠɪᴇ ꜰɪʟᴇ ɪɴ ᴏᴜʀ ɢʀᴏᴜᴘ

🏅 ᴊᴏɪɴ ᴏᴜʀ ᴏᴛᴛ ᴄʜᴀɴɴᴇʟ ɪɴ ᴅᴇsᴄʀɪᴘᴛɪᴏɴ 🏅

📕 ɴʙ: ᴘʟᴇᴀꜱᴇ ꜱʜᴀʀᴇ ᴏᴜʀ ɢʀᴏᴜᴘ ʟɪɴᴋ..... ᴍᴀᴋᴇ ꜱᴜᴘᴘᴏʀᴛ"""
    OWNER_INFO = """
<b>⍟───[ ᴏᴡɴᴇʀ ᴅᴇᴛᴀɪʟꜱ ]───⍟
    
• ꜰᴜʟʟ ɴᴀᴍᴇ : ᴀꜰsᴀʟʜᴀsʜɪᴍ​
• ᴜꜱᴇʀɴᴀᴍᴇ : @crazyspiderr
• ᴘᴇʀᴍᴀɴᴇɴᴛ ᴅᴍ ʟɪɴᴋ : <a href='t.me/TGxFOXY'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a></b>"""
    NORSLTS = """
★ #𝗡𝗼𝗥𝗲𝘀𝘂𝗹𝘁𝘀 ★

𝗜𝗗 <b>: {}</b>
𝗡𝗮𝗺𝗲 <b>: {}</b>
𝗠𝗲𝘀𝘀𝗮𝗴𝗲 <b>: {}</b>"""

    CAPTION = """
•───────────────────•
📁 ➤ 𝒀𝒐𝒖𝒓 𝑭𝒊𝒍𝒆 𝑵𝒂𝒎𝒆 : {file_name}

🧲 ➤ 𝒀𝒐𝒖𝒓 𝑭𝒊𝒍𝒆 𝑺𝒊𝒛𝒆 : {file_size}

✮ 𝐉𝐨𝐢𝐧 𝐍𝐨𝐰 » <a href='https://t.me/CinemaKovilakam_Group'>@CinemaKovilakam</a>
✮ 𝐉𝐨𝐢𝐧 𝐍𝐨𝐰 » @at3movies
◈ ━━━━━━━━ ● ━━━━━━━ ◈"""

    IMDB_TEMPLATE_TXT = """
<b>{title}</b>

⭐️<b>{rating}</b> | ⏰ <b>{runtime}</b> | 📆 <b>{release_date}</b>

● <b>{genres}</b>
● <b>{languages}</b>

📖 sᴛᴏʀʏ : <b>{plot}</b> 

© {message.chat.title}
"""
    ALL_FILTERS = """
<b>Hᴇʏ {}, Tʜᴇsᴇ ᴀʀᴇ ᴍʏ ᴛʜʀᴇᴇ ᴛʏᴘᴇs ᴏғ ғɪʟᴛᴇʀs.</b>"""
    
    GFILTER_TXT = """
<b>Wᴇʟᴄᴏᴍᴇ ᴛᴏ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs. Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs ᴀʀᴇ ᴛʜᴇ ғɪʟᴛᴇʀs sᴇᴛ ʙʏ ʙᴏᴛ ᴀᴅᴍɪɴs ᴡʜɪᴄʜ ᴡɪʟʟ ᴡᴏʀᴋ ᴏɴ ᴀʟʟ ɢʀᴏᴜᴘs.</b>
    
Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
• /gfilter - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /gfilters - <code>Tᴏ ᴠɪᴇᴡ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs.</code>
• /delg - <code>Tᴏ ᴅᴇʟᴇᴛᴇ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /delallg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ɢʟᴏʙᴀʟ ꜰɪʟᴛᴇʀꜱ.</code>"""
    
    FILE_STORE_TXT = """
<b>Fɪʟᴇ sᴛᴏʀᴇ ɪs ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴡʜɪᴄʜ ᴡɪʟʟ ᴄʀᴇᴀᴛᴇ ᴀ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ ᴏғ ᴀ sɪɴɢʟᴇ ᴏʀ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</b>

Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
• /batch - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ʙᴀᴛᴄʜ ʟɪɴᴋ ᴏғ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</code>
• /link - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ sɪɴɢʟᴇ ғɪʟᴇ sᴛᴏʀᴇ ʟɪɴᴋ.</code>
• /pbatch - <code>Jᴜsᴛ ʟɪᴋᴇ /batch, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇs ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴs.</code>
• /plink - <code>Jᴜsᴛ ʟɪᴋᴇ /link, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇ ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴ.</code>"""

    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>v2.7.1 [ Sᴛᴀʙʟᴇ ]</code></b>
©ᴍʟᴢ ʙᴏᴛᴢ"""

    LOGO = """
𝑺𝒕𝒂𝒓𝒕𝒊𝒏𝒈.......🥵"""

    GROUP_TXT = """
<b>⍟ Cʜᴀɴɴᴇʟs & Gʀᴏᴜᴘs Mᴏᴅᴜʟᴇ ⍟

🎬 Cᴏᴍᴘʟᴇᴛᴇ Mᴏᴠɪᴇ Rᴇǫᴜᴇsᴛɪɴɢ Gʀᴏᴜᴘ.
🚦 Aʟʟ Lᴀɴɢᴜᴀɢᴇs Mᴏᴠɪᴇs & Sᴇʀɪᴇs.
🗣️ Bᴏᴛ Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ.
📢 Bᴏᴛ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ.</b>"""

    WHYJOIN = """
⚠ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ⚠

Iғ ᴛʜᴇ ɢʀᴏᴜᴘ ᴄᴏᴘʏ ʀɪɢʜᴛ ɪꜱ ʟᴏꜱᴛ , ᴡʜᴇɴ ᴀ ɴᴇᴡ ɢʀᴏᴜᴘ ɪꜱ ꜱᴛᴀʀᴛᴇᴅ, ɪᴛ ᴡɪʟʟ ʙᴇ ɴᴏᴛɪғɪᴇᴅ ᴏɴ ᴛʜɪꜱ ᴄʜᴀɴɴᴇʟ🤥

©ᴍʟᴢ ʙᴏᴛᴢ"""
    QINFO = """
ʜᴇʏ ʙʀᴏ ☻

Cʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛʜᴇ ғɪʟᴇꜱ ʏᴏᴜ ᴡᴀɴᴛ ᴀɴᴅ ꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ⇓⇓

©ᴍʟᴢ ʙᴏᴛᴢ"""
    REPRT_MSG = """ Reported To Admin"""

    SONG_TXT = """
𝚂𝙾𝙽𝙶 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙼𝙾𝙳𝚄𝙻𝙴

𝚂𝙾𝙽𝙶 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙼𝙾𝙳𝚄𝙻𝙴, 𝙵𝙾𝚁 𝚃𝙷𝙾𝚂𝙴 𝚆𝙷𝙾 𝙻𝙾𝚅𝙴 𝙼𝚄𝚂𝙸𝙲. 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙵𝙴𝙰𝚃𝚄𝙴 𝙵𝙾𝚁 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙰𝙽𝚈 𝚂𝙾𝙽𝙶 𝚆𝙸𝚃𝙷 𝚂𝚄𝙿𝙴𝚁 𝙵𝙰𝚂𝚃 𝚂𝙿𝙴𝙴𝙳.𝚆𝙾𝚁𝙺𝚂 𝙾𝙽𝙻𝚈 𝙾𝙽 𝙶𝚁𝙾𝚄𝙿𝚂../

𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂

⏭️ /song 𝚂𝙾𝙽𝙶 𝙽𝙰𝙼𝙴 

𝚆𝙾𝚁𝙺𝚂 𝙱𝙾𝚃𝙷 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙿𝙼
@at3movies"""

    VIDEO_TXT ="""𝙷𝙴𝙻𝙿 𝚈𝙾𝚄 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝚅𝙸𝙳𝙴𝙾 𝙵𝚁𝙾𝙼 𝚈𝙾𝚄𝚃𝚄𝙱𝙴.
• 𝘜𝘴𝘢𝘨𝘦
𝘠𝘰𝘶 𝘊𝘢𝘯 𝘋𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘈𝘯𝘺 𝘝𝘪𝘥𝘦𝘰 𝘍𝘳𝘰𝘮 𝘠𝘰𝘶𝘵𝘶𝘣𝘦
𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
• 𝘛𝘺𝘱𝘦 /video or /mp4 𝘈𝘯𝘥 (https://youtu.be/example...)
• 𝘌𝘹𝘢𝘮𝘱𝘭𝘦:
<code>/mp4 https://youtu.be/example...</code>
<code>/video https://youtu.be/example...</code>
"""
    TTS_TXT = """Help: <b> TTS 🎤 module:</b>
Translate text to speech
<b>Commands and Usage:</b>
• /tts <text> : convert text to speech"""
    GTRANS_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖦𝗈𝗈𝗀𝗅𝖾 𝖳𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾𝗋
𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚝𝚛𝚊𝚗𝚜𝚕𝚊𝚝𝚎 𝚊 𝚝𝚎𝚡𝚝 𝚝𝚘 𝖺𝗇𝗒 𝚕𝚊𝚗𝚐𝚞𝚊𝚐𝚎𝚜 𝚢𝚘𝚞 𝚠𝚊𝚗𝚝. 𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚠𝚘𝚛𝚔𝚜 𝚘𝚗 𝚋𝚘𝚝𝚑 𝚙𝚖 𝚊𝚗𝚍 𝚐𝚛𝚘𝚞𝚙 ✯
➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
➪/tr - 𝖳𝗈 𝗍𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾𝗋 𝗍𝖾𝗑𝗍𝗌 𝗍𝗈 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝖼 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾
➤ 𝖭𝗈𝗍𝖾:
𝖶𝗁𝗂𝗅𝖾 𝗎𝗌𝗂𝗇𝗀 /tr 𝗒𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝗍𝗁𝖾 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾 𝖼𝗈𝖽𝖾
➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾: /𝗍𝗋 𝗆𝗅
• 𝖾𝗇 = 𝖤𝗇𝗀𝗅𝗂𝗌𝗁
• 𝗆𝗅 = 𝖬𝖺𝗅𝖺𝗒𝖺𝗅𝖺𝗆
• 𝗁𝗂 = 𝖧𝗂𝗇𝖽𝗂"""

    TELE_TXT = """<b>▫️HELP: Telegraph▪️</b>
Do as you wish with telegra.ph module!
</b>USAGE:</b>
✒️ /telegraph - Send me Picture or Vide Under (5MB)
<b>NOTE:</b>
• This Command Is Available in goups and pms
• This Command Can be used by everyone
"""
    CORONA_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖢𝗈𝗏𝗂𝖽
𝚃𝚑𝚒𝚜 𝙲𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚔𝚗𝚘𝚠 𝚍𝚊𝚒𝚕𝚢 𝚒𝚗𝚏𝚘𝚛𝚖𝚊𝚝𝚒𝚘𝚗 𝚊𝚋𝚘𝚞𝚝 𝚌𝚘𝚟𝚒𝚍 
➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
➪ /covid - 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝖼𝗈𝗎𝗇𝗍𝗋𝗒 𝗇𝖺𝗆𝖾 𝗍𝗈 𝗀𝖾𝗍 𝖼𝗈𝗏𝗂𝖽𝖾 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇
➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
<code>/covid 𝖨𝗇𝖽𝗂𝖺</code>
⚠️ This service has been stopped
"""
    ABOOK_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖠𝗎𝖽𝗂𝗈𝖻𝗈𝗈𝗄
𝚈𝚘𝚞 𝚌𝚊𝚗 𝚌𝚘𝚗𝚟𝚎𝚛𝚝 𝚊 𝙿𝙳𝙵 𝚏𝚒𝚕𝚎 𝚝𝚘 𝚊 𝚊𝚞𝚍𝚒𝚘 𝚏𝚒𝚕𝚎 𝚠𝚒𝚝𝚑 𝚝𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 ✯
➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
➪ /audiobook: 𝖱𝖾𝗉𝗅𝗒 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗍𝗈 𝖺𝗇𝗒 𝖯𝖣𝖥 𝗍𝗈 𝗀𝖾𝗇𝖾𝗋𝖺𝗍𝖾 𝗍𝗁𝖾 𝖺𝗎𝖽𝗂𝗈
"""
    DEPLOY_TXT= """𝙸𝙵 𝚈𝙾𝚄 𝙵𝙰𝙲𝙸𝙽𝙶 𝙰𝙽𝚈 𝙸𝚂𝚂𝚄𝙴 𝙸𝙽 𝚃𝙷𝙴 𝚁𝙴𝙿𝙾 𝙲𝙾𝙽𝚃𝙰𝙲𝚃 𝙼𝙴..."""
   
    PINGS_TXT = """<b>Ping Testing:</b>
Helps you to know your ping 🚶🏼‍♂️
<b>Commands:</b>
• /alive - To check you are alive.
• /runs - To Some fun.
• /ping - <b>To get your ping.</b>
<b>🛠️Usage🛠️ :</b>
• This commands can be used in pm and groups
• This commands can be used buy everyone in the groups and bots pm
• Share us for more features
"""

    STICKER_TXT = """<b>𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙼𝙾𝙳𝚄𝙻𝙴 𝚃𝙾 𝙵𝙸𝙽𝙳 𝙰𝙽𝚈 𝚂𝚃𝙸𝙲𝙺𝙴𝚁𝚂 𝙸𝙳.</b>
• 𝐔𝐒𝐀𝐆𝐄
To Get Sticker ID
 
  ⭕ 𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
 
◉ Reply To Any Sticker [/stickerid]"""

    FONT_TXT= """⚙️ 𝐔𝐒𝐀𝐆𝐄
𝐘𝐎𝐔 𝐂𝐀𝐍 𝐔𝐒𝐄 𝐓𝐇𝐈𝐒 𝐌𝐎𝐃𝐔𝐋𝐄 𝐓𝐎 𝐂𝐇𝐀𝐍𝐆𝐄 𝐅𝐎𝐍𝐓 𝐒𝐓𝐘𝐋𝐄 
<b>COMMAND</b> : /font your text (optional)
        <b> Eg:- /font Hello</b>
 <i>This feature added by ©ᴍʟᴢ ʙᴏᴛᴢ"""
    JSON_TXT = """<b>JSON:</b>
Bot returns json for all replied messages with /json or /js
<b>Features:</b>
Message Editting JSON
Pm Support
Group Support
<b>Note:</b>
<b>Everyone can use this command , if spaming happens bot will automatically ban you from the group.</b>"""

    WHOIS_TXT ="""<b>WHOIS MODULE</b>
Note:- <b>Give a user details</b>
•/whois :-give a user full details 📑
"""
    URLSHORT_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖴𝗋𝗅 𝗌𝗁𝗈𝗋𝗍𝗇𝖾𝗋
<i><b>𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚜𝚑𝚘𝚛𝚝 𝚊 𝚞𝚛𝚕 </i></b>
➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
➪ /short: <b>𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝗅𝗂𝗇𝗄 𝗍𝗈 𝗀𝖾𝗍 𝗌𝗁𝗈𝗋𝗍𝖾𝖽 𝗅𝗂𝗇𝗄𝗌</b>
➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
<code>/short https://youtu.be/example...</code>
"""
    FUN_TXT ="""<b>Gᴀᴍᴇs</b> 
    
<b>⚡ 𝙹𝚄𝚂𝚃 𝚂𝙾𝙼𝙴 𝙺𝙸𝙽𝙳 𝙾𝙵 𝙵𝚄𝙽 𝚃𝙷𝙸𝙽𝙶'𝚂 ⚡</b>
 
𝟣. /dice - 𝚁𝙾𝙻𝙴 𝚃𝙷𝙴 𝙳𝙸𝙲𝙴 
𝟤. /Throw 𝗈𝗋 /Dart - 𝚃𝙾 𝙼𝙰𝙺𝙴 𝙳𝙰𝚁𝚃 
3. /Runs - 𝚂𝙾𝙼𝙴 𝚁𝙰𝙽𝙳𝙾𝙼 𝙳𝙸𝙰𝙻𝙾𝙶𝚄𝙴𝚂 
4. /Goal or /Shoot - 𝚃𝙾 𝙼𝙰𝙺𝙴 𝙰 𝙶𝙾𝙰𝙻 𝙾𝚁 𝚂𝙷𝙾𝙾𝚃
5. /luck or /cownd - 𝚂𝙿𝙸𝙽 𝙰𝙽𝙳 𝚃𝚁𝚈 𝚈𝙾𝚄𝚁 𝙻𝚄𝙲𝙺
"""
    CON_TXT = """<b><u>ᴄᴏᴜɴᴛʀʏ ɪɴғᴏ</b></u>
<b>Tʜɪs ᴍᴏᴅᴜʟᴇ ɪs ᴛᴏ ғɪɴᴅ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴄᴏᴜɴᴛʀɪᴇs</b>
• /country [𝖼𝗈𝗎𝗇𝗍𝗋𝗒 𝗇𝖺𝗆𝖾] 
𝖤𝗑𝖺𝗆𝗉𝗅𝖾 :- <code>/country India</code>
"""

    CARB_TXT = """𝗛𝗘𝗟𝗣 𝗙𝗢𝗥 𝗖𝗔𝗥𝗕𝗢𝗡
𝙲𝙰𝚁𝙱𝙾𝙽 𝙸𝚂 𝙰 𝙵𝙴𝚄𝚃𝚄𝚁𝙴 𝚃𝙾 𝙼𝙰𝙺𝙴 𝚃𝙷𝙴 𝙸𝙼𝙰𝙶𝙴 𝙰𝚂 𝚂𝙷𝙾𝚆𝙽 𝙸𝙽 𝚃𝙷𝙴 𝚃𝙾𝙿 𝚆𝙸𝚃𝙷 𝚈𝙾𝚄𝚁𝙴 𝚃𝙴𝚇𝚃𝚂.
𝙵𝙾𝚁 𝚄𝚂𝙸𝙽𝙶 𝚃𝙷𝙴 𝙼𝙾𝙳𝚄𝙻𝙴 𝙹𝚄𝚂𝚃 𝚂𝙴𝙽𝙳 𝚃𝙷𝙴 𝚃𝙴𝚇𝚃 𝙰𝙽𝙳 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙸𝚃 𝚆𝙸𝚃𝙷 /carbon 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝚃𝙷𝙴 𝙱𝙾𝚃 𝚆𝙸𝙻𝙻 𝚁𝙴𝙿𝙻𝚈 𝚆𝙸𝚃𝙷 𝚃𝙷𝙴 𝙲𝙰𝚁𝙱𝙾𝙽 𝙸𝙼𝙰𝙶𝙴

"""
    GEN_PASS = """
Help: Password Generator

There Is Nothing To Know More. Send Me The Limit Of Your Password.
- I Will Give The Password Of That Limit.

Commands and Usage:
• /genpassword or /genpw 20

NOTE:
• Only Digits Are Allowed
• Maximum Allowed Digits Till 84 
(I Can't Generate Passwords Above The Length 84)
• IMDb should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member.
"""
    SHARE_TXT = """
𝗛𝗘𝗟𝗣 𝗙𝗢𝗥 𝗦𝗛𝗔𝗥𝗘 𝗧𝗘𝗫𝗧

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
• /share - 𝚁𝚎𝚙𝚕𝚢 𝚆𝚒𝚝𝚑 𝙰𝚗𝚢 𝚃𝚎𝚡𝚝 𝚃𝚘 𝚂𝚎𝚗𝚍 𝚃𝚑𝚒𝚜 𝙲𝚘𝚖𝚖𝚊𝚗𝚍
"""
    PIN_TXT = """
PIN MODULE
𝙿𝙸𝙽 𝙰 𝙼𝙴𝚂𝚂𝙰𝙶𝙴../

𝙰𝙻𝙻 𝚃𝙷𝙴 𝙿𝙸𝙽 𝚁𝙴𝙿𝙻𝙰𝚃𝙴𝙳 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙲𝙰𝙽 𝙱𝙴 𝙵𝙾𝚄𝙽𝙳 𝙷𝙴𝚁𝙴::

📌𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴📌

◉ /pin :- 𝚃𝙾 𝙿𝙸𝙽 𝚃𝙷𝙴 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝙾𝙽 𝚈𝙾𝚄𝚁 𝙲𝙷𝙰𝚃𝚂
◉ /unpin :- 𝚃𝙾 𝚄𝙽𝙿𝙸𝙽 𝚃𝙷𝙴 𝙲𝚄𝚁𝚁𝙴𝙴𝙽𝚃 𝙿𝙸𝙽𝙽𝙴𝙳 𝙼𝙴𝚂𝙰𝙰𝙶𝙴
"""
    RESTRIC_TXT = """
➤ 𝐇𝐞𝐥𝐩: Mᴜᴛᴇ 🚫

𝚃𝚑𝚎𝚜𝚎 𝚊𝚛𝚎 𝚝𝚑𝚎 𝚌𝚘𝚖𝚖𝚊𝚗𝚍𝚜 𝚊 𝚐𝚛𝚘𝚞𝚙 𝚊𝚍𝚖𝚒𝚗 𝚌𝚊𝚗 𝚞𝚜𝚎 𝚝𝚘 𝚖𝚊𝚗𝚊𝚐𝚎 𝚝𝚑𝚎𝚒𝚛 𝚐𝚛𝚘𝚞𝚙 𝚖𝚘𝚛𝚎 𝚎𝚏𝚏𝚒𝚌𝚒𝚎𝚗𝚝𝚕𝚢.

➪/ban: 𝖳𝗈 𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋 𝖿𝗋𝗈𝗆 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/unban: 𝖳𝗈 𝗎𝗇𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/tban: 𝖳𝗈 𝗍𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋.
➪/mute: 𝖳𝗈 𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/unmute: 𝖳𝗈 𝗎𝗇𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/tmute: 𝖳𝗈 𝗍𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋.

➤ 𝖭𝗈𝗍𝖾:
𝖶𝗁𝗂𝗅𝖾 𝗎𝗌𝗂𝗇𝗀 /tmute 𝗈𝗋 /tban 𝗒𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝗍𝗁𝖾 𝗍𝗂𝗆𝖾 𝗅𝗂𝗆𝗂𝗍.

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾: /𝗍𝖻𝖺𝗇 2𝖽 𝗈𝗋 /𝗍𝗆𝗎𝗍𝖾 2𝖽.
𝖸𝗈𝗎 𝖼𝖺𝗇 𝗎𝗌𝖾 𝗏𝖺𝗅𝗎𝖾𝗌: 𝗆/𝗁/𝖽. 
 • 𝗆 = 𝗆𝗂𝗇𝗎𝗍𝖾𝗌
 • 𝗁 = 𝗁𝗈𝗎𝗋𝗌
 • 𝖽 = 𝖽𝖺𝗒𝗌
"""
    ZOMBIES_TXT = """
𝙷𝙴𝙻𝙿 𝚈𝙾𝚄 𝚃𝙾 𝙺𝙸𝙲𝙺 𝚄𝚂𝙴𝚁𝚂

Kick incative members from group. Add me as admin with ban users permission in group.

Commands and Usage:
• /inkick - command with required arguments and i will kick members from group.
• /instatus - to check current status of chat member from group.
• /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
• /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
• /dkick - to kick deleted accounts.
"""
    GRP_TXT = """
<b>𝐇𝐄𝐘 𝐁𝐑𝐔𝐇
╔════❰ ᴜᴘᴅᴀᴛᴇs​ ❱═❍⊱❁۪۪
║┏━━━━━━━━━━━━━━━➣
║┣🎯✨ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴄɪɴᴇᴍᴀ ᴋᴏᴠɪʟᴀᴋᴀᴍ❣
║┣⚡️🍬ᴊᴏɪɴ ᴏᴜʀ ᴍᴏᴠɪᴇꜱ & ᴄʜᴀɴɴᴇʟꜱ 🦋✨
║┗━━━━━━━━━━━━━━━➣
║┏━━━━━━━━━━━━━━━➣
║┣
║┣🔰✥ <a href='https://t.me/CinemaKovilakam'>▷ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ ◁</a>
║┣
║┣🔰✥ <a href='https://t.me/at3movies'>▷ ᴄɪɴᴇᴍᴀ ᴋᴏᴠɪʟᴀᴋᴀᴍ ɢʀᴏᴜᴘ 1 ◁</a>
║┣
║┣🔰✥ <a href='https://t.me/CinemaKovilakam_Group'>▷ ᴄɪɴᴇᴍᴀ ᴋᴏᴠɪʟᴀᴋᴀᴍ ɢʀᴏᴜᴘ 2 ◁</a>
║┣
║┣🔰✥ <a href='https://t.me/MLZ_BOTZ'>▷ ʙᴏᴛ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ​ ◁</a>
║┣
║┣🦋 ᴍʏ ʙᴇsᴛ ғʀɪᴇɴᴅ :<a href='tg://settings'>ᴛʜɪs ᴘᴇʀsᴏɴ 🙌</a>
║┣
║┗━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁</b>"""

    DELF = """
ꜱᴏʀʀʏ ᴅᴜᴅᴇ ☹,

ᴄᴜʀʀᴇɴᴛʟʏ ᴛʜɪꜱ ʙᴜᴛᴛᴏɴ ɪꜱ ɴᴏᴛ ᴡᴏʀᴋ.. 
ʙᴇᴄᴀᴜꜱᴇ ʙᴜᴛᴛᴏɴ ᴡᴇʀᴇ ʀᴇᴍᴏᴠᴇᴅ ʙʏ ᴀᴅᴍɪɴ

©ᴍʟᴢ ʙᴏᴛᴢ"""
    INFO = """
⚠ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ⚠

ᴀꜰᴛᴇʀ 10 ᴍɪɴᴜᴛᴇꜱ ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴅᴇʟᴇᴛᴇᴅ

ɪꜰ ʏᴏᴜ ᴅᴏ ɴᴏᴛ ꜱᴇᴇ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ ᴍᴏᴠɪᴇ / sᴇʀɪᴇs ꜰɪʟᴇ, ʟᴏᴏᴋ ᴀᴛ ᴛʜᴇ ɴᴇxᴛ ᴘᴀɢᴇ

©ᴍʟᴢ ʙᴏᴛᴢ"""
    FORMAT = """
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
⇄ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ ⇄
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯

ɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ꜱᴇʀɪᴇꜱ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ

⋆ ᴇxᴀᴍᴘʟᴇ : Loki S01E01
⋆ ᴇxᴀᴍᴘʟᴇ : Uncharted

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)"""

    TIPS = """
▣ ᴛɪᴘs ▣

☆ ᴛʏᴘᴇ ᴄᴏʀʀᴇᴄᴛ sᴘᴇʟʟɪɴɢ (ɢᴏᴏɢʟᴇ)

☆ ɪғ ʏᴏᴜ ɴᴏᴛ ɢᴇᴛ ʏᴏᴜʀ ғɪʟᴇ ɪɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ᴛʜᴇɴ ᴛʜᴇ ɴᴇxᴛ sᴛᴇᴘ ɪs ᴄʟɪᴄᴋ ɴᴇxᴛ ʙᴜᴛᴛᴏɴ.

☆ ᴄᴏɴᴛɪɴᴜᴇ ᴛʜɪs ᴍᴇᴛʜᴏᴅ ᴛᴏ ɢᴇᴛᴛɪɴɢ ʏᴏᴜ ғɪʟᴇ

❣ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴍʟᴢ ʙᴏᴛᴢ"""

        
