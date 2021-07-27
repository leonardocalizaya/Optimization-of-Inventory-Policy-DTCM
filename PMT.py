import numpy as np
import pandas as pd


def probability_matrix(s, S, D):
    matrix = []

    for x_n in range(0, S+1):
        row = []
        inv = S if x_n <= s else x_n

        for x_n1 in range (0, S+1):
            p = 0
            for demand in D.keys():
                if x_n1 == 0 and (inv - demand == x_n1 or inv - demand<0):
                    p += D[demand]
                elif inv - demand == x_n1:
                    p += D[demand]

            row.append(p)

        matrix.append(row)

    return matrix

#print(probability_matrix(1, 6, {1:1/6, 2:3/6, 3:2/6}))

def stationary_distribution(matrix):
    size = len(matrix)
    P = np.array(matrix)

    A = np.append(np.transpose(P) - np.identity(size), [[1 for a in range(0, size)]], axis = 0)

    b = [0 for a in range(0, size+1)]
    b[-1] = 1

    b = np.transpose(np.array(b))

    result = np.linalg.solve(np.transpose(A).dot(A), np.transpose(A).dot(b))

    return result

#print(stationary_distribution([[0, 0.5, 0, 0.5], [0.6, 0, 0.4, 0],[0, 0.7, 0, 0.3], [0.8, 0, 0.2, 0]]))
#c=stationary_distribution(probability_matrix(1, 3, {0:0.1, 1:0.4, 2:0.3, 3:0.2}))


# P: Price
# Fc: Fixed Cost
# Vc: Variable Cost
# Hc: Holding Cost
# Bc: Backorder Cost

'''
Returns a dictionary of lists, where each list contains the average weekly variable
of different matrix states. E.g. "Weekly Avg Profit": [100, 200, 500, 400, 300], 100 profit
where the state is 0 (when we end this week with 0 items), 200 for state 1, etc.
'''

def expected_state_numbers(p, Fc, Vc, Hc, Bc, s, S, D):

    result = {"Weekly Avg Profit": [], "Weekly Avg Sales" : [], "Weekly Avg Inventory Cost" : [], "Weekly Avg Order Cost": [], "Weekly Avg Revenues": []}

    for items in range(0, S+1):
        if items <= s:
            inv = S

            TotalOrdCost = Fc + Vc*(S-items)
            TotalHoldCost = items*Hc

        elif items> s:
            inv = items
            TotalOrdCost = 0
            TotalHoldCost = items*Hc

        mindemand = [min(a, b) for a,b in zip(D.keys(), [inv for a in range(0, len(D.keys()))])]

        expected_sales = sum([a*b for a,b in zip(mindemand, D.values())])

        revenue = p*expected_sales

        profit = revenue - TotalOrdCost - TotalHoldCost

        result["Weekly Avg Profit"].append(profit)
        result["Weekly Avg Sales"].append(expected_sales)
        result["Weekly Avg Inventory Cost"].append(TotalHoldCost)
        result["Weekly Avg Order Cost"].append(TotalOrdCost)
        result["Weekly Avg Revenues"].append(revenue)


    return result

#d = expected_profit(2000, 1500, 1000, 100, 0, 1, 3, {0:0.1, 1:0.4, 2:0.3, 3:0.2})

#print(sum([a*b for a, b in zip(c, d)]))

