import asyncio
import ctypes
import discord
import os
import time
from ctypes import wintypes
from datetime import datetime
from dotenv import load_dotenv
from pynput.keyboard import Controller, Key

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_NAME = "futures-trades"
author_window_map = {
    "ES Alert": "Chart - ES 06-23",
}

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

client = discord.Client(intents=intents)
keyboard = Controller()

# Define necessary Windows API functions and constants
FindWindow = ctypes.windll.user32.FindWindowW
FindWindow.argtypes = [wintypes.LPCWSTR, wintypes.LPCWSTR]
FindWindow.restype = wintypes.HWND

SetForegroundWindow = ctypes.windll.user32.SetForegroundWindow
SetForegroundWindow.argtypes = [wintypes.HWND]
SetForegroundWindow.restype = wintypes.BOOL

GetForegroundWindow = ctypes.windll.user32.GetForegroundWindow
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetLastError = ctypes.windll.kernel32.GetLastError

message_queue = asyncio.Queue()


def get_active_window_title():
    """
    Returns the title of the currently active window.
    :return: str, The title of the active window.
    """
    hwnd = GetForegroundWindow()
    length = GetWindowTextLength(hwnd)
    buf = ctypes.create_unicode_buffer(length + 1)
    GetWindowText(hwnd, buf, length + 1)
    active_window_title = buf.value
    print(f"Currently active: {active_window_title}\n")
    return active_window_title


def is_active_window(title):
    """
    Checks if the given window title matches the currently active window title.
    :param title: str, The window title to check against the active window.
    :return: bool, True if the given title matches the active window title, False otherwise.
    """
    active_title = get_active_window_title()
    is_active = active_title == title
    print(
        f"Checking for target ticker'{title}': {is_active}\n")
    return is_active


def switch_to_window(target_window_title, timeout=5):
    """
    Attempts to switch to the window with the given title within the specified timeout.
    :param target_window_title: str, The title of the window to switch to.
    :param timeout: int, Optional. The number of seconds to keep trying before giving up. Default is 5 seconds.
    """
    start_time = time.time()

    while not is_active_window(target_window_title):
        hwnd = FindWindow(None, target_window_title)
        if hwnd:
            print(
                f"Found '{target_window_title}', attempting switch.\n")
            result = SetForegroundWindow(hwnd)
            if result == 0:
                # SetForegroundWindow failed
                error_code = GetLastError()
                print(
                    f"Switch failed with error code: {error_code}\n")
                for _ in range(3):
                    keyboard.press(Key.esc)
                    keyboard.release(Key.esc)
            else:
                print("Switch success\n")
        else:
            print(
                f"No window with the title '{target_window_title}' was found. Trying again")

        time.sleep(0.5)  # Pause for 0.5 seconds before trying again

        if time.time() - start_time > timeout:
            print(
                f"Timeout of {timeout} seconds reached. Stopping the search for the specified window.")
            break


async def send_key_combination(keys):
    """
    Sends a key combination to the active window using pynput.
    :param keys: list, The keys to send in the key combination. For example: [Key.alt, Key.shift, "c"]
    """
    for key in keys:
        keyboard.press(key)
    await asyncio.sleep(0.1)
    for key in keys:
        keyboard.release(key)


async def process_message_queue():
    """
    Asynchronously processes messages in the message queue, performing actions based on the message content.
    """
    while True:
        message = await message_queue.get()
        print(f"Processing message: {message.content}")
        # Process the message here

        now = datetime.now()
        ticker = message.author.name[:-6]

        # Switch to the corresponding window for the message author
        switch_to_window(author_window_map[message.author.name])

        content = message.embeds[0].title.strip().lower(
        ) if message.embeds else message.content.strip().lower()
        print(f"Karma algo: {content}")
        if "open long position alert" in content:
            print(f"Time Check...")
            if not ((now.time() >= datetime.strptime("16:00:00", "%H:%M:%S").time()) and (now.time() < datetime.strptime("23:00:00", "%H:%M:%S").time())):
                await send_key_combination([Key.alt, Key.shift, "c"])
                print(f'\n{now}: Signal Bot: "Long Entry on {ticker}"\n')
                bot_message = f"Closed any open {ticker} positions, Entered long"
                await send_key_combination([Key.alt, Key.shift, "b"])
                await message.channel.send(bot_message)
            else:
                print(f"The current time ({now.time()}) is within the no trade zone, no-op")
        elif "open short position alert" in content:
            print(f"Time Check...")
            if not ((now.time() >= datetime.strptime("16:00:00", "%H:%M:%S").time()) and (now.time() < datetime.strptime("23:00:00", "%H:%M:%S").time())):
                await send_key_combination([Key.alt, Key.shift, "c"])
                print(f'\n{now}: Signal Bot: "Short Entry on {ticker}"\n')
                bot_message = f"Closed any open {ticker} positions, Entered short"
                await send_key_combination([Key.alt, Key.shift, "s"])
                await message.channel.send(bot_message)
            else:
                print(f"The current time ({now.time()}) is within the no trade zone, no-op")
        elif "close" in content:
            print(f'\n{now}: Signal Bot: "Flattened {ticker} position, all out"\n')
            bot_message = f"Closed {ticker} position, all out"
            await send_key_combination([Key.alt, Key.shift, "c"])
            await message.channel.send(bot_message)
        elif "profit" in content:
            print(f"Time Check...")
            now = datetime.now().time()
            if not ((now >= datetime.strptime("23:00:00", "%H:%M:%S").time()) or (now < datetime.strptime("07:00:00", "%H:%M:%S").time())):
                print(f'\n{now}: Signal Bot: "Taking {ticker} Profit, all out"\n')
                bot_message = f"{ticker} Bag secured"
                await send_key_combination([Key.alt, Key.shift, "c"])
                await message.channel.send(bot_message)
            else:
                print(f"Currently within overnight session, no-op")

        message_queue.task_done()
        print("Message processed, waiting for next message")
        # Add a half-second sleep after processing each message
        await asyncio.sleep(0.5)


@client.event
async def on_ready():
    """
    Asynchronously processes messages in the message queue, performing actions based on the message content.
    """
    print(f'We have logged in as {client.user}')
    print("Starting message queue processing\n")
    # Start processing the message queue
    asyncio.create_task(process_message_queue())


@client.event
async def on_message(message):
    """
    Event handler for incoming messages. If the message is from a relevant author and channel, it is added to the message queue for processing.
    """
    content = message.embeds[0].title.strip().lower(
    ) if message.embeds else message.content.strip().lower()
    if message.channel.name == CHANNEL_NAME and message.author.name in author_window_map:
        print(
            f'Message received from {message.author.name} in {CHANNEL_NAME}, adding "{content}" to queue.\n')
        await message_queue.put(message)

client.run(DISCORD_TOKEN)
