import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
bot=commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('로그인중입니다. ')
    print(f"봇={bot.user.name}로 연결중")
    print('연결이 완료되었습니다.')
    await bot.change_presence(status=discord.Status.online, activity=None)

@bot.command(aliases=['hi'])
async def 출첵(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()
    vc = bot.get_channel(channel.id)
    
    member_list = []
    for member in vc.members:
        if "분쟁봇" in member.display_name:
            continue
        member_list.append(member.display_name)
    
    if member_list:
        member_list = member_list.sort()
        print(member_list)
        await ctx.send(' '.join(member_list))
    else:
        await ctx.send("출첵할 멤버가 없다고 멘뚜주면서")
    await ctx.voice_client.disconnect()
@bot.command()
async def 따라하기(ctx,*,text):
    await ctx.send(text)
bot.run("ODgwMzkxMjUwNzg2Nzk1NTQw.YSdmPw.iRS9l1-R0N9Df0xtoqa4eQaUbPU")
