# Quotes_Predictor

This script uses various classification models to predict a quote's 'category type'. 

There are a couple of files dedicated to the retrieval/cleaning of the data. Goodreads.com has pages dedicated entirely to famous quotes and tags which are assigned to them by users. With BeautifulSoup, the data is aggregated with their primary tag, along with secondary tags. 

The final file takes the data and applies sklearn Machine Learning classifiers to the data. Before doing so, I filtered the data a bit further, to make sure none of the secondary tags contained one of the 6 types I was testing for. My best model was Random Forest, with roughly 67% accuracy.

The dataset relies on Wisdom of the Crowd, however, there are probably many quotes on the website which are 'overly tagged'. Let's look at a Dr. Seuss quote: "You know you're in love when you can't fall asleep because reality is finally better than your dreams". This has the tag 'sleep' and 'reality', but this is simply a quote about 'Love', using a sleeping metaphor.

I tried the model against many lyrics/poems, and it doesn't perform very well. I'm guessing this is because of metaphors or other poetic techniques, whereas 'traditional quotes' don't use as much flowery language. ('Shall I compare thee to a summer's day?' is evaluated as either being about Knowledge or Wisdom'). When evaluated on arbitrary sentences I made up, which had a more 'quote-like' nature, the model performed about as expected, ~67%. The model also benefits when the test-quotes are closer in size to actual quotes, which tend to be a little longer than just one line from a song or poem.

I'd like to find another dataset and test the same thing. Song lyrics would be a good place to start. I'm also worried about overfitting, and would need to experiment with breaking up the dataset to smaller chuncks, i.e. Stacking/Blender.

I'm hoping that when optimized, I could refactor this for things like document-type prediction (e.g. a company's scanned files are categorized as contract, memo, training, etc.). Could also be cool in a video game which predicts user input, and has enemy react to a player's language. 
