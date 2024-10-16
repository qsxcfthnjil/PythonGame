import os
import time
import keyboard
import random
import sys
from threading import Timer
import math

incombat = True
refreshrate = 0.4
enemies = 1
difficulty = 3
kindness = 0
kindness2 = 0
stun = 0
tired = False
intutorial = False

def resettotutorialmessage():
    global message
    message = "Tutorial Start - No penalty for death, no stuns.\nUse the up and down arrows to control the speed as you see fit."

def enemytired():
    global intutorial
    global is_fake
    global tired
    global message
    if intutorial == False and not battle == "Shadowking1":
        is_fake = False
        tired = True
        message = "The enemy looks tired."
        clearenemyattacks()
    if battle == "Shadowking1":
        is_fake = False
        message = "The Shadow King looks winded."


def unstun():
    global stun
    global message
    if stun > 0:
        stun = stun - 1
        message = "Unstunned! Stun x" + str(stun)
        refresh()
        if stun > 0:
            stuntimer.start()
from threading import Timer, Lock


class TimerEx(object):
    """
    A reusable thread safe timer implementation
    """

    def __init__(self, interval_sec, function, *args, **kwargs):
        """
        Create a timer object which can be restarted

        :param interval_sec: The timer interval in seconds
        :param function: The user function timer should call once elapsed
        :param args: The user function arguments array (optional)
        :param kwargs: The user function named arguments (optional)
        """
        self._interval_sec = interval_sec
        self._function = function
        self._args = args
        self._kwargs = kwargs
        # Locking is needed since the '_timer' object might be replaced in a different thread
        self._timer_lock = Lock()
        self._timer = None

    def start(self, restart_if_alive=True):
        """
        Starts the timer and returns this object [e.g. my_timer = TimerEx(10, my_func).start()]

        :param restart_if_alive: 'True' to start a new timer if current one is still alive
        :return: This timer object (i.e. self)
        """
        with self._timer_lock:
            # Current timer still running
            if self._timer is not None:
                if not restart_if_alive:
                    # Keep the current timer
                    return self
                # Cancel the current timer
                self._timer.cancel()
            # Create new timer
            self._timer = Timer(self._interval_sec, self.__internal_call)
            self._timer.start()
        # Return this object to allow single line timer start
        return self

    def cancel(self):
        """
        Cancels the current timer if alive
        """
        with self._timer_lock:
            if self._timer is not None:
                self._timer.cancel()
                self._timer = None

    def is_alive(self):
        """
        :return: True if current timer is alive (i.e not elapsed yet)
        """
        with self._timer_lock:
            if self._timer is not None:
                return self._timer.is_alive()
        return False

    def __internal_call(self):
        # Release timer object
        with self._timer_lock:
            self._timer = None
        # Call the user defined function
        self._function(*self._args, **self._kwargs)
        
        
        
        


def clearmessage():
    global message
    message = "Keep going!"
stuntimer = TimerEx(interval_sec=6, function=unstun,)
tiredtimer20 = TimerEx(interval_sec=20, function=enemytired,)
messageresettimer = TimerEx(interval_sec=2,function=resettotutorialmessage,)
timer = Timer(3, clearmessage, args=())
line1 = [">             *  *  *  *","0000","0"]
line2 = [">             *  *  *  *","0000","0"]
line3 = [">             *  *  *  *","0000","0"]
line4 = [">             *  *  *  *","0000","0"]
line5 = [">             *  *  *  *","0000","0"]
line6 = [">             *  *  *  *","0000","0"]
line7 = [">             *  *  *  *","0000","0"]
line8 = [">             *  *  *  *","0000","0"]
line9 = [">             *  *  *  *","0000","0"]
line10 = [">             *  *  *  *","0000","0"]
line11 = [">             *  *  *  *","0000","0"]
line12 = [">             *  *  *  *","0000","0"]
currentline = [">             *  *  *  *","0000","0"]

message = "Do NOT let the X's hit the equals signs. you need to HOLD the button down!"





def generateattack(count,difficulty):
    global nextline
    rngdifficulty = 10 - difficulty
    if count == 2:
        r = random.randint(1,5)
        if r <= 3:
            count = 1
    if count == 3:
        r = random.randint(1,5)
        if r <= 1:
            count = 1
        elif r <= 3:
            count = 2
    if count == 4:
        r = random.randint(1,5)
        if r <= 1:
            count = 1
        elif r <= 3:
            count = 2
        elif r <= 4:
            count = 3
    if rngdifficulty < random.randint(0,10):
        if count == 1:
            possibleattacks = ["1000","0001","0100","0010"]
            nextattack = random.choice(possibleattacks)
            if nextattack == "1000":
                nextline = [">             X  *  *  *","1000","0"]
            elif nextattack == "0001":
                nextline = [">             *  *  *  X","0001","0"]
            elif nextattack == "0100":
                nextline = [">             *  X  *  *","0100","0"]
            elif nextattack == "0010":
                nextline = [">             *  *  X  *","0010","0"]
        elif count == 2:
            possibleattacks = ["1100","0110","0011","1001","1010","0110","0101"]
            nextattack = random.choice(possibleattacks)
            if nextattack == "1100":
                nextline = [">             X  X  *  *","1100","0"]
            elif nextattack == "0110":
                nextline = [">             *  X  X  *","0110","0"]
            elif nextattack == "0011":
                nextline = [">             *  *  X  X","0011","0"]
            elif nextattack == "1001":
                nextline = [">             X  *  *  X","1001","0"]
            elif nextattack == "1010":
                nextline = [">             X  *  X  *","1010","0"]
            elif nextattack == "0101":
                nextline = [">             *  X  *  X","0101","0"]
        elif count == 3:
            possibleattacks = ["1110","0111","1011","1101"]
            nextattack = random.choice(possibleattacks)
            if nextattack == "1110":
                nextline = [">             X  X  X  *","1110","0"]
            elif nextattack == "0111":
                nextline = [">             *  X  X  X","0111","0"]
            elif nextattack == "1011":
                nextline = [">             X  *  X  X","1011","0"]
            elif nextattack == "1101":
                nextline = [">             X  X  *  X","1101","0"]
        elif count == 4:
            nextline = [">             X  X  X  X","1111","0"]
    else:
        nextline = [">             *  *  *  *","0000","0"]



