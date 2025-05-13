

message=input(">")
words=message.split(' ')
emojis={
    ":)":"k",
    ":(":"s"
}

output=""
for word in words:
    output+=emojis.get(word,word)+" "
print(output)

