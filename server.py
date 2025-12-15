from anilist_model import get_last_activity, get_user_id
from discord_rpc import connect_rpc, update_rpc
from logger import log
from dotenv import load_dotenv
from os import getenv
import time

load_dotenv()
ANILIST_USERNAME=getenv('ANILIST_USERNAME')
ANILIST_USERID=get_user_id(ANILIST_USERNAME)
UPDATE_FREQUENCE=int(getenv('UPDATE_FREQUENCE'))

def run(stop_event):

    log('AniList Discord RPC Launched')

    rpc = connect_rpc()

    activity = get_last_activity(ANILIST_USERID)

    update_rpc(rpc, activity)

    log('RPC active')

    while not stop_event.is_set():
        new_activity = get_last_activity(ANILIST_USERID)
        if activity != new_activity:
            activity = new_activity
            update_rpc(rpc, activity)
            log(f'RPC updated, new activity: {activity}')
        time.sleep(UPDATE_FREQUENCE)

    rpc.clear()
    rpc.close()
    log('RPC cleared')
    log('AniList Discord RPC stopped')