from ast import Delete
import asyncio, discord
import time
from cgitb import text
from unicodedata import name
from pydoc import describe
from turtle import title
from dice import *
from discord.ext import commands

bot = commands.Bot(command_prefix="-")

@bot.event
async def on_ready():
	print("켜졌는데 어쩌라고".format(bot))

@bot.command()
async def 도움말(ctx):
    await ctx.send("-안녕 : 안뇽!이라고 대답함 \n\n -주사위 1/2/3/4 : 주사위를 1/2/3/4개 굴리고, 그 값을 더해서 보여줌 \n\n -주사위게임 : 주사위게임을 한다. \n\n -들어와 : 음성채널에 있을 때 하서봇이 참가한다 (별 기능 없음) \n\n -나가 : 음성채널에 하서봇이 있을 때 이 기능을 쓰면 나가게 된다 (별 기능 없음) \n\n\n\n\n !추후 업데이트 예정!")
   
@bot.command()
async def 안녕(ctx):
	await ctx.send("안뇽!")

@bot.command()
async def 주사위1(ctx):
    await ctx.send("주사위 1개 굴리고 있어. 기다려봐")
    n = random.randrange(1,7)
    
    await ctx.send(str(n) + "이네, 근데 내가 왜 이걸 해주고있지..")

@bot.command()
async def 주사위2(ctx):
    await ctx.send("주사위 2개 굴리고 있어. 기다려봐")
    n = random.randrange(1,7)
    m = random.randrange(1,7)
    
    await ctx.send(str(n+m) + "이네, 근데 내가 왜 이걸 해주고있지..")


@bot.command()
async def 주사위3(ctx):
    await ctx.send("아니... 2개까지는 그럴만한데.. 하 그래.. 알겠어..주사위 3개 굴리고 있어.. 기다려봐")
    n = random.randrange(1,7)
    m = random.randrange(1,7)
    l = random.randrange(1,7)
    
    await ctx.send(str(n+m+l) + "이네, 근데 내가 왜 이걸 해주고있지..")

@bot.command()
async def 주사위4(ctx):
    await ctx.send("야.. 4개.. 하 그래.. 알겠어.. 이거 다음에는 안해줄거야.. 그래..주사위 4개 굴리고 있어.. 기다려봐")
    n = random.randrange(1,7)
    m = random.randrange(1,7)
    l = random.randrange(1,7)
    o = random.randrange(1,7)
    
    await ctx.send(str(n+m+l+o) + "이네, 근데 내가 왜 이걸 해주고있지..")

@bot.command()
async def 주사위게임(ctx):
    result, _color, bot, user = dice()
    embed = discord.Embed(title = "주사위 게임 결과", description = None, color = _color)
    embed.add_field(name = "HASEO BOT의 숫자", value = ":game_die: " + bot, inline = True)
    embed.add_field(name = ctx.author.name+"의 숫자", value = ":game_die: " + user, inline = True)
    embed.set_footer(text="결과!  " + result)
    await ctx.send(embed=embed)


@bot.command()
async def 들어와(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
        await channel.connect()

    else:
        await ctx.send("음성채널에 들어가고 오라해라;")

@bot.command()
async def 나가(ctx):
    await bot.voice_clients[0].disconnect()

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("그런 명령어가 없는데 어떻게 실행하냐;")

bot.run('OTQ2NzMyMjQwMjQ1NzU1OTQ0.Yhi_Gw.k7FSH26FbEIaCV-vYMp2XdE84E4') 