import re

def slug_text(text):
    text = text.replace(' ', '-')
    text = re.sub("[^\w\-]", "", text)
    return text

print(slug_text("h^&e ll`.,|o w]{+o rld1234 5"))