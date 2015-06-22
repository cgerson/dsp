# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

 * pwd - print working directory
 * hostname - my computer's network name
*mkdir - make directory 
*cd - change directory
*ls - list directory
*rmdir - remove directory
*pushd - push directory, pushes it into a list then changed directory
*popd - pop directory, takes list directory you pushed and takes you back there
*cp - copy a file or dir
*mv - move a file or dir
*cat - print the whole file
*xargs - execute arguments
*find - find files
*grep - find things inside files
*man - read a manual page
*apropos - find what man page is appropriate
*env - look at your environment
*echo - print some arguments
*export - export/set a new environment variable
*exit - exit the shell
*sudo - become super user root (careful...)
*chmod - change permission modifiers
*chown - change ownership
*cd .. - moves up in the tree/path
*mkdir -p - makes an entire path even if directories don't exist
*touch - +file name, makes empty file
*cd file1 file2 - copies file1 and names it file2
*cp file1 dir - copies file1 into dir, same name
*cp -r dir1 dir2 - copies contents of dir1 and deposits into newly created dir2
*mv file1 file2 - renames file1 with name file2
*mv dir1 dir2 - renames dir1 with name dir2
*less file - display file (type q to quit display)
*more file - display file (stays in Terminal)
*rm file - removes file
*$|$ - takes output from left and pipes it to the command on the right
*$<$ - the < will take and send the input from the file on the right to the program on the left
*$>$ - the > takes the output of the command on the left, then writes it to the file on the right
*$>>$ - the >> takes the output of the cmd on the left, then appends it to the file on the right
** - wildcard

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
