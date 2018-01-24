# SCRIP SHELL PERMETTANT L'IMPORTATION DES DONNÉES DEPUIS L'OPEN DATA DE NYC
if [ -d "data" ];then rm -r data; fi
mkdir data
cd data
# DATASET COLLISION 2013
wget https://data.cityofnewyork.us/api/views/vzwb-a4md/rows.json?accessType=DOWNLOAD
mv rows.json?accessType=DOWNLOAD collision.json
# DATASET COMPLAINT FELONY
wget https://data.cityofnewyork.us/api/views/64t7-9bba/rows.json?accessType=DOWNLOAD
mv rows.json?accessType=DOWNLOAD complaint.json
# DATASET CULTURE
wget https://data.cityofnewyork.us/api/views/u35m-9t32/rows.json?accessType=DOWNLOAD
mv rows.json?accessType=DOWNLOAD culture.json
# DATASET PARK
wget https://data.cityofnewyork.us/api/views/p7jc-c8ak/rows.json?accessType=DOWNLOAD
mv rows.json?accessType=DOWNLOAD park.json
# DATASET RESTAURANT
wget https://data.cityofnewyork.us/api/views/43nn-pn8j/rows.json?accessType=DOWNLOAD
mv rows.json?accessType=DOWNLOAD restaurant.json
# DATASET TREE
wget https://data.cityofnewyork.us/api/views/5rq2-4hqu/rows.json?accessType=DOWNLOAD
mv rows.json?accessType=DOWNLOAD tree.json
# DATASET WATER
wget https://data.cityofnewyork.us/api/views/qfe3-6dkn/rows.json?accessType=DOWNLOAD
mv rows.json?accessType=DOWNLOAD water.json

# REAGENCEMENT DES DATASET
cd ./..
python3 ./DAO/manageData.py