def generateslash(fake):
    global nextslash
    global nextline
    global nextatkline
    if fake == False:
        attackchance = random.randint(0,19)
        if attackchance < 6 and tired == False:
            possibleslashes = ["01","10","11","00"]
            nextslash = random.choice(possibleslashes)
            if nextslash == "00":
                nextatkline = ["                *  *"]
                nextline[2] = "00"
            elif nextslash == "11":
                nextatkline = ["                X  X"]
                nextline[2] = "11"
            elif nextslash == "10":
                nextatkline = ["                X  *"]
                nextline[2] = "10"
            elif nextslash == "01":
                nextatkline = ["                *  X"]
                nextline[2] = "01"
        elif attackchance < 8 and tired == True:
            possibleslashes = ["01","10","11","00"]
            nextslash = random.choice(possibleslashes)
            if nextslash == "00":
                nextatkline = ["                *  *"]
                nextline[2] = "00"
            elif nextslash == "11":
                nextatkline = ["                X  X"]
                nextline[2] = "11"
            elif nextslash == "10":
                nextatkline = ["                X  *"]
                nextline[2] = "10"
            elif nextslash == "01":
                nextatkline = ["                *  X"]
                nextline[2] = "01"        
        else:
            nextatkline = ["                *  *"]
            nextline[2] = "00"
    else:
        nextatkline = ["                *  *"]
        nextline[2] = "00"


def connectattackdef():
    nextline[0] = nextline[0] + nextatkline[0]






















def clearattacks():
    global currentline
    global line12
    global line11
    global line10
    global line9
    global line8
    global line7
    global line6
    global line5
    global line4
    global line3
    global line2
    global line1
    global nextline
    line1[2] = "0"
    line2[2] = "0"
    line3[2] = "0"
    line4[2] = "0"
    line5[2] = "0"
    line6[2] = "0"
    line7[2] = "0"
    line8[2] = "0"
    line9[2] = "0"
    line10[2] = "0"
    line11[2] = "0"
    line12[2] = "0"
    currentline[2] = "0"
    nextline[2] = "0"
    line1str = line1[0]
    line1[0] = line1str[:24] + "                *  *"
    line2str = line2[0]
    line2[0] = line2str[:24] + "                *  *"
    line3str = line3[0]
    line3[0] = line3str[:24] + "                *  *"
    line4str = line4[0]
    line4[0] = line4str[:24] + "                *  *"
    line5str = line5[0]
    line5[0] = line5str[:24] + "                *  *"
    line6str = line6[0]
    line6[0] = line6str[:24] + "                *  *"
    line7str = line7[0]
    line7[0] = line7str[:24] + "                *  *"
    line8str = line8[0]
    line8[0] = line8str[:24] + "                *  *"
    line9str = line9[0]
    line9[0] = line9str[:24] + "                *  *"
    line10str = line10[0]
    line10[0] = line10str[:24] + "                *  *"
    line11str = line11[0]
    line11[0] = line11str[:24] + "                *  *"
    line12str = line12[0]
    line12[0] = line12str[:24] + "                *  *"
    nextlinestr = nextline[0]
    nextline[0] = nextlinestr[:24] + "                *  *"
    
    
def clearenemyattacks():
    global currentline
    global line12
    global line11
    global line10
    global line9
    global line8
    global line7
    global line6
    global line5
    global line4
    global line3
    global line2
    global line1
    global nextline
    line1[1] = "0000"
    line2[1] = "0000"
    line3[1] = "0000"
    line4[1] = "0000"
    line5[1] = "0000"
    line6[1] = "0000"
    line7[1] = "0000"
    line8[1] = "0000"
    line9[1] = "0000"
    line10[1] = "0000"
    line11[1] = "0000"
    line12[1] = "0000"
    currentline[2] = "0000"
    nextline[2] = "0000"
    line1str = line1[0]
    line1[0] = ">             *  *  *  *" + line1str[24:]
    line2str = line2[0]
    line2[0] = ">             *  *  *  *" + line2str[24:]
    line3str = line3[0]
    line3[0] = ">             *  *  *  *" + line3str[24:]
    line4str = line4[0]
    line4[0] = ">             *  *  *  *" + line4str[24:]
    line5str = line5[0]
    line5[0] = ">             *  *  *  *" + line5str[24:]
    line6str = line6[0]
    line6[0] = ">             *  *  *  *" + line6str[24:]
    line7str = line7[0]
    line7[0] = ">             *  *  *  *" + line7str[24:]
    line8str = line8[0]
    line8[0] = ">             *  *  *  *" + line8str[24:]
    line9str = line9[0]
    line9[0] = ">             *  *  *  *" + line9str[24:]
    line10str = line10[0]
    line10[0] = ">             *  *  *  *" + line10str[24:]
    line11str = line11[0]
    line11[0] = ">             *  *  *  *" + line11str[24:]
    line12str = line12[0]
    line12[0] = ">             *  *  *  *" + line12str[24:]
    currentlinestr = currentline[0]
    currentline[0] = ">             *  *  *  *" + currentlinestr[24:]
    nextlinestr = nextline[0]
    nextline[0] = ">             *  *  *  *" + nextlinestr[24:]



def clearboard():
    global currentline
    global line12
    global line11
    global line10
    global line9
    global line8
    global line7
    global line6
    global line5
    global line4
    global line3
    global line2
    global line1
    line1 = [">             *  *  *  *","0000","0"]
    line2 = [">             *  *  *  *","0000","0"]
    line3 = [">             *  *  *  *","0000","0"]
    line4 = [">             *  *  *  *","0000","0"]
    line5 = [">             *  *  *  *","0000","0"]
    line6 = [">             *  *  *  *","0000","0"]
    line7 = [">             *  *  *  *","0000","0"]
    line8 = [">             *  *  *  *","0000","0"]
    line9 = [">             *  *  *  *","0000","0"]
    line10 = [">             *  *  *  *","0000","0"]
    line11 = [">             *  *  *  *","0000","0"]
    line12 = [">             *  *  *  *","0000","0"]
    currentline = [">             *  *  *  *","0000","0"]



def chanceofclearattacks():
    randomthing = random.randint(1,10)
    if randomthing < 7:
        clearenemyattacks()






