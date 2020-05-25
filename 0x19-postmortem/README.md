# 0x19. Post mortem 📜

## Overview

The goal of this project was to write a postmortem based on a lived project or case. Everything that will be seen below was invented in order to learn how to write them.


# Apache2 Postmortem

## Issue Summary 📄

Last week we detected failures in the web server after merge to the master with the new spring, as a result users could not access the page. This led to complaints and low traffic for a few hours. It is estimated that only new users were affected and some others who emptied their browser cache. The main cause is associated with an apache2 configuration file. It seems that they mistyped the name of the file.

## Timeline 🕤

* 05/19 09:10 GMT-5 First complaint from a user
* 05/19 09:12 GMT-5 Devops engineers begin testing to detect what may be going wrong
* 05/19 09:20 GMT-5 With the help of STRACE they start local testing by making requests.
* 05/19 09:20 GMT-5 With the help of STRACE they start local testing by making requests.
* 05/19 09:25 GMT-5 An ID was found that made some calls to the system
* 05/19 09:40 GMT-5 The problem was found to be associated with the Apache2 process
* 05/19 09:50 GMT-5 With the help of cURl the error log shows that the file called locale-wp.phpp did not exist
* 05/19 10:00 GMT-5 The file that called that non-existent file was corrected, tests were performed and the error in master was corrected 

## Root Cause 🔧

The problem first became apparent on Tuesday, 05/19. After testing STRACE with some GEt requests, and observing the error logs, DevOps engineers found the problem of a file that did not exist, which made the service unable to start, causing an error and leaving the website unusable. By human intervention in the file wp-settings.php pointed to a non-existent file. The problem was fixed by changing the file to its real name.

## Preventative Measures 📊

To reduce the frequency of this type of problem the files that are uploaded will have to be reviewed and well documented in the pull requests.


* Add tools that monitor the website every 5 minutes

## Author ⌨️

Juan Felipe Cubillos Prado