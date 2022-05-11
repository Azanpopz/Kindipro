from pyrogram import Client, filters
from database.Database import find, delthumb, addthumb

@Client.on_message(filters.command(['viewthumb']))
async def viewthumb(client,message):
		thumb = find(int(message.chat.id))
		if thumb :
			await client.send_photo(message.chat.id,photo =f"{thumb}")
		else:
			await message.reply_text("**You dont have any custom Thumbnail**")
	
	
@Client.on_message(filters.command(['delthumb']))
async def removethumb(client,message):
	delthumb(int(message.chat.id))
	await message.reply_text("**Custom Thumbnail Deleted Successfully**")

@Client.on_message(filters.group & filters.photo & filters.command(['addthumb']))
async def addthumbs(client,message):
	file_id = str(message.photo.file_id)
	addthumb(message.chat.id , file_id)
	await message.reply_text("**Your Custom Thumbnail Saved Successfully** ✅")
	
