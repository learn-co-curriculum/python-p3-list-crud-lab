# List CRUD Lab

## Learning Goals

- Create, read, update, and delete elements from lists.

***

## Key Vocab

- **Interpreter**: a program that executes other programs. Python programs
require the Python interpreter to be installed on your computer so that they
can be run.
- **Python Shell**: an interactive interpreter that can be accessed from the
command line.
- **Data Type**: a specific kind of data. The Python interpreter uses these
types to determine which actions can be performed on different data items.
- **Exception**: a type of error that can be predicted and handled without
causing a program to crash.
- **Code Block**: a collection of code that is interpreted together. Python
groups code blocks by indentation level.
- **Function**: a named code block that performs a sequence of actions when it
is called.
- **Scope**: the area in your program where a specific variable can be called.

***

## Instructions

This is a **test-driven lab**. Run `pipenv install` to create your virtual
environment and `pipenv shell` to enter the virtual environment. Then run
`pytest -x` to run your tests. Use these instructions and `pytest`'s error
messages to complete your work in the `lib/` folder.

In this lab, we will be coding the solutions for each of the above tasks in the
body of a function. In `lib/list_crud.py` we've defined a series of functions for
you, each of which is responsible for one of the tasks above. Your job is to
write the code in the body of each function to get the test passing.

Let's go through the first challenge together.

### `create_an_empty_list()`

Let's run our test suite to get started. Run the tests one at a time with the
`pytest -x` command in your terminal.

If we do so, we'll see our first failure.

Our test is telling us that we are expected to code the content of our
`create_an_empty_list()` function such that a new, empty list is created and
returned. Our test `expected` an empty list, `[]`, but got `None`.

Open up `lib/list_crud.py` and check out the `create_an_empty_list()` function.
It's empty! Let's write the code that will get the test passing.

We'll use the literal constructor to make a new list with nothing in it:

```py
def create_an_empty_list():
    return []
```

Run the test suite again and we should be passing that first test.

### `create_a_list()`

This function should use the literal constructor to create a new list, just like
we did above. This time, however, create a list that contains four elements.
The four elements can be any elements of your choosing, as long as there are
only four of them.

### `add_element_to_end_of_list()`

This function takes in two arguments, a list and the element we want to add to
it. Use the [`append()` method][append] to add that element to the end of the new list.

### `add_element_to_start_of_list()`

This function takes in two arguments, a list and the element we want to add to
it. Use the [`insert()` method][insert] to add that element to the start of that list.

### `remove_element_from_end_of_list()`

This function takes in one argument, the list on which we want to operate. Use
the [`pop()`][pop] method to remove the last item from the list.

### `remove_element_from_start_of_list()`

This function takes in one argument, the list on which we want to operate. Use
the [`del` keyword][del] to remove the first item from the list.

### `retrieve_first_element_from_list()`

This function takes in one argument, the list from which we want to retrieve an
element. Use `[]` notation to return the value stored at the first index of the
list. Remember that lists are zero-indexed. This means that the first index
number is `0` and it counts up from there. So, the first element of a list is
stored at index `0`.

### `retrieve_element_from_index()`

This function takes in two arguments, a list and the index number whose element
we want to retrieve. Use the `[]`, bracket notation, to return the element stored
at that index number of the given list.

### `retrieve_last_element_from_list()`

This function takes in one argument, the list from which we want to retrieve an
element. There are a number of ways to do this, but we recommend using the `[]`
notation with the following hint:

The last element of a list is considered to be stored at an index of `-1`.

***

## Resources

- [5. Data Structures - Python](https://docs.python.org/3/tutorial/datastructures.html)
- [Python List append() Method - W3schools][append]
- [Python List insert() Method - W3schools][insert]
- [Python List pop() Method - W3schools][pop]
- [Python del Keyword - W3schools][del]

[append]: https://www.w3schools.com/python/ref_list_append.asp
[insert]: https://www.w3schools.com/python/ref_list_insert.asp
[pop]: https://www.w3schools.com/PYTHON/ref_list_pop.asp
[del]: https://www.w3schools.com/python/ref_keyword_del.asp
