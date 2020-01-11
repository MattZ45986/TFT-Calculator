class Champion(object):
    def __init__(self, name, traits):
        self.name = name
        self.traits = traits
        self.synergies = []

    def setAffinities(self, num):
        self.affinities = num

class Synergy(object):
    def __init__(self, trait, champ1, champ2):
        self.trait = trait
        self.champ1 = champ1
        self.champ2 = champ2

    def __str__(self):
        return self.trait + ": " + self.champ1.name + ", " + self.champ2.name

class Team(object):
    def __init__(self, champs, affs=0, links=0, score=0):
        self.size = len(champs)
        self.champs = champs
        self.synergies = getSynergies(champs)
        self.affinities = affs
        self.links = links
        self.score = score

    def __str__(self):
        string = self.champs[0].name
        for i in range(len(self.champs)-1):
            string += " & " + self.champs[i+1].name
        addition = " "*(60-len(string))
        string += addition
        string += "\taffs: " + str(self.affinities) + " \tlinks: " + str(self.links) + " \tscore: " + str(self.score)
        return string

    def getAffinities(self):
        self.affinities = 0
        for champ in self.champs:
            self.affinities += champ.affinities
        self.affinities -= self.links *2
        return self.affinities

    def getLinks(self):
        self.links = getLinks(self.champs)
        return getLinks(self.champs)

    def hasSameChampsAs(self, team):
        ourNames = sorted(champ.name for champ in self.champs)
        theirNames = sorted(champ.name for champ in team.champs)
        if ourNames == theirNames: return True
        else: return False

    def getScore(self):
        self.score = getRawScore(self.champs)

aatrox = Champion("Aatrox", ["light", "blademaster"])
amumu= Champion("Amumu", ["inferno", "warden"])
annie= Champion("Annie", ["inferno", "summoner"])
ashe = Champion("Ashe", ["crystal", "ranger"])
azir = Champion("Azir", ["desert", "summoner"])
brand = Champion("Brand", ["inferno", "mage"])
braum = Champion("Braum", ["glacial", "warden"])
diana = Champion("Diana", ["inferno", "assassin"])
drmundo= Champion("Drmundo", ["poison", "beserker"])
ezreal = Champion("Ezreal", ["glacial", "ranger"])
ivern = Champion("Ivern", ["woodlands", "druid"])
janna = Champion("Janna", ["cloud", "mystic"])
jax = Champion("Jax", ["light", "beserker"])
karma = Champion("Karma", ["lunar", "mystic"])
khazix= Champion("Khazix", ["desert", "assassin"])
kindred = Champion("Kindred", ["shadow", "inferno", "ranger"])
kogmaw = Champion("Kogmaw", ["poison", "predator"])
leblanc = Champion("Leblanc", ["woodlands", "mage", "assassin"])
leona = Champion("Leona", ["lunar", "warden"])
lucian = Champion("Lucian", ["light", "soulbound"])
lux = Champion("Lux", ["avatar"])
malphite = Champion("Malphite", ["mountain", "warden"])
malzahar = Champion("Malzahar", ["shadow", "summoner"])
maokai = Champion("Maokai", ["woodlands", "druid"])
masteryi = Champion("Masteryi", ["shadow", "mystic", "blademaster"])
nami = Champion("Nami", ["ocean", "mystic"])
nasus = Champion("Nasus", ["light", "warden"])
nautilus = Champion("Nautilus", ["ocean", "warden"])
neeko = Champion("Neeko", ["woodlands", "druid"])
nocturne = Champion("Nocturne", ["steel", "assassin"])
olaf = Champion("Olaf", ["glacial", "beserker"])
ornn = Champion("Ornn", ["electric", "warden"])
qiyana= Champion("Qiyana", ["assassin"])
reksai= Champion("Reksai", ["steel", "predator"])
renekton = Champion("Renekton", ["desert", "beserker"])
senna= Champion("Senna", ["shadow", "soulbound"])
singed = Champion("Singed", ["poison", "alchemist"])
sion = Champion("Sion", ["shadow", "beserker"])
sivir = Champion("Sivir", ["desert", "blademaster"])
skarner = Champion("Skarner", ["crystal", "predator"])
soraka = Champion("Soraka", ["light", "mystic"])
syndra = Champion("Syndra", ["ocean", "mage"])
taliyah = Champion("Taliyah", ["mountain", "mage"])
taric = Champion("Taric", ["crystal", "warden"])
thresh = Champion("Thresh", ["ocean", "warden"])
twitch = Champion("Twitch", ["poison", "ranger"])
varus = Champion("Varus", ["inferno", "ranger"])
vayne = Champion("Vayne", ["light", "ranger"])
veigar = Champion("Veigar", ["shadow", "mage"])
vladimir = Champion("Vladimir", ["ocean", "mage"])
volibear = Champion("Volibear", ["glacial", "electric", "beserker"])
warwick = Champion("Warwick", ["glacial", "predator"])
yasuo = Champion("Yasuo", ["cloud", "blademaster"])
yorick = Champion("Yorick", ["light", "summoner"])
zed = Champion("Zed", ["electric", "assassin", "summoner"])
zyra= Champion("Zyra", ["inferno", "summoner"])

