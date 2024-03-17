import random
import matplotlib.pyplot as plt

def roll_two_dice():
    # Simulate rolling two dice and return the sum of their values
    return random.randint(1, 6) + random.randint(1, 6)

def simulate_dice_rolls(num_rolls):
    # Simulate rolling two dice a large number of times and calculate the probabilities of each sum
    results = {i: 0 for i in range(2, 13)}  # Initialize dictionary to store counts of each sum

    for _ in range(num_rolls):
        roll_sum = roll_two_dice()
        results[roll_sum] += 1

    probabilities = {key: value / num_rolls * 100 for key, value in results.items()}  # Calculate probabilities

    return probabilities

def plot_probabilities(probabilities):
    # Plot a bar chart showing the probabilities of each sum
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.bar(sums, probs, color='green')
    plt.xlabel('Sum of Two Dice')
    plt.ylabel('Probability')
    plt.title('Probabilities of Sums from Two Dice Rolls')
    plt.xticks(sums)
    plt.grid(axis='y')
    plt.show()


def display_table(probabilities):
    print("Table of amounts and their probabilities:")
    print("Sum \t| Probability (%)")
    for total, probability in sorted(probabilities.items()):
        print(f"{total}\t|{probability:.2f}%")



if __name__ == '__main__':
    num_rolls = 1000000  # Number of dice rolls to simulate
    probabilities = simulate_dice_rolls(num_rolls)
    plot_probabilities(probabilities)
    # table_of_probabilities(probabilities, num_rolls)
    display_table(probabilities)

