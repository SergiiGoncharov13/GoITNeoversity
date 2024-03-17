import turtle

def pythagorean_tree(t, length, angle, depth):
    if depth == 0:
        return
    t.forward(length)
    t.left(angle)
    pythagorean_tree(t, length * 0.7, angle, depth - 1)
    t.right(angle * 2)
    pythagorean_tree(t, length * 0.7, angle, depth - 1)
    t.left(angle)
    t.backward(length)

def main():
    depth = int(input("Enter the level of recursion: "))
    
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-50, -200)
    t.pendown()
    t.left(90)
    pythagorean_tree(t, 100, 45, depth)
    
    turtle.done()

if __name__ == "__main__":
    main()
