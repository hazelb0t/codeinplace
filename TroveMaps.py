"""
This program will take a CSV file of digitised maps from Trove that I retrieved from GLAM WORKBENCH
https://github.com/GLAM-Workbench/trove-maps/blob/master/single_maps.csv
It will ask the user enter a place name and then provide the title and URL for any map that has this name in the title.
If the user enters no place name the program will ask whether user wants a random map and provide one if the answer is yes.
"""

import pandas as pd
import random
import webbrowser

def main():
    # imports csv file and turns it into DataFrame
    trove_maps = pd.read_csv('single_maps.txt')
    #print(trove_maps.shape)
    find_map(trove_maps)
    while True:
        find_map(trove_maps)


'''
Find_map will take a users input and find a map with that word in the title. If there is more than one map that fits this
criteria it will return the first result only.
It will print the title and open the map in a browser (using the fulltext_url column).
If user enters nothing, they will be asked if they wish to have a random map retrieved. If user enters no the program exits.
If a user's input is not found program will advise and ask user to try again.
'''
def find_map(trove_maps):
    query_word = input("Please enter a place name to find a map: ")
    # Retrieves first row from the title column based on a search for the query_word in the title column
    map_title = (trove_maps.loc[(trove_maps['title'].str.contains(query_word, case=False)), 'title']).head(1)
    # Retrieves first row from the fulltext_url column based on a search for the query_word in the title column
    map_url = (trove_maps.loc[(trove_maps['title'].str.contains(query_word, case=False)), 'fulltext_url']).head(1)
    if query_word == "":
        print("Would you like a random map?")
        random_map = str.lower(input("Please type Yes for a random map or No to exit: "))
        if random_map == "yes":
            find_rand_map(trove_maps)
        else:
            exit()
    elif map_title.empty:
        print("No map found. Please try again.")
    else:
        # Takes just the value of the cell, turns it into a string and strips any spaces
        map_url = (map_url.to_string(index=False)).strip()
        print("Map title is:", map_title.to_string(index=False))
        # Opens map in browser
        webbrowser.open(map_url)

'''
A random map is retrieved, the title is printed and the map opens in browser.
'''
def find_rand_map(trove_maps):
    random_row = random.randint(0, 20157)
    map_title = trove_maps.loc[random_row, 'title']
    map_url = trove_maps.loc[random_row, 'fulltext_url']
    print("Your random map is:", map_title)
    webbrowser.open(map_url)  # opens map in browser











if __name__ == '__main__':
    main()