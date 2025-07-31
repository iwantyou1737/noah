import os
from flask import Flask
import threading

import discord
from discord.ext import commands

# Heroku의 환경변수에서 DISCORD_TOKEN 읽기
TOKEN = os.environ["DISCORD_TOKEN"]

# 디스코드 봇 설정
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ 봇 로그인 완료: {bot.user}")

# 간단한 웹 서버 (UptimeRobot용)
app = Flask('')

@app.route('/')
def home():
    return "봇이 작동 중입니다."

def run_web():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 3000)))

# 웹 서버를 백그라운드에서 실행
threading.Thread(target=run_web).start()

# 디스코드 봇 실행
print("🤖 봇 실행 시도 중...")
try:
    bot.run(TOKEN)
except Exception as e:
    print(f"❌ 실행 중 오류 발생: {e}")