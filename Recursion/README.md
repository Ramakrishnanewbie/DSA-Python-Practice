## Recursion Theory - Most Important Concept


What is a function ?

Function -> 

```
def greet() :
  print("Rama")

```

When greet is called, Rama is printed and when recalled it will print again.

So, what is recursion > A function that calls itself somewhere inside it somewhere.

Basic template :
```
def greet():
  print("Rama")
  greet()
```

Most important Condition : It has to terminate somewhere right, meaning an end condition. Otherwise, it is a stack overflow error. 

In python it does for 987 times before throwing stack overflow error before stopping.

