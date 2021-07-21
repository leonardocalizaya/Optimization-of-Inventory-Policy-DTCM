import PMT as pm
import json

# Data from the problem

price = 200
fixed_cost = 300
variable_cost = 50

holding_cost = 10
backorder_cost = 50

demand_dist = {0: 0.05, 1:0.10, 2:0.10, 3:0.10, 4: 0.15, 5: 0.15, 6:0.2, 7:0.1, 8:0.05}

expected_profit = {}


#Different types of (s, S) policies.
for a in range(2, 10):
    for b in range(3, 11):
        stati_dist = pm.stationary_distribution(pm.probability_matrix(a, b, demand_dist))
        exp_profits = pm.expected_profit(price, fixed_cost, variable_cost, holding_cost, backorder_cost, a, b, demand_dist)

        total_profit = sum([prob*profit for prob, profit in zip(stati_dist, exp_profits)])

        expected_profit[f"({a}, {b})"] = total_profit

with open("expected_profit_results.json", "w") as f:
        json.dump(expected_profit, f, sort_keys=True, indent=4)

a = pm.stationary_distribution(pm.probability_matrix(5, 7, demand_dist))
b = pm.expected_profit(price, fixed_cost, variable_cost, holding_cost, backorder_cost, 5, 7, demand_dist)

#print(a)
#print(b)
#print(sum([c*d for c, d in zip(a, b)]))
