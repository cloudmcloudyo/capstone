# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Seinfeld Script Generator
---
### Problem Statement

In 1996, Bill Gates wrote an essay whose title became so prevailing that every marketer knows and quotes-- "Content is King." In his essay, he believed that content "is where I expect much of the real money will be made on the Internet." Fast forward to today, his idea still stands the test of time, if not turns even truer.

We live in a world filled with content. Tehcnology has significantly lowered the bar of creating and consuming content. With the explosion of social media, the landscape of marketing has been changed completely. 10 years ago, it was fancy for a brand to have a Facebook page; now it's a must, along with a list of other must-haves: Instagram, Twitter, Pinterest, to name just a few.

To stay relevent, brands need to constantly supply content with high quality for informational or entertainment purpose, which sets a new requirment for marketers: not only do they need to generate content with great quality, they need to generate it more and fast, as well as with minimum costs possible. The good news, as Bill stated, is that "no company is too small to participate." However the question remains, how do we achieve all those? 

That is where text generation comes in. 

Recent years has witnessed series of jaw-droppping breakthroughs in the field of natural language processing, with new pre-trained NLP models producing state-of-arts results on various tasks from sentiment analysis to question answering. From a marketing's perspective, the applicatoin of text generation is endless: community engagement, developing derivatives based on an existing IP, A/B testing and so forth. Being able to utilize the text generation models will be a compelling advantage that sets the brand apart. 

This project aims to use text generation models to build a script generator for the popular 90s sitcom _Seinfeld_, with the hope to showcase marketing and operation professionals how far text generation can go and be applied with a vivid example. TV writers get paid \\$26,832 per 30-minute prime time episode. For a phenomenal show like _Seinfeld_, the price tag to hire a writer is much higher. In fact, one of the show's main writers is the leading actor Jerry Seinfeld himself, who made a staggering $13,000 per line arriving the final season of the show. Imagine that NBC would like to initiate a marketing campaign featuring reimagined _Seinfeld_ scenes, the script generator will help to afford the idea and likely achieve it faster.

Specific questions this project would like to answer:
1. Can a RNN-LSTM model be used to generate scripts with meaningful sentences in the same formality as the input data?
2. Does word level RNN-LSTM models outperfrom character level ones and why?
3. Is it possible to fine tune pre-trained GPT-2 model to generate _Seinfeld_-specific scripts? 
4. Can diversity be specified to meet different creative demands?
4. Which of the GPT-2 and RNN-LSTM perform better with regard to the form, content and speed of the script generation?
5. What are the thredholds of data size for each model?
6. Can these models be trained with a budget-friendly method?


### Risks & Assumptions
Challenge: 
- Long running time, hard to generate meaningful words or dialogue. 
- Formatting
Assumptions: 


### Initial Goals & Success Criteria
Line goals: will decide based on model performance
Readability: score each line and decide the percentage of meaningful dialogues.
Sentiment Analysis: See if each character has a similar sentiment score compared to original scripts


### Data Source
https://www.imsdb.com/TV/Seinfeld.html
Data Retrieving: build an automated scraper to perform web scrapping from the data source.

### Modeling
- simpleRNN
- LSTM
- LSTM with attention mechanism
- GPT-2

### Parameter Tuning
loss --> under 1
LSTM --> 2-3 layers 
batch size -->
Steps
max sequence length

### Evaluation
- loss --> should shoot for under 1, however hard to get lower 
- texts --> compare models

### What's New
Built a model from scratch using bags of words rather than character based
batch generator --> address the hardware limitation
incorporated keras tokenizer
Seinfeld script generator

### Script Generator API
streamlit

### System Requirment
- RNN under py 3.7
- GPT-2 tensorflow 1.15

### Findings

### Conclusions
- for text generation, data size is still the key?

Dataset sizes: Note that if your data is too small (1MB is already considered very small) the RNN won't learn very effectively. Remember that it has to learn everything completely from scratch. Conversely if your data is large (more than about 2MB), feel confident to increase rnn_size and train a bigger model (see details of training below). It will work significantly better. For example with 6MB you can easily go up to rnn_size 300 or even more. The biggest that fits on my GPU and that I've trained with this code is rnn_size 700 with num_layers 3 (2 is default).

business writing, legal writing etc very useful, efficient


### Limitations
- Loss didn't change much -- indicate that the model might be too simple -- attention model? bidirectional? Simply more training time

- GPT-2 --> too big to load, too slow to run, everytime needs to load the entire package.

- Streamlit --> how to incorporate cache to improve the performance & user experience, --> version issue: how to incorporate both models together to compare

### Next Steps
- Train on jokes to make it more funny although seinfeld's jokes are very sophisticated/ insightful.

- Would be great to build in printouts during the modeling

- Figure out an automated way to read through the generated texts. Would be great to automate the counting how many words 

### Reflection
Deepfake: what is the boundary
Not that writers can be replaced!!! but it's a latent area that can save us possible time: think about customer service: responding emails?
Data quality is not great
Transfer Learning --> if it's there, use it!

### Executive Summary

### Reference

https://medium.com/@HeathEvans/content-is-king-essay-by-bill-gates-1996-df74552f80d9#:~:text=Ever%20wondered%20where%20the%20phrase,as%20it%20was%20in%20broadcasting.

https://towardsdatascience.com/openai-gpt-2-understanding-language-generation-through-visualization-8252f683b2f8

https://towardsdatascience.com/examining-the-transformer-architecture-part-1-the-openai-gpt-2-controversy-feceda4363bb

paper
https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf