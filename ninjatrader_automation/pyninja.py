import ctypes
import time

# Load the DLL
dll = ctypes.WinDLL(r"C:\Program Files (x86)\NinjaTrader 8\bin\NtDirect.dll")
#"C:\Program Files (x86)\NinjaTrader 8\bin\NinjaTrader.Client.dll"

# Define the argument types and return types for functions we're going to use
dll.SetUp.argtypes = [ctypes.c_char_p, ctypes.c_int]
dll.SetUp.restype = ctypes.c_int

dll.Connected.argtypes = [ctypes.c_int]
dll.Connected.restype = ctypes.c_int

dll.SubscribeMarketData.argtypes = [ctypes.c_char_p]
dll.SubscribeMarketData.restype = ctypes.c_int

dll.MarketData.argtypes = [ctypes.c_char_p, ctypes.c_int]
dll.MarketData.restype = ctypes.c_double

# Set up the connection
host = ctypes.c_char_p(b"localhost")
port = ctypes.c_int(36973)

if dll.SetUp(host, port) == -1:
    print("Error setting up the connection")
    exit()

# Check if connected
if dll.Connected(0) == -1:
    print("Not connected to NinjaTrader")
    exit()

# Subscribe to market data
instrument = ctypes.c_char_p(b"ES")

if dll.SubscribeMarketData(instrument) == -1:
    print("Error subscribing to market data")
    exit()

# Wait for a few seconds to receive market data
time.sleep(3)

# Get the last price of the instrument
price_type = ctypes.c_int(0)  # 0 = last, 1 = bid, 2 = ask
price = dll.MarketData(instrument, price_type)
print(f"Last price of 'ES': {price:.2f}")

# Unsubscribe from market data (optional)
dll.UnsubscribeMarketData(instrument)

##import ctypes
##
### Load the DLL (replace 'your_dll_name.dll' with the actual DLL file name)
##dll = ctypes.CDLL("your_dll_name.dll")
##
### Define the functions from the DLL documentation
##Ask = dll.Ask
##Ask.argtypes = [ctypes.c_char_p, ctypes.c_double, ctypes.c_int]
##Ask.restype = ctypes.c_int
##
##AskPlayback = dll.AskPlayback
##AskPlayback.argtypes = [ctypes.c_char_p, ctypes.c_double, ctypes.c_int, ctypes.c_char_p]
##AskPlayback.restype = ctypes.c_int
##
### ... continue defining all other functions similarly
##
### Call the functions
##instrument = "ES".encode('utf-8')
##price = 100.0
##size = 10
##
##result = Ask(instrument, price, size)
##print(f"Ask result: {result}")
##
##timestamp = "20210414123000".encode('utf-8')
##result = AskPlayback(instrument, price, size, timestamp)
##print(f"AskPlayback result: {result}")
##
### ... continue calling all other functions similarly
