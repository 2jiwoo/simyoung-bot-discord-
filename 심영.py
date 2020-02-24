import asyncio
import discord

app = discord.Client()

token = "NjgxMDk5MDY0MjEyOTc5NzQz.XlJhQQ.LEBsdHfU0jyb0nurtzpcxgr4eX4"
calcResult = 0

@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("==========")
    game = discord.Game("님 연설")
    await app.change_presence(status=discord.Status.online, activity=game)

@app.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content.startswith("안녕"):
        await message.channel.send("안녕하시오 동무!")
    if message.content.startswith("나 김두한이다!"):
        await message.channel.send("ㅁ,뭐 김두한? 반동이다! 전위대! 전위대!")
    if message.content.startswith("그러게 왜 공산당인가 뭔가해서 이 모양이냐ㅠㅠ"):
        await message.channel.send("아 어서요 어머니...! 지금 그런 얘기할 때가 아닙니다. 김두한 놈들이 올 거에요. 그 놈들이 오면 내가 죽는다구요! 어서가서 전화를 하세요. 어서가서 전화를 하세요, 어머니...! ")
    if message.content.startswith("닌텐도 스위치"):
        await message.channel.send("재밌다! 재밌다고허허허헣헣")             
    if message.content.startswith("안된다고 했잖소!"):
        await message.channel.send("이 반동노무 새끼들..!")
    if message.content.startswith("야이 빨갱이 새끼야!"):
        await message.channel.send("(형용할 수 없는 고통)아아앍...") 
    if message.content.startswith("도움말"):
        await message.channel.send("```(아래 대본을 쓰면 무슨일이..?)\n안녕\n나 김두한이다!\n그러게 왜 공산당인가 뭔가해서 이 모양이냐ㅠㅠ\n닌텐도 스위치\n안된다고 했잖소!\n야이 빨갱이 새끼야!```")          
    if message.content.startswith("심영봇 정보"):
        pass
        embed=discord.Embed(title="심영봇", description="사회주의자")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/681037117081518091/681110535294550039/d700da5b8321e372.jpg")
        embed.add_field(name="생성일", value="2020.02.23", inline=False)
        embed.add_field(name="만든놈", value="夜同界正", inline=True)
        embed.set_footer(text="님은 바로 사회주의 낙원입니다 여러부우운!")
        await message.channel.send(embed=embed)               


            
app.run(token)