# resume classification

Clean the data first

Things like : 
*  removing punctuation marks
*  Remove links and...
*  tokenize
*  Stemmer

---
Chart of 10 words that have been repeated the most :


![image](https://github.com/parvvaresh/resume-classification/assets/89921883/17719721-b730-4879-af84-dd8a05325aba)

word cloud :


![image](https://github.com/parvvaresh/resume-classification/assets/89921883/91e7b2e4-7f4f-46c3-bf41-31409c5e91fe)

---

Job titles :‌ 

![image](https://github.com/parvvaresh/resume-classification/assets/89921883/6aa623d3-1541-4c7d-a818-2fa6e84b58fb)


![image](https://github.com/parvvaresh/resume-classification/assets/89921883/08ac5a11-5575-4c13-b027-c498f5d79dbc)

---
Vectorized by **tf-idf** and **freq-word** algorithms and for **tf-idf** use **ch2** for select best feature.


By algorithms

*  KNN
*  Native bayesn
*  descion tree
*  random forest
  
classifiction the resumes


| name of ALG | accuracy with tf-idf    | accuracy with frew-word
| :---:   | :---: | :---: |
| knn   | 73.52 %| 64.70 % |
| Native bayesn   | 8.82 % | 29.41 % |
| descion tree   | 32.35 % | 26.47 % |
| random forest   | 32.35 %| 26.47 % |
