import random as rand

class Apple:

    eaten = 0
    appPosition = 82
    aX = 421
    aY = 326

    def __init__(self):
        self.eaten = 0
        self.appPosition = 82

    def spawn(cls, grid, canvas, appleItem):
        
        found = False
        num = rand.randint(1, 144)
        cls.appPosition = num

        for i in grid:
            
            for j in i:
                if (j == num):
                    cls.aX = i[0]
                    cls.aY = i[1]
                    found = True
                    break
            
            if (found == True):
                break

        canvas.coords(appleItem, cls.aX + + 5, cls.aY + 5)