# Linkedin-Posts-Link-Scraping
The logic of the code revolves around two main tasks: 
web scraping and interacting with Google Sheets API. 

Here's the breakdown of the logic:

--> Web Scraping with Selenium and BeautifulSoup:

1. The script uses Selenium WebDriver to automate the browser actions, such as navigating to a specific LinkedIn profile page.
2. Once the page is loaded, it extracts the HTML content of the page.
3. BeautifulSoup is then used to parse the HTML content and extract specific elements, in this case, the URLs of LinkedIn posts.
4. The extracted URLs are stored in a list for further processing.

--> Interacting with Google Sheets API using gspread:

1. The script authenticates with the Google Sheets API using service account credentials stored in a JSON file.
2. It then uses the gspread library to interact with Google Sheets.
3. The Google Sheets document is opened using its URL.
4. The script selects a specific worksheet within the Google Sheets document.
5. Finally, it appends the scraped data (in this case, LinkedIn post URLs) to the selected worksheet.
