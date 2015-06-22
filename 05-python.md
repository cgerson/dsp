# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

[![Think Python](img/think_python.png)](http://www.greenteapress.com/thinkpython/)

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

Complete the following exercises to check your ability with Python.

These exercises are implemented with doctests, which are runnable tests inside docstrings. Fill in the function definitions. Correct solutions will make it possible to run (for example) `python -m doctest strings.py` with no messages about failures.

 * [Strings](python/strings.py)
 * [Lists](python/lists.py)


---

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

> Both lists and tuples are data structures that hold values separated by commas. Tuples however are immutable, or rather their value is fixed. It's been noted then that the difference is also semantic: due to the immutability of tuples, one would expect different kinds of information in each one. Tuples can be used as keys in dictionaries, while lists cannot. An error would result if the list as key is modified, because its modification would change the hash value used to look up the value, and therefore its value would not be retrievable. 

---


---

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

> Lists and sets are both data types that hold elements in Python. Both can be modified (unless set is initalized as a frozenset). Both can have functions applied to elements, for example, map(fun, seq) applies function fun to every element in seq. Both can hold elements of different data types. However, lists are sequence objects, in which every element is indexed, while sets are unordered collections of unique values and can be used as keys in dictionaries. 

> Lists are the most basic type of sequence in Python. They can hold duplicate values, and can access built-in methods such as index(), insert(), and sort(), for example, with list a where a = ['test','test',1,2,3], we can insert element 'inserted' at index 1 with a.insert(1,'inserted').

> Sets hold only unique values, ordered in an arbitrary manner, and can be used to perform mathematical operations between sets such as intersections (for sets a and b, >>> a&b) and unions (>>> a|b). 

> Finding elements in sets is faster than in lists, because sets are implemented using hash tables, while lists are not.  


---


---

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

'lambda' functions are anonymous functions constructed at runtime. Let's say we have a list of tuples with book titles and years published:
> books = [("Infinite Jest",1996),("Foundation",1951),("The Martian Chronicles",1950)]

And we want to sort by year. We can call the sorted() function and use 'lambda' in the 'key' argument like so:
> sorted(books,key=lambda book: book[1])

Where book[1] references the index of the year in each tuple.


---


---

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehensions are a way to create lists in Python. It is an alternative to using lambda, map() and filter(). 

Map(): In my answer to the first question above, I noted that map() could be used to apply function fun to sequence seq with map(fun, seq) to create a new list. We can do the same with list comprehension:
> [x**2 for x in seq]

Where our function is x**2. In this example, we go through every element x in sequence seq and generate the square. 

Filter(): The filter() function is used to filter out certain elements of a list. For example, say we have a list names:
> names = ['Claire','Cathy','Hannah','Kevin','Chris']

And we want to filter out names beginning with 'C'. We can apply the filter() function as such:
> filter(lambda x: x[0]=='C',names)

Alternatively, we can use list comprehension to obtain the same result:
> [x for x in names if x[0]=='C']

Set comprehensions work the same as list comprehensions, but return a set. Dictionary comprehensions can be created from a list using comprehension, for example, given seq1 = [1,2,3] and seq2 = ['cat','dog','bird'], we can make this dictionary with elements of seq1 as keys and their square as the value:
> {x: x**2 for x in seq}

Or elements of seq1 as keys and elements of seq2 as values:
> {x: y for x in seq1 for y in seq2}

List comprehension creates more readable and compact code, and therefore may be preferible to map() and filter(). 

---


Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

```bash
./markov.py chains.txt 40
```

A possible output would be:

> show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.
