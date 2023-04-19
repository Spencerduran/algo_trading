import ctypes
import time

# Load the DLL
dll = ctypes.WinDLL(r"C:\Program Files (x86)\NinjaTrader 8\bin\NtDirect.dll")

# Define the functions from the DLL documentation
CashValue = dll.CashValue
CashValue.argtypes = [ctypes.c_char_p]
CashValue.restype = ctypes.c_double

SetUp = dll.SetUp
SetUp.argtypes = [ctypes.c_char_p, ctypes.c_int]
SetUp.restype = ctypes.c_int

Connected = dll.Connected
Connected.argtypes = [ctypes.c_int]
Connected.restype = ctypes.c_int

Command = dll.Command
Command.argtypes = [ctypes.c_char_p]
Command.restype = ctypes.c_int

Last = dll.Last
Last.argtypes = [ctypes.c_char_p]
Last.restype = ctypes.c_double

# Set up the connection
host = ctypes.c_char_p(b"127.0.0.1")
port = ctypes.c_int(36973)

if SetUp(host, port) == -1:
    print("Error setting up the connection")
    exit()

# Check if connected
if Connected(0) == -1:
    print("Not connected to NinjaTrader")
    exit()

# Get the account balance for Sim101
account = "Sim101".encode('utf-8')
balance = CashValue(account)
print(f"Account balance for Sim101: {balance:.2f}")

ticker = "ES 06-23".encode('utf-8')
current_price = Last(ticker)
print(f"Current price of {ticker.decode('utf-8')}: {current_price:.2f}")
