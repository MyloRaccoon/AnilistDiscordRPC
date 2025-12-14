from datetime import datetime

def log(message: str):
	print(message)
	with open("anilist_rpc.log", "a") as f:
		f.write(f"{datetime.now()} | {message}\n")