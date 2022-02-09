from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

# =============================================================================
# Acollection of quotes assigned a tag(romance, wisdom, god, etc)
# =============================================================================

romance_df = pd.read_csv('Romance_Quotes.csv').drop('Unnamed: 0', axis='columns')
love_df = pd.read_csv('Love_Quotes.csv').drop('Unnamed: 0', axis='columns')

wisdom_df = pd.read_csv('Wisdom_Quotes.csv').drop('Unnamed: 0', axis='columns')
truth_df = pd.read_csv('Truth_Quotes.csv').drop('Unnamed: 0', axis='columns')

god_df = pd.read_csv('God_Quotes.csv').drop('Unnamed: 0', axis='columns')
faith_df = pd.read_csv('Faith_Quotes.csv').drop('Unnamed: 0', axis='columns')

humor_df = pd.read_csv('Humor_Quotes.csv').drop('Unnamed: 0', axis='columns')
writing_df = pd.read_csv('Writing_Quotes.csv').drop('Unnamed: 0', axis='columns')

death_df = pd.read_csv('Death_Quotes.csv').drop('Unnamed: 0', axis='columns')
time_df = pd.read_csv('Time_Quotes.csv').drop('Unnamed: 0', axis='columns')

knowledge_df = pd.read_csv('Knowledge_Quotes.csv').drop('Unnamed: 0', axis='columns')
science_df = pd.read_csv('Science_Quotes.csv').drop('Unnamed: 0', axis='columns')


# =============================================================================
# All dfs are pseudo grouped, in a purely biased fashion by myself. I will remove all quotes which have a tagg outside the pseudo-group.
# e.g. From truth_df, I will remove romance and love, god and faith etc. But I will NOT remove wisdom_df.
# I suspect this might lead to overfitting. TBD.
# =============================================================================

love_list = ['love', 'romance']
wisdom_list = ['wisdom', 'truth']
religion_list = ['god', 'faith']
wit_list = ['humor', 'writing']
death_list = ['death', 'time']
intel_list = ['knowledge', 'science']

full_list = love_list+ wisdom_list+ religion_list+ wit_list+ death_list+ intel_list

# =============================================================================
# A function to remove all the rows which contain a genre which belongs to another category
# =============================================================================
def strip_df(df, keepers, f_l): #From this df, keep these two genres, and remove what's left in full_list
    
    #Make list of things to remove
    #
    for k in keepers:
        if k in f_l:
            f_l.remove(k)
   
    #define keepers as items which don't contain first item in list, then iterate over others
    #
    df['Keeper'] = ~df.Genre.str.contains(f_l[0])
    for f in f_l[1:]:
        
        #Make a temp out of next value, make an 'AND' of all of them
        #
        df['Temp'] = ~df.Genre.str.contains(f)
        df['Keeper'] = df['Temp'] & df['Keeper'] 
        
    df = df.where(df['Keeper']).dropna()
    df.drop(['Keeper', 'Temp'], axis='columns', inplace=True)
    f_l += keepers
    
    return df

# =============================================================================
# There is definitely a better vectorized way to perform the filtering of multiple words.
# I tried to do with Select and a condition and results list, couldn't figure it out. 
# If data increased by an order of magnitude or so, would likely be very costly
# =============================================================================

# =============================================================================
# Hardcoding the function to every df to extract a cleaner dataframe. Will then save in CSV 
# =============================================================================

clean_romance = strip_df(romance_df, love_list, full_list)
clean_love = strip_df(love_df, love_list, full_list)
    
clean_wisdom = strip_df(wisdom_df, wisdom_list, full_list)
clean_truth = strip_df(truth_df, wisdom_list, full_list)

clean_god = strip_df(god_df, religion_list, full_list)
clean_faith = strip_df(faith_df, religion_list, full_list)
    
clean_humor = strip_df(humor_df, wit_list, full_list)
clean_writing = strip_df(writing_df, wit_list, full_list)
    
clean_death = strip_df(death_df, death_list, full_list)
clean_time = strip_df(time_df, death_list, full_list)

clean_knowledge = strip_df(knowledge_df, intel_list, full_list)
clean_science = strip_df(science_df, intel_list, full_list)

clean_romance.to_csv('Clean_Romance.csv')
clean_love.to_csv('Clean_Love.csv')
clean_wisdom.to_csv('Clean_Wisdom.csv')
clean_truth.to_csv('Clean_Truth.csv')
clean_god.to_csv('Clean_God.csv')
clean_faith.to_csv('Clean_Faith.csv')
clean_humor.to_csv('Clean_Humor.csv')
clean_writing.to_csv('Clean_Writing.csv')
clean_death.to_csv('Clean_Death.csv')
clean_time.to_csv('Clean_Time.csv')
clean_knowledge.to_csv('Clean_Knowledge.csv')
clean_science.to_csv('Clean_Science.csv')
   
    
   
    
   
    
   
    
   
    
   
    


    
