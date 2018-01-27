// Répartition des plaintes sur la qualité de l’eau selon l’arrondissement

var nums = db.water.count();

db.water.aggregate([
   {$group: 
       {_id: "$borough", count:{ "$sum": 1}}},    
   {$project: { 
           percentage: { 
                "$multiply":[{"$divide":["$count",{"$literal":nums}]},100]}}},
   {$sort : {percentage : 1}}
])
