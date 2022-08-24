import sys,time,os
from pyfiglet import figlet_format
choisir = figlet_format("Choisir")
print(choisir)

inventory = "+--------------------------+\n| +--+ +--+ +--+ +--+ +--+ |\n| |  | |  | |  | |  | |  | |\n| +--+ +--+ +--+ +--+ +--+ |\n+--------------------------+"

def annonce(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.07)        

states = {
    "start": {
        "annonce": "You are in a very dark room.",
        "choices": [
            {
                "annonce": "You stand up.",
                "command": "i stand up",
                "state": "stand"
            },
            {
                "annonce": "You look at the time.",
                "command": "i look at the time",
                "state": "time"
            },
            {
                "annonce": "You don't move.",
                "command": "i don't move",
                "state": "stay"
            }
        ]
    },
    "stand": {
        "annonce": "You see that you are lonely and shut in. You remember that you have your phone with you, but, you have only 13% battery.",
        "choices": [
            {
                "annonce": "You turn on your flashlight.",
                "command": "i turn on my flashlight",
                "state": "flashlight"
            },
            {
                "annonce": "You look at google maps to know where are you located.",
                "command": "i look at google maps",
                "state": "maps"
            },
            {
                "annonce": "You call the cops.",
                "command": "i call the cops",
                "state": "cops"
            }
        ]
    },
    "time": {
        "annonce": "It is 4 AM, but your watch seems to be broken, beacause the needles doesn't move.",
        "state": "start"
    },
    "stay": {
        "annonce": "You fall asleep, and one hour later, a man come kill you.",
        "game_over": True
    },
    "flashlight": {
        "annonce": "You see a iron gate. But it is locked.",
        "choices": [
            {
                "annonce": "You try to break the gate.",
                "command": "i try to break the gate",
                "state": "gate"
            },
            {
                "annonce": "You sit down.",
                "command": "i sit down",
                "state": "sit"
            }
        ]
    },
    "maps": {
        "annonce": "Your geolocation doesn't seems to work, you can turn on it but, you hear some footsteps.",
        "choices": [
            {
                "annonce": "You turn on your geolocation but the footsteps are getting closer and closer."
            },
            {
                "annonce": "You will hide.",
                "command": "i will hide",
                "state": "hide"
            }
        ]
    },
    "cops": {
        "annonce": "You call . . . \n\n[911] - 911 what's your emergency ?",
        "choices": [
            {
                "annonce": "(a) I'm shut in.",
                "command": "a",
                "state": "cops-a"
            },
            {
                "annonce": "(b) Help, i will die if you don't come !",
                "command": "b"
            },
            {
                "annonce": "(c) Where am I please ?",
                "command": "c"
            }
        ]
    },
    "gate": {
        "annonce": "You manage to break down the door but they kill you.",
        "game_over": True
    },
    "sit": {
        "annonce": "You are becoming crazy.",
        "game_over": True
    },
    "hide": {
        "annonce": "You drop your phone not on purpose."
    },
    "cops-a": {
        "annonce": "[You] I'm shut in, help me please.\n\n[911] Where are you sir ?"
    }
}

state_name = "start"

while True:
    state = states[state_name]
    annonce(state["annonce"] + "\n")

    if "state" in state:
        state_name = state["state"]

    elif "choices" in state:
        for choice in state["choices"]:
            print(" - " + choice["annonce"])

        command = input("What do you do ? ")

        selected = None
        for choice in state["choices"]:
            if command.lower() == choice["command"]:
                selected = choice
                break

        if selected is not None:
            state_name = selected["state"]

    elif "game_over" in state and state["game_over"] == True:
        over = figlet_format("Game Over")  
        print(over)   
        break     

    else:
        break
