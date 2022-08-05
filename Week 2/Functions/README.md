# Functions

A group of statements that perform a given task is a function. They help separate specific logic and organize the code. They can be called repeatedly to perform the same task over and over again.

**Table of Contents**:

- [Function Definitions](#function-definition)
- [Passing values to Functions](#passing-values-to-functions)
- [Scope of names](#scope-of-names)
- [Defining Functions](#defining-functions)
- [Recursive functions](#recursive-functions)

## Function Definition

```python
def func(a, b, c):
    statement_1
    statement_2
    ..
    return(v)
```

A function definition includes the following:

- Function Name (`func`)
- Arguments/Parameters (`a`, `b`,`c`)
- A `return` statement, exits the function and returns a value.
- If there is no `return`, function ends when last statement is reached.

## Passing values to Functions

Same as defining the function, instead actual values are passed into the arguments.

```python
def twice(n):
    return(2*n)

print(twice(12)) # 24
```

## Scope of names

Names within the function have local scope.

## Defining Functions

- A function must be defined before it is invoked.
- Interpreter reads the code from top to bottom.
- Functions are not read, but their definition is remembered.
- They're read when the function is invoked.

## Recursive Functions

- A function can all itself.

```python
def factorial(n):
    if n <= 0:
        return(1)
    else:
        val = n * factorial(n-1)
        return(val)
```
