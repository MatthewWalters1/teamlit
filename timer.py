import time
import keyboard

class GameTimer:

    def __init__(self, timeLength): #When a timer is created the user gives what time they would like to start from and how long until the timer should go
        self.timeLength = timeLength
        self.isPaused = False
        self.endGame = False

    def toggle_pause(self):
        if self.isPaused == True:
            self.isPaused = False

        else:
            self.isPaused = True

    def start_timer(self):
        startTime = time.time()
        toggled = False

        lastPrintedNumber = 0
        elaspedTime = 0
        addedTime = 0
        
        while True:

            if not self.isPaused:
                elaspedTime = time.time() - startTime + addedTime
                elaspedTime = round(elaspedTime, 2)

                difference = elaspedTime - lastPrintedNumber
                if difference != 0:
                    #Prints every 0.01 seconds and will print it only once
                    format_float = "{:.2f}".format(elaspedTime)
                    print(format_float)
                    lastPrintedNumber = round(elaspedTime, 2)
                    toggled = False

                endCal = self.timeLength - elaspedTime
                if endCal <= 0:
                    self.endGame = True

                if keyboard.is_pressed("p") and toggled == False:
                    #Pauses the program if you press p
                    print("Paused!")
                    toggled = True
                    self.toggle_pause()
                    time.sleep(0.25)

                if keyboard.is_pressed("e"):
                    #Ends the program if you press e
                    self.endGame = True

                if self.endGame:
                    print("GAME OVER!")
                    #Insert end game senario here
                    exit()

            else:
                #Activate pause menu here
                if keyboard.is_pressed("p"):
                    self.toggle_pause()
                    time.sleep(0.25)
                    startTime = time.time()
                    addedTime = elaspedTime
                    print("Unpaused!")

#To test just remove the comments below the number 5 indicates a 5 second time limit
#gametime = GameTimer(5)
#gametime.start_timer()