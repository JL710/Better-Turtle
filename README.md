# Better-Turtle

## installation
```
pip install git+https://github.com/JL710/Better-Turtle.git
```

## updating
```
pip install --force-reinstall git+https://github.com/JL710/Better-Turtle.git
```

## basic usage
```python
from BetterTurtle import BetterTurtle
screen = BetterTurtle()
t = screen.get_turtle()

for i in range(10):
    t.forward(100)
    t.right(90)

screen.not_exit()
```
