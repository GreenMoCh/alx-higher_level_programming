#!/usr/bin/python3
def text_identation(text):
    """
    Prints text with 2 new lines after each '.', '?' and ':' chars

    Args:
        text: the input text

    Raises:
        TypeError: if 'text' is not a str
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    sentences = []
    current_sentence = ""
    for char in text:
        if char in ['.', '?', ':']:
            sentences.append(current_sentence)
            current_sentence = ""
        else:
            current_sentence += char
    if current_sentence:
        sentences.append(current_sentence)
    for sentence in sentences:
        print(sentence.strip())
        print()
