#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 11:10:11 2018

@author: charlene
"""
import json

#### Collision

json_data=open('./data/collision.json')
data = json.load(json_data)
taille = len(data["data"])

datas = []
for i in range(0,taille):
    ligne = data["data"][i]
    boro = ligne[10]     # 10. borough
    nbPedInj = int(ligne[20]) # 20. number_of_pedestrians_injured
    nbPedKil = int(ligne[21]) # 21. number_of_pedestrians_killed
    nbCycInj = int(ligne[22]) # 22. number_of_cyclist_injured
    nbCycKil = int(ligne[23]) # 23. number_of_cyclist_killed
    datas.append({"id":i+1,"borough":boro,"number_of_pedestrians_injured":nbPedInj,"number_of_pedestrians_killed":nbPedKil,"number_of_cyclist_injured":nbCycInj,
                  "number_of_cyclist_killed":nbCycKil})

json_data.close()

with open("./data/collision.json", "w") as outfile:
    json.dump(datas,outfile,indent=4)
  
#### Complaint

json_data=open('./data/complaint.json')
data = json.load(json_data)
taille = len(data["data"])

datas = []
for i in range(0,taille):
    ligne = data["data"][i]
    ofns = ligne[8]  # 8. ofns_desc
    boro = ligne[12] # 12. borough
    datas.append({"id":i+1,"ofns_desc":ofns,"borough":boro})

json_data.close()

with open("./data/complaint.json", "w") as outfile:
    json.dump(datas,outfile,indent=4)

#### Park

json_data=open('./data/park.json')
data = json.load(json_data)
taille = len(data["data"])

datas = []
dic = {"Q":"QUEENS","B":"BROOKLYN","R":"STATEN ISLAND","M":"MANHATTAN","X":"BRONX"}

for i in range(0,taille):
    ligne = data["data"][i]
    boro = dic[ligne[21]] # 21. borough
    classe = ligne[27]    # 27. class
    datas.append({"id":i+1,"borough":boro,"class":classe})

json_data.close()

with open("./data/park.json", "w") as outfile:
   json.dump(datas,outfile,indent=4)
    
#### Restaurant

json_data=open('./data/restaurant.json')
data = json.load(json_data)
taille = len(data["data"])

datas = []
for i in range(0,taille):
    ligne = data["data"][i]
    grade = ligne[22]     # 22. grade
    boro = ligne[10]      # 10. borough
    date = ligne[16][:-9] # 16. inspection_date
    datas.append({"id":i+1,"grade":grade,"borough":boro,"inspection_date":date})

json_data.close()

with open("./data/restaurant.json", "w") as outfile:
   json.dump(datas,outfile,indent=4)
 
#### Tree

json_data=open('./data/tree.json')
data = json.load(json_data)
taille = len(data["data"])

datas = []
for i in range(0,taille):
    ligne = data["data"][i]
    cr = ligne[8]      # 8. created_at
    boro = ligne[38]   # 38. boroname
    status = ligne[15] # 15. status
    health = ligne[16] # 16. health
    datas.append({"id":i+1,"created_at":cr,"borough":boro,"status":status,"health":health})

json_data.close()

with open("./data/tree.json", "w") as outfile:
   json.dump(datas,outfile,indent=4)
     
#### Water

json_data=open('./data/water.json')
data = json.load(json_data)
taille = len(data["data"])

datas = []
for i in range(0,taille):
    ligne = data["data"][i]
    boro = ligne[31]   # 31. borough
    cd = ligne[9][:-9] # 9. createdDate
    datas.append({"id":i+1,"createdDate":cd,"borough":boro})

json_data.close()

with open("./data/water.json", "w") as outfile:
    json.dump(datas,outfile,indent=4)
 
#### Culture

json_data=open('./data/culture.json')
data = json.load(json_data)
taille = len(data["data"])

datas = []
for i in range(0,taille):
    ligne = data["data"][i]
    id_data = ligne[0] # 0. id
    org = ligne[8]     # 8. organization name
    disc = ligne[14]   # 14. discipline
    boro = ligne[17]   # 17. borough
    datas.append({"id":id_data,"organization_name":org,"discipline":disc,"borough":boro})

json_data.close()

with open("./data/culture.json", "w") as outfile:
    json.dump(datas,outfile,indent=4)
































