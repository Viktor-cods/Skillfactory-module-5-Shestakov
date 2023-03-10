from django import templates

register=templates.Library()

@register.filter()
def censor(text):
    bad='чеснок'

    for word in text.split():
        if word.lower() in bad:
            text = text.replace(word,f"{word[0]}{'*'* (len(word)-1)}")
        return text
