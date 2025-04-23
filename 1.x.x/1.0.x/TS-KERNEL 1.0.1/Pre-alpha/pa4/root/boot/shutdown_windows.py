from os import system
import keyboard # type: ignore
import sys

def shutdown_windows():
    system("echo This Will Shutdown Windows, This is windows Talking. Press Y to shutdown Windows, N to Shutdown TS-KERNEL")
while True:
    if keyboard.is_pressed("y"):
        system("echo Shutting Down Windows")
        system("shutdown -s")

    elif keyboard.is_pressed("n"):
        sys.exit(0)