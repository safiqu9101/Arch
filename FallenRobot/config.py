class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = "26792767"
    API_HASH = "d5892fe7d458bff884fde1f1efbaadf3"

    CASH_API_KEY = "HXV2U7BXH8LB04NV"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = ""  # A sql database url from elephantsql.com

    EVENT_LOGS = ()  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://rr:rr@cluster0.5pjchfv.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/725b20e82c195163a6fc0.jpg"

    SUPPORT_CHAT = "DOSTO_KI_PIYAR"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6581320481:AAGt5mrZ63M3dHvzZO5iaypFr0JP4jV3MAg"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "41W425DBL510"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 6060534504  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
