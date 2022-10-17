from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import discord
from discord.ext import commands, tasks
import asyncio
from datetime import datetime, timedelta
from pytz import timezone



intents = discord.Intents.default()
intents.members = True
bot=commands.Bot(command_prefix='!', intents=intents)
# 886951659052351589 달토 달님반
dalto_voice_channel_id = 709351837802692714 # 패자
dalto_txt_channel_id = 936955271845122058 # 패자 출석
dispute_hidden_txt_channel = 992383504321085540 # 분쟁방 인원 히든 채팅 방
dispute_voice_channel = 967217414070747240 # 분쟁 채널
siege_voice_channel = 967217936643276860 # 공성1 < 다이곳에서 채널
dispute_txt_channel = 967217414070747238 # 분쟁 출석 체크 방:

# 패자 자동 출첵
async def pizza_time():
    await bot.wait_until_ready()
    txt_channel = bot.get_channel(dalto_txt_channel_id)
    voice_channel = bot.get_channel(dalto_voice_channel_id)
    current_vc = None
    try:
        current_vc = await voice_channel.connect()
    except:
        pass
    member_list = []
    for member in voice_channel.members:
        if "분쟁봇" in member.display_name:
            continue
        member_list.append(member.display_name)

    if member_list:
        member_list.sort()
        new_member_list = [mem.split("@")[1] if "@" in mem and str(mem) else mem for mem in member_list]
        await txt_channel.send(' '.join(new_member_list))
    else:
        await txt_channel.send("출첵할 멤버가 없다고 멘뚜주면서")
    await current_vc.disconnect()

# 분쟁 자동 출첵
async def dispute_time():
    await bot.wait_until_ready()
    txt_channel = bot.get_channel(dispute_txt_channel)
    voice_channel = bot.get_channel(dispute_voice_channel)
    current_vc = None
    try:
        current_vc = await voice_channel.connect()
    except:
        pass
    member_list = []
    for member in voice_channel.members:
        if "분쟁봇" in member.display_name:
            continue
        member_list.append(member.display_name)

    if member_list:
        member_list.sort()
        new_member_list = [mem.split("@")[1] if "@" in mem and str(mem) else mem for mem in member_list]
        await txt_channel.send(' '.join(new_member_list))
    else:
        await txt_channel.send("출첵할 멤버가 없다고 멘뚜주면서")
    await current_vc.disconnect()

# 인원조사
async def get_headcount():
    is_dispute = True
    await bot.wait_until_ready()
    txt_channel = bot.get_channel(dispute_hidden_txt_channel)
    voice_channel = None
    if is_dispute:
        voice_channel = bot.get_channel(dispute_voice_channel)
    else:
        voice_channel = bot.get_channel(siege_voice_channel)


    current_vc = None
    try:
        current_vc = await voice_channel.connect()
    except:
        pass
    member_list = []
    for member in voice_channel.members:
        if "분쟁봇" in member.display_name:
            continue
        member_list.append(member.display_name)

    dalto_count = 0
    dalto_string = ""
    yuri_count = 0
    yuri_string = ""
    hava_count = 0
    hava_string = ""
    we_count = 0
    we_string = ""
    jung_count = 0
    jung_string = ""

    headline_txt = "분쟁" if is_dispute else "공성"


    if member_list:
        member_list.sort()
        total_memeber_list = [mem.split("@")[1] if "@" in mem and str(mem) else mem for mem in member_list]
        total_memeber_string = ' '.join(total_memeber_list)
        for member in member_list:
            mem_split_string = member.split("@")[1] if "@" in member and str(member) else member
            if "달토끼" in member:
                dalto_count = dalto_count + 1
                dalto_string = dalto_string + mem_split_string + " "
            elif "유리" in member:
                yuri_count = yuri_count + 1
                yuri_string = yuri_string + mem_split_string + " "
            elif "해바라기" in member:
                hava_count = hava_count + 1
                hava_string = hava_string + mem_split_string + " "
            elif "의리" in member:
                we_count = we_count + 1
                we_string = we_string + mem_split_string + " "
            elif "정" in member:
                jung_count = jung_count + 1
                jung_string = jung_string + mem_split_string + " "
        total_count = dalto_count + yuri_count + hava_count + we_count + jung_count
        datetime_kst = datetime.now(timezone('Asia/Seoul'))
        headline_total_string = datetime_kst.strftime("%Y-%m-%d %H") + "시 " + headline_txt + " " + "인원 현황"
        content_string = "달토끼 : {}명\n> {}\n유리 : {}명\n> {}\n해바라기 : {}명\n> {}\n의리 : {}명\n> {}\n정 : {}명\n> {} \n".format(
            dalto_count,
            dalto_string,
            yuri_count,
            yuri_string,
            hava_count,
            hava_string,
            we_count,
            we_string,
            jung_count,
            jung_string
        )
        chong_string = "총합: **{}**명".format(total_count)
        if not is_dispute: # 공성이라면
            await txt_channel.send(total_memeber_string)
        await txt_channel.send("=========================\n")
        await txt_channel.send(headline_total_string)
        await txt_channel.send(content_string)
        await txt_channel.send(chong_string)
    else:
        await txt_channel.send("오늘의 {} 시간에는 참여 인원이 없습니다.".format(headline_txt))
    await current_vc.disconnect()

# 인원조사
async def get_headcount_siege():
    is_dispute = False
    await bot.wait_until_ready()
    txt_channel = bot.get_channel(dispute_hidden_txt_channel)
    voice_channel = None
    if is_dispute:
        voice_channel = bot.get_channel(dispute_voice_channel)
    else:
        voice_channel = bot.get_channel(siege_voice_channel)


    current_vc = None
    try:
        current_vc = await voice_channel.connect()
    except:
        pass
    member_list = []
    for member in voice_channel.members:
        if "분쟁봇" in member.display_name:
            continue
        member_list.append(member.display_name)

    dalto_count = 0
    dalto_string = ""
    yuri_count = 0
    yuri_string = ""
    hava_count = 0
    hava_string = ""