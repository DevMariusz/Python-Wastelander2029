#add inventory when items found
def getWater(self):
    if self.tut:
        xList=w_getWater(0,self.Level)
    else:
        xList=w_getWater(1,self.Level)

    for n in range(len(xList[0])):
        if xList[0][n] not in self.waterInv[0]:
            self.waterInv[0].append(xList[0][n])
            self.waterInv[1].append(xList[1][n])
        else:
            count=0
            for items in self.waterInv[0]:
                if items == xList[0][n]:
                    self.waterInv[1][count]+=xList[1][n]
                else:
                    count+=1

#inventory item stat setup
dirtywaterstats={"name":"Dirty Water","health":10,"water":40,"cost":2}
spoiledmilkstats={"name":"Spoiled Milk","health":14,"water":33,"cost":3}

if level==1:
    wateritems={"Dirty Water":dirtywaterstats,"Spoiled Milk":spoiledmilkstats}

#Weapon cost increase with level
if level==1:
    l=1
else:
    l=random.randint(1,level+3)
d=random.randint(l,15*(l+3))
c=250*l
Pistolstats={"name":"Pistol","damage":d,"optimal distance":8,"Max distance":15,"level":l,"cost":c}
