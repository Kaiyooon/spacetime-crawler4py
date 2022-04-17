# Jake's PartA tokenizer
# Please replace with yours if it is faster!


def tokenize(theTextFile):
    # Code from outside sources for handling exceptions:
    # https://betterprogramming.pub/handling-errors-in-python-9f1b32952423
    try:
        # Code used from outside source for file operations:
        # https://www.tutorialspoint.com/python/python_files_io.htm
        #
        # Open the file as read only
        theFile = open(theTextFile,"r")

    # I learned about this exception here:
    # https://www.section.io/engineering-education/files-and-exceptions-in-python/
    except FileNotFoundError:
        # This exception will execute if the user enters a file, but it cannot be found.
        #
        # During discussion session, Qi said we shouldn't be printing anything
        # to console otherwise the autograder would break, so this exception simply exists
        # to denote that it should be accounted for in an actual program.
        #
        # Outside code used to quit program:
        # https://pythonguides.com/python-exit-command/
        quit()

    # General exception
    except Exception:
        # During discussion session, Qi said we shouldn't be printing anything
        # to console otherwise the autograder would break, so this exception simply exists
        # to denote that it should be accounted for in an actual program.
        #
        # Outside code used to quit program:
        # https://pythonguides.com/python-exit-command/
        quit()

    # Outside code used to learn about lists
    # https://www.tutorialspoint.com/python/python_lists.htm
    #
    # This will store the tokens
    tokens = []

    # Outside code used for while loop structure:
    # https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/
    #
    # While loop to read each line of the file
    while True:
        # Code from outside sources for handling exceptions:
        # https://betterprogramming.pub/handling-errors-in-python-9f1b32952423
        try:
            # Outside code used for the below file operations:
            # https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/
            #
            # This will read each line from the file
            fileLine = theFile.readline()
        except IndexError:
            # For if there are issues parsing the file lines.
            #
            # During discussion session, Qi said we shouldn't be printing anything
            # to console otherwise the autograder would break, so this exception simply exists
            # to denote that it should be accounted for in an actual program.
            #
            # Outside code used to quit program:
            # https://pythonguides.com/python-exit-command/
            quit()
        except Exception:
            # During discussion session, Qi said we shouldn't be printing anything
            # to console otherwise the autograder would break, so this exception simply exists
            # to denote that it should be accounted for in an actual program.
            #
            # Outside code used to quit program:
            # https://pythonguides.com/python-exit-command/
            quit()

        # Used through outside code referenced above (file operations).
        #
        # This is executed when there's no more lines in the file
        if not fileLine:
            # Used through outside code referenced above (file operations).
            #
            # This breaks out of the while loop so that the below operations do not occur on a line that does not exist
            break

        # Outside code used for the regular expression:
        # https://www.tutorialspoint.com/What-is-the-Python-regular-expression-to-check-if-a-string-is-alphanumeric
        #
        # Outside code used for the asterisk:
        # https://docs.python.org/3/howto/regex.html
        #
        # Code from outside source for regular expressions:
        # https://www.tutorialspoint.com/python/python_reg_expressions.htm
        #
        # Outside code used for findall()
        # https://www.pythontutorial.net/python-regex/python-regex-findall/
        matchObjectTwo = re.findall('[a-zA-Z0-9]*',fileLine,re.I)

        # Outside code for using the range() to loop through indices:
        # https://www.w3schools.com/python/python_lists_loop.asp
        #
        # Clean up the matchObjectTwo list and move to the tokens list
        for index in range(len(matchObjectTwo)):
            # Executes if the token is alphanumeric
            # This is because non-alphanumeric tokens are converted to blank strings.
            if (matchObjectTwo[index] != ""):
                # Outside code used for .lower():
                # https://www.w3schools.com/python/ref_string_lower.asp
                #
                # Clean up the matchObjectTwo list by making all uppercase, lowercase.
                matchObjectTwo[index] = matchObjectTwo[index].lower()
                # Code from outside source for appending string to a list:
                # https://www.geeksforgeeks.org/python-append-string-to-list/
                #
                # Puts the token into the tokens list
                tokens.append(matchObjectTwo[index])

    # Outside code used for the below file operations:
    # https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/
    #
    # Close the file
    theFile.close()

    # Outside code used to help with return values for methods:
    # https://www.geeksforgeeks.org/python-return-statement/
    #
    # Return the list of tokens
    return tokens
