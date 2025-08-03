import discord
from discord.ext import commands
import asyncio
from google import genai
from google.genai import types

def generate_quiz(user, github_url):
    prompt = f"""
    あなたはソフトウェア開発の教育アシスタントです。
    以下の GitHub のレポジトリでの「アウトプット」がつく最新コミット内容を元に、
    {user} さんのエンジニアレベルを評価して、{user} さん向けに全部で 1500 文字以内で 3 問の技術クイズを作成してください。

    - Github レポジトリ： {github_url}

    出力フォーマット:
        Q1: ...
            A.
            B.
            C.
            D. 
        Q2: ...
            A.
            B.
            C.
            D.
        Q3: ...
            A.
            B.
            C.
            D.
    """

    # === Ito Gemini Start ===
    client = genai.Client(api_key="GEMINI_API_KEY")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0) # Disables thinking
        ),
    )
    print(response.text)
    test = str(response.text)
    # === Ito Gemini End ===

    return test

intents = discord.Intents.default()
intents.message_content = True  # メッセージ内容を取得するのに必要
intents.guilds = True
intents.messages = True

client = discord.Client(intents=intents)

# チャンネルIDを指定
TARGET_CHANNEL_ID = YOUR_CHANNEL_ID

@client.event
async def on_ready():
    print(f'✅ ログイン成功: {client.user}')

# チャンネルからメッセージを取得してクイズを生成
@client.event
async def on_message(message):
    channel = client.get_channel(TARGET_CHANNEL_ID)

    if channel is None:
        print("❌ チャンネルが見つかりません。")
        return

    if message:
        msg = message.content
        lines = msg.splitlines()
        error = "💬 ユーザー名またはGitHub URLが見つかりません。"

        # メッセージの最初の行に「成果物」または「アウトプット」が含まれているか確認
        if "成果物" in lines[0] or "アウトプット" in lines[0]:
            for line in lines:
                if "ユーザー" in line:
                    user = line.split("ユーザー: ")[-1].strip()
                elif "https://github.com/" in line:
                    github_url = line.strip("🔗 ").strip()

            # ユーザー名とGitHub URLが両方とも存在する場合にクイズを生成
            if 'user' in locals() and 'github_url' in locals():
                test = generate_quiz(user, github_url)
                await channel.send(test)
            else:
                await channel.send(error)
    else:
        await channel.send(error)

# 実行
client.run("YOUR_DISCORD_TOKEN")
