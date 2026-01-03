"""
Supply Planning using Linear Programming

This script optimizes stock allocation across distribution centers
to meet customer demand at minimum transportation cost.
"""

import pandas as pd
import numpy as np
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpStatus, value
import matplotlib.pyplot as plt


def load_data():
    """Load transportation costs and demand data from data folder."""
    # Inbound costs (from plants to DCs)
    df_inbound = pd.read_csv("data/df_inprice.csv", index_col=0)

    # Outbound costs (from DCs to stores)
    df_outbound = pd.read_csv("data/df_outprice.csv", index_col=0)

    # Demand data
    df_demand = pd.read_csv("data/df_demand.csv", index_col=0)

    return df_inbound, df_outbound, df_demand


def create_sample_data():
    """Create sample data for demonstration."""
    # 2 plants, 2 DCs, 10 stores
    np.random.seed(42)

    # Inbound costs
    inbound = pd.DataFrame({
        "FROM": ["P1", "P2"],
        "D1": [3.0, 2.3],
        "D2": [5.0, 6.6],
    }).set_index("FROM")

    # Outbound costs
    stores = [f"S{i}" for i in range(1, 11)]
    outbound = pd.DataFrame({
        "from": ["D1", "D2"],
        **{s: np.random.uniform(1, 10, 2) for s in stores}
    }).set_index("from")

    # Demand
    demand = pd.DataFrame({
        "STORE": stores,
        "DEMAND": np.random.randint(50, 300, 10)
    })

    return inbound, outbound, demand


def optimize_supply_planning(df_inbound, df_outbound, df_demand,
                            n_plants=2, n_dcs=2, n_stores=None):
    """
    Solve the transhipment problem using linear programming.

    Minimizes total transportation cost (inbound + outbound).
    """
    if n_stores is None:
        n_stores = len(df_demand)

    # Initialize model
    model = LpProblem("Supply_Planning", LpMinimize)

    # Decision variables
    # Inbound flows: I[plant, dc]
    I = LpVariable.dicts(
        "inbound",
        [(i+1, j+1) for i in range(n_plants) for j in range(n_dcs)],
        lowBound=0,
        cat="Integer"
    )

    # Outbound flows: O[dc, store]
    O = LpVariable.dicts(
        "outbound",
        [(i+1, j+1) for i in range(n_dcs) for j in range(n_stores)],
        lowBound=0,
        cat="Integer"
    )

    # Objective: minimize total transportation cost
    inbound_cost = lpSum([
        df_inbound.iloc[i, j+1] * I[i+1, j+1]
        for i in range(n_plants)
        for j in range(n_dcs)
    ])

    outbound_cost = lpSum([
        df_outbound.iloc[i, j+1] * O[i+1, j+1]
        for i in range(n_dcs)
        for j in range(n_stores)
    ])

    model += inbound_cost + outbound_cost

    # Constraints
    # 1. Meet store demand
    for j in range(n_stores):
        model += lpSum([O[i+1, j+1] for i in range(n_dcs)]) >= df_demand.iloc[j, 1]

    # 2. Flow conservation at DCs (inbound = outbound)
    for dc in range(n_dcs):
        model += lpSum([I[i+1, dc+1] for i in range(n_plants)]) == \
                 lpSum([O[dc+1, j+1] for j in range(n_stores)])

    # Solve
    model.solve()

    # Extract results
    inbound_flow = np.zeros((n_plants, n_dcs))
    outbound_flow = np.zeros((n_dcs, n_stores))

    for i in range(n_plants):
        for j in range(n_dcs):
            inbound_flow[i, j] = I[i+1, j+1].varValue or 0

    for i in range(n_dcs):
        for j in range(n_stores):
            outbound_flow[i, j] = O[i+1, j+1].varValue or 0

    return model, inbound_flow, outbound_flow


def display_results(model, inbound_flow, outbound_flow, df_demand):
    """Display optimization results."""
    print("=" * 60)
    print("SUPPLY PLANNING OPTIMIZATION RESULTS")
    print("=" * 60)

    print(f"\nStatus: {LpStatus[model.status]}")
    print(f"Total Transportation Cost: ${value(model.objective):,.2f}")

    # Inbound flows
    print("\n--- INBOUND FLOWS (Plants to DCs) ---")
    df_inbound_result = pd.DataFrame(
        inbound_flow.astype(int),
        index=[f"P{i+1}" for i in range(inbound_flow.shape[0])],
        columns=[f"D{j+1}" for j in range(inbound_flow.shape[1])]
    )
    print(df_inbound_result)

    # DC throughput
    print("\n--- DC THROUGHPUT ---")
    for j in range(inbound_flow.shape[1]):
        throughput = inbound_flow[:, j].sum()
        print(f"D{j+1}: {throughput:,.0f} units")

    # Outbound flows summary
    print("\n--- OUTBOUND FLOWS (DCs to Stores) ---")
    for i in range(outbound_flow.shape[0]):
        stores_served = (outbound_flow[i, :] > 0).sum()
        total_shipped = outbound_flow[i, :].sum()
        print(f"D{i+1}: {total_shipped:,.0f} units to {stores_served} stores")

    # Demand fulfillment
    total_demand = df_demand.iloc[:, 1].sum()
    total_shipped = outbound_flow.sum()
    print(f"\n--- DEMAND FULFILLMENT ---")
    print(f"Total Demand: {total_demand:,.0f} units")
    print(f"Total Shipped: {total_shipped:,.0f} units")
    print(f"Fill Rate: {total_shipped/total_demand*100:.1f}%")


def main():
    """Main function for supply planning optimization."""
    # Load or create data
    try:
        df_inbound, df_outbound, df_demand = load_data()
        print("Data loaded from files.")
        n_stores = len(df_demand)
    except FileNotFoundError:
        print("Data files not found. Using sample data.")
        df_inbound, df_outbound, df_demand = create_sample_data()
        n_stores = 10

    # Display input data
    print("\n--- INBOUND COSTS ($/unit) ---")
    print(df_inbound)

    print(f"\n--- DEMAND ({n_stores} stores) ---")
    print(f"Total demand: {df_demand.iloc[:, 1].sum():,} units")

    # Optimize
    model, inbound_flow, outbound_flow = optimize_supply_planning(
        df_inbound, df_outbound, df_demand,
        n_plants=2, n_dcs=2, n_stores=n_stores
    )

    # Display results
    display_results(model, inbound_flow, outbound_flow, df_demand)


if __name__ == "__main__":
    main()
