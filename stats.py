def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    count_char = {}
    for char in text.lower():
        if char in count_char:
            count_char[char] += 1
        else:
            count_char[char] = 1
    return count_char

def sort_on(dict):
    return dict["num"]

def sort_dict(char_dict):
    sorted_list = []
    for key in char_dict:
        sorted_list.append({"char": key, "num": char_dict[key]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

    