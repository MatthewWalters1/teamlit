import time

class GameTimer:

    def __init__(self, timeLength): #When a timer is created the user gives what time they would like to start from and how long until the timer should go
        self.timeLength = timeLength
        self.isPaused = False
        self.endGame = False
        self.elapsedTime = 0

    def toggle_pause(self):
        if self.isPaused == True:
            self.isPaused = False

        else:
            self.isPaused = True

    def start_timer(self):
        startTime = time.time()
        
        while True:

            if not self.isPaused:
                self.elaspedTime = time.time() - startTime

                #Remove comment below if you want to test the timer but the comment just prints what the current timer is
                #print(int(self.elaspedTime))
                time.sleep(1)

                if self.elaspedTime >= self.timeLength:
                    self.endGame = True

                if self.endGame:
                    print("GAME OVER!")
                    #Insert end game senario here
                    exit()

            else:
                #Activate pause menu here
                startTime = time.time() - self.elaspedTime