def shiftlines():
    checkdeath()
    checkattack()
    global currentline
    global line12
    global line11
    global line10
    global line9
    global line8
    global line7
    global line6
    global line5
    global line4
    global line3
    global line2
    global line1
    global nextline
    currentline = line12
    line12 = line11
    line11 = line10    
    line10 = line9    
    line9 = line8
    line8 = line7    
    line7 = line6    
    line6 = line5    
    line5 = line4    
    line4 = line3    
    line3 = line2
    line2 = line1    
    line1 = nextline    


combo = 0
def combospeedup():
    global combo
    global incombat
    global additivecomborefresh
    global message
    if combo == 3:
        additivecomborefresh = 1.1
    elif combo == 5:
        if battle == "Goblin":
            incombat = False
            if tiredtimer20.is_alive():
                tiredtimer20.cancel()
            if stuntimer.is_alive():
                stuntimer.cancel()
        additivecomborefresh = 1.2
    elif combo == 6:
        additivecomborefresh = 1.5
    elif combo == 7:
        if battle == "Goblin gang":
            incombat = False
            if tiredtimer20.is_alive():
                tiredtimer20.cancel()
            if stuntimer.is_alive():
                stuntimer.cancel()
        additivecomborefresh = 1.6
    elif combo == 8:
        additivecomborefresh = 1.7
    elif combo == 9:
        additivecomborefresh = 2
    elif combo == 10:
        incombat = False
        clearboard()
        message = "End of Demo."
        refresh()


def checkattack():
    global combo
    global tired
    global additivecomborefresh
    global message
    global refreshrate
    global kindness2
    reqkeys = currentline[2]
    if reqkeys == "01":
        if keyboard.is_pressed('j'):
            message = "HIT! Combo X" + str(combo)
            combo = combo + 1
            combospeedup()
            tired = True
            kindness2 = 0
            chanceofclearattacks()
            refresh()
        elif keyboard.is_pressed('d'):
            if kindness2 == 0:
                kindness2 = 1
            else:
                if not combo == 0:
                    message = "Miss! Combo ended."
                additivecomborefresh = 1
                combo = 0
                tired = False
                if not tiredtimer20.is_alive():
                    tiredtimer20.start()
        else:
            if kindness2 == 0:
                kindness2 = 1
            else:
                if not combo == 0:
                    message = "Miss! Combo ended."
                additivecomborefresh = 1
                combo = 0
                tired = False
                if not tiredtimer20.is_alive():
                    tiredtimer20.start()
    if reqkeys == "10":
        if keyboard.is_pressed('d'):
            message = "HIT! Combo X" + str(combo)
            combo = combo + 1
            combospeedup()
            tired = True
            kindness2 = 0
            chanceofclearattacks()
            refresh()
        elif keyboard.is_pressed('j'):
            if kindness2 == 0:
                kindness2 = 1
            else:
                if not combo == 0:
                    message = "Miss! Combo ended."
                additivecomborefresh = 1
                combo = 0
                tired = False
                if battle == "Shadowking1":
                    refreshtimer = 0.6
                if not tiredtimer20.is_alive():
                    tiredtimer20.start()
        else:
            if kindness2 == 0:
                kindness2 = 1
            else:
                if not combo == 0:
                    message = "Miss! Combo ended."
                additivecomborefresh = 1
                combo = 0
                tired = False
                if battle == "Shadowking1":
                    refreshtimer = 0.6
                if not tiredtimer20.is_alive():
                    tiredtimer20.start()
    if reqkeys == "11":
        if keyboard.is_pressed('d') and keyboard.is_pressed('j'):
            message = "HIT! Combo X" + str(combo)
            combo = combo + 1
            tired = True
            kindness2 = 0
            combospeedup()
            chanceofclearattacks()
            refresh()
        else:
            if kindness2 == 0:
                kindness2 = 1
            else:
                if not combo == 0:
                    message = "Miss! Combo ended."
                additivecomborefresh = 1
                combo = 0
                tired = False
                if battle == "Shadowking1":
                    refreshtimer = 0.6
                if not tiredtimer20.is_alive():
                    tiredtimer20.start()


battle = "tutorial/test"



def checkstun():
    global stun
    global stuntimer
    global incombat
    global message
    global is_fake
    global intutorial
    global messageresettimer
    global tired
    global tiredtimer20
    if intutorial == False:
        if stun < 3:
            time.sleep(0.5)
            stun = stun + 1
            message = "STUNNED! (x" + str(stun) + ")"
            is_fake = True
            clearattacks()
            tired = False
            if not stuntimer.is_alive():
                stuntimer.start()
            if not tiredtimer20.is_alive():
                tiredtimer20.start()
        else:
            if battle == "tutorial/test":
                incombat = False
                clear()
                slowprintintroduction("Bruh you died.")
            elif battle == "Shadowking1":
                incombat = False
                if tiredtimer20.is_alive():
                    tiredtimer20.cancel()
                if stuntimer.is_alive():
                    stuntimer.cancel()
                message = "..."
            elif battle == "Goblin":
                incombat = False
                if tiredtimer20.is_alive():
                    tiredtimer20.cancel()
                if stuntimer.is_alive():
                    stuntimer.cancel()
                message = "..."
                refresh()
                time.sleep(5)
                clear()
                extraslowprintintroduction(f"{playername} was felled by a Goblin on day {day}.   \nBut you can't give up now! Who else will save the world?")
                time.sleep(5)
                quit()
            elif battle == "Goblin gang":
                incombat = False
                if tiredtimer20.is_alive():
                    tiredtimer20.cancel()
                if stuntimer.is_alive():
                    stuntimer.cancel()
                message = "..."
                refresh()
                time.sleep(5)
                clear()
                extraslowprintintroduction(f"{playername} was suprised by a goblin ambush on day {day}.   \nBut you can't give up now! Who else will save the world?")
                time.sleep(5)
                quit()

                
    else:
        message = "Ah, you got hit!"
        if not messageresettimer.is_alive():
            messageresettimer.start()
        refresh()
        time.sleep(0.5)
        clearboard()




















