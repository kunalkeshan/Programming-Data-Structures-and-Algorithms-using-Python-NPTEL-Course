# Control Flow

**Table of Contents**:

- [Conditional Execution](#conditional-execution)
  - [Alternative Execution](#alternative-execution)
  - [Shortcut for Conditionals](#shortcut-for-conditional)
  - [Multiway Branching](#multiway-branching)
- [Loops: Repeated Actions](#loops-repeated-actions)
  - [Repeating n times](#repeating-n-times)
  - [Loop based on a condition](#loop-based-on-a-condition)

- Interpreter executes statements from top to bottom.
- Function definitions are "digested" for future fuse.

**Control Flow**: determines order in which statements are executed.

- Conditional Execution.
- Repeated execution - loops.
- Function definitions.

## Conditional Execution

```python
if(condition):
    statement_1! # Execute conditionally
statement_2 # Executed in flow, not a part of the if condition
```

- Second condition is executed only if the `condition` is True.
- Use uniform indentation to construct body of the conditional.

### Alternative Execution

```python
if(condition):
    statement_1
else:
    statement_2
```

If `condition` is True, then `statement_1` is executed and if it is not, then `statement_2` is executed.

### Shortcut for conditional

- Numeric value `0` is treated as `False`.
- Empty sequence, `""`, `[]` is treated as `False`.
- Everything else is `True`.

### Multiway branching

```python
if(condition):
    statement_1
elif(condition):
    statement_2
elif(condition):
    statement_3
else:
    statement_4
```

- When check is being done for multiple conditions. `elif` helps evaluate multiple conditions and executes the statement within it and then exits the conditional flow.

## Loops: Repeated actions

Repeat something a fixed number of times. Indentation is used for marking the body of the loop.

```python
for i in [1,2,3,5]:
    y = y*i
    z = i + 1
```

### Repeating n times

- Fixed loops, do something for a fixed amount of time.
- But usually, there will be cases where looping is required `n` number of times.
- Use `range(0,n)`. Returns a list of numbers from 0 to n.

```python
for i in range(0,n):
    statements
```

### Loop based on a condition

```python
while(condition):
    statements
```

- Execute body if `condition` evaluates to `True`.
- After each iteration `condition` is checked again.
- Body must ensure loops moves towards termination.
