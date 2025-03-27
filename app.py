import os
import discord
import ollama
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is ready as {bot.user.name}")
    
@bot.command(name="hello")
async def hello(ctx):
    await ctx.send("Hello, I'm Ollama Bot")

@bot.command(name="ask")
async def ask(ctx, *, message):
    response = ollama.chat(model='llama3.2:1b', messages=[
        {
            'role':'system',
            'content':'You are a helpful assistant that answers the user\'s questions in no more than 100 words.',
        },
        {
            'role': 'user',
            'content':message,
        },
    ])
    await ctx.send(response['message']['content'])
    

@bot.command(name="summarise")
async def summarise(ctx):
    
    messages = [message.content async for message in ctx.channel.history(limit=10)]
    summarisePrompt= f"""
    Summarise the following messages delimited by 3 backticks
    ```
    {messages}
    ```
    """
    response = ollama.chat(model='llama3.2:1b', messages=[
        {
            'role':'system',
            'content':'You are a helpful assistant who summarises the provided messages in a short, concise manner'
        },
        {
            'role':'user',
            'content':summarisePrompt,
        }
    ])
    await ctx.send(response['message']['content'])


bot.run(os.getenv("Discord_bot_token"))

