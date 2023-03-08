# TeleBot

This is a Python Telegram bot that sends a daily **rebus puzzle** to users who make request. 

The bot is build with **Telebot** and implemented with **Flask library**.\
The bot uses a **SQLite database** to store users information. → The bot only sends **one rebus per day** to each user.

&emsp;&emsp; When users type the command `'/start'`, the bot sends a welcome message and instructions.\
&emsp;&emsp; When users type the command `'/rebus'`, the bot sends a rebus puzzle to the user.\
&emsp;&emsp; Users can request the solution to the last rebus by typing the command `'/solution'`.

Currently living on [**PythonAnywhare**](https://www.pythonanywhere.com/)