def checkdeath():
    global incombat
    global kindness
    reqkeys = currentline[1]
    if reqkeys == "0000":
        if keyboard.is_pressed("s") or keyboard.is_pressed("k") or keyboard.is_pressed("l") or keyboard.is_pressed("a"):
            if kindness == 0:
                kindness = 1
            else:
                checkstun()
    elif reqkeys == "1000":
        if not keyboard.is_pressed("a"):
            checkstun()
        else:
            kindness = 0
        if keyboard.is_pressed("s") or keyboard.is_pressed("k") or keyboard.is_pressed("l"):
            checkstun()
        else:
            kindness = 0      
    elif reqkeys == "0100":
        if not keyboard.is_pressed("s"):
            checkstun()
        else:
            kindness = 0
        if keyboard.is_pressed("a") or keyboard.is_pressed("k") or keyboard.is_pressed("l"):
            checkstun()
        else:
            kindness = 0

    elif reqkeys == "0010":
        if not keyboard.is_pressed("k"):
            checkstun()
        else:
            kindness = 0
        if keyboard.is_pressed("s") or keyboard.is_pressed("a") or keyboard.is_pressed("l"):
            checkstun() 
        else:
            kindness = 0
    elif reqkeys == "0001":
        if not keyboard.is_pressed("l"):
            checkstun()
        else:
            kindness = 0
        if keyboard.is_pressed("s") or keyboard.is_pressed("a") or keyboard.is_pressed("k"):
            checkstun() 
        else:
            kindness = 0
    elif reqkeys == "1100":
        if not (keyboard.is_pressed("a") and keyboard.is_pressed("s")):
            checkstun()
        else:
            kindness = 0
        if keyboard.is_pressed("k") or keyboard.is_pressed("l"):
            checkstun() 
    elif reqkeys == "1010":
        if not (keyboard.is_pressed("a") and keyboard.is_pressed("k")):
            checkstun()
        else:
            kindness = 0
        if keyboard.is_pressed("s") or keyboard.is_pressed("l"):
            checkstun() 
    elif reqkeys == "1001":
        if not (keyboard.is_pressed("a") and keyboard.is_pressed("l")):
            checkstun()
        else:
            kindness = 0
        if keyboard.is_pressed("s") or keyboard.is_pressed("k"):
            checkstun() 
    elif reqkeys == "0110":
        if not (keyboard.is_pressed("s") and keyboard.is_pressed("k")):
            checkstun()
        else:
            kindness = 0
        if keyboard.is_pressed("a") or keyboard.is_pressed("l"):
            checkstun() 
    elif reqkeys == "0101":
        if not (keyboard.is_pressed("s") and keyboard.is_pressed("l")):
            checkstun()
        else:
            kindness = 0
        if keyboard.is_pressed("a") or keyboard.is_pressed("k"):
            checkstun() 
    elif reqkeys == "0011":
        if not (keyboard.is_pressed("k") and keyboard.is_pressed("l")):
            checkstun()
        else:
            kindness = 0
        if keyboard.is_pressed("a") or keyboard.is_pressed("s"):
            checkstun() 
    elif reqkeys == "0111":
        if not (keyboard.is_pressed("k") and keyboard.is_pressed("l") and keyboard.is_pressed('s')):
            checkstun()
        else:
            kindness = 0
        if keyboard.is_pressed("a"):
            checkstun() 
    elif reqkeys == "1011":
        if not (keyboard.is_pressed("a") and keyboard.is_pressed("l") and keyboard.is_pressed('k')):
            checkstun()
        else:
            kindness = 0
        if keyboard.is_pressed("s"):
            checkstun() 
    elif reqkeys == "1101":
        if not (keyboard.is_pressed("a") and keyboard.is_pressed("l") and keyboard.is_pressed('s')):
            checkstun()
        else:
            kindness = 0
        if keyboard.is_pressed("k"):
            checkstun() 
    elif reqkeys == "1110":
        if not (keyboard.is_pressed("k") and keyboard.is_pressed("a") and keyboard.is_pressed('s')):
            checkstun()
        else:
            kindness = 0
        if keyboard.is_pressed("l"):
            checkstun() 
    elif reqkeys == "1111":
        if not (keyboard.is_pressed("k") and keyboard.is_pressed("a") and keyboard.is_pressed('s') and keyboard.is_pressed('l')):
            checkstun()
        else:
            kindness = 0



def clear():
    os.system('cls')

def slowprintintroduction(string):
    i = 0
    resultstring = ""
    while i < len(string):
        clear()
        resultstring = resultstring + string[i]
        print(resultstring)
        i += 1
        time.sleep(0.005)
        
        
def dialogue(name,string):
    global cancontinue
    i = 0
    resultstring = f"\n---- ({name}) ---------------------------------------------\n"
    cancontinue = False
    while i < len(string):
        clear()
        resultstring = resultstring + string[i]
        i += 1
        if i == len(string):
            print(resultstring + "\n(x)")
            cancontinue = True
        else:
            print(resultstring)
        time.sleep(0.05)


def cutscene(string):
    global cancontinue
    i = 0
    resultstring = ""
    cancontinue = False
    while i < len(string):
        clear()
        resultstring = resultstring + string[i]
        i += 1
        if i == len(string):
            print(resultstring + "\n(x)")
            cancontinue = True
        else:
            print(resultstring)
        
        
        
        
        
def extraslowprintintroduction(string):
    i = 0
    resultstring = ""
    while i < len(string):
        clear()
        resultstring = resultstring + string[i]
        print(resultstring)
        i += 1
        time.sleep(0.2)        
        
        


def slowprint(string):
    i = 0
    resultmessage = ""
    while i < len(string):
        resultmessage = resultmessage + string[i]
        global message
        message = resultmessage
        i += 1
        refresh()
        time.sleep(0.05)




