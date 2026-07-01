def modsent(sentence):
    mod1 = sentence.replace(' ','-')
    return mod1

sentence = input("Enter the string:")
mod1 = modsent(sentence)

print(mod1)