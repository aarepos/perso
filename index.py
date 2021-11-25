from pyrogram import Client, filters
import time
import asyncio

api = Client("api")



@api.on_message(filters.command('timer'))
async def timer_func(client, message):

	timer = await message.reply_text("Timer: 0")

	for i in range(30):

		if i == 0:
			continue

		await asyncio.sleep(1)
		await timer.edit(f"Timer: {i}")


api.run()