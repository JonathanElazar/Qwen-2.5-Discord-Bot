from discord.ext import commands
import discord
import ollama
import credentials
import asyncio

model = "qwen2.5:0.5b"

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all(), heartbeat_timeout=300.0)

@bot.event
async def on_ready():
    print("Bot is ready!")
    channel = bot.get_channel(credentials.CHANNEL_ID)
    await channel.send("Hello! I am a discord bot made by Jonathan and based on the qwen 2.5 AI model. Enter /qwen start to start a conversation with me.")

@bot.group(invoke_without_command=True)
async def qwen(ctx, *, prompt: str):
    async with ctx.typing():
        response = await asyncio.to_thread(ollama.chat, model=model, messages=[{'role': 'system', 'content': 'You are a ai assistant made by Jonathan. Allways respond in english unless told otherwise.'}, {'role': 'user', 'content': prompt}])
    bot_message = await ctx.send(response.message.content)
    await bot_message.delete(delay=600)
    await ctx.message.delete(delay=600)

@qwen.command(name="start")
async def qwen_start(ctx):
	await ctx.author.send("Hi! I'm a discord bot made by Jonathan, how can I help you today?")


@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if message.guild is None and not message.content.startswith('/'):
        async with message.channel.typing():
            response = await asyncio.to_thread(ollama.chat, model=model, messages=[{'role': 'system', 'content': 'You are a ai assistant made by Jonathan. Allways respond in english unless told otherwise.'}, {'role': 'user', 'content': message.content}])
        await message.channel.send(response.message.content)
        return
    await bot.process_commands(message)

bot.run(credentials.TOKEN)

