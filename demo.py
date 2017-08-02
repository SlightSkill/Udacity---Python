# Use string slicing to store everything before "NOUN" in substring1,
# everything after "NOUN" and before "VERB" in substring2, and everything after "VERB"
# in substring3.

sentence = "A NOUN went on a walk. It can VERB really fast."
substring1 = sentence[:2]
substring2 = sentence[6:30]
substring3 = sentence[34:]

noun_replacement = "apple" # your noun here
verb_replacement = "fall" # your verb here

new_sentence = ""
new_sentence += substring1
new_sentence += noun_replacement
new_sentence += substring2
new_sentence += verb_replacement
new_sentence += substring3

print new_sentence
