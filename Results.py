import PMT as pm
import json

# Data from the problem

price = 200
fixed_cost = 300
variable_cost = 50

holding_cost = 10
backorder_cost = 50

demand_dist = {0: 0.05, 1:0.10, 2:0.10, 3:0.10, 4: 0.15, 5: 0.15, 6:0.2, 7:0.1, 8:0.05}

results = {}


#Different types of (s, S) policies.
for s in range(2, 10):
    for S in range(3, 11):

        if s < S:
            dict_a = {}

            stati_dist = pm.stationary_distribution(pm.probability_matrix(s, S, demand_dist))
            expected_states_nums = pm.expected_state_numbers(price, fixed_cost, variable_cost, holding_cost, backorder_cost, s, S, demand_dist)

            for variable in expected_states_nums.keys():
                long_run_average = sum([prob*state_data for prob, state_data in zip(stati_dist, expected_states_nums[variable])])

                dict_a[variable] = long_run_average

            #weekly_profit_np = sum([prob*profit for prob, profit in zip(stati_dist, exp_profits)])
            #dict_a["Average Weekly Profit (no penalty)"] = weekly_profit_np

            fraction_weeks_ordered = sum(stati_dist[:s+1])
            dict_a["Fraction of weeks that an order is placed"] = fraction_weeks_ordered


            results[f"({s}, {S})"] = dict_a

with open("results.json", "w") as f:
    json.dump(results, f, sort_keys=True, indent=4)

#a = pm.stationary_distribution(pm.probability_matrix(5, 7, demand_dist))
#b = pm.expected_profit(price, fixed_cost, variable_cost, holding_cost, backorder_cost, 5, 7, demand_dist)

#print(a)
#print(b)
#print(sum([c*d for c, d in zip(a, b)]))
