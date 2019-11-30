from collections import defaultdict, Counter
from nltk import wordpunct_tokenize
import string

inv_index_database = defaultdict(set)
documents = []


def searching(word, number_of_res):
    """Search - Given a word, search for it
    and retrieve the top 10 paragraphs (Documents) that contain it"""
    try:
        present_in = sorted(
            inv_index_database.get(word.lower()), key=lambda x: x[1], reverse=True
        )
        results = [documents[i[0]] for i in present_in]
        return results[:number_of_res]
    except:
        return []


def processing(input_text):
    try:
        input_text = input_text[0].replace("\r", "")
        # comment above line to test ifmain

        paragraphs = input_text.split("\n\n")
        for i in range(len(paragraphs)):
            doc = list(
                map(
                    str.lower,
                    filter(lambda x: len(x) > 2, wordpunct_tokenize(paragraphs[i])),
                )
            )
            indexing(i, doc)
        documents.extend(paragraphs)
        return True
    except Exception as e:
        print(e)
        return False


def clear():
    """clear - Clear the index and all indexed documents"""
    inv_index_database.clear()
    documents.clear()


def indexing(ID, words, count=0):
    """index - Index a given document
    (After having split the input into paragraphs a.k.a document )"""
    c = Counter()
    ID += len(documents)
    for word in words:
        c[word] += 1
    for word in set(words):
        inv_index_database[word].add((ID, c.get(word)))


if __name__ == "__main__":
    # x = input("Enter paragraphs:")

    print("Uncomment to check")

    # x = "I am Ankur.\nI'm testing this thing.\n \
    # This thing should be in paragraph one too. \
    # \n\nBut this should be in para 2.\n\nLet's hope this is in para 3."
    # x1 = "This is para 1.\n\nThis is para 2."
    # processing(x)
    # processing(x1)
    # print(searching("para"))
    # print(searching("this"))

    # for i in range(1, 3):
    #     with open("./documents/d{}.txt".format(i)) as file:
    #         x = file.read()
    #
    #     # print(x.count('Moby')+x.count('moby'))
    #     splitting(x)
    #     # searching('Maecenas')
    #     with open("./inputs/i{}.txt".format(i)) as file:
    #         inp = map(lambda x: x[:-1], file.readlines())
    #     # print(inp)
    #     for each in inp:
    #         print(searching(each))
    #     clear()
