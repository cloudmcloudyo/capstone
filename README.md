# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Seinfeld Script Generator
---
### Problem Statement

To build a script generator for popular sitcom, Seinfeld, based on the scripts of the 178 aired episodes. Each script generated should have at least 50 meaningful dialogue exchanges.

### Methods & Models
Word Embedding
basic: RNN - LSTM model
advanced: BART/GPT-2 model


### Risks & Assumptions
Risks: Long running time, hard to generate meaningful dialogue. 
Assumptions: 


### Initial Goals & Success Criteria
Line goals: will decide based on model performance
Readability: score each line and decide the percentage of meaningful dialogues.
Sentiment Analysis: See if each character has a similar sentiment score compared to original scripts


### Data Source
https://www.imsdb.com/TV/Seinfeld.html
Data Retrieving: build an automated scraper to perform web scrapping from the data source.