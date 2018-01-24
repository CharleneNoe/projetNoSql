var nums = db.complaint.count();

db.complaint.aggregate([
   {$group: 
       {_id: "$borough", count:{ "$sum": 1}}},    
   {$project: { 
           percentage: { 
                "$multiply":[{"$divide":["$count",{"$literal":nums}]},100]}}},
   {$sort : {percentage : 1}}
])