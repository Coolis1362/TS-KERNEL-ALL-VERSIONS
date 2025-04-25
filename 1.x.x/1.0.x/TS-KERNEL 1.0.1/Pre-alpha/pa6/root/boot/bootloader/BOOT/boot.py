import time
import datetime

def printtext():

    user_input = input("PRINT>> ")
    print(user_input)



def bootos():
    # Simulating a user input scenario
    return input(
        "-----------------------------------------------"
        "\n-1. TS-KERNEL 1.0.1pa6:                       - "
        "\n-2. Exit                                      -"
        "\n-----------------------------------------------\n")


def boot():
    print("starting BOOT...")
    time.sleep(1)
    print("TIME: SYSTEM READABLE TIME NOT SET HUMAN READABLE TIME NOT SET BOOTING: Commands Booting help As Expanple...")
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
        print("distro - Show current Distro")
        time.sleep(0.05)
        print("TIME: SYSTEM READABLE TIME NOT SET HUMAN READABLE TIME NOT SET BOOTED: Commands")
    except Exception as e:
        print(f"BOOT: ERROR: Error Code 634: {e}")
        return False
    time.sleep(1)
    print("TIME: SYSTEM READABLE TIME NOT SET HUMAN READABLE TIME NOT SET BOOTING: tskerlan Booting print Code From tskerlan For Test...")
    try:
        printtext()
    except Exception as e:
        print(f"BOOT: ERROR: Error Code 634: {e}")
        return False
    time.sleep(0.05)
    print("TIME: SYSTEM READABLE TIME NOT SET HUMAN READABLE TIME NOT SET BOOTED: tskerlan")
    time.sleep(1)
    print("TIME: SETTING UP SYSTEM READABLE TIME HUMAN READABLE TIME NOT SET BOOTING: time.time()")
    try:
        print(time.time())
    except Exception as e:
        print(f"BOOT: ERROR: Error Code 634: {e}")
        return False
    print("TIME:", time.time(), "HUMAN READABLE TIME NOT SET BOOTED: time.time()")
    time.sleep(1)
    print("TIME:", time.time(), "HUMAN READABLE TIME NOT SET BOOTING: datetime.datetime.now")
    try:
        print(datetime.datetime.now())
    except Exception as e:
        print(f"BOOT: ERROR: Error Code 634: {e}")
        return False
    print("TIME:", time.time(), datetime.datetime.now, "BOOTED: datetime.datetime.now()")
    time.sleep(1)
    print("BOOT: BOOT has done booting and testing, booting TS-KERNEL...")
    time.sleep(2)
    return True