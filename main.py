import time
import subprocess

def menu():
    print("Hello There!")
    
    minutes = get_minutes()
    display_notification(["notify-send","-u", "critical","⏰ Timer - session start",f"Timer set to {minutes}:00 minutes.\nStarting session now! "])
    timer(minutes) 
    display_notification(["notify-send","-u", "critical","⏰ Timer","Time is up!"])

def display_notification(info_list):
    """Dependency required: libnotify-bin"""
    subprocess.run(info_list)

def assert_dependencies(title, message):
    """Dependency required: libnotify-bin"""
    try:
        subprocess.run(
            ["notify-send", title, message],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False
    return True

def minutes_input():
    return input("Enter minutes for work-session: ")

def get_minutes():
    while True:
        try:
            minutes = int(minutes_input());
        except ValueError:
            print("Time must bed a non-negative int!")
            minutes = -1

        if minutes != -1:
            return minutes

def timer(minutes):

    for minute_counter in range(minutes):
        for second_counter in range(60):
            current_minutes = f"{minutes - minute_counter - 1}"
            if len(current_minutes) < 2:
                current_minutes = f"0{current_minutes}"

            current_seconds = f"{60 - second_counter - 1}"
            if len(current_seconds) < 2:
                current_seconds = f"0{current_seconds}"

            print(f"{current_minutes} : {current_seconds}")
            time.sleep(1)


if __name__ == "__main__":
    if assert_dependencies("Initializing Timer","Hello There!"):
        menu()

