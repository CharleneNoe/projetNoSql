# -*- coding: utf-8 -*-

# Liste des imports requis
from pymongo import MongoClient
from bson.son import SON
from collections import OrderedDict

## Paramètrage de la base mongoDB
db = MongoClient('localhost',27017).projet

## Fonction qui regroupe tous les classements dans un dictionnaire
dic = {}
def addRes(pipeline,collection):
    res = list(collection.aggregate(pipeline))
    #print(res)
    for i in range(len(res)):
        borough = res[i]["_id"]
        if(len(dic)<5):
            dic[borough.upper()] = [i+1]
        else:
            dic[borough.upper()].append(i+1)   
    
## Définitions des requêtes
# Collection : collision
pipeline_collision = [
    {'$match':{'borough':{'$ne':None}} },
    {'$group':
            {'_id': "$borough",
             'total_coll':{'$sum': {'$add': ["$number_of_pedestrians_injured",
                       "$number_of_pedestrians_killed",
                        "$number_of_cyclist_injured",
                          "$number_of_cyclist_killed"]}}}},
        {'$sort' : SON({'total_coll' : 1})}
]

# Collection : complaint
pipeline_complaint = [
        {'$group': 
            {'_id': "$borough", 'count_complaint':{ "$sum": 1}}},  
            {'$sort' : SON({'count_complaint' : 1})}
]

# Collection : water quality
pipeline_water = [
   {'$group': 
       {'_id': "$borough", 'count_water':{ "$sum": 1}}},    
       {'$sort' : SON({'count_water' : 1})}
]

# Collection : culture
pipeline_culture = [
    {'$match':{'discipline':{'$in':['Theater','Museum']}}},
    {'$group':{'_id' : "$borough",'count':{'$sum':1}}},
    {'$sort':{'count':-1}}
]
  
# Collection : restaurant 
pipeline_restaurant = [
    {'$match':{"grade":"A","borough":{'$ne':"Missing"}}},
    {'$group':{'_id' : "$borough",'count':{'$sum':1}}},
    {'$sort':{'count':-1}}
]

# Collection : tree 
pipeline_tree = [
    {'$match':{'status':"Alive",'health':{'$in':['Fair','Good']}}},
    {'$group':{'_id':"$borough",'count':{'$sum':1}}},
    {'$sort':{'count':-1}}
]

# Collection : park
pipeline_park = [
    {'$match':{"class":"PARK"}},
    {'$group':{'_id':"$borough",'count':{'$sum':1}}},
    {'$sort':{'count':-1}}
]

## Ajout dans le dictionnaire les différents classements
addRes(pipeline_collision,db.collision)
addRes(pipeline_complaint,db.complaint)
addRes(pipeline_water,db.water) 
addRes(pipeline_culture,db.culture)
addRes(pipeline_restaurant,db.restaurant)
addRes(pipeline_tree,db.tree)
addRes(pipeline_park,db.park)

### On obtient le classement suivant pour chaque critère
print("--> Résultat des classements -------------")
print("Dans l'ordre : collision, complaint, water, culture, restaurant, tree, park")
print(dic)
print("\n")

### On agrège selon les critères supérieurs
# Création d'un nouveau dictionnaire qui va contenir les moyennes des classements
# selon les critères "Sécurité", "Dynamisme" et "Espaces verts"
newDic = {}
# En position 0 : sécurité
# En position 1 : dynamisme
# En position 2 : espaces verts

for borough in dic:
    newDic[borough] = [(dic[borough][0] + dic[borough][1] + dic[borough][2])/3]
    newDic[borough].append((dic[borough][3] + dic[borough][4]) / 2)
    newDic[borough].append((dic[borough][5] + dic[borough][6]) / 2)

# On obtient le nouveau classement suivant pour chaque critère global
print("--> Résultat des classements par critère global -------------")
print("Dans l'ordre : sécurité, dynamisme, espaces verts")
print(newDic)
print("\n")

### On applique les poids
for borough in dic:
    newDic[borough] = newDic[borough][0]*0.4+newDic[borough][1]*0.2+newDic[borough][2]*0.4

#On trie le dictionnaire
sorted_list=sorted(newDic.items(), key=lambda x: x[1])
myOrdDic = list(OrderedDict(sorted_list).items())

# On obtient le nouveau classement suivant pour chaque critère pondéré
print("--> Résultat des classements finaux par ordre croissant -------------")
print(myOrdDic)
print("\n")
print("L'arrondissement idéal est donc le",myOrdDic[0][0],"!!!")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    