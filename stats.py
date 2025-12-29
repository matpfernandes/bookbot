def words_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    characters = {}
    for c in text.lower():
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1

    return characters

def sort_on(item):
    return item['num']

def order_characters(characters):
    to_order = []

    for key, value in characters.items():
        to_order.append({"char": key, "num": value})
    
    to_order.sort(reverse=True, key=sort_on)
    
    return to_order
    