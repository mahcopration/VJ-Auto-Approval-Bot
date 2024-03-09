# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "10917377"))
    API_HASH = getenv("API_HASH", "22bfe49f4482c5cb5424729249a5f097")
    BOT_TOKEN = getenv("BOT_TOKEN", "6931230949:AAH4EP6ceOhqEKJwtZG7Hoo9KVd_4cpPdo0")
    FSUB = getenv("FSUB", "Call_me_futurepilot")
    CHID = int(getenv("CHID", "-1001938180288"))
    SUDO = list(map(int, getenv("SUDO", "6412533552 6112399514").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://mahsoom:mahsoommah123@@cluster0.agyddbb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
