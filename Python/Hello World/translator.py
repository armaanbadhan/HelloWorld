# giraffe language
# turns every vowel to f
# dog -> dfg
# cat -> cft


def translator(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "F"
            else:
                translation = translation + "f"
        else:
            translation = translation + letter
    return translation


print(translator(input("Enter a word to translate: ")))
