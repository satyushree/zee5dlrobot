class script(object):

    START_TEXT = """<b>Hai ,
    
I'm A simple Zee5 link downloader bot With Permanent Thumbnail Supportð¯.
Please send me any Zee5 link, I can upload it to telegram as File/Video.
Currently I'm in beta mode ð¥º, If found any bugs, report @shreevish !
Click <i>/help</i> for more details....</b>"""


    HELP_USER = """<b>Hai, Follow these steps..</b>
 
1. Send Custom Thumbnail (It will be saved permenantly!)
2. Send your zee5 url and select desired option.
NOTE: Download may take some time! So please wait for it to complete!"""


    ABOUT_TEXT = """â­ï¸<b>My Name : TroJanZ Zee5 DL</b>
â­ï¸<b>Creater :</b> @shreevish
â­ï¸<b>Language :</b> <code>Python3</code>
â­ï¸<b>Library :</b> <a href='https://docs.pyrogram.org/'>Pyrogram 1.0.7</a> 
â­ï¸<b>Source Code :</b> ð <a href='https://telegram.dog/All_Movie_rockers'>Click Here</a>"""



    FORMAT_SELECTION = """<b>Choose appropriate option</b> <a href='{}'>â¬ï¸</a>
ð  - Stream format
ð  - File format
<i>NOTE : Taking high resolutions may result in files above 2GB and hence cannot Upload to TG. So better select a medium resolution.</i> ð
"""    
    
    UPGRADE_TEXT = "PING at @shreevish"
    
    DOWNLOAD_START = "Downloading to my server ð¥ Please wait...â³ ððð it takes time depend on File Size"
    
    UPLOAD_START = "Yay,File Download Successfully ð Now Uploading to Telegram ð¤"
    
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."

    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "**Thank you for Using Meh!! â¤ï¸**\nJoin @All_Movie_Rockers"
    
    SAVED_CUSTOM_THUMB_NAIL = "<b>âCustom thumbnail Saved.\nThis thumbnail will be Permanent for all future uploads\n\nDo /delthumb to clear your thumbnail!</b>"
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "â Custom Thumbnail cleared succesfully."
    
    SHOW_THUMB = "@All_Movie_Rockers\n\nUse /delthumb to clear this thumbnail."
    
    NO_THUMB = "SEDð No saved thumbnails Found!!"
    
    CUSTOM_CAPTION_UL_FILE = "<b>{newname}\n\nÂ©ï¸ @All_Movie_Rockers</b>"
    
    TIMEOUT = "<b><i>Sorry for the delay. It'll help reduce the flood wait</i> ð\n\nWait for {} sec and try again.</b>"