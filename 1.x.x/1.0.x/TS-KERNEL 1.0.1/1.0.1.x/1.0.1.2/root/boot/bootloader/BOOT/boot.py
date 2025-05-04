import time
import datetime
import sys
import webbrowser
from datetime import datetime, timezone
from zoneinfo import ZoneInfo  # Standard timezone handling for Python 3.14+

# Define the TS-KERNEL Epoch Start Time
epoch_start = datetime(2025, 4, 9, 0, 0, 0, tzinfo=ZoneInfo("America/New_York"))  # US Eastern Time

# Function to calculate elapsed seconds
def get_seconds_since_epoch():
    now = datetime.now(ZoneInfo("America/New_York"))  # Get current time in US Eastern
    elapsed_seconds = (now - epoch_start).total_seconds()  # Calculate elapsed seconds
    return int(elapsed_seconds)



def printtext():

    user_input = input("PRINT>> ")
    print(user_input)



def bootos():
    # Simulating a user input scenario
    return input(
        "-------------------------------------------------------"
        "\n- Choose A Number, This Key Will Tell What It Will Do -"
        "\n- 1 = TS-KERNEL 1.0.1.1 Codename 'Pulse'            -"
        "\n- 2 = Exit                                            -"
        "\n-------------------------------------------------------\n")


def boot():
    print("starting BOOT...")
    time.sleep(1)
    print(f"Reading root\\boot\\bootloader\\BOOT\\__pycache__\\boot.cpython-{sys.version_info.major}{sys.version_info.minor}.pyc")
    time.sleep(1)
    print("DONE PROCESS: 0% TIME: SYSTEM READABLE TIME NOT SET HUMAN READABLE TIME NOT SET BOOTING: Commands Booting help As Expanple...")
    time.sleep(1)
    try:
        print("Commands:")
        print("help - Show this help message")
        print("exit - Exit the console")
        print("clear - Clear the console")
        print("whoami - Show the current user")
        print("tskerlan - start The TS-KERNEL-LANAGUAGE Interpiler")
        print("tsdesktop - start TS-DESKTOP and end cmd.exe")
        print("switch user --USER - Switch to user USER")
        print("shutdown --host_os - Shutdown Windows")
        print("ts-package - starts ts-package")
        print("time - Tells The Time")
        print("admindo - If A Linux User Is Seeing this, It's the Same As sudo")
        print("ts-distro - Same As neofetch")
        print("tscli - Same As ts-distro But with tscli")
        print("python - Same As The python Command In Other Terminals And Shells")
        print("boot - Boot Again")
        print("msnetwork - Start The Microsoft Network")
        print("version - Show the version of the distro and kernel")
        print("git - Same As The git Command In Other Terminals And Shells")
        print("gh - Same As The gh Command In Other Terminals And Shells")
        print("time --sys - Show The System Time")
        time.sleep(0.05)
        print("DONE PROCESS: 16.6666666667% TIME: SYSTEM READABLE TIME NOT SET HUMAN READABLE TIME NOT SET BOOTED: Commands")
    except Exception as e:
        print(f"BOOT: ERROR: Error Code 634: {e}")
        return False
    time.sleep(1)
    print("DONE PROCESS: 16.6666666667% TIME: SYSTEM READABLE TIME NOT SET HUMAN READABLE TIME NOT SET BOOTING: tskerlan Booting print Code From tskerlan For Test...")
    try:
        printtext()
    except Exception as e:
        print(f"BOOT: ERROR: Error Code 634: {e}")
        return False
    time.sleep(0.05)
    print("DONE PROCESS: 50.0000000001% TIME: SYSTEM READABLE TIME NOT SET HUMAN READABLE TIME NOT SET BOOTED: tskerlan")
    time.sleep(1)
    print("DONE PROCESS: 50.0000000001% TIME: SETTING UP SYSTEM READABLE TIME HUMAN READABLE TIME NOT SET BOOTING: time.time()")
    try:
        print(time.time())
    except Exception as e:
        print(f"BOOT: ERROR: Error Code 634: {e}")
        return False
    print("DONE PROCESS: 66.6666666668% TIME:", time.time(), "HUMAN READABLE TIME NOT SET BOOTED: time.time()")
    time.sleep(1)
    print("DONE PROCESS: 66.6666666668% TIME:", time.time(), "HUMAN READABLE TIME NOT SET BOOTING: datetime.now()")
    try:
        print(datetime.now())
    except Exception as e:
        print(f"BOOT: ERROR: Error Code 634: {e}")
        return False
    print("DONE PROCESS: 83.3333333335% TIME:", time.time(), datetime.now(), "BOOTED: datetime.now()")
    time.sleep(1)
    print("DONE PROCESS: 83.3333333335% TIME:", time.time(), datetime.now(), "BOOTING: Default Network (Microsoft Network (MSN))")
    try:
        webbrowser.open("https://www.msn.com")
    except Exception as e:
        print(f"BOOT: ERROR: Error Code 634: {e}")
        return False
    print("DONE PROCESS: 83.3333333335% TIME:", time.time(), datetime.now(), "BOOTED: Default Network (Microsoft Network (MSN))")
    time.sleep(1)
    print("DONE PROCESS: 83.3333333335% TIME:", time.time(), datetime.now(), "BOOTING: 2nd System Readable Time")
    try:
        print(get_seconds_since_epoch())
    except Exception as e:
        print(f"BOOT: ERROR: Error Code 634: {e}")
        return False
    print("DONE PROCESS: 100% TIME:", time.time(), datetime.now(), "BOOTED: Default Network (Microsoft Network (MSN))")
    time.sleep(1)
    print("BOOT: BOOT has done booting and testing, booting TS-KERNEL and tscli...")
    time.sleep(2)
    return True