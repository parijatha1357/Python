print ("Enter your username: ")
username = input()
print ('Hello ' + username+'!')
print ('Also, type your password')
password = input()

if username == "paaru" or        password == "paaru123":
    print("success! You will be redirected to login page.")
else:
    print ("Incorrect username or password")
    print ('Your password hint is your username without @gmail.com')