import heapq

def min_cost_to_connect_cables(cable_lengths):
    if not cable_lengths:
        return 0

    # Initializing the minimum heap
    heapq.heapify(cable_lengths)
    total_cost = 0
    connection_order = []

    # Combine cables while there is more than one cable in the heap
    while len(cable_lengths) > 1:
        # Remove the two smallest cables
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)

        # Combine cables and add the cost of combining to the total cost
        cost = first + second
        total_cost += cost
        connection_order.append((first, second, cost))

        # Adding a new spliced cable to the heap
        heapq.heappush(cable_lengths, cost)

    return total_cost, connection_order


if __name__ == '__main__':
    cable_lengths = [15, 4, 4, 2, 1, 5, 7, 1]
    total_cost, order = min_cost_to_connect_cables(cable_lengths)

    for i, (first, second, cost) in enumerate(order, start=1):
        print(f"Step {i}: Combining cables {first} and {second}, Cost: {cost}")

    print(f"\nTotal Cost: {total_cost}")