def refreshspeedcontrol():
    global stun
    global difficulty
    global enemies
    global additivecomborefresh
    global additiverefresh
    global is_fake
    global incombat
    if stun == 0:
        generateattack(enemies,difficulty)
        additiverefresh = 0
    elif stun == 1:
        if difficulty < 10:
            generateattack(enemies,difficulty + 1)      
        else:
            additiverefresh = 0.02 
    elif stun == 2:
        if difficulty < 9:
            generateattack(enemies,difficulty + 2)  
        else:
            additiverefresh = 0.05
    elif stun == 3:
        if difficulty < 8:
            generateattack(enemies,difficulty + 3)  
        else:
            additiverefresh = 0.1
    generateslash(is_fake)
    connectattackdef()
    shiftlines()
    if incombat == True:
        refresh()
        if stun == 0:
            if tired == True:
                time.sleep((refreshrate + 0.2) / additivecomborefresh)
            else:
                time.sleep(abs(refreshrate - additiverefresh)/ additivecomborefresh)
        elif stun == 1:
            try:
                time.sleep(refreshrate - additiverefresh - 0.05)
            except:
                time.sleep(0.1)
        elif stun == 2:
            try:
                time.sleep(refreshrate - additiverefresh - 0.05)
            except:
                time.sleep(0.1)
        elif stun == 3:
            try:
                time.sleep(refreshrate - additiverefresh - 1)
            except:
                time.sleep(0.05)

def endgame():
    clear()
    print("Stopping Game")
    quit()

def refresh():
    clear()
    print("")
    print("_____________________________________________________________")
    print("-------------D E F E N D-------------A T T A C K-------------")
    print("------------  A  S  K  L-------------   D  J    -------------")
    print(line1[0])
    print(line2[0])
    print(line3[0])
    print(line4[0])
    print(line5[0])
    print(line6[0])
    print(line7[0])
    print(line8[0])
    print(line9[0])
    print(line10[0])     
    print(line11[0])
    print(line12[0])
    print("_____________________________________________________________") 
    print(currentline[0])
    print("=============================================================") 
    print("_____________________________________________________________") 
    print("\n")
    print("> " + message)
    print("\n")
    print("_____________________________________________________________") 

playername = ''
startup = 0



def speedup():
    global refreshrate
    if refreshrate > 0.1:
        refreshrate = refreshrate - 0.1


def gamestart():
    global playername
    global startup
    clear()
    if startup == 0:
        startup = 1
        slowprintintroduction("Hey there. What may your name be?")
        clear()
        playername = input("Hey there. What may your name be?\n> ")
        playername = playername.strip()
        if playername == "":
            startup = 0
            slowprintintroduction("Sorry, invalid name.")
            time.sleep(2)
            gamestart()



#slowprintintroduction("""_____________________________________________________________
#-------------D E F E N D-------------A T T A C K-------------
#------------  A  S  K  L-------------   D  J    -------------""")


#slowprint("Hi. This is a demo of a game i'm working on.\n> The objective will be to hit the keys as they come in from above.")

#time.sleep(2)
#slowprint("Press X to continue.")
additiverefresh = 0
additivecomborefresh = 1
menu = 1
is_fake = False
menuselection = 0
slowprintintroduction("Menu:\nStart new game\nTutorial\nCredits\nTesting\n\n(Use the shift key to navigate the menu)")

while menu == 1:
    if keyboard.is_pressed("Shift"):
        if menuselection == 0 or menuselection == 4:
            menuselection = 1
            clear()
            print("Menu:\n> Start new game\nTutorial\nCredits\nTesting\n\n(Use the Control key to select.)")
        elif menuselection == 1:
            menuselection = 2
            clear()
            print("Menu:\nStart new game\n> Tutorial\nCredits\nTesting\n\n(Use the Control key to select.)")
        elif menuselection == 2:
            menuselection = 3
            clear()
            print("Menu:\nStart new game\nTutorial\n> Credits\nTesting\n\n(Use the Control key to select.)") 
        elif menuselection == 3:
            menuselection = 4
            clear()
            print("Menu:\nStart new game\nTutorial\nCredits\n> Testing\n\n(Use the Control key to select.)") 
        time.sleep(0.2)
        
    if keyboard.is_pressed("Control"):
        if menuselection == 0:
            pass
        elif menuselection == 1:
            menu = "Main - Intro"
            introstage = 1
            cancontinue = False


        elif menuselection == 2:
            menu = "Tutorial"
            cancontinue = False
            slowprintintroduction("Hey there! Welcome to the first game I've made on python.\n(x)\nPRESS Z TO SKIP DIALOGUE")
            cancontinue = True
            tutorialdialogue = 0
        elif menuselection == 3:
            menu = False
            slowprintintroduction("Hey man, this game was made by a really epic person by the name of Richardo Liu.\nPlaytesting credits go to Mr. Mick Laughing, Mr. O, and uhhhhhh that other guy.")
            time.sleep(5)
            menu = 1
            clear()
            print("Menu:\nStart new game\nTutorial\n> Credits\nTesting\n\n(Use the enter key to select.)")  
            
        elif menuselection == 4:
            menu = "password"
            clear()
            time.sleep(0.5)

        time.sleep(0.2)
    if keyboard.is_pressed('p') and menu == 1:
        endgame()
        
        
        
        
while menu == "password":
    userpassword = input("Enter the admin password or be smited.\n> ")
    if userpassword == "Qsxc333":
        menu = 2
        refresh()
    else:
        pass




def gamestart2():
    global partnername
    slowprintintroduction(f"Greetings, {playername}. What is your partner named?")
    clear()
    partnername = input(f"Greetings, {playername}. What is your partner named?\n> ")
    partnername = partnername.strip()
    if partnername == "":
        slowprintintroduction("Invalid name. Try again.")
        time.sleep(2)





