from pathlib import Path
from threading import Thread, Lock, current_thread
from collections import defaultdict
import logging
import timeit


def search_words_in_file(filepath, keywords):
    """Search words in file"""
    result = defaultdict(list)
    try:
        with open(filepath) as f:
            content = f.read()

        for word in keywords:
            if word in content:
                result[word].append(str(filepath))

    except IOError as e:
        logging.error(e)

    return result


def worker(files, keywords, results, lock):
    """Thread function"""
    logging.info(f"Thread {current_thread().name} started")
    for file in files:
        result = search_words_in_file(file, keywords)
        for key, value in result.items():
            with lock:
                results[key].extend(value)

    logging.info(f"Thread {current_thread().name} finished")


def main_threading(file_paths, keywords, num_threads):
    threads = []
    results = defaultdict(list)

    # Distribute files among threads
    files_per_thread = len(file_paths) // num_threads
    reminder = len(file_paths) % num_threads
    start_index = 0

    for i in range(num_threads):
        end_index = start_index + files_per_thread + (1 if i < reminder else 0)
        files = file_paths[start_index:end_index]
        lock = Lock()
        t = Thread(
            target=worker, name=f"Thread_{i}", args=(files, keywords, results, lock)
        )
        threads.append(t)
        t.start()
        start_index = end_index

    for t in threads:
        t.join()

    return results


if __name__ == "__main__":
    message_format = "%(threadName)s %(asctime)s: %(message)s"
    logging.basicConfig(format=message_format, level=logging.INFO, datefmt="%H:%M:%S")
    file_paths = ["f.txt", "d.txt"]
    keywords = ["потоки", "Windows", "Microsoft", "автори"]
    num_threads = 15

    start_time = timeit.default_timer()
    results = main_threading(file_paths, keywords, num_threads)
    duration = timeit.default_timer() - start_time

    print(f"\nThreaded version took {duration:.2f} seconds\n")

    for key, value in results.items():
        print(f"{key}: {value}\n")