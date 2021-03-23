# Project-of-dataMining
Problem Statement: The dataset was of various doctors of USA and the details of doctors includes of their First name , Middle name , Last name, Credential , Address, State, Zip code and Phone Number. The goal was to check from the web that whether the phone number of a particular doctor given in the dataset is correct or not if the phone number given was correct than provide the link of the website from where this phone number was verified and if the number was not matched then extract the expected phone numbers and headings obtained for that particular doctor.
Approach:
Step 1:  Import Required Python libraries

 

Step 2:  Data Cleaning

Data cleaning is the first step in data mining. It holds importance as dirty data if used directly in mining can cause confusion in procedures and produce inaccurate results. Basically, this step involves the removal of noisy or incomplete data from the collection. Many methods that generally clean data by itself are available but they are not robust.
Pandas Library is mainly used for the process of Data Cleaning.
Here in this project the data given contains of many columns like ‘middle name’ or ‘state’ etc contains of missing values and these missing values could be removed and filled by some methods such as:
•	Ignoring the tuple.
•	Filling the missing value manually.
•	Use the measure of central tendency, median or
•	Filling in the most probable value.



Step 3: Data Integration

Integrate the data of different columns to some other new columns as because these new columns contains the data that needs to be searced on the web for the phone number verification and extraction.Integrate the data of different columns to a single column 

 

Step 4: URL Collection

Collect URLs of the pages where you want to extract data from. These URLs are collected by iterating to each and every entry of the new named column as in the image above and taking the data of each and every row and concatenating it with the common URL i.e. 'https://google.com/search?q='  and then make a request to these URLs to get the HTML of the page.

Step 5: Extract Text From HTML 
Now in the next step the text is extracted from the HTML page as the page contains of many things but we need is the snippets of that page and the urls above those snippets.
This program does three things:
1.	Opens the URL request for the text from the urllib.request module
2.	Reads the HTML from the page as a string and assigns it to the html variable
3.	Creates a BeautifulSoup object and assigns it to the soup variable
The BeautifulSoup object assigned to soup is created with two arguments. The first argument is the HTML to be parsed, and the second argument, the string "html.parser", tells the object which parser to use behind the scenes. "html.parser" represents Python’s built-in HTML parser.

Step 6: Data Reduction

Remove all the data that is not required means that remove all the alphabets symbols etc and at last the page is left with the text of only numbers. The data is reduced from the page will lots of different kind of text to only numerical values between 0-9.
 Concatenate all the numbers as because these numbers are in the form of string use the function .replace(" ","") to remove all the spaces between them.


 





Step 7: Save the data in a JSON or CSV file or some other structured format.

In these numbers find the number that is required by using the function of .find(number) .If the above function returns a positive value than it means that on that webpage that particular phone number is present so append “TRUE” to the list and also  provide the URL of that particular snippet from which that phone number was verified and append this to another list named as source.
But if the number is not verified from the website in that case append “FALSE” to the present named list and empty string to the other list that contains of URLs and after that try to extract the phone numbers from the web by using the same method but the changes that come into play will be instead of using new named column use the newcol named column that contains of the first name, last name, state and the phone number string that will help to fetch out some numbers that lies between range of 10 or 11 digits .Then append these numbers to the list and their corresponding headings of the snippets to the other list.
Save all the lists to the csv file by creating new columns and obtain the result in the another new csv file .  

