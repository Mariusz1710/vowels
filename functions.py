def del_vow(txt):
    txt = txt.lower()
    vowels = ['a','ą','e','ę','i','o','ó','u','y']
    new = txt

    for ch in txt:
        if ch in vowels:
            new = new.replace(ch, '')
    return new

def del_con(txt):
    txt = txt.lower()
    consonants = ['b','c','ć','d','f','g','h','j','k','l','ł','m','n','p','q','r','s','t','v','w','x','z','ź','ż']
    new = txt

    for ch in txt:
        if ch in consonants:
            new = new.replace(ch,'')
    return new