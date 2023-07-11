'''

This files is meant for everything related with the user's account credentials.

Saves the checks and the Credentials. Use the SaveCredentials(Credentials) to save. Will only save if the
the credentials are valid.


'''

import re # More string functions


def ValidInfo(Credentials): # Validating info (parameters and not already existing)
    print("Validating info")
    RejecInputs = re.compile("[@_!#$%^&*()<>?/\|}{~:]")
    
    # Username(>4 characters / Special Characters / Empty)
    print("Checking username")
    if RejecInputs.search(Credentials["UserName"]) or not "" in str(Credentials["UserName"]): #special characters and emtpy field
        print("Calling warning")
        return("Invalid username, don't use special characters")

    elif len(str(Credentials["UserName"])) < 4: # 4 Minimum characters
        print("Calling warning")
        return("Username needs to be at least 4 characters")
    elif Credentials["UserName"] == "Admin": # Checks for admin
        return True
    

    print("Checking email")
    # Email(>3 characters / needs '@'and dot / Empty)
    if "@" not in Credentials["Email"] or not "" in Credentials["Email"] or not "." in Credentials["Email"]:
        print("Calling warning")
        return("Invalid Email")
    elif len(str(Credentials["Email"])) < 3:
        print("Calling warning")
        return("Email needs to have at least 3 characters")


##########################
#///////////////////////  <------ NEEDS WORK
    # Password(>4 characters / )
    #if RejecInputs.search(Credentials["Password"]) or "" in str(Credentials["UserName"]): #special characters and emtpy field
    #    Warning("Invalid username, don't use special characters") # Email
    #    ValidCred = False
    #    return
    #lif len(str(Credentials["UserName"])) < 4: # 4 Minimum characters
    #   Warning("Username needs to be at least 4 characters")
    #    ValidCred = False
    #    return
#///////////////////////  <------ NEEDS WORK
##########################

    # Check for existing credentials
    File = open(r'Credentials.txt', 'r')
    if File.read(): # If has content
        File.seek(0)
        Lines = File.readlines()
        for line in Lines:
            # Turns the string into Dictionary so it can be used to check
            DataBase = eval(line)
            if DataBase["UserName"] == Credentials["UserName"]:
                print("Calling warning")
                return("Username already being used")
            if DataBase["Email"] == Credentials["Email"]:
                print("Calling warning")
                return("Email already being used") #Change this if more checks are done
            return True
    else:
        return("File not found")



def SaveCredentials(Credentials):
    # Checks for file, if doesn't exist create one
    try:
        file = open(r'Credentials.txt', 'a')
        file.close
    except:
        print("Creating the txt file")
        file = open(r'Credentials.txt', 'w')
        file.close
        return True
    
    # Checks the credentails and then appends them to the txt
    print("Calling ValidInfo with: " + str(Credentials))
    Info = ValidInfo(Credentials)
    if Info == True:# If file exists and True
        print("Validated info")
        file = open(r'Credentials.txt', 'a')
        file.write(str(Credentials) +  "\n")
        file.close
        return True # Returns True to go to main
    elif isinstance(Info, str):
        return(Info) # Returns Warning