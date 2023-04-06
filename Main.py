import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

# Set the travel date and flight sector
travel_date = input("Enter travel date (YYYY/MM/DD): ")
year, month, day = travel_date.split('/')
paytm_date = f"{year}-{month}-{day}"
cleartrip_date=f"{day}/{month}/{year}"
# print(cleartrip_date)
# print(paytm_date)

# Set the URLs for the two flight aggregation websites
cleartrip_url = f'https://www.cleartrip.com/flights/results?adults=1&childs=0&infants=0&depart_date={cleartrip_date}&return_date=&intl=n&from=DEL&to=IXC&airline=&carrier=&sd=1679636540153&page=&sellingCountry=IN&ssfi=&flexi_search=&ssfc=&origin=DEL%20-%20New%20Delhi,%20IN&destination=IXC%20-%20Chandigarh,%20IN&class=Economy&sft='
paytm_url = f'https://tickets.paytm.com/flights/flightSearch/DEL-Delhi/IXC-Chandigarh/1/0/0/E/{paytm_date}'

# Set up the Chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install())



# Scrape data from paytm
driver.get(paytm_url)
content = driver.page_source
paytm_soup = BeautifulSoup(content, "html.parser")
paytm_flights = paytm_soup.find_all("div", class_="_2TFk")

# print(paytm_flights)



# Create a list to store paytm flight data
paytm_data = []

# Extract flight data from Paytm
# print("Paytm Data")
for paytm_flight in paytm_flights:
    paytm_details = paytm_flight.find_all("div", class_="_3215 row")
    if paytm_flight.find("div", class_="_7BOG").text.strip() == "Non Stop":
        paytm_operator = paytm_flight.find("div", class_="_3H-S _1Eia").text.strip()
        paytm_flight_num = paytm_flight.find("div", class_="NqXj _2GoO").text.strip()
        paytm_price = paytm_flight.find("div", class_="_2gMo").text.strip()
        paytm_price = paytm_price.replace(",", "")
        paytm_price = int(paytm_price)
        paytm_data.append([paytm_operator, paytm_flight_num, paytm_price])
        # print([paytm_operator, paytm_flight_num, paytm_price, "Non-Stop"])
# print(paytm_data)



# Scrape data from cleartrip

driver.get(cleartrip_url)
contant = driver.page_source
cleartrip_soup = BeautifulSoup(content, "html.parser")
cleartrip_flights = cleartrip_soup.find_all("div", class_="_2TFk")
# print(cleartrip_flights)


# Create a list to store cleartrip flight data
cleartrip_data=[]

# Extract flight data from Paytm
# print("cleartrip Data")
for cleartrip_flight in cleartrip_flights:
    cleartrip_details = cleartrip_flight.find_all("div", class_="_3215")
    if cleartrip_flight.find("div", class_="_7BOG").text.strip() == "Non Stop":
        cleartrip_operator = cleartrip_flight.find("div", class_="_3H-S _1Eia").text.strip()
        cleartrip_flight_num = cleartrip_flight.find("div", class_="NqXj _2GoO").text.strip()
        cleartrip_price = cleartrip_flight.find("div", class_="_2gMo").text.strip()
        cleartrip_price = cleartrip_price.replace(",", "")
        cleartrip_price = int(cleartrip_price)
        cleartrip_data.append([cleartrip_operator, cleartrip_flight_num,cleartrip_price])
        # print([cleartrip_operator, cleartrip_flight_num, paytm_price, "Non-Stop"])
#  print(cleartrip_data)

# Create a common flights list
common_flights = []

#finding common flights between paytm_data list and cleartrip_data list
for paytm_flight in paytm_data:
    for cleartrip_flight in cleartrip_data:
        if paytm_flight[0] == cleartrip_flight[0] and paytm_flight[1] == cleartrip_flight[1]:
            common_flights.append([paytm_flight[0], paytm_flight[1], paytm_flight[2],cleartrip_flight[2]])
            break

# Write common_flights data in flight.csv file
with open('flight.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Operator", "Flight Num", "Paytm Price", "Cleartrip Price"])
    writer.writerows(common_flights)

# Close the Chrome driver
driver.quit()