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
# Multiple permissions
Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.
```bash
#!/bin/bash
chmod 554 hello
```
# Everybody!
Write a script that adds execution permission to the owner, the group owner and the other users, to the file hello
```bash
#!/bin/bash
chmod 751 hello
```
Write a script that sets the permission to the file hello as follows:
* Owner: no permission at all
* Group: no permission at all
* Other users: all the permissions
```bash
#!/bin/bash
chmod 7 hello
```
# Look in the mirror
Write a script that sets the mode of the file hello the same as olleh’s mode.
* The file hello will be in the working directory
* The file olleh will be in the working directory
```bash
#!/bin/bash
chmod --reference=olleh hello
```