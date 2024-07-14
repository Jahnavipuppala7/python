'''add "ing" at the end of the given string if length is more than 3 
if the given string already ends with "ing" then add "ly"
if the length is less than 3 leave it unchanged'''
string=input()
y="ly"
z="ing"
if len(string)>3:
  if string[-3:]=="ing":
    print(string+y)
  else:
    print(string+z)
else:
  print(string)
