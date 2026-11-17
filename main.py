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
clearTerminal()
def typing(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def slowingtext(text):
    typing(text, delay=0.07)

def pause(seconds = 1.5):
    time.sleep(seconds)

# Global variables (Soph)
'''
>> How each one works
- Money
Total amount of money, enough said
- Event chance
how likely a special event is too happen from
1 to 100, the higher the number for a specific 
event the more likely it is to occur
- Tax
Varies depending on the amount of money and 
investors they have, the tax for the next week
is 15% of the final amount of money the player
has by the end of the current week, however
each additional investor decreases it by 2%
- Revenue
How much money the player makes each weak, 
adds 250$ every week plus an additional 5%
of that for every employee (employee stat is
player controlled for the most part)
- Reputation
Varies depending on the players performance,
works on a scale of 1-10. Reputation impacts
all events, higher reputation will increase
the chance for positive events while a lower
reputation makes negative events more likely
'''
Money = 100
Event_chance = 0
Tax = 0
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
    "Collaboration with another company", 
    "Got into controversy", 
    "Spider found in server room (we aint going in there)",
    "Taco tusday!"
]

Events = {
    "Positive events" : POS_events,
    "Nuetral events" : NUE_events,
    "Negative Events" : NEG_events,
    "Special events" : SPEC_events
}

weeks_left = 4
Endings = ["Talk of the town", "Infamous mark", "Bankrupt"]

# Start/Describe story to user (Soph)
slowingtext("<-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•>")
slowingtext("Welcome sir! You are the new CEO of Generic.CO, and we \n"
"need your help to keep both our STOCKS and REPUTATION up! \n"
"During your time as CEO, you'll need to maintain many things \n" 
"alongside the previously mentioned stocks and reputation, these \n" 
"include TAX and EVENTS. TAX is something you must pay by the \n"
"end of the week, EVENTS are things that happen after the week \n"
"is finished and these events can either have positive, nuetral, \n"
"or negative effects depending on your performancing during the week")
slowingtext("<-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•>")
print()

# Player options
'''
day = 5
while day != 0:
    print
'''

# outcomes


# events


# End story/results (Soph)
if weeks_left == 0:
    if Money >= 1500 and Reputation >= 7:
        slowingtext("<-♦-♦-♦-♦-♦-♦ Talk of the town ♦-♦-♦-♦-♦-♦-> \n"
        "You successfully kept both money and reputation \n"
        "in check! Good job :)")
    if Money == 0:
        slowingtext("-◈-◈-◈-◈-◈ Bankrupt ◈-◈-◈-◈-◈- \n"
        "What were you doing, selling literal trash!? \n"
        "YOU'RE FIRED!")
    if Reputation <= 7:
        slowingtext("-◈-◈-◈-◈-◈ Infamous mark ◈-◈-◈-◈-◈- \n" \
        "You've doomed us all")
