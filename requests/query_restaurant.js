db.restaurant.aggregate([
    {$match:{"grade":"A","borough":{$ne:"Missing"}}},
    {$group:{_id : "$borough",count:{$sum:1}}},
    {$sort:{count:-1}}
])