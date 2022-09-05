# Rin
# Ready to Ride🔥

<p align="center">
 <img src="https://telegra.ph/file/c83549257099febca7349.jpg">
</p>
<p align="center">
    <a href="https://python.org">
        <img src="http://forthebadge.com/images/badges/made-with-python.svg" alt="made-with-python">
    </a>
    <a href="https://GitHub.com/spryslade">
        <img src="http://ForTheBadge.com/images/badges/built-with-love.svg" alt="built-with-love">
    </a> <br>
    <img src="https://img.shields.io/github/license/spryslade/RinSuperBot-A01?style=for-the-badge&logo=appveyor" alt="LICENSE">
    <img src="https://img.shields.io/github/contributors/spryslade/RinSuperBot-A01?style=for-the-badge&logo=appveyor" alt="Contributors">
    <img src="https://img.shields.io/github/repo-size/spryslade/RinSuperBot-A01?style=for-the-badge&logo=appveyor" alt="Repository Size"> <br>
    <img src="https://img.shields.io/badge/python-3.9-green?style=for-the-badge&logo=appveyor" alt="Python Version">
    <img src="https://img.shields.io/github/issues/spryslade/RinSuperBot-A01?style=for-the-badge&logo=appveyor" alt="Issues">
    <img src="https://img.shields.io/github/forks/spryslade/RinSuperBot-A01?style=for-the-badge&logo=appveyor" alt="Forks">
    <img src="https://img.shields.io/github/stars/spryslade/RinSuperBot-A01?style=for-the-badge&logo=appveyor" alt="Stars">
</p>


<h2 align="center">
    ⇝ SUPPORT ⇜
</h2>

<p align="center">
<a href= "https://t.me/RinSuperBot"> <img src="https://img.shields.io/badge/RinSuperBot-saffron?style=for-the-badge&logo=telegram" alt=ErzaScarlet_GroupBot on Telegram" /> </a>
<a href= "https://t.me/AstorSupport"> <img src="https://img.shields.io/badge/Powered_by_Astor-red?style=for-the-badge&logo=telegram" alt="Support Chat" /> </a>
<a href="https://t.me/DarkkkCarnage"> <img src="https://img.shields.io/badge/DarkkkCarnage-orange?style=for-the-badge&logo=telegram" alt="Update Channel" /> </a>
</p>

 ⇝ Install Locally Or On A VPS ⇜
</h2>

```console
git clone https://github.com/spryslade/RinSuperBot-A01
cd RinSuperBot
pip3 install -U -r requirements.txt
cp sample_config.env config.env
```

<h3 align="center">
    Edit <b>config.env</b> with your own values
</h3>

<h2 align="center">
   ⇝ Run Directly ⇜
</h2>

```console
python3 -m rin
```
<h1>
    <p align="center">
        <a href="https://cloud.okteto.com/deploy?repository=https://github.com/spryslade/RinSuperBot-A01"><img src="https://img.shields.io/badge/Deploy%20To%20Okteto-informational?style=for-the-badge&logo=Okteto" width="200""/></a>

<h1>
    <p align="center">
        <a href="https://heroku.com/deploy?template=https://github.com/spryslade/RinSuperBot-A01">
            <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
        </a>
    </p>
</h1>

<h1 align="center">
   ⇝ Docker ⇜
</h1>

```console
git clone https://github.com/spryslade/RinSuperBot-A01
cd RinSuperBot
cp sample_config.env config.env
```
<h3 align="center">
    Edit <b> config.env </b> with your own values
</h3>

```console
sudo docker build . -t rinsuperbot
sudo docker run rinsuperbot
```

<h2 align="center">
   ⇝ Write new modules ⇜
</h2>

```py
# Add license text here, get it from below

from nezuko import app # This is bot's client
from pyrogram import filters # pyrogram filters
...


# For /help menu
__MODULE__ = "Module Name"
__HELP__ = "Module help message"
@app.on_message(filters.command("start"))
async def some_function(_, message):
    await message.reply_text("I'm already up!!")

```

<h3 align="center">
   And put that file in rinsuperbot/modules/, restart and test your bot.

<h2 align="center">
     ⇝ Credits ⇜
</h2>

<p align="center">
<a href="https://github.com/spryslade"> <img src="https://img.shields.io/badge/OWNER_SLADE-Github-crystalgreen?style=for-the-badge&logo=github" alt="SLADE Github" /> </a>
<a href="https://github.com/JACKSAMAA"> <img src="https://img.shields.io/badge/ASTOR_STAFF_JEANSAMA-GITHUB-crystalgreen?style=for-the-badge&logo=github" alt="SLADE Github" /> </a>
</p>
