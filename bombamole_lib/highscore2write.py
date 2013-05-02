file = open("High Score.txt", "a")

score = 650

textToWrite = raw_input('Please type a username to save your score: ')

a = ','+textToWrite+'.'+str(score)

file.write(a)