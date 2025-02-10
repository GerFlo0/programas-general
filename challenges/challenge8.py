def count_words(string = str):
    string = [x for x in string.split() if x != " "]
    for i in range(len(string)): string[i] = "".join(char for char in string[i] if char.isalnum())
    print(string)
    return dict((wrd, string.count(wrd)) for wrd in string)

txt = "magica/ Hola. magica/ Hola. caracola, Hola."
print(txt)
print(count_words(txt))