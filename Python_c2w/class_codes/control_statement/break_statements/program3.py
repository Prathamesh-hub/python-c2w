playerList=["rohit","virat","dhoni","rahul"]
playername=input("enter player name")

for player in playerList:
    if player==playername:
        print(playername,"present")
        break
else:
    print(playername,"not present")
