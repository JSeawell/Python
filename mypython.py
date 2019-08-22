'''

Name: Jake Seawell
Date: 7/9/19
Assignment: CS-344 - Program Py
Description: 

This python program creates 3 new files,
generates and a random string of 10 lowercase alphabetic
characters in each file, followed by a newline character,
and prints the contents of each file to the console.

Then, two random integers from 1-46 (inclusive) are
generated and printed to the screen, followed by the
product of the two integers.

'''

#Libraries Needed
import random
import string

#Length of character string
strLen =10

#Random LowerCase String Function 
def randLCstr(strLen):
    #get all lowercase letters
    allLowers = string.ascii_lowercase
    #choose 10 letters from allLowers, and join in result
    result = ''.join(random.choice(allLowers) for i in range(strLen))
    return result

#In loop, create 3 new files, put a randLCstring in each,
#print the string to the console, then close the file
for i in xrange(3):
    f= open("newFile_"+`i+1`+".txt","w")
    string1 =randLCstr(strLen)
    f.write(string1)
    f.write("\n")
    print (string1)
    f.close()

#Generate random 2 number integers from 1-42 (inclusive)
randInt1 = random.randint(0,43)
randInt2 = random.randint(0,43)
#calculate the product
productOfInts = randInt1 * randInt2

#Print integers and product to console
print(randInt1)
print(randInt2)
print(productOfInts)
