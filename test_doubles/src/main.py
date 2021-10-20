import requests

def add(x, y):
    return x + y

def multiply(x, y):
    """未完成"""
    return None

def sample():
    result_add = add(2, 4)
    result_add_multiply = multiply(result_add, 2)

    return result_add_multiply

def read_file(f, path):
    print("READING ALL FILE")
    return f.read(path)

# 依存性を持った箇所
def most_common_word_in_web_page(words, url, user_agent=requests):
    """
    finds the most common word from a list of words
    in a web page, identified by its URL
    """
    response = user_agent.get(url)
    return most_common_word(words, response.text)

# 依存性を持った箇所
def most_common_word_in_web_page2(words, url):
    """
    finds the most common word from a list of words
    in a web page, identified by its URL
    """
    response = requests.get(url)
    return most_common_word(words, response.text)
    
# 依存性を持っていない箇所
def most_common_word(words, text):
    """
    finds the most common word from a list of words
    in a piece of text
    """
    word_frequency = {w: text.count(w) for w in words}
    return sorted(words, key=word_frequency.get)[-1]

if __name__ == '__main__':
    most_common = most_common_word_in_web_page(
        ['python', 'Python', 'programming'],
        'https://python.org/',
    )
    print(most_common)