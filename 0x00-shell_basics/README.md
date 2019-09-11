# Where am i?
command use for show the current directory working.
```bash
#!/bin/bash
pwd
```
# What's in there?
command to list of your current directory.
```bash
#!/bin/bash
ls
```
# There is no place like home
Write a script that changes the working directory to the user’s home directory.
```bash
#!/bin/bash
cd
```
# The long format
display contents in a long format
```bash
#!/bin/bash
ls -al
```
# Hidden files
including all hidden files
```bash
#!/bin/bash
ls -a
```
# I love numbers
Display current directory contents.
```bash
#!/bin/bash
ls -al -1
```
ve the file betty from /tmp/ to /tmp/holberton.
# Welcome holberton
creates a directory named holberton in the /tmp/ directory.
```bash
#!/bin/bash
mkdir /tmp/holberton
```
# Betty in Holberton
Move the file betty from /tmp/ to /tmp/holberton.
```bash
#!/bin/bash
mv betty /tmp/holberton/
```
# Bye bye betty
Delete the file betty.
```bash
#!/bin/bash
rm /tmp/holberton/betty
```
# Bye bye holberton
Delete the directory holberton that is in the /tmp directory.
```bash
#!/bin/bash
rmdir /tmp/holberton/
```
# Back to the future
Write a script that changes the working directory to the previous one.
```bash
#!/bin/bash
cd -
```
# Lists
Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.
```bash
#!/bin/bash
ls . ~/github/holberton-system_engineering-devops /boot  -al -1
```
