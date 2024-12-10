'''
Write a program that takes two numbers x and y as user inputs. The inputs must be
taken so that the value of y must be greater than the value of x (y > x). Next, the
program will print the square of all the numbers starting from x all the way up to y.
After reaching this range, the program will print “END”.
'''



x, y = map(int, input().split())  # Prompt the user to input two space-separated integers and assign them to variables x and y

if x == y:  # Check if x is equal to y
    print('END')  # If x is equal to y, print 'END'
else:
    while x <= y:  # Execute the block of code as long as x is less than or equal to y
        print(x * x, end=' ')  # Print the square of x followed by a space
        x += 1  # Increment the value of x by 1 in each iteration
    else:
        print('END')  # Print 'END' after the while loop is finished
    
    # Or
    # print('END')
