from django import template


register = template.Library()

@register.filter()
def censor(text, bad_words):
      for word in bad_words:
      text = text.replace(word, '*' * len(word))
      return text
      title = "This is a bad example"
      text = "This is a bad example of using bad words in the text"
      bad_words = ["bad", "example"]
      censored_title = censor(title, bad_words)
      censored_text = censor(text, bad_words)
      print(censored_title)
      print(censored_text)