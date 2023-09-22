num_purchases = int(input("Number of purchases: "))
sales_tax = float(input("Sales Tax: "))

customer_names = []
item_costs = []

for person in range(num_purchases):
        customer = input("Customer: ")
        customer_names.append(customer)
        cost = float(input("Cost: "))
        item_costs.append(cost)



#print(customer_names)
#print(item_costs)

def add_tax(item_costs, sales_tax): #function that applies to tax to the price of each item
    for item in range(len(item_costs)):
        taxed_item = item_costs[item] * (1+sales_tax)
        item_costs[item] = taxed_item
    return item_costs

taxed_costs = add_tax(item_costs, sales_tax)  #call the function


def add_tax(item_cost, sales_tax):
    for item in item_cost:
        item *= sales_tax
    return item_cost

customers_tax = {}
# idx is the index position of both lists
for pers in range(num_purchases):
    if customer_names[pers] not in customers_tax:
        customers_tax[customer_names[pers]] = item_costs[pers]
    else:
        customers_tax[customer_names[pers]] = item_costs[pers] + customers_tax[customer_names[pers]]

print(customers_tax)
