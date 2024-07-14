#counting number of uppercase and lowercase letters.
def count_of_letters(words):
  count1=0
  count2=0
  for i in words:
    if i.isupper():
      count1=count1+1
    else:
      count2=count2+1
  return (count1,count2)
x=input()
print(count_of_letters(x))
