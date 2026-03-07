sariki = {

        "hello": "salam",
        "goodbye": "salaam",
        "please": "meherbani",
        "thank you": "shukriya",
        "yes": "gia",
        "no": "ko",
        "friend": "sangti",
        "family": "tbar",
        "love": "mohabbat",
        "peace": "aman",
        "my" : "meda"

}

word = (input("Enter a word in English: ").lower())

print(f'The meaning of the word is "{sariki.get(word, "word not found in the dictionary")}"')

