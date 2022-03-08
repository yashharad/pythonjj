introString=input("Please enter the string")
characterCount=0
wordcount=1
for i in introString:
    characterCount=characterCount+1
    if(i==" "):
        wordCount=wordcount+1

print("number of word in the string")
print(wordcount)
print("number of characters in the string")
print(characterCount)