while menu == "Main - Intro":
    if cancontinue == True:
        if keyboard.is_pressed('x'):
            cancontinue = False
            introstage = introstage[0] + 1
        if keyboard.is_pressed("u") and keyboard.is_pressed('i'):
            cancontinue = False
            introstage = 17
        if keyboard.is_pressed("m") and keyboard.is_pressed('n'):
            menu = 'maingame'
            day = 1
            revivalseeds = 0
            progress = 0
            menuselection = 0
            inmenu = True
            
            slowprintintroduction(f"-----------------\n{playername}\n-----------------\nDay {day}\nRevival seeds: {revivalseeds}\nProgress: {progress}\n\nWhat do you do?\nTravel\nForage\nRest\nSave\n(Use the shift key to navigate)")

    if introstage == 1:
        gamestart()
        gamestart2()

        extraslowprintintroduction("\n...")
        clear()
        if keyboard.is_pressed("u") and keyboard.is_pressed('i'):
            cancontinue = False
            introstage = 17
        else:
            time.sleep(0.5)
            extraslowprintintroduction("\n...")
            clear()
            time.sleep(2)
            dialogue("???","Hey.")
            introstage = [1,'waiting']
    if introstage == 2:
        dialogue("???",f"{playername}. {playername.upper()}! Wake up. Someone's coming.")
        introstage = [2, 'waiting']
    if introstage == 3:
        dialogue(f"{playername}","(Huh? Where am I?)")
        introstage = [3,'waiting']
    if introstage == 4:
        dialogue(f"{playername}",f"(...{partnername}? Is that you?)")
        introstage = [4,'waiting']
    if introstage == 5:
        dialogue(f"{playername}",f"(What's happening? Where are we?)")
        introstage = [5,'waiting']
    if introstage == 6:
        dialogue(f"{partnername}",f"Shh! No time to explain. Grab your sword. Our visitor doesn't look friendly...")
        introstage = [6,'waiting']
    if introstage == 7:
        dialogue(f"{playername}",f"(I have a sword...?)")
        introstage = [7,'waiting']
    if introstage == 8:
        dialogue(f"{partnername}",f"Here they come! {playername}! Get ready!")
        introstage = [8,'waiting']
    if introstage == 9:
        cancontinue = False
        cutscene("""              .
             /.\\
             |.|
             |.|
             |.|
             |.|   ,'`.
             |.|  ;\  /:
             |.| /  \/  \\
             |.|<.<_\/_>,>
             |.| \`.::,'/
             |.|,'.'||'/.
          ,-'|.|.`.____,'`.
        ,' .`|.| `.____,;/ \\
       ,'=-.`|.|\ .   \ |,':
      /_   :)|.|.`.___:,:,'|.
     (  `-:;\|.|.`.)  |.`-':,\\
     /.   /  ;.:--'   |    | ,`.
    / _>-'._.'-'.     |.   |' / )._
   :.'    ((.__;/     |    |._ /__ `.___
   `.>._.-' |)=(      |.   ;  '--.._,`-.`.
            ',--'`-._ | _,:          `='`'
            /_`-. `..`:'/_.\\
           :__``--..\\\_/_..:
           |  ``--..,:;\__.|
           |`--..__/:;  :__|
           `._____:-;_,':__;
            |:'    /::'  `|
            |,---.:  :,-'`;
            : __  )  ;__,'\\
            \\' ,`/   \__  :
            :. |,:   :  `./
            | `| |   |   |:
            |  | |   |   ||
            |  | |   |   ||
            |  | |   '   ||
            |  : |    \  ||
            |  ; :    :  ||
            | / ,;    |\,'`.
            ;-.(,'    '-._,-`.
          ,'-.//          `--' 
          `---'""")
        introstage = [9,'waiting']
    if introstage == 10:
        dialogue(f"???",f"Ah. It seems Lady Fate smiles upon me today.")
        introstage = [10,'waiting']
    if introstage == 11:
        dialogue(f"{partnername}",f"What do you want with us?")
        introstage = [11,'waiting']
    if introstage == 12:
        dialogue(f"???",f"That is a good question. My answer is that I know not what I want, but I know what I must do.")
        introstage = [12,'waiting']
    if introstage == 13:
        dialogue(f"{playername}",f"(This guy is kind of freaking me out...)")
        introstage = [13,'waiting']
    if introstage == 14:
        dialogue(f"{partnername}",f"What is it you must do, then?")
        introstage = [14,'waiting']
    if introstage == 15:
        dialogue(f"???",f"I regret to say this; what I must do is to end your lives this instant.")
        introstage = [15,'waiting']
    if introstage == 16:
        dialogue(f"{partnername}",f"W-Why? No... It can't be!")
        introstage = [16,'waiting']
    if introstage == 17:
        dialogue(f"{playername}",f"({partnername}? What are you talking about?)                    \n(Oh, never mind that, here he comes...)")
        introstage = [17,'waiting']
    if introstage == 18:
        clearboard()
        slowprintintroduction("""\n_____________________________________________________________
-------------D E F E N D-------------A T T A C K-------------
------------  A  S  K  L-------------   D  J    -------------""")
        slowprint("The Shadow King draws near!")
        time.sleep(1)
        slowprint(f"{partnername}: \n> Focus on defending! We've got to get away from here!")
        stun = 0
        combo = 0
        incombat = True
        additivecomborefresh = 1
        additiverefresh = 0
        enemies = 1
        difficulty = 8
        refreshrate = 0.6
        speeduptimer = TimerEx(interval_sec=10,function=speedup,)
        is_fake = True
        battle = "Shadowking1"
        jkl = 1
        while incombat == True:
            if not speeduptimer.is_alive():
                speeduptimer.start()
            refreshspeedcontrol()
        while incombat == False:
            if jkl == 1:
                jkl = 0
                dialogue(f"{playername}",f"(Oh no. No. NO!)            \n(...Huh? I'm not dead?)")
                introstage = [18,'waiting']
                break
    if introstage == 19:
        dialogue(f"The Shadow King",f"Ugh. Your friend here appears to have caught me off-guard. Well Played.")
        introstage = [19,'waiting']
    if introstage == 20:
        extraslowprintintroduction("\n* The sound of a sword clanging against steel rings out.")
        time.sleep(1)
        introstage = 21
    if introstage == 21:
        dialogue(f"{partnername}",f"*Oww...*")
        introstage = [21,'waiting']
    if introstage == 22:
        dialogue(f"The Shadow King",f"Oh well. I don't think I have enough energy left in myself to fight you again, so I'll have to just settle for your friend for now.\nIf you wish to rescue them, you may find me waiting in the Castle of Reflections.           \nFarewell, {playername}. I'm sure we will meet again.")
        introstage = [22,'waiting']
    if introstage == 23:
        dialogue(f"{playername}",f"(Wait! {partnername}! No! I still don't know what all this is about!)")
        introstage = [23,'waiting']
    if introstage == 24:
        dialogue(f"{partnername}",f"(Far off) {playername}! Never give up! Do your best, as always, okay?")
        introstage = [24,'waiting']
    if introstage == 25:
        slowprintintroduction("\n...")
        time.sleep(2)
        slowprintintroduction(f"That night, {playername} decided to take a rest under a nearby tree, unsure of what was to come.\nEventually, {playername} drifted off into an uneasy slumber...")
        time.sleep(3)
        extraslowprintintroduction("\n...")
        time.sleep(1)
        dialogue(f"{playername}",f"(It's a new day... I have no idea what I need to do, or why I am here, but one thing's for sure:\nI need to rescue {partnername}!)")
        introstage = [25,'waiting']
    if introstage == 26:
        menu = 'maingame'
        day = 1
        revivalseeds = 0
        progress = 0
        menuselection = 0
        inmenu = True
        
        slowprintintroduction(f"-----------------\n{playername}\n-----------------\nDay {day}\nRevival seeds: {revivalseeds}\nProgress: {progress}\n\nWhat do you do?\nTravel\nForage\nRest\nSave\n(Use the shift key to navigate)")






