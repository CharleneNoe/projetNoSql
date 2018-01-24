db.collision.aggregate([
    {$match:{"borough":{$ne:null}}},
    {$group:
        {_id: "$borough",
         total:{$sum: {$add: ["$number_of_pedestrians_injured",
                       "$number_of_pedestrians_killed",
                       "$number_of_cyclist_injured",
                       "$number_of_cyclist_killed"]}}}},
    {$sort : {total : 1}}
])
