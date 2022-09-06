####################################################################################
########################### IDC409 Assignment 1 ####################################
####################################################################################
### Fetch all the links (<a href=...>) from 'all the result pages' of your search on 'findaphd.com'.
### Reference python script is attached.############################################
### KINDLY COMMENT YOUR CODE.#######################################################
### Mention the relative contribution of each group-member in %.####################
####################################################################################
### MS18117 - Akshay - 50% - scraped the maximum page number of obtained results####
### MS18194 - Mirudula - 50% - managed file I/O				        ####
####################################################################################

import requests
from bs4 import BeautifulSoup

"""
@param keyword: Input string to search in the website
@param filename: Input string to store the results (links)
@return: None; Results are stored to filename.txt
"""

def getAllLinks(keyword, filename):

    base_url="https://www.findaphd.com/phds/?Keywords=" + (str(keyword).lower()).replace(' ', '+') + "&PG="
    
    filename = str(filename) + ".txt" #To create a variable for given txt file
    g = open(filename, "w")
        
    p=requests.get(base_url) #get the html content of base-url page
    s=BeautifulSoup(p.content, "html.parser") #parse the first page
    
    #check if any results exist for this keyword
    if(isinstance(s.find("div", {"class": "pagingAreaOuter"}), type(None))):
        
        g.write("\n-------------\nNo Result Found:\n-------------\n") #To add page number       
        
        for a in s.find_all('a', href = True): #find all links and write to file
            g.write(str(a['href']) + "\n")
                
        print("No results found for this keyword.") 
        
    #if results exist
    else:        
        max_page = s.find("div", {"class": "pagingAreaOuter"}).findAll("li")[-1].text #find max page number
        max_page = int(max_page)

        for page in range(1, max_page + 1): #iterate through every page and print links
            
            p=requests.get(base_url + str(page)) #get the html content of the page
            s=BeautifulSoup(p.content, "html.parser") #parse the page
            
            g.write("\n-------------\nPage no: "+ str(page) + "\n-------------\n") #To add page number       

            for a in s.find_all('a', href = True): #find all links and write to file
                g.write(str(a['href']) + "\n")
                
        g.close()

getAllLinks("Data Science", "results")