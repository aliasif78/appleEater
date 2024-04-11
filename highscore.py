class Highscore:
    
    pb = 0
    newPB = 0

    
    def newScore(self):
        with open('highScore.txt', 'r') as file:
            contents = file.read()

        # Replace the existing number with the new number
        modified_contents = contents.replace(str(self.pb), str(self.newPB))

        # Open the file in write mode ('w' mode) and write the modified contents
        with open('highScore.txt', 'w') as file:
            file.write(modified_contents)