


def emoji_converter(message3):
    message3 = input(">")
    words = message3.split(' ')
    emojis = {
        ":)": "k",
        ":(": "s"
    }

    output = ""
    for word in words:
        output += emojis.get(word, word) + " "

message=input(">")
print(emoji_converter(message3))
