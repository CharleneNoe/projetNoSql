// Classement du nombre de meilleurs restaurants (grade = A) après inspection
// dans les différents arrondissements
db.restaurant.aggregate([
    {$match:{"grade":"A","borough":{$ne:"Missing"}}},
    {$group:{_id : "$borough",count:{$sum:1}}},
    {$sort:{count:-1}}
])
