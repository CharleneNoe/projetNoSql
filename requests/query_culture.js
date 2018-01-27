// Répartition des cinémas et musées de NYC selon l’arrondissement
db.culture.aggregate([
    {$match:{'discipline':{$in:['Theater','Museum']}}},
    {$group:{_id : "$borough",count:{$sum:1}}},
    {$sort:{count:-1}}
])
