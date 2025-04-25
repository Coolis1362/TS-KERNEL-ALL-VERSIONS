import time
import datetime

def printtext():

    user_input = input("PRINT>> ")
    print(user_input)



def bootos():
    # Simulating a user input scenario
    return input(
        "-----------------------------------------------"
        "\n-1. TS-KERNEL 1.0.1pa5:                       - "
        "\n-2. Exit                                      -"
        "\n-----------------------------------------------\n")


def boot():
    print("starting BOOT...")
    time.sleep(1)
    print("TIME:", time.time(), datetime.datetime.now(), "BOOTING: Commands Booting help As Expanple...")
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
        print("TIME:", time.time(), datetime.datetime.now(), "BOOTED: Commands")
    except Exception as e:
        print(f"BOOT: ERROR: Error Code 634: {e}")
        return False
    time.sleep(1)
    print("TIME:", time.time(), datetime.datetime.now(), "BOOTING: tskerlan Booting print Code From tskerlan For Test...")
    try:
        printtext()
    except Exception as e:
        print(f"BOOT: ERROR: Error Code 634: {e}")
        return False
    time.sleep(0.05)
    print("TIME:", time.time(), datetime.datetime.now(), "BOOTED: tskerlan")
    time.sleep(1)
    print("BOOT: BOOT has done botoing and testing, booting TS-KERNEL...")
    time.sleep(2)
    return True