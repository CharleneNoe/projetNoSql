db.park.aggregate([
    {$match:{"class":"PARK"}},
    {$group:{_id:"$borough",count:{$sum:1}}},
    {$sort:{count:-1}}
])