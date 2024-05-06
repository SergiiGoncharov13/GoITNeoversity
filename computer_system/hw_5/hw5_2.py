import string
import asyncio
from collections import defaultdict, Counter

import httpx
from matplotlib import pyplot as plt


async def get_text(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None


def remove_punctuation(text):
    return text.translate(str.maketrans("", "", string.punctuation))


async def map_function(word) -> tuple:
    return word, 1


def shuffle_function(mapped_values):
    shuffled = defaultdict(list)
    for key, value in mapped_values:
        shuffled[key].append(value)
    return shuffled.items()


async def reduce_function(key_values):
    key, values = key_values
    return key, sum(values)


# MapReduce
async def map_reduce(text, search_words=None):
    text = await get_text(url)
    if text:
        # Remove punctuation
        text = remove_punctuation(text)
        words = text.split()

        if search_words:
            words = [word for word in words if word in search_words]  # filter

        # Mapping
        mapped_values = await asyncio.gather(*[map_function(word) for word in words])

        # Shuffle
        shuffled_values = shuffle_function(mapped_values)

        # Reduce
        reduced_values = await asyncio.gather(*[reduce_function(key_values) for key_values in shuffled_values])

        return dict(reduced_values)
    else:
        return None


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
    result = asyncio.run(map_reduce(url, search_words))

    print("Result:", result)
    visual_result(result)