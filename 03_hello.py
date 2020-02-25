#print
name = "Ed"
message = name + ' said to me "i will see you later"'
print(message)

#Ask for name
name = input("What is your name?: ")
print(name)

#Ask for age
age = input("What is your age?: ")
print(age)

#Ask for age
song_fav = input("What is your fav ed song?: ")
print(song_fav)

#Create output text
string = "Your name is {} and you age is {}. Your fav song of ed is {}"
output = string.format(name,age,song_fav)
#print
print(output)