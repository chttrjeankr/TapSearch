from collections import defaultdict

database = defaultdict(set)

def searching(word="something"):
    '''Search - Given a word, search for it
    and retrieve the top 10 paragraphs (Documents) that contain it'''
    return database[word]

def splitting(input_text):
    paragraphs = input_text.split('\n\n')
    # document = {}
    # print(paragraphs)
    for i in range(len(paragraphs)):
        document = set(map(str.lower, paragraphs[i].split()))
        # document[i] = {lower(word) for word in document}
        # print(document)
        indexing(i,document)
    # print()

def clear():
    '''clear - Clear the index and all indexed documents'''
    database.clear()
    print("Database cleared")

def indexing(ID, words):
    '''index - Index a given document
    (After having split the input into paragraphs a.k.a document )'''
    for word in words:
        database[word].add(ID)

if __name__ == '__main__':
    # x = input("Enter paragraphs:")

    # x = "I am Ankur.\nI'm testing this thing.\n \
    # This thing should be in paragraph one too. \
    # \n\nBut this should be in para 2.\n\nLet's hope this is in para 3."

    for i in range(1,3):
        with open('./documents/d{}.txt'.format(i)) as file:
            x = file.read()

        # print(x.count('Moby')+x.count('moby'))
        splitting(x)
        # searching('Maecenas')
        with open('./inputs/i{}.txt'.format(i)) as file:
            inp = map(lambda x: x[:-1].lower(), file.readlines())
        # print(inp)
        for each in inp:
            print(searching(each))
        clear()
