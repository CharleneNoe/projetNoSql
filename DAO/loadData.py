# -*- coding: utf-8 -*-

# Liste des imports requis
import json
import pymongo
import allDAO

# Paramètrage de la base mongoDB
cnx_string = "mongodb://localhost:27017"
cnx = pymongo.MongoClient(cnx_string)

# Paramètrage de la base mongoDB
database = cnx.projet

# Paramètrage des DAO
projet = allDAO.AllDAO(database)

# Chemin des JSON
json_dir_collision = './data/collision.json'
json_dir_complaint = './data/complaint.json'
json_dir_culture = './data/culture.json'
json_dir_park = './data/park.json'
json_dir_restaurant = './data/restaurant.json'
json_dir_tree = './data/tree.json'
json_dir_water = './data/water.json'

# Lecture des fichiers
json_data_collision = open(json_dir_collision).read()
json_data_complaint = open(json_dir_complaint).read()
json_data_culture = open(json_dir_culture).read()
json_data_park = open(json_dir_park).read()
json_data_restaurant = open(json_dir_restaurant).read()
json_data_tree = open(json_dir_tree).read()
json_data_water = open(json_dir_water).read()

# Chargement et import des données
try:
    data_collision= json.loads(json_data_collision)
    data_complaint= json.loads(json_data_complaint)
    data_culture = json.loads(json_data_culture)
    data_park= json.loads(json_data_park)
    data_restaurant= json.loads(json_data_restaurant)
    data_tree= json.loads(json_data_tree)
    data_water = json.loads(json_data_water)
except:
    print("ko")
else:
    projet.insert("collision",data_collision)
    projet.insert("complaint",data_complaint)
    projet.insert("culture",data_culture)
    projet.insert("park",data_park)
    projet.insert("restaurant",data_restaurant)
    projet.insert("tree",data_tree)
    projet.insert("water",data_water)



