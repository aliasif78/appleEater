import tkinter as tk
import apple
import highscore
import pygame


# GRID
grid = []
xDiff = 66
yDiff = 88

for i in range (1, 145):
    grid.append((xDiff, yDiff, i))
    xDiff += 39

    if (i % 12 == 0):
        yDiff += 39
        xDiff = 66


# FUNCTIONS
def right(event):
    global pX
    global playerPosition

    if (pX < 456):
        pX += 39
        playerPosition += 1
        canvas.coords(playerItem, pX, pY)  # Update the image's coordinates

    if (playerPosition == apple.Apple.appPosition):
        apple.Apple.eaten += 1
        
        # Load a sound file
        sound_path = "Graphics/eatApple.wav"  # Replace with the actual path to your sound file
        sound_effect = pygame.mixer.Sound(sound_path)

        # Play the sound effect asynchronously
        sound_effect.play()
        
        canvas.itemconfig(appleScore, text=apple.Apple.eaten)
        apple.Apple.spawn(apple.Apple, grid=grid, canvas=canvas, appleItem=appleItem)

def left(event):
    global pX
    global playerPosition

    if (pX > 70):
        pX -= 39
        playerPosition -= 1
        canvas.coords(playerItem, pX, pY)  # Update the image's coordinates

    if (playerPosition == apple.Apple.appPosition):
        apple.Apple.eaten += 1
        
        # Load a sound file
        sound_path = "Graphics/eatApple.wav"  # Replace with the actual path to your sound file
        sound_effect = pygame.mixer.Sound(sound_path)

        # Play the sound effect asynchronously
        sound_effect.play()
        
        canvas.itemconfig(appleScore, text=apple.Apple.eaten)
        apple.Apple.spawn(apple.Apple, grid=grid, canvas=canvas, appleItem=appleItem)

def up(event):
    global pY
    global playerPosition

    if (pY > 90):
        pY -= 39
        playerPosition -= 12
        canvas.coords(playerItem, pX, pY)  # Update the image's coordinates

    if (playerPosition == apple.Apple.appPosition):
        apple.Apple.eaten += 1
        
        # Load a sound file
        sound_path = "Graphics/eatApple.wav"  # Replace with the actual path to your sound file
        sound_effect = pygame.mixer.Sound(sound_path)

        # Play the sound effect asynchronously
        sound_effect.play()
        
        canvas.itemconfig(appleScore, text=apple.Apple.eaten)
        apple.Apple.spawn(apple.Apple, grid=grid, canvas=canvas, appleItem=appleItem)

def down(event):
    global pY
    global playerPosition

    if (pY < 500):
        pY += 39
        playerPosition += 12
        canvas.coords(playerItem, pX, pY)  # Update the image's coordinates

    if (playerPosition == apple.Apple.appPosition):
        apple.Apple.eaten += 1
        
        # Load a sound file
        sound_path = "Graphics/eatApple.wav"  # Replace with the actual path to your sound file
        sound_effect = pygame.mixer.Sound(sound_path)

        # Play the sound effect asynchronously
        sound_effect.play()
        
        canvas.itemconfig(appleScore, text=apple.Apple.eaten)
        apple.Apple.spawn(apple.Apple, grid=grid, canvas=canvas, appleItem=appleItem)


def updateTime():
    global timeLeft

    if timeLeft > 0:
        canvas.itemconfig(tLeft, text=timeLeft)
        timeLeft -= 1
        window.after(1000, updateTime)  # Call update_timer after 1000ms (1 second)
    else:
        if (apple.Apple.eaten > highscore.Highscore.pb):
            highscore.Highscore.newPB = apple.Apple.eaten
            highscore.Highscore.newScore(highscore.Highscore)

        window.destroy()


# Initialize pygame
pygame.init()


# Create the main application window
window = tk.Tk()
window.title('Apple Eater')
window.resizable(width=False, height=False)
window.geometry('600x585+350+40')


# LOADING IMAGES
app = tk.PhotoImage(file="Graphics/apple.png")
appleIMG = app.subsample(18)

boardIMG = tk.PhotoImage(file='Graphics/board.png')

player = tk.PhotoImage(file='Graphics/player.png')
playerIMG = player.subsample(10)


# CREATING CANVAS
canvas = tk.Canvas(window, width=600, height=585)
canvas.pack()


# TIMER
timeLeft = 30


# HIGH SCORE
with open('highScore.txt', 'r') as file:
            contents = file.read()

highscore.Highscore.pb = int(contents)


# DRAWING IMAGES
boardItem = canvas.create_image(0,0,image=boardIMG, anchor=tk.NW)
appleItem = canvas.create_image(421, 326, anchor=tk.NW, image=appleIMG)
playerItem = canvas.create_image(138, 317, anchor=tk.NW, image=playerIMG)
appleScore = canvas.create_text(125, 32, text=apple.Apple.eaten, font=("Graphics/Roboto-Bold", 20), fill="white")
hsScore = canvas.create_text(258, 32, text=highscore.Highscore.pb, font=("Graphics/Roboto-Bold", 20), fill="white")
tLeft = canvas.create_text(400, 32, text=timeLeft, font=("Graphics/Roboto-Bold", 20), fill="white")


# BINDING CONTROLS
window.bind("<Right>", right)
window.bind("<Left>", left)
window.bind("<Up>", up)
window.bind("<Down>", down)


# STARTING POSITION
pX, pY = 138, 317
playerPosition = 75
appPosition = 82


# UPDATE TIME
updateTime()


# Start the main event loop
window.mainloop()

# Quit pygame
pygame.quit()