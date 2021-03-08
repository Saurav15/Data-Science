# Web Scrapping has 3 steps :
# 1.) First using Request module in python we will download the content i.e HTML content of the website .... GET THE HTML !
#     now we will have the whole HTML code but in the form of string !
# 2.) Once the HTML is fetched using Requests as a String we need to parse it .
#      For parsing we will use Pythons BeautifulSoup module which will create a tree like Structure for our DOM
# 3.) Once the HTML is fetched and parsed , the next step is to manipulate the tree using BeautifulSoup functions in order to get the job done .



# Lets Start : 

import requests 
from  bs4 import BeautifulSoup

# The website that we are going to scrape is :
url = 'https://codewithharry.com'

# Step 1 : Get the HTML
r = requests.get(url)  # To get the website 
htmlContent = r.content # to get the HTML content from the website
print(htmlContent) # now as we have the HTML in the String Format , Lets go to Step 2.


# Step 2 : PArse the HTML 
soup = BeautifulSoup(htmlContent ,'html.parser') # First argument is what to parse and second is to what eg. HTML,XML... So as we need HTML we use html.parser
print(soup) # So we have the parsed HTML now , but its too messy 
print(soup.prettify) # This will make the code look bit good
# Now as we have the parsed HTML . So lets go to next step 



# Step 3 : HTML tree traversal

# The HTML code is like a Tree . inside HTML tags there are several tags then inside those tags like body there are several other tags 
# So our soup is a tree         ##### SERCH HTML TREE ####
# Now its time time to travese through the tree 

title = soup.title # To get the title of the HTML page
print(title) 
print(type(title)) # Now as we have parsed the content the Data type of the title variable will be bs4.element.Tag
# Now the object title also have some more features 
print( type(title.string) )

# LETS see commanly used types of objects in BeautifulSoup
print(type(title)) # 1. Tag
print(type(title.string) # 2. NavigableString     Its a special type of string that the BeautifulSoup uses 
print(type(soup)) # 3. BeautifulSoup       The soup variable in our program is of type BeautifulSoup
# 4. Comment


# So 
# We have title now 
title = soup.title
print(title)

# Get all the paragrapgs from the page
paras = soup.find_all('p')
print(paras) # Now we have all the paragraphs 






# Get all the anchor tags
anchors = soup.find_all('a')
print(anchors)

# To get all the links 
for link in anchors:
    print(link.get('href')) 
# we have a problem here These are repeated links and another is that we cannot visit any link 
# so what we will do is 
all_links = set() # will make a set to add links to it . Why set? Because even if the links are repeated we wont get it !

for links in anchors:
    all_links.add(links.get('href')) # Now we got rid of repeated elements !

#But still we cant click and visit the links ! So what we will so is :
for links in anchors:
    all_links.add('https://codewithharry.com'+links.get('href'))
    link_text = 'https://codewithharry.com'+links.get('href')
    print(link_text)
# Now we got all the links 





print(soup.find('p')) # This will give me the first para
print(soup.find('p')['class']) # This will give me the class used in para i.e ['lead','text-muted']





# Find all the elements with the class lead
print( soup.find_all('p',class_=('lead')))




#Get all the text 
print( soup.find('p').get_text() )
# We can also get the text of whole page 
print( soup.get_text() )

