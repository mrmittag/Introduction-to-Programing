A basic list Linux/Unix commands(this list will grow throughout class)
====

###Command : cd
Change directory
#####Options:
* -p print
* -v entries are printed one per line
* check man for more options
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
* cp sourceFile targetFile 
#####Links:
* [more on cp](http://www.tecmint.com/15-basic-ls-command-examples-in-linux/)


###Command : ls
List contents of directory
#####Options:
* -a all files including hidden files
* -R recursively list subdirectories
* -h print sizes in human readable format
* -l list directory information. 
* check man for more options for example man ls
#####Links:
* [more on ls](http://www.tecmint.com/15-basic-ls-command-examples-in-linux/)


###Command : touch
Create a file.
#####Options:
* -a change the access time only.
* -m change the modification time only.
* check man for more options for example man touch
#####Usage:
* touch nameOfFile
#####Links:
* [more on touch](http://www.linfo.org/touch.html)


