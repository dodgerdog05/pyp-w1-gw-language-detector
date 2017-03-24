def detect_language(text, languages):
    """Returns the detected language of given text."""
    split_text = text.split()
    words = {}

    for language in languages:
        words[language['name']] = 0
        for word in language['common_words']:
            words[language['name']] += split_text.count(word)

    
    return max(words.keys(), key=(lambda x: words[x]))
