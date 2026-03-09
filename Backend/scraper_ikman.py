import time
import os
import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


BASE_URL = "https://ikman.lk/en/ads/sri-lanka/cars"


def scrape_ikman(pages=5):

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    data = []

    for page in range(1, pages + 1):

        url = f"{BASE_URL}?page={page}"
        print(f"Scraping page {page}...")

        driver.get(url)
        time.sleep(4)

        listings = driver.find_elements(By.CSS_SELECTOR, "li.normal--2QYVk")

        print("Listings found:", len(listings))

        for item in listings:

            try:

                # TITLE + LINK
                title_el = item.find_element(By.CSS_SELECTOR, "a")
                title = title_el.text
                link = title_el.get_attribute("href")

                # PRICE
                price_el = item.find_element(By.CSS_SELECTOR, "span")
                price = price_el.text

                # LOCATION
                location_el = item.find_element(By.CSS_SELECTOR, "div")
                location = location_el.text

                print("Scraped:", title)

                data.append({
                    "title": title,
                    "price": price,
                    "location": location,
                    "link": link
                })

            except Exception as e:
                print("Skipping listing:", e)

    driver.quit()

    df = pd.DataFrame(data)

    os.makedirs("dataset", exist_ok=True)

    df.to_csv("dataset/ikman_cars.csv", index=False)

    print("Saved", len(df), "records")


if __name__ == "__main__":
    scrape_ikman(60)