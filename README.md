# TapSearch

It takes in multiple paragraphs of text, assigns a unique ID to each paragraph and stores the words to paragraph mappings on an inverted index. This paragraph can also be referred to as a `document`. This is similar to what elasticsearch does.

Given a word to search for, it lists out the top 10 paragraphs in which the word is present.

## To read the app testing instructions, go to [SETUP.md](./SETUP.md)

## `SEARCH`

To search for a particular word in documents. The results would return `documents` (paragraphs) which contain the word. Searching is not case sensitive. Retrieves top 10 results by default providing a field for user to request for more results.

## `INPUT TEXT`

To provide input to the database which is to be indexed. The text field takes input and defines a `document` (paragraph) by two newline characters. Further inputs add on to the database unless `CLEAR` is executed.

## `DATABASE`

To view the an exhaustive list of `documents` indexed in the database.

## `CLEAR`

To remove all the indexed `documents` and flush the existing database.

### **P.S.**

**Indexing** happens by ignoring words which have less than 3 characters in it, which automatically counts in punctuation and numbers. This makes the database cleaner and more efficient. Indexes provided to the documents are nothing but integral indices denoting their position in a list of documents.
