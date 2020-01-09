#enemy gets behind cover
xcover=random.randint(1,10)
if xcover>5:
    enemiesToFight[x].inCover=2
else:
    enemiesToFight[x].inCover=1

#Enemy down
if enemiesToFight[sel_enemy-1].health<1:
    player.gainedXpPoints+=(player.Level*5)+(enemiesToFight[sel_enemy-1].MaxHealth/enemiesToFight[sel_enemy-1].gotHit)
    input("Enemy down!")
    pointsnotused=int(qtyApUsed)-x-1
    player.ActionPoints-=pointsnotused
    enemiesToFight.pop(sel_enemy-1)
    break

#Starts player turn to attack
player,enemiesToFight=playerAttack(player,enemiesToFight)
player.ActionPoints=7+player.Level
if len(enemiesToFight)>0:
    player,enemiesToFight=enemyAttack(player,enemiesToFight)
