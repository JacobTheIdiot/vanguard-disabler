from pyfiglet import figlet_format
import subprocess
import ctypes
import os

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def get_input():
    print("1) Disable vanguard\n2) Enable vanguard\n3) Restart computer")

    try:
        task = int(input("What would you like to do: "))
    except ValueError:
        print("Enter a number.")
        return get_input()
    
    use_input_or_smth_idk_what_to_name_this(task)

def disable_vanguard():
    subprocess.run(['sc config vgc start= disabled & sc config vgk start= disabled & net stop vgc & net stop vgk & taskkill /IM vgtray.exe'], shell=True)
    print("You are now safe from the rat that is vanguard! if you'd like to play valorant again you will need to start vanguard again and restart your pc.")
    get_input()

def enable_vanguard():
    subprocess.run(['sc config vgc start= demand & sc config vgk start= system'], shell=True)
    print("For vanguard to fully boot you need to restart your pc (option 3)")
    get_input()

def restart_pc():
    subprocess.run("shutdown /r /t 5", shell=True)

def use_input_or_smth_idk_what_to_name_this(task: int):
        match task:
            case 1:
                print("Disabling vanguard...")
                disable_vanguard()
            case 2:
                print("Enabling vanguard...")
                enable_vanguard()
            case 3:
                print("Restarting pc in 5 seconds...")
                restart_pc()
            case _:
                print("Please enter a number between 1-3!")
                get_input()


def main():
    print(figlet_format("Vanguard-Disabler", font="standard"), "\n------------------------------------- by jacob")
    if not is_admin():
        print("This script must be run as admin!")
        os.system('pause')
        return

    get_input()

if __name__ == "__main__":
    main()