README
This Python script is used to scrape flight data from two flight aggregation websites, Paytm and Cleartrip, and compare the prices of common flights between them. The scraped data is then written to a CSV file called flight.csv.
The script requires the following packages to be installed:
* pandas
* selenium
* beautifulsoup4
* webdriver_manager
To run the script, execute the Main.py file in a Python environment with the required packages installed. The script will prompt the user to enter a travel date in the format YYYY/MM/DD. The script then scrapes flight data from Paytm and Cleartrip using the entered travel date and a fixed flight sector (Delhi to Chandigarh). The scraped data is then compared to find common flights and their prices. The results are saved to a CSV file called flight.csv in the same directory as the script.
Note that the script uses the Chrome webdriver to scrape data from the websites, so Google Chrome must be installed on the system and the Chrome webdriver must be compatible with the installed version of Chrome. The webdriver_manager package is used to automatically install the appropriate Chrome webdriver.

