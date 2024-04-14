# lab_exercise_14.py
'''A T20 cricket game lasts 20 overs. The analysts need to predict if the team chasing
down the target can win the game or not, given their current runs and number of overs
finished. In order to make a fair (but not accurate) prediction, the analysts calculate
the run rate and assume that the team will maintain this run rate till the end of the
game. Next, they estimate the amount of runs the team will score within the remaining
overs by taking the product of the run rate and the number of overs remaining. If
the estimated score is greater than the target to be chased, then the team is predicted
to win. If not, then the team will lose.
Help the analysts write this program. Ask the analysts for the number of runs scored,
the number of overs finished, and the current target. Finally, print “Might win” if the
team is predicted to win, else “Might lose”.'''

runs = int(input('Runs: '))
over_bowled = int(input('Over Bowled: '))
target = int(input('Target: '))

run_rate = runs / over_bowled
over_remaining = 20 - over_bowled
current_runs = (run_rate * over_remaining) + runs

if current_runs > target:
    print('Might Win')
else:
    print('Might Loose')

print()
