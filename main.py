
import discord
import datetime


class chatbot(discord.Client):
    async def on_ready(self):
        game = discord.Game("async def on_ready(self):")

        await client.change_presence(status=discord.Status.online, activity=game)

        print("READY")

    async def on_message(self, message):
        global date
        if message.author.bot:
            return None

        if message.content == "=바보":
            channel = message.channel
            msg = "에??"
            await channel.send(msg)
        if message.content == "=Http://":
            channel = message.channel
            msg = "홍보 경고!"
            await channel.send(msg)
        if message.content == "=hTtp://":
            channel = message.channel
            msg = "홍보 경고!"
            await channel.send(msg)
        if message.content == "=htTp://":
            channel = message.channel
            msg = "홍보 경고!"
            await channel.send(msg)
        if message.content == "=httP://":
            channel = message.channel
            msg = "홍보 경고!"
            await channel.send(msg)
        if message.content == "=HTtp://":
            channel = message.channel
            msg = "홍보 경고!"
            await channel.send(msg)
        if message.content == "=HTTp://":
            channel = message.channel
            msg = "홍보 경고!"
            await channel.send(msg)
        if message.content == "=HtTp://":
            channel = message.channel
            msg = "홍보 경고!"
            await channel.send(msg)
        if message.content == "=HtTP://":
            channel = message.channel
            msg = "홍보 경고!"
            await channel.send(msg)
        if message.content.startswith("https://"):
            channel = message.channel
            msg = "홍보 경고!"
            await channel.send(msg)
        if message.content.startswith("http://"):
            channel = message.channel
            msg = "홍보 경고!"
            await channel.send(msg)
        if message.content.startswith("HTTPS://"):
            channel = message.channel
            msg = "홍보 경고!"
            await channel.send(msg)
        if message.content.startswith("HTTP://"):
            channel = message.channel
            msg = "홍보 경고!"
            await channel.send(msg)
        if message.content == "=hTtps://":
            channel = message.channel
            msg = "홍보 경고!"
            await channel.send(msg)
        if message.content == "=htTps://":
            channel = message.channel
            msg = "홍보 경고!"
            await channel.send(msg)
        if message.content == "=httPs://":
            channel = message.channel
            msg = "홍보 경고!"
            await channel.send(msg)
        if message.content == "=HTtps://":
            channel = message.channel
            msg = "홍보 경고!"
            await channel.send(msg)
        if message.content == "=HTTps://":
            channel = message.channel
            msg = "홍보 경고!"
            await channel.send(msg)
        if message.content == "=HtTpS://":
            channel = message.channel
            msg = "홍보 경고!"
            await channel.send(msg)
        if message.content == "=HtTPS://":
            channel = message.channel
            msg = "홍보 경고!"
            await channel.send(msg)
        if message.content == "=hTtpS://":
            channel = message.channel
            msg = "홍보 경고!"
            await channel.send(msg)
        if message.content == "=htTpS://":
            channel = message.channel
            msg = "홍보 경고!"
            await channel.send(msg)
        if message.content == "=httPS://":
            channel = message.channel
            msg = "홍보 경고!"
            await channel.send(msg)
        if message.content == "=HTtpS://":
            channel = message.channel
            msg = "홍보 경고!"
            await channel.send(msg)
        if message.content == "=HTTpS://":
            channel = message.channel
            msg = "홍보 경고!"
            await channel.send(msg)
        if message.content == "=HtTpS://":
            channel = message.channel
            msg = "홍보 경고!"
            await channel.send(msg)
        if message.content == "=HtTPS://":
            channel = message.channel
            msg = "홍보 경고!"
            await channel.send(msg)
        if message.content.startswith("https://"):
            channel = message.channel
            msg = "홍보 경고!"
            await channel.send(msg)
        if message.content.startswith("http://"):
            channel = message.channel
            msg = "홍보 경고!"
            await channel.send(msg)
        if message.content.startswith("HTTPS://"):
            channel = message.channel
            msg = "홍보 경고!"
            await channel.send(msg)
        if message.content.startswith("HTTP://"):
            channel = message.channel
            msg = "홍보 경고!"
            await channel.send(msg)
        if message.content.startswith("=명령어"):
            embed = discord.Embed(title="명령어 모음", description="명령어 모음입니다!", color=0x00ff56)
            embed.set_author(name="불가리아", url="https://media.discordapp.net/attachments/812485396067647492/812491265723072512/TV.png1",
                             icon_url="https://media.discordapp.net/attachments/812485396067647492/812491265723072512/TV.png")
            embed.set_thumbnail(
                url="https://media.discordapp.net/attachments/812485396067647492/812491265723072512/TV.png")
            embed.add_field(name="=주식", value="네오포스 방의 주식을 알려줍니다.", inline=True)
            embed.add_field(name="=안녕", value="||~~찐따들한테~~|| 인사해줍니다.", inline=True)
            embed.add_field(name="아직 추가 되지 않았습니다.", value="아직 추가 되지 않았습니다", inline=True)
            embed.set_footer(text="(1. 2만원 내고 주식회사 건설 ㄱㄴ, 2. 주식을 팔때 10%는 회사가 수수료로 가져감, 3. 주식의 주가 변동은 따로 관리자가 앱 만들어서 할 예정임")
            await message.channel.send(embed=embed)
        if message.content == "=안녕":
            channel = message.channel
            msg = "안녕하세요"
            await channel.send(msg)
        if message.content.startswith("=주식"):
            embed = discord.Embed(title="주식", description="주식!", color=0x00ff56)
            embed.set_author(name="불가리아", url="https://media.discordapp.net/attachments/812485396067647492/812491265723072512/TV.png1",
                             icon_url="https://media.discordapp.net/attachments/812485396067647492/812491265723072512/TV.png")
            embed.set_thumbnail(
                url="https://media.discordapp.net/attachments/812485396067647492/812491265723072512/TV.png")
            embed.add_field(name="닛신 라멘 (일본)", value="1000 (-)", inline=True)
            embed.add_field(name="이딸딸이 도우(이탈리아)", value="5000 (-)", inline=True)
            embed.add_field(name="불가리아식 요구르트(불가리아)", value="5000 (-)", inline=True)
            embed.add_field(name="시카 중앙 코코넛기구(시카)", value="5000 (-)", inline=True)
            embed.add_field(name="어글리 스테이크 집(네오포스)", value="5000 (-)", inline=True)
            embed.add_field(name="너튜브(네오포스)", value="5000 (-)", inline=True)
            embed.add_field(name="면상책[페이스북](네오포스)", value="5000 (-)", inline=True)
            embed.add_field(name="빅데이터 해법수학 우등생(네오포스)", value="5000 (-)", inline=True)
            embed.set_footer(text="1. 2만원 내고 주식회사 건설 ㄱㄴ, 2. 주식을 팔때 10%는 회사가 수수료로 가져감, 3. 주식의 주가 변동은 따로 관리자가 앱 만들어서 할 예정임")
            await message.channel.send(embed=embed)

if __name__ == "__main__":
    client = chatbot()
    client.run("ODEyMjY2MTgwNTUwMTk3MjU4.YC-P1A.cZah6ttFI3zyJ3aiM-ESOjR6eO8")