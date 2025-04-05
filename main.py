import discord
from discord import app_commands
import os

# 建立 Client（Intents 預設即可）
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# Discord Bot Token（從環境變數讀取）
TOKEN = os.environ.get("TOKEN")

# 圖片資料夾路徑
IMAGE_FOLDER = "images"

# 星期列表
DAYS = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]

# 機器人啟動時註冊指令
@client.event
async def on_ready():
    await tree.sync()
    print(f"✅ 已登入為 {client.user}")

# 註冊所有斜線指令（動態綁定）
for day in DAYS:
    @tree.command(name=day, description=f"傳送 {day} 的圖片")
    async def send_image(interaction: discord.Interaction, day=day):
        image_path = os.path.join(IMAGE_FOLDER, f"{day}.jpg")
        if os.path.exists(image_path):
            await interaction.response.send_message(file=discord.File(image_path))
        else:
            await interaction.response.send_message(f"⚠️ 找不到圖片：{day}", ephemeral=True)

# 啟動 bot
client.run(TOKEN)
