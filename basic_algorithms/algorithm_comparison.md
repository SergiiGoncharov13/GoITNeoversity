##  algorithm comparison

| Algorithm            | Small                | Medium               | Large                |
| -------------------- | -------------------- | -------------------- | -------------------- |
| Insertion Sort       |              0.00113 |              0.10446 |             10.19887 |
| Merge Sort           |              0.00105 |              0.01076 |              0.14106 |
| Timsorted            |              0.00004 |              0.00047 |              0.00789 |
| Timsort              |              0.00003 |              0.00042 |              0.00784 |

   
    data_small = 100
    data_medium = 1_000
    data_large = 10_000
    Кількість повтору = 10

Часові складності алгоритмів:
    Insertion Sort    O(n^2)
    Merge Sort  O(n * log n)
    Timsorted O(n * log n)
    Timsort O(n * log n)

Відповідно до часовою складності алгоритму  Insertion Sort  має найбільший час виконання 10.19887. 
Merge Sort вже має набагато меньший час виконання 0.14106
Timsorted, Timsort це гібридний алгоритм сортування, який комбінує алгоритми  Insertion Sort та Merge Sort. 
І має найкращі результати  0.00789 та  0.00784 відповідно. 
Timsort показує кращий результат, тому що він імутабельний