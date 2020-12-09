# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Capstone - Seinfeld Script Generator
---
### Problem Statement

This project

To build a script generator for popular sitcom, Seinfeld, based on the scripts of the 178 aired episodes. Each script generated should have at least 50 meaningful dialogue exchanges.


Text generation. --> from a marketing perspective
Why: inspiration? less significant events -- cost-cutting, more efficient?
Writing partner
They want to generate some jokes, marketing campaign but they are on a budget. Using seinfeld as an example.
contents is the king but they come with a price

media-transcendence: IP operation --> "stranger things" experience. video games, online interactive, CRM-community management, etc

### Methods & Models
Word Embedding
basic: RNN - LSTM model
advanced: BART/GPT-2 model


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

### Findings & Conclusions
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