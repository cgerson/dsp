# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

'ls' lists the files in the current directory. The '-a' flag makes sure to include all files, even if they are hidden. The '-l' flag shows files in long-list format (printing more information on the file such as permissions to read/write/execute, number of links, owner, modified date, etc, as opposed to just the file names). The '-lh' flag prints the same info as '-l', but prints the size of the file in human readable format (3.2K instead of 3200). To print details about all files in long-list form and with human-readable sizes, including hidden files, you can combine flags: 'ls -a -lh'. 

---


---

What does `xargs` do? Give an example of how to use it.

'xargs' constructs and executes command lines that it inteprets from standard input. It comes in handy when trying to input and work with lists too long to be accepted as argument, lists generated from commands like 'grep' and 'find'. 'xargs' divides the list into sublists. One example using 'xargs' is to delete certain files. We can use 'find' to find specific files fitting a condition, then remove them. The following removes any text files in the current directory.

$ find . -name "*.txt" | xargs rm 

---
