#preset numbers, and information
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#Finding the average price of a cut
total_price = 0
for x in prices: 
  total_price += x
average_price = total_price / len(prices)
print("Average Haircut Price: $" + str(average_price))
print("")

#Creating a new list with reduced pricing.
new_prices = []
for x in prices:
  x -= 5
  new_prices.append(x)
print("These are the new prices:", new_prices)
print("")

#Finding out how much revenue and the average of what was brought in last week.
total_revenue = 0

for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue: $" + str(total_revenue))

average_daily_revenue = total_revenue / 7
print("Average Daily Revenue: $" + str(average_daily_revenue))
print("")

#Find all haircuts under $30 and advertise those
cuts_under_30 = []
print("Advertise these haircuts:")
for x in range(len(new_prices)):
  if new_prices[x] < 30:
    cuts_under_30.append(hairstyles[x])
print(cuts_under_30)
