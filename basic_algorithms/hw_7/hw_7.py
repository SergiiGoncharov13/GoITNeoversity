class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def insert(root, key):
    if root is None:
        return Node(key)
    elif key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
        root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)
    # LL
    if balance > 1 and key < root.left.key:
        return rotate_right(root)
    # RR
    if balance < -1 and key > root.right.key:
        return rotate_left(root)
    # LR
    if balance > 1 and key > root.left.key:
        root.left = rotate_left(root.left)
        return rotate_right(root)
    # RL
    if balance < -1 and key < root.right.key:
        root.right = rotate_right(root.right)
        return rotate_left(root)
    return root

def get_height(root):
    if root is None:
        return 0
    return root.height

def get_balance(root):
    if root is None:
        return 0
    return get_height(root.left) - get_height(root.right)

def rotate_right(z):
    y = z.left
    T3 = y.right
    y.right = z
    z.left = T3
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y


def rotate_left(y):
    x = y.right
    T2 = x.left
    x.left = y
    y.right = T2
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    return x

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

def delete(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        root.val = min_value_node(root.right).val
        root.right = delete(root.right, root.val)
    return root

def find_min_value(root):
    while root.left is not None:
        root = root.left
    return root.key

def find_max_value(root):
    while root.right is not None:
        root = root.right
    return root.key

def find_sum_of_values(root):
    if root is None:
        return 0
    return root.key + find_sum_of_values(root.left) + find_sum_of_values(root.right)


if __name__ == "__main__":
    root = None
    keys = [40, 20, 50, 10, 40, 70, 90]

    for key in keys:
        root = insert(root, key)

    max_value = find_max_value(root)
    print("Max value:", max_value)

    min_value = find_min_value(root)
    print("Min value:", min_value)

    sum_of_values = find_sum_of_values(root)
    print("Sum of values:", sum_of_values)
   
