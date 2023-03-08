# Rebus-Bot

This is a Telegram [**bot**](https://web.telegram.org/k/#@Bot4Rebus_bot), made with Python, that sends a daily **rebus puzzle** to users who make request. 

The bot is build with **Telebot** and implemented with **Flask library**.\
The bot uses a **SQLite database** to store users information. → The bot only sends **one rebus per day** to each user.

&emsp;&emsp; When users type the command `'/start'`, the bot sends a welcome message and instructions.\
&emsp;&emsp; When users type the command `'/rebus'`, the bot sends a rebus puzzle to the user.\
&emsp;&emsp; Users can request the solution to the last rebus by typing the command `'/solution'`.


Previously hosted on [Heroku](https://www.heroku.com), currently living on [**PythonAnywhare**](https://www.pythonanywhere.com/)
