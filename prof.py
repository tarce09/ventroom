!pip install better-profanity

from better_profanity import profanity

def prof_filter(t):
  profanity.load_censor_words()
  return profanity.censor(t)