champions = [aatrox, amumu, annie, ashe, azir, brand, braum, diana,
            drmundo, ezreal, ivern, janna, jax, karma, khazix, kindred,
            kogmaw, leblanc, leona, lucian, lux, malphite, malzahar, maokai,
            masteryi, nami, nasus, nautilus, neeko, nocturne, olaf, ornn,
            qiyana, reksai, renekton, senna,
            singed, sion, sivir, skarner, soraka, syndra, taliyah, taric,
            thresh, twitch, varus, vayne, veigar, vladimir, volibear, warwick,
            yasuo, yorick, zed, zyra]

traits = ['light', 'blademaster', 'inferno', 'warden', 'summoner', 'crystal', 'ranger',
         'desert', 'mage', 'glacial', 'assassin', 'poison', 'beserker', 'woodlands',
         'druid', 'cloud', 'mystic', 'lunar', 'shadow', 'predator', 'soulbound', 'avatar',
         'mountain', 'ocean', 'steel', 'electric', 'alchemist']

buffs1 = {'light':3, 'blademaster':3, 'inferno':3, 'warden':2, 'summoner':3, 'crystal':2, 'ranger':2,
         'desert':2, 'mage':3, 'glacial':2, 'assassin':3, 'poison':3, 'beserker':3, 'woodlands':3,
         'druid':2, 'cloud':2, 'mystic':2, 'lunar':2, 'shadow':2, 'predator':3, 'soulbound':2, 'avatar':1,
         'mountain':2, 'ocean':2, 'steel':2, 'electric':2, 'alchemist':10}

buffs2 = {'light':6, 'blademaster':6, 'inferno':6, 'warden':4, 'summoner':6, 'crystal':4, 'ranger':4,
         'desert':4, 'mage':6, 'glacial':4, 'assassin':6, 'beserker':6,'cloud':3, 'mystic':4,
          'shadow':4, 'ocean':4, 'steel':4, 'electric':3, 'avatar':1, 'woodlands':10, 'predator':10,
          'druid':10, 'alchemist':10, 'soulbound':10, 'mountain':10, 'poison':10, 'lunar':10}

buffs3 = {'blademaster':9, 'cloud':4, 'electric':4, 'glacial':6, 'inferno':9,
          'light':9, 'ocean':6, 'ranger':6, 'steel':6, 'warden':6, 'summoner':10,
          'crystal':10, 'desert':10, 'mage':10, 'assassin':10, 'beserker':10, 'mystic':10,
          'shadow':10, 'avatar':10, 'woodlands':10, 'druid':10, 'alchemist':10,
          'soulbound':10, 'mountain':10, 'poison':10, 'lunar':10, 'predator':10}

light = [aatrox, jax, lucian, nasus, soraka, vayne, yorick]
blademaster = [aatrox, masteryi, sivir, yasuo]
inferno = [amumu, annie, brand, diana, kindred, varus, zyra]
warden = [amumu, braum, leona, malphite, nasus, nautilus, ornn, taric, thresh]
summoner = [annie, azir, malzahar, yorick, zed, zyra]
crystal = [ashe, skarner, taric]
ranger = [ashe, ezreal, kindred, twitch, varus, vayne]
desert = [azir, khazix, renekton, sivir]
mage = [brand, leblanc, syndra, taliyah, veigar, vladimir]
glacial = [braum, ezreal, olaf, volibear, warwick]
assassin = [diana, khazix, leblanc, nocturne, qiyana, zed]
poison = [drmundo, kogmaw, singed, twitch]
beserker = [drmundo, jax, olaf, renekton, sion, volibear]
woodlands = [ivern, leblanc, maokai, neeko]
druid = [ivern, maokai, neeko]
cloud = [janna, yasuo, qiyana]
mystic = [janna, karma, masteryi, nami, soraka]
lunar = [karma, leona]
shadow = [kindred, malzahar, masteryi, senna, sion, veigar]
predator = [kogmaw, reksai, skarner, warwick]
soulbound = [lucian, senna]
avatar = [lux]
mountain = [malphite, taliyah]
ocean = [nami, nautilus, syndra, thresh, vladimir]
steel = [nocturne, reksai]
electric = [ornn, volibear, zed]
alchemist = [singed]

