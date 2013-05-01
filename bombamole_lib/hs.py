import os
import datetime
import cPickle,primary

# just a constants we can use to define our score file location
SCORES_FILE = "scores.pickle"

def get_user_data():
    time1 = datetime.datetime.now()
    print "Current time:", time1.strftime("%d.%m.%Y, %H:%M")

    a = primary.playerScore

    return ['', a, time1]

def read_high_scores():
    # initialize an empty score file if it does
    # not exist already, and return an empty list
    if not os.path.isfile(SCORES_FILE):
        write_high_scores([])
        return []

    with open(SCORES_FILE, 'r') as f:
        scores = cPickle.load(f)
    return scores

def write_high_scores(scores):
    with open(SCORES_FILE, 'w') as f:
        cPickle.dump(scores, f)

def update_scores(newScore, highScores):
    # reuse an anonymous function for looking
    # up the `c` (4th item) score from the object
    key = lambda item: item[2]

    # make a local copy of the scores
    highScores = highScores[:]

    lowest = None
    if highScores:
        lowest = min(highScores, key=key)

    # only add the new score if the high scores
    # are empty, or it beats the lowest one
    if lowest is None or (newScore[2] > lowest[2]):
        newScore[0] = raw_input("Enter name: ")
        highScores.append(newScore)

    # take only the highest 5 scores and return them
    highScores.sort(key=key, reverse=True)
    return highScores[:5]

def print_high_scores(scores):
    # loop over scores using enumerate to also
    # get an int counter for printing
    for i, score in enumerate(scores):
        name, a, time1 = score
        # #1    50.0    jdi    (20.12.2012, 15:02)
        print "#%d\t%s\t%s\t(%s)" % \
            (i+1, a, name, time1.strftime("%d.%m.%Y, %H:%M"))


def main():
    score = get_user_data()
    highScores = read_high_scores()

    highScores = update_scores(score, highScores)

    write_high_scores(highScores)
    print_high_scores(highScores)

if __name__ == "__main__":
    score = main()
    score.run()
