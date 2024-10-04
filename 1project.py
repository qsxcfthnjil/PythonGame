import os
import time
import keyboard
import random
import sys
from threading import Timer


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
    if intutorial == False:
        is_fake = False
        tired = True
        message = "The enemy looks tired."
        clearenemyattacks()


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
        additivecomborefresh = 1.2
    elif combo == 6:
        additivecomborefresh = 1.5
    elif combo == 7:
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
                if not tiredtimer20.is_alive():
                    tiredtimer20.start()






def checkstun():
    global stun
    global stuntimer
    global incombat
    global message
    global is_fake
    global intutorial
    global messageresettimer
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
            incombat = False
            clear()
            slowprintintroduction("Bruh you died.")
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
            print("Menu:\n> Start new game\nTutorial\nCredits\nTesting\n\n(Use the enter key to select.)")
        elif menuselection == 1:
            menuselection = 2
            clear()
            print("Menu:\nStart new game\n> Tutorial\nCredits\nTesting\n\n(Use the enter key to select.)")
        elif menuselection == 2:
            menuselection = 3
            clear()
            print("Menu:\nStart new game\nTutorial\n> Credits\nTesting\n\n(Use the enter key to select.)") 
        elif menuselection == 3:
            menuselection = 4
            clear()
            print("Menu:\nStart new game\nTutorial\nCredits\n> Testing\n\n(Use the enter key to select.)") 
        time.sleep(0.2)
        
    if keyboard.is_pressed("Return"):
        if menuselection == 0:
            pass
        elif menuselection == 1:
            clear()
            slowprintintroduction("You FOOL this game isnt done yet")
            SystemExit("FOOL")
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
    if keyboard.is_pressed('p'):
        endgame()
        
        
        
        
while menu == "password":
    userpassword = input("Enter the admin password or be smited.\n> ")
    if userpassword == "Qsxc333":
        menu = 2
        refresh()
    else:
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


                


    
    




