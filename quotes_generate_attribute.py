from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

def url_list(base_url, no_of_pages):
    nos = np.linspace(1, no_of_pages, no_of_pages)
    
    pages = []
    for n in nos:
        page = base_url+str(int(n))
        pages.append(page)
    return pages

def quote_list(url):
    site = requests.get(url)
    soup = BeautifulSoup(site.text, features='lxml')
    
    quotes = []
    genres = []
    
    items = soup.find_all('div', {'class':'quote mediumText'})
    for item in items:
        q = item.find('div', {'class':'quoteText'}).text
        quote = str.split(q, '―')
        quotes.append(quote[0].strip())
        
        genre_box = item.find('div', {'class':'greyText smallText left'}).find_all('a')
        genre = ''
        for g in genre_box:
            genre += (g.text + ',')
        genre = genre[:-1]
        genres.append(genre)
        
    df = pd.DataFrame({'Quote':quotes, 'Genre':genres})    
    
    return df

def make_quote_df(base_url, no_of_pages):
    pages = url_list(base_url, no_of_pages)
    
    list_of_dfs = []
    counter=1
    for page in pages:
        print(f'About to make dataframe: {counter}')
        counter +=1
        df = quote_list(page)
        list_of_dfs.append(df)
    
    final_df=pd.concat(list_of_dfs, ignore_index=True)
        
    return final_df


# =============================================================================
# Love category of quotes
# =============================================================================

romance_urls = 'https://www.goodreads.com/quotes/tag/romance?page='

romance_df = make_quote_df(romance_urls, 100)

love_urls = 'https://www.goodreads.com/quotes/tag/love?page='

love_df = make_quote_df(love_urls, 100)


# =============================================================================
# Wisdom category of quotes
# =============================================================================

wisdom_urls = 'https://www.goodreads.com/quotes/tag/wisdom?page='

wisdom_df = make_quote_df(wisdom_urls, 100)

truth_urls = 'https://www.goodreads.com/quotes/tag/truth?page='

truth_df = make_quote_df(truth_urls, 100)


# =============================================================================
# Religion category of quotes
# =============================================================================

god_urls = 'https://www.goodreads.com/quotes/tag/god?page='

god_df = make_quote_df(god_urls, 100)

faith_urls = 'https://www.goodreads.com/quotes/tag/faith?page='

faith_df = make_quote_df(faith_urls, 100)


# =============================================================================
# Witty and clever category of quotes
# =============================================================================

humor_urls = 'https://www.goodreads.com/quotes/tag/humor?page='

humor_df = make_quote_df(humor_urls, 100)

writing_urls = 'https://www.goodreads.com/quotes/tag/writing?page='

writing_df = make_quote_df(writing_urls, 100)


# =============================================================================
# Dark and contemplative category of quotes
# =============================================================================

death_urls = 'https://www.goodreads.com/quotes/tag/death?page='

death_df = make_quote_df(death_urls, 100)

time_urls = 'https://www.goodreads.com/quotes/tag/time?page='

time_df = make_quote_df(time_urls, 100)


# =============================================================================
# Intellectual category of quotes
# =============================================================================

knowledge_urls = 'https://www.goodreads.com/quotes/tag/knowledge?page='

knowledge_df = make_quote_df(knowledge_urls, 100)

science_urls = 'https://www.goodreads.com/quotes/tag/science?page='

science_df = make_quote_df(science_urls, 100)



# =============================================================================
# Giving each df the column category, with respective category
# =============================================================================
CATEGORY = 'Category'

romance_df[CATEGORY] = 'Romance'
love_df[CATEGORY] = 'Love'
wisdom_df[CATEGORY] = 'Wisdom'
truth_df[CATEGORY] = 'Truth'
god_df[CATEGORY] = 'God'
faith_df[CATEGORY] = 'Faith'
humor_df[CATEGORY] = 'Humor'
writing_df[CATEGORY] = 'Writing'
death_df[CATEGORY] = 'Death'
time_df[CATEGORY] = 'Time'
knowledge_df[CATEGORY] = 'Knowledge'
science_df[CATEGORY] = 'Science'


# =============================================================================
# Converting every df into a CSV for future use
# =============================================================================

romance_df.to_csv('Romance_Quotes.csv')
love_df.to_csv('Love_Quotes.csv')
wisdom_df.to_csv('Wisdom_Quotes.csv')
truth_df.to_csv('Truth_Quotes.csv')
god_df.to_csv('God_Quotes.csv')
faith_df.to_csv('Faith_Quotes.csv')
humor_df.to_csv('Humor_Quotes.csv')
writing_df.to_csv('Writing_Quotes.csv')
death_df.to_csv('Death_Quotes.csv')
time_df.to_csv('Time_Quotes.csv')
knowledge_df.to_csv('Knowledge_Quotes.csv')
science_df.to_csv('Science_Quotes.csv')








