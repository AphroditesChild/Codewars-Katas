def alphabet_position(text):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    return " ".join([str(abc.index(i.lower())+1) for i in text if i.lower() in abc])
