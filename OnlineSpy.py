#Бесплатные софты только тут - t.me/thiasoft

from threading import Thread
import collections
from telethon import TelegramClient, events
from datetime import datetime
from time import sleep

DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'

API_ID = input("Enter API_ID: ")
API_HASH = input("Enter API_HASH: ")
BOT_TOKEN = input("Enter BOT_TOKEN: ")
USER_NAME = input("Enter USERNAME: ")

try:
    client = TelegramClient('data_thief', API_ID, API_HASH)
    client.connect()
    client.start()
    bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
except Exception as e:
    print(f"Error during initialization: {str(e)}")
    exit()

data = {}

help_messages = ['/start - start online monitoring ',
                 '/stop - stop online monitoring ',
                 '/help - show help ',
                 '/add - add user to monitoring list "/add +79991234567 UserName"',
                 '/list - show added users',
                 '/clear - clear user list',
                 '/remove - remove user from list with position in list (to show use /list command)"/remove 1"',
                 '/setdelay - set delay between user check in seconds',
                 '/logs - display command log',
                 '/clearlogs - clear the command log file',
                 '/cleardata - reset configuration',
                 '/disconnect - disconnect bot',
                 '/getall - status']


print('running')
class Contact:
    online = None
    last_offline = None
    last_online = None
    id = ''
    name = ''

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f'{self.name}: {self.id}'

@bot.on(events.NewMessage(pattern='^/logs$'))
async def logs(event):
    """Send a message when the command /logs is issued."""
    str = ''
    with open('spy_log.txt', 'r') as file:
        str = file.read()
    await event.respond(str)

@bot.on(events.NewMessage(pattern='^/help$'))
async def help(event):
    await event.respond('\n'.join(help_messages))


@bot.on(events.NewMessage(pattern='^/start$'))
async def start(event):
    """Send a message when the command /start is issued."""
    try:
        message = event.message
        id = message.chat_id
        if id not in data:
            data[id] = {}
        user_data = data[id]
        if 'is_running' in user_data and user_data['is_running']:
            await event.respond('Spy is already started')
            return

        if 'contacts' not in user_data:
            user_data['contacts'] = []

        contacts = user_data['contacts']

        if len(contacts) < 1:
            await event.respond('No contacts added')
            return

        await event.respond('Monitoring has been started')

        counter = 0
        user_data['is_running'] = True

        while True:
            user_data = data[id]
            if not user_data['is_running'] or len(contacts) < 1:
                break
            print(f'running {id}: {counter}')
            counter += 1
            for contact in contacts:
                print(contact)
                account = await client.get_entity(contact.id)


            delay = 5
            if 'delay' in user_data:
                delay = user_data['delay']
            sleep(delay)
        user_data['is_running'] = False
        await event.respond('Spy gonna zzzzzz...')
    except Exception as e:
        await event.respond(f"Error: {str(e)}")

@bot.on(events.NewMessage(pattern='^/start'))
async def send_help_after_auth(event):
    """Send a help message after successful authorization."""
    await event.respond('Welcome! Type /help for a list of available commands.')

    if 'contacts' not in user_data:
        user_data['contacts'] = []

    contacts = user_data['contacts']

    if(len(contacts) < 1):
        await event.respond('No contacts added')
        return
    await event.respond('Monitoring has been started')

    counter = 0
    user_data['is_running'] = True

    while True:
        user_data = data[id]
        if(not user_data['is_running'] or len(contacts) < 1):
            break;
        print(f'running {id}: {counter}')
        counter+=1
        for contact in contacts:
            print(contact)
            account = await client.get_entity(contact.id)

        if isinstance(account.status, UserStatusOnline):
            if contact.online != True:
                contact.online = True
                contact.last_offline = datetime.now()
                was_offline='unknown offline time'
                if contact.last_online is not None:
                    was_offline = (contact.last_offline - contact.last_online).strftime(DATETIME_FORMAT)
                await event.respond(f'{get_interval(was_offline)}: {contact.name} went online.')
        elif isinstance(account.status, UserStatusOffline):
            if contact.online == True:
                contact.online = False
                last_time_online = utc2localtime(account.status.was_online)
                if (last_time_online is None):
                    last_time_online = datetime.now()
                contact.last_online = account.status.was_online

                was_online='unknown online time'
                if contact.last_offline is not None:
                    was_online = (contact.last_online - contact.last_offline).strftime(DATETIME_FORMAT)

                await event.respond(f'{get_interval(was_online)} {contact.name} went offline.')
            contact.last_offline = None
        else:
            if contact.online == True:
                contact.online = False
                contact.last_online = datetime.now()

                was_online='unknown online time'
                if contact.last_offline is not None:
                    was_online = (contact.last_online - contact.las_offline).strftime(DATETIME_FORMAT)

                await event.respond(f'{get_interval(was_online)}: {contact.name} went offline.')
                contact.last_offline = None
        delay = 5
        if('delay' in user_data):
            delay = user_data['delay']
        sleep(delay)
    user_data['is_running'] = False
    await event.respond(f'Spy gonna zzzzzz...')

@bot.on(events.NewMessage(pattern='^/add'))
async def add(event):
    message = event.message
    person_info = message.message.split()
