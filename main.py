import discord
from discord import app_commands
import os

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

IMAGE_FOLDER = "images"
DAYS = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]

@client.event
async def on_ready():
    await tree.sync()
    print(f"✅ Bot 上線: {client.user}")

# 一個指令，帶一個參數 day，從選項中選
@tree.command(name="圖片", description="傳送指定星期的圖片")
@app_commands.describe(day="選擇星期幾")
@app_commands.choices(day=[
    app_commands.Choice(name=day, value=day) for day in DAYS
])
async def send_image(interaction: discord.Interaction, day: app_commands.Choice[str]):
    file_path = os.path.join(IMAGE_FOLDER, f"{day.value}.jpg")
    if os.path.exists(file_path):
        await interaction.response.send_message(file=discord.File(file_path))
    else:
        await interaction.response.send_message(f"⚠️ 找不到圖片：{day.value}", ephemeral=True)

# 啟動機器人
TOKEN = os.environ["TOKEN"]
client.run(TOKEN)

