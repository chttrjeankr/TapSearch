from collections import defaultdict, Counter
from nltk import wordpunct_tokenize
import string

inv_index_database = defaultdict(set)
documents = []


def searching(word, number_of_res):
    """
    Search - Given a word, search for it
    and retrieve the top 10 paragraphs (Documents) that contain it
    """
    try:
        present_in = sorted(
            inv_index_database.get(word.lower()), key=lambda x: x[1], reverse=True
        )
        results = [documents[i[0]] for i in present_in]
        return results[:number_of_res]
    except:
        return []


def processing(input_text):
    """
    Preprocesses the raw input data into separate paragraphs to index accordingly.
    Indexing function is called from within here to ensure clean database.
    """
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
    """
    clear - Clear the index and all indexed documents
    """
    inv_index_database.clear()
    documents.clear()


def indexing(ID, words, count=0):
    """
    index - Index a given document
    (After having split the input into paragraphs a.k.a document )
    """
    c = Counter()
    ID += len(documents)
    for word in words:
        c[word] += 1
    for word in set(words):
        inv_index_database[word].add((ID, c.get(word)))
