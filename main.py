from anilist_model import get_last_activity, get_user_id
from discord_rpc import connect_rpc, update_rpc
from dotenv import load_dotenv
from os import getenv

load_dotenv()
ANILIST_USERNAME=getenv('ANILIST_USERNAME')

rpc = connect_rpc()

activity = get_last_activity(get_user_id(ANILIST_USERNAME))

update_rpc(rpc, activity)

print('rpc active')

try:
    while True:
        pass
except KeyboardInterrupt:
    rpc.clear()
    rpc.close()
