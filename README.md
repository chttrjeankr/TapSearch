## Coding Challenge:

You are to build a simple program called TapSearch that achieves these objectives.

It takes in multiple paragraphs of text, assigns a unique ID To each paragraph and stores the words to paragraph mappings on an inverted index. This is similar to what elasticsearch does. This paragraph can also be referred to as a ‘document’

Given a word to search for, it lists out the top 10 paragraphs in which the word is present



Few points to consider

- Tokenize to words by splitting at whitespace

- Convert all words to lowercase

- Index these words against the documents they are from

- Generate a unique ID for every document that is index

- A paragraph is defined by two newline characters



TapSearch APIs you’ll need to  build

- clear - Clear the index and all indexed documents

- index - Index a given document (After having split the input into paragraphs a.k.a document )

- Search - Given a word, search for it and retrieve the top 10 paragraphs (Documents) that contain it



If you successfully create an Inverted Index, Your code will be judged primarily on:

**Performance**: What we love about Elasticsearch is it’s speed while search for words through an inverted index.

**Coding style** - How good are your abstraction and overall architecture. Is your code readable and maintainable? We believe that well-written code requires little to no documentation.

Your code must be hosted on the cloud, please ONLY use Heroku that is available free of cost. It must have a basic frontend that lets us input text and submit it to be indexed, and another that simple piece of UI that lets us search for top 10 documents given a word.



What exactly you have to put in for your submission.

- Link to Cloud deployment

- Link to the Github Repo

- A Readme file in the repo that briefly explains how to use TapSearch

- Your grand Vision. Where would you take this project if you had a tech arsenal at your disposal?

- Sample Inputs and Outputs that you have personally tested the program on



If you think this isn’t challenging enough for you, here are two bonus questions to really let you stick out among your peers.



### Bonus 1

Add the functionality to upload PDFs and index them. The uploaded PDFs are first parsed into text and then indexed as a document. Given a word to search, return the top 10 matches with the ability to download the PDF



### Bonus 2

Add the functionality to upload Images and index them after feature extraction. Given an image to search for, your program must return the top 10 images that look similar to the image I searched for - very similar to Google search by Image.



### A few general notes

- Your code must be hosted on the cloud

- You will provide instruction to accurately test your app in the Readme

- You may use whatever language you want to. Only performance and accuracy matters.

### Please Note

A preprocessing function is called before the Index function that splits the user submission to index at paragraphs and index each paragraph as a separate document.
