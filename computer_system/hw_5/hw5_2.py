import string
import requests

from collections import defaultdict, Counter
from concurrent.futures import ThreadPoolExecutor
from matplotlib import pyplot as plt

def get_text(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        return None

def remove_punctuation(text):
    return text.translate(str.maketrans("", "", string.punctuation))

def map_function(word) -> tuple:
    return word, 1

def shuffle_function(mapped_values):
    shuffled = defaultdict(list)
    for key, value in mapped_values:
        shuffled[key].append(value)
    return shuffled.items()

def reduce_function(key_values):
    key, values = key_values
    return key, sum(values)

# MapReduce
def map_reduce(text, search_words=None):
    text = remove_punctuation(text)
    words = text.split()

    if search_words:
        words = [word for word in words if word in search_words]  # filter

    with ThreadPoolExecutor() as executor:
        mapped_values = list(executor.map(map_function, words))

    shuffled_values = shuffle_function(mapped_values)

    with ThreadPoolExecutor() as executor:
        reduced_values = list(executor.map(reduce_function, shuffled_values))

    return dict(reduced_values)

def visual_result(result):
    top_10 = Counter(result).most_common(10)
    labels, values = zip(*top_10)
    plt.figure(figsize=(10, 5))
    plt.barh(labels, values, color='b')
    plt.xlabel('Quantity')
    plt.ylabel('Word')
    plt.title('10 most used words')
    plt.show()


if __name__ == '__main__':
    url = "https://gutenberg.net.au/ebooks01/0100021.txt"
    search_words = None 
    text = get_text(url)
    if text:
        result = map_reduce(text)

    print("Result:", result)
    visual_result(result)