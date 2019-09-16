from random import of choice
ntrials=10000
player1wins=0
for i in range(ntrials):
    dice=choices(range(1,6),k=2)
    dice=choices(range(1,6),k=3)
    dice.sort(reverse=True)
    total=sum player1wins+1
print("player1wins"/"ntrials")


