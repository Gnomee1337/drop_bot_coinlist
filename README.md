# User Registration for Crypto Platforms
A bot for registering users (drops) by filling in user data to register on platforms like Coinlist.
> <sub>FAQ text and countries list taken from https://github.com/SoDeepASMR/CoinListBot</sub>

## Setup Bot:
1. Create DB 
    - Import sql template [./database/mysql/reg_bot_mysql.sql](./database/mysql/reg_bot_mysql.sql)
1. Create `.env` (based on `.env.example`) and fill it
1. `pip install -r requirements.txt`
1. Run `main.py`

## Setup AdminPanel:
1. Create `.env` (based on `.env.example`) in [/webregpanel/inc/](/webregpanel/inc/) and fill it
1. Run `composer install` in `webregpanel/`
1. Create Admin-User for login to AdminPanel in `webpanel_accouts` DB table

## Bot functions:
* RU/ENG Languages
* User Registration
* Notifying a user/group-chat about a new filled user
* User input checks:
  - forbidden countries (Coinlist)
  - latin characters
  - invalid symbols
* Moderator role:
  - invited users statistics
  - add an infinite number of users
  - create a referral link

## Admin-Panel functions:
* Verify filled users
* Add/Edit/Delete users
* Add/Edit/Delete bot-moderators
* <sub>(Admin-Panel UI has only RU localization)</sub>

## Bot Example:
![](git_images/registration_process.gif)

## Admin-Panel Example:
![](git_images/adminpanel_process.gif)
