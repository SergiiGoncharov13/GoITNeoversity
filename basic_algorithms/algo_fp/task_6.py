def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    selected_items = {}
    current_budget = budget

    for item_name, item_data in sorted_items:
        if item_data["cost"] <= current_budget:
            selected_items[item_name] = item_data
            current_budget -= item_data["cost"]
    
    return selected_items


def dynamic_programming(items, budget):
    dp_matrix = [[0] * (budget + 1) for _ in range(len(items) + 1)]

    for i, (item_name, item_data) in enumerate(items.items(), start=1):
        for j in range(budget + 1):
            if item_data["cost"] <= j:
                dp_matrix[i][j] = max(dp_matrix[i - 1][j], dp_matrix[i - 1][j - item_data["cost"]] + item_data["calories"])
            else:
                dp_matrix[i][j] = dp_matrix[i - 1][j]

    # Reconstruct the result
    selected_items = {}
    i, j = len(items), budget
    while i > 0 and j > 0:
        if dp_matrix[i][j] != dp_matrix[i - 1][j]:
            item_name = list(items.keys())[i - 1]
            selected_items[item_name] = items[item_name]
            j -= items[item_name]["cost"]
        i -= 1

    return selected_items





items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}



if __name__ == "__main__":
    budget = 95
    greedy_result = greedy_algorithm(items, budget)
    dynamic_result = dynamic_programming(items, budget)

    print("Greedy algorithm:")
    for item, data in greedy_result.items():
        print(f"{item}: Cost: {data['cost']}, Calories: {data['calories']}")

    print("====" * 10)

    print("Dynamic_programming algorithm:")
    for item, data in dynamic_result.items():
        print(f"{item}: Cost: {data['cost']}, Calories: {data['calories']}")