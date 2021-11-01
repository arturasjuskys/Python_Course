from random import choice
food = choice(["cheese pizza", "quiche", "morning bun", "gummy bear", "tea cake"])
bakery_stock = {
	"almond croissant": 12,
	"toffee cookie": 3,
	"morning bun": 1,
	"chocolate chunk cookie": 9,
	"tea cake": 25
}

#    in

print(food)
item = bakery_stock.get(food)
if item:
	print(f"{bakery_stock[food]} {food} left")
else:
	print("we don't make that")

#    .get
	
if food in bakery_stock:
	print(f"{food}: {bakery_stock[food]} in stock")
else:
	print("we don't make that")