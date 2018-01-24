db.tree.aggregate([
    {$match:{status:"Alive",health:{$in:['Fair','Good']}}},
    {$group:{_id:"$borough",count:{$sum:1}}},
    {$sort:{count:-1}}
])