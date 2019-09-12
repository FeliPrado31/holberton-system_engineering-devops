# My name is Betty 
Create a script that changes your user ID to betty.
```bash
#!/bin/bash
su - betty
```
# Who am i
Write a script that prints the effective userid of the current user.
```bash
#!/bin/bash
whoami
```
# Groups
Write a script that prints all the groups the current user is part of.
```bash
#!/bin/bash
groups
```
# New Owner
Write a script that changes the owner of the file hello to the user betty.
```bash
#!/bin/bash
chown betty hello
```
# Empty!
Write a script that creates an empty file called hello.
```bash
#!/bin/bash
touch hello
```
# Execute
Write a script that adds execute permission to the owner of the file hello.
```bash
#!/bin/bash
chmod u+x hello
```