def travel():
    global progress
    global day
    global stun
    global combo
    global incombat
    global additivecomborefresh
    global additiverefresh
    global enemies
    global difficulty
    global refreshrate
    global is_fake
    global battle
    global cancontinue
    global menu
    menu = "Traveling"
    if progress < 5:
        progress += 1
        day += 1
        r = random.randint(1,4)
        if r == 1:
            slowprintintroduction("...\n...\n...\n...")
            time.sleep(2)
            slowprintintroduction("\nYou travel along the well-worn path through a grassy plain...")
            time.sleep(3)
            slowprintintroduction("\nThankfully, you were able to find a place to rest as the night turned dark.")
        if r == 2:
            slowprintintroduction("...\n...\n...\n...")
            time.sleep(2)
            slowprintintroduction("\nYou travel along a small stream...")
            time.sleep(3)
            slowprintintroduction("\nA small green creature jumps out from the water and blocks your path!")
            time.sleep(3)
            clearboard()
            slowprintintroduction("""\n_____________________________________________________________
-------------D E F E N D-------------A T T A C K-------------
------------  A  S  K  L-------------   D  J    -------------""")
            slowprint("A goblin attacks!")
            time.sleep(1)
            slowprint(f"{playername}: \n> Alright. Let's do this!")

            stun = 0
            combo = 0
            incombat = True
            additivecomborefresh = 1
            additiverefresh = 0
            enemies = 1
            difficulty = 4
            refreshrate = 0.6
            is_fake = False
            battle = "Goblin"
            jkl = 1
            while incombat == True:
                refreshspeedcontrol()
            while incombat == False:
                if jkl == 1:
                    jkl = 0
                    dialogue(playername,"Man, that was tough. But I need to keep going.")
                if cancontinue == True:
                    if keyboard.is_pressed('x'):
                        cancontinue = False
                        slowprintintroduction(f"Exausted, {playername} found a place to rest and slept the night away soundly.")
                        time.sleep(2)
                        menu = 'maingame'
        if r == 3:
            slowprintintroduction("...\n...\n...\n...")
            time.sleep(2)
            slowprintintroduction("\nYou travel along the edge of a small forest...")
            time.sleep(3)
            slowprintintroduction("\nGah! It's an ambush!")
            time.sleep(3)
            clearboard()
            slowprintintroduction("""\n_____________________________________________________________
-------------D E F E N D-------------A T T A C K-------------
------------  A  S  K  L-------------   D  J    -------------""")
            slowprint("A goblin gang attacks!")
            time.sleep(1)
            slowprint(f"{playername}: \n> Ah shoot.")

            stun = 0
            combo = 0
            incombat = True
            additivecomborefresh = 1
            additiverefresh = 0
            enemies = 2
            difficulty = 6
            refreshrate = 0.5
            is_fake = False
            battle = "Goblin gang"
            jkl = 1
            while incombat == True:
                refreshspeedcontrol()
            while incombat == False:
                if jkl == 1:
                    jkl = 0
                    dialogue(playername,"Man, that was close!")
                if cancontinue == True:
                    if keyboard.is_pressed('x'):
                        cancontinue = False
                        slowprintintroduction(f"Exausted, {playername} found a place to rest and slept the night away soundly.")
                        time.sleep(2)
                        menu = 'maingame'
        if r == 4:
            slowprintintroduction("...\n...\n...\n...")
            time.sleep(2)
            slowprintintroduction("\nYou travel along a small stream...")
            time.sleep(3)
            slowprintintroduction("\nA small green creature jumps out from the water and blocks your path!")
            time.sleep(3)
            clearboard()
            slowprintintroduction("""\n_____________________________________________________________
-------------D E F E N D-------------A T T A C K-------------
------------  A  S  K  L-------------   D  J    -------------""")
            slowprint("A goblin attacks!")
            time.sleep(1)
            slowprint(f"{playername}: \n> Alright. Let's do this!")

            stun = 0
            combo = 0
            incombat = True
            additivecomborefresh = 1
            additiverefresh = 0
            enemies = 1
            difficulty = 4
            refreshrate = 0.6
            is_fake = False
            battle = "Goblin"
            jkl = 1
            while incombat == True:
                refreshspeedcontrol()
            while incombat == False:
                if jkl == 1:
                    jkl = 0
                    dialogue(playername,"Man, that was tough. But I need to keep going.")
                if cancontinue == True:
                    if keyboard.is_pressed('x'):
                        cancontinue = False
                        slowprintintroduction(f"Exausted, {playername} found a place to rest and slept the night away soundly.")
                        time.sleep(2)
                        menu = 'maingame'





















while menu == 'maingame':
    if keyboard.is_pressed("Shift") and inmenu == True:
        clear()
        if menuselection == 0:
            menuselection = 1
            print(f"-----------------\n{playername}\n-----------------\nDay {day}\nRevival seeds: {revivalseeds}\nProgress: {progress}\n\nWhat do you do?\n> Travel\nForage\nRest\nSave\n(Use the control key to select)")
            time.sleep(0.2)
        elif menuselection == 1:
            menuselection = 2
            print(f"-----------------\n{playername}\n-----------------\nDay {day}\nRevival seeds: {revivalseeds}\nProgress: {progress}\n\nWhat do you do?\nTravel\n> Forage\nRest\nSave\n(Use the control key to select)")
            time.sleep(0.2)
        elif menuselection == 2:
            menuselection = 3
            print(f"-----------------\n{playername}\n-----------------\nDay {day}\nRevival seeds: {revivalseeds}\nProgress: {progress}\n\nWhat do you do?\nTravel\nForage\n> Rest\nSave\n(Use the control key to select)")
            time.sleep(0.2)
        elif menuselection == 3:
            menuselection = 1
            print(f"-----------------\n{playername}\n-----------------\nDay {day}\nRevival seeds: {revivalseeds}\nProgress: {progress}\n\nWhat do you do?\n> Travel\nForage\nRest\nSave\n(Use the control key to select)")
            time.sleep(0.2)


    if keyboard.is_pressed('Control'):
        if menuselection == 1:
            travel()
        if menuselection == 2:
            pass
        if menuselection == 3:
            pass












        
