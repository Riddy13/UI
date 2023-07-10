File = open(r'./Credentials.txt', 'r')

if File.read():
    print(True)
else:
    print(False)