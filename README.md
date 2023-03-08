# TeleBot

This is a Python Telegram bot that sends a daily rebus puzzle to users who make request. 

The bot is build with **Telebot** and implemented with **Flask library**.\
The bot uses a **SQLite database** to store users information.

When users type the command `'/start'`, the bot sends a welcome message and instructions.\
When users type the command `'/rebus'`, the bot sends a rebus puzzle to the user.\
The bot only sends one rebus puzzle per day to each user.
Users can request the solution to the most recent rebus puzzle by typing the command `'/solution'\`.
