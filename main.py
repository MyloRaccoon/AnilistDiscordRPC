from pystray import Icon, Menu, MenuItem 
from PIL import Image
import threading
import server
from dotenv import load_dotenv
from os import getenv

load_dotenv()
ICON_PATH = getenv('ICON_PATH')

stop_event = threading.Event()

def on_clicked(icon, item):
	stop_event.set()
	icon.stop()

threading.Thread(
	target=server.run,
	args=(stop_event,),
	daemon=True
).start()

icon = Icon(
	'AniList Activity RPC',
	icon= Image.open(ICON_PATH),
	menu= Menu(
		MenuItem('Quit', on_clicked)
	)
)

icon.run()