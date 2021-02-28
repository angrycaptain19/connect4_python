#!/usr/local/bin/python3

import cgi, cgitb
cgitb.enable()   

print ("Content-type: text/html\n")

formInfo = cgi.FieldStorage()
submit = formInfo.getvalue("submit")
first = formInfo.getvalue("first")


print ("The first name is {}<br>".format( first ))
print ("The name of the submit button was {}<br>".format(submit))

if submit == "Don't ever click me!":
    for i in range(1000000):
        print ("AAAAHHH!")
