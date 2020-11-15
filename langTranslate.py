from googletrans import Translator

def e2t(s):
    t = Translator()
    result = t.translate(s,des='ta')
    return result.text

def t2e(s):
    t = Translator()
    result = t.translate(s,des='en')
    return result.text