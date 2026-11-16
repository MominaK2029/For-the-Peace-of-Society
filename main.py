# imports
import os
import sys
import time
import random

# Typing Effects
def clearTerminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def typing(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def slowingtext(text):
    typing(text, speed=0.07)

def pause(seconds = 1.5):
    time.sleep(seconds)

# Global variables (Soph)
Money = 0
Event_chance = 0
Tax = 0
Reputation = 0
Investors = 0
POS_events = ["Popularity increase", "Revenue increase", "More investors", "Less tax"]
NUE_events = ["No popularity change", "No revenue change", "Same amount of investors", "Same tax"]
NEG_events = ["Lost popularity", "Revenue decrease", "Lost investors", "More tax"]
SPEC_events = [
    "Collaboration with another company", 
    "Got into controversy", 
    "Spider found in server room (we aint going in there)",
    ""
]
Events = {
    "Positive events" : POS_events,
    "Nuetral events" : NUE_events,
    "Negative Events" : NEG_events,
    "Special events" : SPEC_events
}
Endings = ["Talk of the town", "Stocks crashed", "Infamous mark", "Bankrupt"]

# Start/Describe story to user (Soph)
print("<-------------------------------------------------------->")
print("Welcome sir! You are the new CEO of Generic.CO, and we \n"
"need your help to keep both our STOCKS and REPUTATION up! \n"
"During your time as CEO, you'll need to maintain many things \n" 
"alongside the previously mentioned stocks and reputation, these \n" 
"include TAX and EVENTS. TAX is something you must pay by the \n "
"end of the week, EVENTS are things that happen after the week \n"
"is finished and these events can either have positive, nuetral, \n"
"or negative effects depending on your performancing during the week")

# events


# Player options


# outcomes


# End story/results (Soph)

