import logging
from telegram.ext import Updater, CommandHandler
from datetime import datetime, time, timedelta
import pytz

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Your bot token
TOKEN = '7461006476:AAFGtU6OeIP4em6NDoaeCsJWSq7H0ugIkOU'
CHAT_ID = '1114198707'
TIMEZONE = 'ASIA/YEREVAN'  # e.g., 'Europe/Berlin'

def start(update, context):
    update.message.reply_text('Hi! I will remind you to drink water and send love messages throughout the day.')

def send_water_reminder(context):
    context.bot.send_message(chat_id=CHAT_ID, text="Hey love, it's time to hydrate! Water break for you. 💧💕")

def send_love_message(context):
    context.bot.send_message(chat_id=CHAT_ID, text="Just a quick reminder - I love you more than words can say. You mean the world to me. AND DRINK WATERRRRRR ❤️")

def main():
    # Create the Updater and pass it your bot's token
    updater = Updater(TOKEN, use_context=True)
    
    # Get the job queue
    jq = updater.job_queue
    
    # Timezone
    tz = pytz.timezone(TIMEZONE)
    
    # Start and end times for reminders (9 AM to 9 PM)
    start_time = time(9, 0, tzinfo=tz)
    end_time = time(21, 0, tzinfo=tz)
    
    # Calculate the intervals and schedule the jobs
    now = datetime.now(tz)
    first_water_reminder = datetime.combine(now.date(), start_time, tz) + timedelta(hours=2)
    first_love_message = datetime.combine(now.date(), start_time, tz) + timedelta(hours=1)
    
    while first_water_reminder < now:
        first_water_reminder += timedelta(hours=2)
    while first_love_message < now:
        first_love_message += timedelta(hours=2)
    
    jq.run_repeating(send_water_reminder, interval=timedelta(hours=2), first=first_water_reminder)
    jq.run_repeating(send_love_message, interval=timedelta(hours=2), first=first_love_message)
    
    # Start the Bot
    updater.start_polling()
    
    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
