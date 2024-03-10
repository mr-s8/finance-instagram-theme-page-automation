<div align="center">
  <p>
    <a href="https://github.com/mr-s8/finance_instagram_theme_page_automation/blob/main/images/instagram_logo.png"><img src="https://github.com/mr-s8/finance_instagram_theme_page_automation/blob/main/images/instagram_logo.png" width="80" alt="instagram logo" /></a>
    <a href="https://github.com/mr-s8/finance_instagram_theme_page_automation/blob/main/images/robot_emoji.png"><img src="https://github.com/mr-s8/finance_instagram_theme_page_automation/blob/main/images/robot_emoji.png" width="100" alt="robot emoji" /></a>
  </p>
</div>

# finance-instagram-theme-page-automation
This python script scrapes the prices of popular stocks from yahoo finance. It uses them to create images or videos with moviepy, that it automatically posts to instagram using the instagrapi package. 


## How to use
1. Download the repository
2. In the folder where the requirements.txt file is located, open a terminal and install the dependencies with:
```bash
pip install -r requirements.txt
```
3. Download ImageMagick from: https://imagemagick.org/script/download.php
4. Starting from your Python folder, go to /Lib/site-packages/moviepy and open config_defaults.py.
   In there, specify the path to the ImageMagick executable. Moviepy uses it to put text over images.
5. In script.py specify your Instagram credentials. If you want to use Discord to receive logging messages,
   create a Discord bot, add it to a server with only you on there and set the bot token and the id of the
   channel where you want to receive the messages.
6. At the bottom of script.py you can edit the upload schedule.
7. Personalize if needed.
8. Run the script 24/7 (ideally on a Raspberry Pi) or delete the schedules and call the stockImageUpload()
   and stockVideoUpload() functions manually.

## Pictures
<div align="center">
  <p>
    <a href="https://github.com/mr-s8/finance_instagram_theme_page_automation/blob/main/images/1topost.jpg"><img src="https://github.com/mr-s8/finance_instagram_theme_page_automation/blob/main/images/1topost.jpg" alt="screenshot" width= "800" /></a>
    <a href="https://github.com/mr-s8/finance_instagram_theme_page_automation/blob/main/images/2topost.jpg"><img src="https://github.com/mr-s8/finance_instagram_theme_page_automation/blob/main/images/2topost.jpg" alt="screenshot" width= "800" /></a>
  </p>
</div>
