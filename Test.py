import os
import sys
import time
import random

def clearTerminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
clearTerminal()
def typing(text, delay=0.):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def slowingtext(text):
    typing(text, delay=0)
def slowingtext1(text):
    typing(text, delay=0)

def pause(seconds = 1.5):
    time.sleep(seconds)

Money = 250
Tax = Money * 0.15
Reputation = 5
Investors = 0
Revenue = 250
POS_events = [
    "Popularity increase", 
    "Revenue increase", 
    "More investors", 
    "Less tax"
]

NUE_events = [
    "No popularity change", 
    "No revenue change", 
    "Same amount of investors", 
    "Same tax"
]

NEG_events = [
    "Lost popularity", 
    "Revenue decrease", 
    "Lost investors", 
    "More tax"
]

SPEC_events = [
    "Collaboration with another company (+15%, revenue)", 
    "Got into controversy (-3 reputation)", 
    "Spider found in server room (we aint going in there)",
    "Taco tusday! (+5 motivation :>)",
    "Became an internet legend (+999 aura and +6 reputation)",
    "Employees went on strike (-15%, revenue and -3 reputation)",
]

Events = {
    "Positive events" : POS_events,
    "Nuetral events" : NUE_events,
    "Negative Events" : NEG_events,
    "Special events" : SPEC_events
}

weeks_left = 2

Name = input("Enter your name... ")

slowingtext("<-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•>")
slowingtext(f"Welcome {Name}! You are the new CEO of Generic.CO, and we \n"
"need your help to keep both our STOCKS and REPUTATION up! \n"
"During your time as CEO, you'll need to maintain many things \n" 
"alongside the previously mentioned stocks and reputation, these \n" 
"include TAX and EVENTS. TAX is something you must pay by the \n"
"end of the week, EVENTS are things that happen after the week \n"
"is finished and these events can either have positive, nuetral, \n"
"or negative effects depending on your performancing during the week")
slowingtext("<-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•>")
print()

slowingtext("-◈-◈-◈-◈-◈-◈-◈ START ◈-◈-◈-◈-◈-◈-◈-")
slowingtext("Info:")
slowingtext(f" Weeks left: {weeks_left}")
slowingtext(f" Current tax: {Tax}")

slowingtext("The day drawls on as everyone works in the office. The people are okay but never the less work on and on. \n The taxes are alright, the managers are trying to make schedules and the company runs smoothly with the workers. \n Opportunities can be presented at any moment.")

pos_event = random.choice(POS_events)
neg_event = random.choice(NEG_events)
nue_event = random.choice(NUE_events)

slowingtext1("------------------------------------------------\n")
slowingtext1(" |                                             |\n")
slowingtext1(" |       A:", (pos_event),                    "|\n")
slowingtext1(" |                                             |\n")
slowingtext1(" |                                             |\n")
slowingtext1(" |       A:", (neg_event),                    "|\n")
slowingtext1(" |                                             |\n")
slowingtext1(" |                                             |\n")
slowingtext1(" |       A:", (nue_event),                    "|\n")
slowingtext1(" |                                             |\n")
slowingtext1("------------------------------------------------\n")

# slowingtext("After Text")

# slowingtext("Day Text")
slowingtext1("------------------------------------------------\n")
slowingtext1(" |                                             |\n")
slowingtext1(f"|       A:", (pos_event),                    "|\n")
slowingtext1(" |                                             |\n")
slowingtext1(" |                                             |\n")
slowingtext1(f"|       A:", (neg_event),                    "|\n")
slowingtext1(" |                                             |\n")
slowingtext1(" |                                             |\n")
slowingtext1(f"|       A:", (nue_event),                    "|\n")
slowingtext1(" |                                             |\n")
slowingtext1(" |                                             |\n")
slowingtext1("------------------------------------------------\n")


# slowingtext("After Text")

# slowingtext("Day Text")
slowingtext1("------------------------------------------------\n")
slowingtext1(" |                                             |\n")
slowingtext1(f"|       A:", (random.choice(POS_events)),    "|\n")
slowingtext1(" |                                             |\n")
slowingtext1(" |                                             |\n")
slowingtext1(f"|       B:", (random.choice(NEG_events)),    "|\n")
slowingtext1(" |                                             |\n")
slowingtext1(" |                                             |\n")
slowingtext1(f"|      C:", (random.choice(NUE_events)),     "|\n")
slowingtext1(" |                                             |\n")
slowingtext1(" |                                             |\n")
slowingtext1("------------------------------------------------\n")

# slowingtext("After text")

if Money > 500:
    if Reputation >= 7:
        if Tax < 75:
            slowingtext("The office is happy, everyone is working hard and making good money. The taxes \n" "are beginning to become nothing. Everyone is happy to have you as their CFO. What a good week.\n" "Society is stable and peaceful.")
        slowingtext("The office is working moderately. The taxes are keeping everyone on a livable wage. But if something happens, they hope you can help them. Society is peaceful.")
    slowingtext("The office is bland and colorless. Everyone just comes to work and leaves. No one is happy and everything they do is the bare minimum. What is wrong? Everyone makes good money but is anyone really happy. Society is stable.") 
