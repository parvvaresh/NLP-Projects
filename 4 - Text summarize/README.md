# NLP text summarizer from scratch

## What is a text summarizer?
NLP text summarizer is one of the cool applications of NLP(Natural Language Processing), which shortens the long document into shorter while retaining all important information from the document.

## Idea behind this project
So how are we gonna do this? Actually, there are lots of ways we can do this but today I will show you the most basic and easy version of NLP text summarizer, which you can create by yourself very easily. So, below are the steps we are going to perform

---

### Steps
1.  After loading the data we will create two copy of the data, one for word vector and another one for sentence vector
2.  On the word vector data, we will first clean it by removing all useless elements like stopwords, punctuation marks, etc.
3.  Then we will Tokenize the word vectorizer (split each word) and create a count vector out of it. If you don’t know what count vectorizer is then here’s the thing, count vectorizer extracts all the unique words from the text(sentence/paragraph/document) and then creates a word matrix where each unique word is plotted as columns and each unique text as a row. So this matrix represents the number of occurrences of each word in a document, you can see this in the image below

Now in case, you got a question, why do we do this weird stuff? It is because it helps us find the most used word which actually turns out to be an important word or word which adds the most value to a document.


4.  After calculating the count vectorizer we will move to the second part of the process which is handling sentence vectors. Here we will not remove stopwords and punctuation marks because if we do, then we won’t be able to read the document as normally as we do.
So, here we will create a sentence vector, which is nothing but a vector of a sentence (list of all unique sentence)

5.  Now here comes the most important part. In this step, we will score each sentence by taking out each word of the sentence and checking its score from the word vectorizer, and then we will sum up all the values of words available in a particular sentence.

After doing that we will have a score for all sentences, which we will use to filter out the most important sentence from the document.

6. In this final step, we will create the actual summary of the document, here we will create a threshold score like a score of 1.5xaverage of sentence score and we will choose any sentence for the threshold only if it passes the threshold.
The threshold can be anything you can tweak it by yourself to find out how much shorter summary best fits you.


------------------------

Follow me on virtual pages : 


[![Twitter Badge](https://img.shields.io/badge/-Twitter-1da1f2?style=flat-square&labelColor=1da1f2&logo=twitter&logoColor=white&link=https://twitter.com/Yaronzz)](https://twitter.com/parvvaresh)
[![Email Badge](https://img.shields.io/badge/-Email-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:yaronhuang@foxmail.com)](mailto:parvvaresh@gmail.com)
[![Instagram Badge](https://img.shields.io/badge/-Instagram-purple?style=flat&logo=instagram&logoColor=white&link=https://instagram.com/parvvaresh/)](https://space.bilibili.com/7708412)
[![Github Badge](https://img.shields.io/badge/-Github-232323?style=flat-square&logo=Github&logoColor=white&link=https://space.bilibili.com/7708412)](https://github.com/parvvaresh)
