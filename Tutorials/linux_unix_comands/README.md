A basic list Linux/Unix commands(this list will grow throughout class)
====

###Command : cat
 This command can be used to display the contents of a file on the screen.

#####Options:
* -b number non-blank output lines.
* -n number all output lines.
* -v displays nonprinting characters, except for tabs and the end of line character
* check man for more options.

#####Usage:

* cat file.txt will print the contents of file.txt .
* cat file.txt file2.txt > newfilecombined.txt combines the contents of the first and second file into newfilecombined.txt.

#####Links:
* [more on cat](https://en.wikipedia.org/wiki/Cat_%28Unix%29)

###Command : cd
Change directory.

#####Options:
* -p print.
* -v entries are printed one per line.
* check man for more options.

#####Usage:
* cd ~username will put you in the usernames home directory.
* cd .. will move you up one directory. So if you are in /var/www/html cd ../ will move you to /var/www.
* cd - will switch you to the previous directory.
* cd and then the path will switch you to that directory. So cd /etc/ssh will take you to the ssh directory.

#####Links:
* [more on cd](https://kb.iu.edu/d/afsk#cd)

###Command : cp
Copy a file.  

#####Options:
* -f (force) - specifies removal of the target file if it cannont be opened.
* -i (interactive) -prompts with the name of a file to be overwritten.
* -r (recursuve) - copy directories recursively.

#####Usage:
* cp sourceFile targetFile.
 
#####Links:
* [more on cp](http://www.tecmint.com/15-basic-ls-command-examples-in-linux/)


###Command : ls
List contents of directory.

#####Options:
* -a all files including hidden files.
* -R recursively list subdirectories.
* -h print sizes in human readable format.
* -l list directory information. 
* check man for more options.

#####Links:
* [more on ls](http://www.tecmint.com/15-basic-ls-command-examples-in-linux/)

###Command : mkdir
Make a directory.

#####Options:
* -p will also create all directories leading up to the given directory that do not exist already.
* -v display each directory that mkdir creates.
* -m specify the octal permissions of directories created by mkdir.
* man mkdir list more options and info about mkdir.

#####Links:
* [more on mkdir](http://www.basicconfig.com/linux/mkdir)

###Command : mv
Move. Can also be used to rename a file.

#####Options:
* -i interactive prompt user first.
* -f force overwritting the destination.

#####Usage:
* mv nameoffile /path/of/where/its/going.
* mv nameoffile newnameoffile.

#####Links:
* [more on mv](http://www.ee.surrey.ac.uk/Teaching/Unix/unix2.html)

###Command : pwd
Print working directory.

#####Usage:
* pwd   The path /var/www/html may be printed indicating that you are in the aforementioned directory.

###Command : rm
remove file(delete).

#####Usage:
* rm nameoffile deletes file.

#####Links:
* [more on rm](http://www.ee.surrey.ac.uk/Teaching/Unix/unix2.html)

###Command : touch
Create a file.

#####Options:
* -a change the access time only.
* -m change the modification time only.
* check man for more options.

#####Usage:
* touch nameOfFile.

#####Links:
* [more on touch](http://www.linfo.org/touch.html)




