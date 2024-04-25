# Measure similarity between two sentences using nlp

**about of Algorithm :)**

**What is cosine similarity?**

Cosine similarity measures the similarity between two vectors by calculating the cosine of the angle between the two vectors.

Cosine similarity is one of the most widely used and powerful similarity measure in Data Science. It is used in multiple applications such as finding similar documents in NLP, information retrieval, finding similar sequence to a DNA in bioinformatics, detecting plagiarism and may more.
---
Cosine similarity is calculated as follows,


![image](https://user-images.githubusercontent.com/89921883/222828696-34e16e00-1a7d-4d5f-8bb5-46b910e6d699.png)


![image](https://user-images.githubusercontent.com/89921883/222828617-2d8fcbe1-d733-4b81-96bf-9052ffc7005f.png)
---

Why cosine of the angle between A and B gives us the similarity?

If you look at the cosine function, it is 1 at theta = 0 and -1 at theta = 180, that means for two overlapping vectors cosine will be the highest and lowest for two exactly opposite vectors. You can consider 1-cosine as distance.


![image](https://user-images.githubusercontent.com/89921883/222829259-e4bb4b5a-1725-4dc8-9490-159f42e12a64.png)

![image](https://user-images.githubusercontent.com/89921883/222829194-dabc4f9b-9ac7-44e4-a397-739ed2c45400.png)


---

How to calculate it in Python?

The numerator of the formula is the dot product of the two vectors and denominator is the product of L2 norm of both the vectors. Dot product of two vectors is the sum of element wise multiplication of the vectors and L2 norm is the square root of sum of squares of elements of a vector.

We can either use inbuilt functions in Numpy library to calculate dot product and L2 norm of the vectors and put it in the formula or directly use the cosine_similarity from sklearn.metrics.pairwise. Consider two vectors A and B in 2-D, following code calculates the cosine similarity,



---------------------------------------------------



**about of data set :)**
![image](https://user-images.githubusercontent.com/89921883/224299236-ab11fe15-8006-4272-bd84-f0be24436061.png)

These are given by Wikipedia 

On Mehsa Amini's Wikipedia page, first copy the first paragraph([text1](https://github.com/parvvaresh))
translate it into Farsi using Google Translate, and then translate it again into English.([text2](https://github.com/parvvaresh))

Intuitively, the two texts were different, and the percentage of similarity between the two texts was 71% (according to the algorithm).



![image](https://user-images.githubusercontent.com/89921883/224300881-47e5768e-ce91-4368-b410-d5e0f6b18366.png)



------------------------

Follow me on virtual pages : 


[![Twitter Badge](https://img.shields.io/badge/-Twitter-1da1f2?style=flat-square&labelColor=1da1f2&logo=twitter&logoColor=white&link=https://twitter.com/Yaronzz)](https://twitter.com/parvvaresh)
[![Email Badge](https://img.shields.io/badge/-Email-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:yaronhuang@foxmail.com)](mailto:parvvaresh@gmail.com)
[![Instagram Badge](https://img.shields.io/badge/-Instagram-purple?style=flat&logo=instagram&logoColor=white&link=https://instagram.com/parvvaresh/)](https://space.bilibili.com/7708412)
[![Github Badge](https://img.shields.io/badge/-Github-232323?style=flat-square&logo=Github&logoColor=white&link=https://space.bilibili.com/7708412)](https://github.com/parvvaresh)