while menu == "Tutorial":
    if keyboard.is_pressed('x') and cancontinue == True:
        cancontinue = False
        tutorialdialogue = tutorialdialogue + 1
        if tutorialdialogue == 1:
            slowprintintroduction("Anyhow, the name's Richard, nice to meet you.\n(x)")
            cancontinue = True
        elif tutorialdialogue == 2:
            slowprintintroduction("Because this game is made almost completely through text, there are a few notable limitations.\n(x)")
            cancontinue = True
        elif tutorialdialogue == 3:
            slowprintintroduction("Most importantly, the gameplay might feel a bit counter-intuitive at first.\n(x)")
            cancontinue = True
        elif tutorialdialogue == 4:
            slowprintintroduction("That's why it is strongly suggested to play the tutorial until you feel comfortable with the controls.\n(x)")
            cancontinue = True
        elif tutorialdialogue == 5:
            slowprintintroduction("That aside, let me explain how the game works.\n(x)")
            cancontinue = True
        elif tutorialdialogue == 6:
            slowprintintroduction("Basically, all you gotta do is use the AS and KL keys on your keyboard to 'block' the X's as they come down from above.\n(x)")
            cancontinue = True
        elif tutorialdialogue == 7:
            slowprintintroduction("It's like a rythem game! Except for the fact that rythem games don't have an attack function. But you should probablly ignore that part of the UI for now.\n(x)")
            cancontinue = True
        elif tutorialdialogue == 8:
            slowprintintroduction("Mostly because if you miss even a few 'defend' X's, you will die. And I was too lazy to implement a respawn system.\n(x)")
            cancontinue = True
        elif tutorialdialogue == 9:
            slowprintintroduction("Anyways, after you defend for a while, enemy attacks will become slower. You will have a chance to 'Attack' with minimal interferences.\nHit a few combos and the enemy will perish!\n(x)")
            cancontinue = True
        elif tutorialdialogue == 10:
            slowprintintroduction("I'll let you go practice now. When you're done practicing, press 'q'.\n(x)")
            cancontinue = True
        elif tutorialdialogue == 11:
            intutorial = True
            tutorialspeed = 0.5
            refresh()
            incombat = True
            message = "Tutorial Start - No penalty for death, no stuns.\nUse the up and down arrows to control the speed as you see fit."
            print(incombat)
            while incombat == True:
                generateattack(1,7)
                additiverefresh = 0
                generateslash(True)
                connectattackdef()
                shiftlines()
                if incombat == True:
                    refresh()
                    if keyboard.is_pressed("Up"):
                        tutorialspeed = tutorialspeed - 0.05
                        message = f"Speed changed. Refresh rate is now {tutorialspeed}."
                        refresh()
                    if keyboard.is_pressed("Down"):
                        tutorialspeed = tutorialspeed + 0.05
                        message = f"Speed changed. Refresh rate is now {tutorialspeed}."
                        refresh()
                    time.sleep(tutorialspeed)
                    if keyboard.is_pressed("q"):
                        if messageresettimer.is_alive():
                            messageresettimer.cancel()
                        menu = 1
                        menuselection = 0
                        incombat = False
                        intutorial = False
                        slowprintintroduction("Menu:\nStart new game\nTutorial\nCredits\nTesting\n\n(Use the shift key to navigate the menu)\nSorry, this unintentially crashes the game. I honestly don't know how to fix this")
                        break
    if keyboard.is_pressed("z"):
        if cancontinue == True:
            cancontinue = False
            tutorialdialogue = 10
            slowprintintroduction("I'll let you go practice now. When you're done practicing, press 'q'.\n(x)")
            cancontinue = True
                        


while menu == 2:
    if keyboard.is_pressed('x'):
        slowprint("itworked!")
    if keyboard.is_pressed('p'):
        endgame()
    if keyboard.is_pressed("u"):
        generateattack(1,10)
        generateslash(True)
        connectattackdef()
        shiftlines()
        refresh()
    if keyboard.is_pressed("o"):
        clearboard()
    if keyboard.is_pressed("i"):
        clearenemyattacks()
    if keyboard.is_pressed("r"):
        refresh()
    if keyboard.is_pressed("v"):
        clear()
        
        if incombat == True:
            incombat = False
        else:
            incombat = True
            message = "Battle Start"
            if not tiredtimer20.is_alive():
                tiredtimer20.start()
        print(incombat)
        while incombat == True:
            if stun == 0:
                generateattack(enemies,difficulty)
                additiverefresh = 0
            elif stun == 1:
                if difficulty < 10:
                    generateattack(enemies,difficulty + 1)      
                else:
                    additiverefresh = 0.02 
            elif stun == 2:
                if difficulty < 9:
                    generateattack(enemies,difficulty + 2)  
                else:
                    additiverefresh = 0.05
            elif stun == 3:
                if difficulty < 8:
                    generateattack(enemies,difficulty + 3)  
                else:
                    additiverefresh = 0.1
            generateslash(is_fake)
            connectattackdef()
            shiftlines()
            if incombat == True:
                refresh()
                if stun == 0:
                    if tired == True:
                        time.sleep((refreshrate + 0.2) / additivecomborefresh)
                    else:
                        time.sleep((refreshrate - additiverefresh)/ additivecomborefresh)
                elif stun == 1:
                    time.sleep(refreshrate - additiverefresh - 0.05)
                elif stun == 2:
                    time.sleep(refreshrate - additiverefresh - 0.05)
                elif stun == 3:
                    time.sleep(refreshrate - additiverefresh - 0.1)


                


    
    




