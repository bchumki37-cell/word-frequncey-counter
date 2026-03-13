string =input("Give your text :")
text = string.strip().lower()
text = text.replace(","," ").replace("."," ").replace("?"," ")
words = text.split()
for word in words:
    print(words.count(word))