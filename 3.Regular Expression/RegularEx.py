import re

#method1 most directly
def plural(noun):
    if re.search('[sxz]$', noun):
        return re.sub('$', 'es', noun)
    elif re.search('[^aeioudgkprt]h$', noun):
        return re.sub('$', 'es', noun)
    elif re.search('[^aeiou]y$', noun):
        return re.sub('y$', 'ies', noun)
    else: return noun + 's'

#method2 more efficient but need time to write
def match_sxz(noun): return re.search('[sxz]$', noun)
def apply_sxz(noun): return re.sub('$', 'es', noun)
def match_h(noun): return re.search('[^aeioudgkprt]h$', noun)
def apply_h(noun): return re.sub('$', 'es', noun)
def match_y(noun): return re.search('[^aeiou]y$', noun)
def apply_y(noun): return re.sub('y$', 'ies', noun)
def match_default(noun): return True
def apply_default(noun): return noun + 's'

rules = ((match_sxz, apply_sxz), (match_h, apply_h), (match_y, apply_y),
(match_default, apply_default))
def plural2(noun):
    for matches_rule, apply_rule in rules:
        if(matches_rule(noun)):
            return apply_rule(noun)

#Closure for write rules instead of doing them manualy because 
#bored and slow

def build_match_and_apply_function(pattern, search, replace):
    #to show how to done with function
    def matches_rule(word):
        return re.search(pattern, word)
    #to show it's doable with lambda too
    apply_rule = lambda word : re.sub(search, replace, word)
    return (matches_rule, apply_rule)
patterns = (\
    ('[sxz]$', '$', 'es'), ('[^aeioudgkprt]h$', '$', 'es'), 
    ('(qu|[^aeiou])y$', 'y$', 'ies'), ('$', '$', 's')
)


def plural3(noun):
    for matches_rule, apply_rule in rules_auto_bild:
        if(matches_rule(noun)):
            return apply_rule(noun)

rules_auto_bild = [build_match_and_apply_function(pattern, search, replace) \
    for (pattern, search, replace) in patterns]
if __name__ == "__main__":
    #give a word, convert it to plural
    print(plural("askdjwky"))
    print(plural2("aksjdwijdi"))
    print(plural3('askdjwkjda'))
