import sys
import requests
from importlib import import_module

from pytgcalls import idle

from CokUBot import BOT_VER, blacklist
from CokUBot import DEVS, LOGS, LOOP, bot, call_py
from CokUBot.clients import ram_ubot_on, ramulti
from CokUBot.modules import ALL_MODULES

try:
    client = ramulti()
    total = 5 - client
    bot.start()
    call_py.start()
    user = bot.get_me()
    blacklist = requests.get(
        "https://raw.githubusercontent.com/ramadhani892/Ramblack/master/ramblacklist.json"
    ).json()
    if user.id in blacklist:
        LOGS.warning(
            "TIDAK DAPAT BERJALAN, KARNA LO KONTOL MAKE SEMEMA MENA, BOT LO DI MATIIN HEHEH, LAPORKAN KE @zulfhanmt"        )
        sys.exit(1)
    if 1826643972 not in DEVS:
        LOGS.warning(
            f"乂𝗖𝗼𝗸-𝗨𝘀𝗲𝗿𝗯𝗼𝘁乂 🔥 V7.0 [AKTIF COKKK😎!!!!"
        )
        sys.exit(1)
except Exception as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("rams,CokUBot.modules." + module_name)

LOGS.info(f"Total Clients = {total} User")
LOGS.info(f"Jika {user.first_name} Membutuhkan Bantuan, Silahkan Tanyakan di Grup https://t.me/zulfhanmt")
LOGS.info(f"乂𝗖𝗼𝗸-𝗨𝘀𝗲𝗿𝗯𝗼𝘁乂 🔥 V7.0 [AKTIF COKKK😎!!!!]")


LOOP.run_until_complete(ram_ubot_on())
idle()
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    try:
        bot.run_until_disconnected()
    except ConnectionError:
        pass
