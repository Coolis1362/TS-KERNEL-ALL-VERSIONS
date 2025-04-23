import time
import os
from ts_kernel_language.tskerlan import tskerlan
from shutdown_windows import shutdown_windows
import datetime
from ts_kernel_language.grammer.print.print import printtext
import sys



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
    return True



def put_distro_name_here(): # Replace put_distro_name_here with the name of your distro
    MAIN_USER_NAME = "ADMIN_USER"
    DISTRO_NAME_PREFIX = "TS-DISTRO"
    DISTRO_NAME = "distro_name" # Replace distro_name with the name of your distro
    KERNEL_VERSION = "1.0.1pa3"
    DISTRO_VERSION = "version name" # Replace This with Version name Of your Distor e.g TS-DISTRO MAIN >>1.0.1pa2<< (The >> and << Are Pointing to A Version Number As A Version number)
    print(f"Welcome To {DISTRO_NAME_PREFIX} {DISTRO_NAME} KERNEL VERSION: {KERNEL_VERSION} DISTRO VERSION: {DISTRO_VERSION}!")
    time.sleep(2)
    print(f"This is Based on TS-KERNEL {KERNEL_VERSION}")
    time.sleep(2)
    print("Loading...")
    time.sleep(2)
    for step in range(100):
        print("#", end="", flush=True)
        time.sleep(0.05)
    
    os.system("cls" if os.name == "nt" else "clear")
    time.sleep(2)
    print("****************************************************************")
    print(f"*        WELCOME TO {DISTRO_NAME_PREFIX} {DISTRO_NAME}                      *") # The Spaces Depends On How Long The Distro Name
    print("*                        NO COPYRIGHT                          *")
    print("*             YOU CAN MAKE A DISTRO BASED ON IT!               *")
    print("*                  TYPE 'help' FOR COMMANDS                    *")
    print("****************************************************************")

    while True:
        tsdistrocommand = input(f"CONSOLE FOR {DISTRO_NAME_PREFIX} {DISTRO_NAME}>>>> ")
        if tsdistrocommand == "help":
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
            print("add your commands here") # Replace It With Your Comamnds and On

        elif tsdistrocommand == "exit":
            print("Exiting...")
            time.sleep(1)
            os.system("taskkill /F /IM cmd.exe")
            os._exit(0)

        elif tsdistrocommand == "clear":
            os.system("cls" if os.name == "nt" else "clear")

        elif tsdistrocommand == "whoami":
            print(f"Current user: {MAIN_USER_NAME}")

        elif tsdistrocommand == "tskerlan":
            try:
                tskerlan()
            except Exception as e:
              print(f"Error 305: An issue occurred while executing 'tskerlan': {e}")
        elif tsdistrocommand == "tsdesktop":
            try:
                os.chdir("C:\\Users\\<Username>\\<NestedFolder>\\Desktop\\TS-KERNEL VERSIONS\\1.x.x\\1.0.x\\TS-KERNEL 1.0.1\\Pre-alpha\\pa2\\root\\ts-desktop\\1.x.x\\1.0.x\\1.0.0\\")
                os.system("ts-desktop100")
                time.sleep(1)
                os.system("taskkill /F /IM cmd.exe")
                os._exit(0)
            except Exception as e:
                print(f"ERROR 758: ERROR FOUND ERROR: {e}")
        elif tsdistrocommand == "switch user --USER":
            MAIN_USER_NAME = "USER"
        
        elif tsdistrocommand == "shutdown --host_os":
            try:
                shutdown_windows()
            except Exception as e:
                print(f"ERROR CODE 575: {e}")
        elif tsdistrocommand == "ts-package":
            os.system("git clone https://github.com/Coolis1362/ts-package-OFFICAL-PACKAGE-MANAGER")
            os.chdir("ts-package-OFFICAL-PACKAGE-MANAGER\\ts-package\\main")
            os.system("ts-package.bat")




if __name__ == "__main__": # DON'T REMOVE THIS LINE
    if boot():
        os.system("cls")
        put_distro_name_here() # REPLACE THIS LINE WITH THE NAME OF THE MAIN FUNCTION
    else:
        print("BOOT Failed")
        sys.exit(0)


# use auto-py-to-exe to Turn this Code To An .exe And replace The current .exe With Yours If auto-py-to-exe is not installed use pip install auto-py-to-exe to install it
# And Add C:\Users\<YourUsername>\AppData\Local\Programs\Python\<PythonVersion>\Lib\site-packages to Yuor PATH (Search How To Add It to PATHS)
# And Type in auto-py-to-exe In Your Terminal To Run It and Choose This File Yuo Had Edited and Choose The Output Folder As C:\Path\To\TS-KERNEL 1.0.0\root\boot\ And Choose The Icon You Want To Use And Click On Convert .py To .exe And Wait For It To Finish (Replace C:\Path\To\TS-KERNEL 1.0.0 With The Actal Path To Your TS-KERNEL 1.0.0 Folder) (AND DON'T FORGET TO TEST IT!)
# When You're Done Upload This To GitHub As Your Title Being Like TS-DISTRO Put Distro Here (REPLACE Put Distro Here WITH ACTAL NAME OF YOUR DISTRO) And Add A Description Like TS-DISTRO Put Distro Here Is A Distro Based On TS-KERNEL 1.0.0 And Add Tags Like TS-KERNEL, TS-DISTRO, Put Distro Here (REPLACE Put Distro Here WITH ACTAL NAME OF YOUR DISTRO) And Click On Publish And Wait For It To Finish (If You Don't Want To Upload It To GitHub Just Delete The .exe File And The .py File Will Be Left) And You're Done! Enjoy Your New Distro! (REPLACE Put Distro Here WITH ACTAL NAME OF YOUR DISTRO) (And Don't Forget To Replace The Name Of Your Distro In The Code!) (AND DON'T REMOVE THEESE LINES)