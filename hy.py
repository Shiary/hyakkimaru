import discord
from discord.ext import commands
import asyncio
from itertools import cycle
import time
import youtube_dl

bot=commands.Bot(command_prefix='hy!')

@bot.event
async def on_ready():
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print('--------------------')
    
@bot.command(pass_context=True)
async def ping():
    await bot.say('Saya Telah Online!!')
    await bot.say('Apa Ada Iblis Disini?')
    
@bot.command(pass_context=True)
async def mute(ctx,target:discord.Member):
    role=discord.utils.get(ctx.message.server.roles,name='Muted')
    
    await bot.add_roles(target,role)
    
@bot.command(pass_context=True)
async def warn(ctx,target:discord.Member):
    await bot.send_message(target,'Jangan Melanggar Peraturan Ya Bisa Bisa Kamu Dikick Atau Diban Lho')
    
@bot.command(pass_context=True)
async def kick(ctx,target:discord.Member):
    await bot.kick(target)
    
@bot.command(pass_context=True)
async def ban(ctx,target:discord.Member):
    await bot.ban(target)
   
bot.run('NTUxNTAwMDU3MDYxMzU5NjI2.D1zGmw.qezxgGaCLoRKwl-2EWuR8liNCdY')