traitLists = [light, blademaster, inferno, warden, summoner,
              crystal, ranger, desert, mage, glacial, assassin,
              poison, beserker, woodlands, druid, cloud, mystic,
              lunar, shadow, predator, soulbound, avatar,
              mountain, ocean, steel, electric, alchemist]

def getSynergies(champs):
    synergies = []
    for i in range(len(champs)-1):
        for j in range(i+1, len(champs)):
            if haveSynergy(champs[i], champs[j]):
                for trait in champs[i].traits:
                    if trait in champs[j].traits: synergies.append(Synergy(trait, champs[i], champs[j]))
    return synergies
                
def getLinks(champs):
    links = 0
    for i in range(len(champs)-1):
        for j in range(i+1, len(champs)):
            if haveSynergy(champs[i], champs[j]):
                for trait in champs[i].traits:
                    if trait in champs[j].traits: links += 1
    return links

def haveSynergy(champ1, champ2):
    for trait in champ1.traits:
        if trait in champ2.traits: return True
    return False

def haveTeamSynergy(team1, team2):
    for champ1 in team1.champs:
        for champ2 in team2.champs:
            if haveSynergy(champ1, champ2): return True
    return False

def areOverlapping(team1, team2):
    if bool(set(team1.champs) & set(team2.champs)): return True
    return False

def getScore(champs):
    synergies = {}
    score = 0
    for champ in champs:
        for trait in champ.traits:
            if trait in synergies:
                synergies[trait] += 1
            else: synergies[trait] = 1
    for trait in synergies:
        if synergies[trait] >= buffs3[trait]:
            score +=1
        if synergies[trait] >= buffs2[trait]:
            score +=1
        if synergies[trait] >= buffs1[trait]:
            score +=1
    return(score, synergies)

def getRawScore(champs):
    synergies = {}
    score = 0
    for champ in champs:
        for trait in champ.traits:
            if trait in synergies:
                synergies[trait] += 1
            else: synergies[trait] = 1
    for trait in synergies:
        if synergies[trait] >= buffs3[trait]:
            score +=1
        if synergies[trait] >= buffs2[trait]:
            score +=1
        if synergies[trait] >= buffs1[trait]:
            score +=1
    return score




def partition(arr,l,h): 
    i = ( l - 1 ) 
    x = arr[h].score 
    for j in range(l , h): 
        if   arr[j].score <= x: 
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]   
    arr[i+1],arr[h] = arr[h],arr[i+1] 
    return (i+1)
def quickSortIterative(arr,l,h): 
    size = h - l + 1
    stack = [0] * (size) 
    top = -1
    top = top + 1
    stack[top] = l 
    top = top + 1
    stack[top] = h 
    while top >= 0: 
        h = stack[top] 
        top = top - 1
        l = stack[top] 
        top = top - 1
        p = partition( arr, l, h ) 
        if p-1 > l: 
            top = top + 1
            stack[top] = l 
            top = top + 1
            stack[top] = p - 1
        if p+1 < h: 
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h

########### START CODE  ###############

links = []
for k in range(len(traits)):
    trait = traits[k]
    traitList = traitLists[k]
    for i in range(len(traitList)-1):
        for j in range(i+1, len(traitList)):
            s1 = Synergy(trait, traitList[i], traitList[j])
            links.append(s1)
            traitList[i].synergies.append(s1)
            traitList[j].synergies.append(Synergy(trait, traitList[j], traitList[i]))
for champ in champions:
    champ.setAffinities(len(champ.synergies))


thirdTier = []
fin = open("thirdTier.txt","r")
for line in fin.readlines():
    team = line.strip().split()
    for i in range(1,6):
        team.pop(i)
    thirdTier.append(Team([eval(team[0].lower()),eval(team[1].lower()),eval(team[2].lower())], int(team[3]),int(team[4]),int(team[5])))
fin.close()




sixthTier = []

print("initialization done")
for i in range(len(thirdTier)-1):
    for j in range(i+1, len(thirdTier)):
        team1 = thirdTier[i]
        team2 = thirdTier[j]
        if not areOverlapping(team1, team2) and haveTeamSynergy(team1, team2):
            sixthTier.append(Team(team1.champs+team2.champs))

print("creation of tier 6 done")

for team in sixthTier:
    team.getLinks()
    team.getAffinities()
    team.getScore()

print("population of tier 6 data done")

scoreLists = [[],[],[],[],[],[],[],[],[]]
for team in sixthTier:
    scoreLists[team.score].append(team)

sixthTier = scoreLists[0]+scoreLists[1]+scoreLists[2]+scoreLists[3]+scoreLists[4]+scoreLists[5]+scoreLists[6]+scoreLists[7]+scoreLists[8]

print("sorting of tier 6 done")

fout = open("sixthTier.txt", "w")
for team in sixthTier:
    fout.write(str(team)+"\n")
fout.close()

print("outputting tier 6 done")


