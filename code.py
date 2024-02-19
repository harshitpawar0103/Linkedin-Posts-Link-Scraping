from google.oauth2.service_account import Credentials
import gspread
from bs4 import BeautifulSoup
from selenium import webdriver

# Function to scrape LinkedIn post URLs from profile page
def scrape_post_urls():
    # Initialize Selenium WebDriver and navigate to LinkedIn profile page
    driver = webdriver.Chrome()
    driver.get('https://in.linkedin.com/company/ozibook')
    
    # Extract HTML content of the page
    page_source = driver.page_source
    
    # Use BeautifulSoup to parse HTML
    soup = BeautifulSoup(page_source, 'html.parser')
    
    # Find all post elements on the page
    post_elements = soup.find_all('a', {'data-id': 'main-feed-card__full-link'})
    print(post_elements)
    # Extract URLs of each post
    post_urls = [post['href'] for post in post_elements]
    print(post_urls)
    # Close Selenium WebDriver
    driver.quit()
    
    return post_urls

# Function to authenticate with Google Sheets API and add data
def add_to_google_sheets(data):
    # Authenticate with Google Sheets API
    credentials = Credentials.from_service_account_file('lateral-boulder-414805-8e1c4038f8e1.json')
    print(credentials)
    scoped_credentials = credentials.with_scopes(['https://www.googleapis.com/auth/spreadsheets'])
    client = gspread.Client(auth=scoped_credentials)
    
    # Open the spreadsheet
    spreadsheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1ctNbB21htm_EGcTnEbTXtlwH4kFmGT8f02PivBW6E4k/edit#gid=0')
    
    # Select the first worksheet
    worksheet = spreadsheet.sheet1
    
    # Append data to the worksheet
    worksheet.append_row(data)

# Main function to scrape LinkedIn posts and add data to Google Sheets
def main():
    # Scrape post URLs from LinkedIn profile
    post_urls = scrape_post_urls()
    print(post_urls)
    # Add post data to Google Sheets
    add_to_google_sheets(post_urls)

if __name__ == '__main__':
    main()
