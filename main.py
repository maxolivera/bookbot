def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_num_chars(text)
    chars_dict_list = dict_to_list(chars_dict)
    chars_dict_list.sort(reverse=True, key=sort_on)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    
    for char_dict in chars_dict_list:
        char = char_dict["char"]
        times = char_dict["count"]
        print(f"The '{char}' character was found {times} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["count"]

def dict_to_list(dict):
    list = []
    for k in dict:
        list.append({"char": k, "count": dict[k]})
    return list

def get_num_chars(text):
    chars = {}
    for char in text:
       if not char.isalpha():
           continue
       low_char = char.lower()
       if low_char in chars:
            chars[low_char] += 1
       else:
            chars[low_char] = 1
    return chars

def get_num_words(text):
   words = text.split()
   return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
