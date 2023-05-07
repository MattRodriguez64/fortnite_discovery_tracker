#!/usr/bin/python3
from Discovery import Discovery
from MapInfo import MapInfo
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from DiscoveryTrackerDAO import DiscoveryTrackerDAO
import os
import shutil


base_url = "https://www.fortnite.com"


def setup_connexion():
    option = Options()
    option.add_argument('--headless')
    option.add_argument('--no-sandbox')
    option.add_argument('--window-size=1920,1080')
    option.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36")

    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option, port=5555)
    return browser


def get_source_code_html(url: str) -> str:
    browser = setup_connexion()
    browser.get(url)
    browser.maximize_window()
    return browser.page_source


def browse_map_info(currentDiscovery: Discovery):
    browser = setup_connexion()
    browser.get(f"{base_url}{currentDiscovery.get_map_url()}")
    tags = browser.find_element(By.XPATH, "/html/body/main/div/div[2]/div/div[2]/div/div/div/div[1]/div").text.split("•")
    tags = [tag.replace("\n", "") for tag in tags]
    #print(f"TAGS : {tags}")
    description = browser.find_element(By.XPATH, "/html/body/main/div/div[2]/div/div[2]/div/div/div/div[2]")\
        .text.replace("ADD TO PLAYLIST", "").replace("Add to favorites", "").replace("Share", "")
    #print(f"description : {description}")
    if len(description) > 200:
        description = "Description TOO LONG"
    try:
        island_creator = browser.find_element(By.XPATH, "/html/body/main/div/div[2]/div/div[2]/div/div/div/div[3]/div[1]").text[2:]
    except Exception as e:
        island_creator = description[2:]
        print(f"--> func browse_map_info : island_creator error ({e}")
    #print(f"island creator : {island_creator}")
    if len(tags) < 4:
        for i in range(0, 4 - len(tags)):
            tags.append(None)
    #print(tags)

    current_map_info = MapInfo(currentDiscovery.get_map_url(), currentDiscovery.get_map_name(), island_creator, tags[0],
                               tags[1], tags[2], tags[3], description)
    return current_map_info


if __name__ == "__main__":
    for directory in [d for d in os.listdir('../../../../tmp/')]:
        if '.com.google' in directory:
            try:
                shutil.rmtree(f"../../../../tmp/{directory}")
            except Exception as e:
                print(f"Error dir remove : {e}")
    while True:
        b_soup = BeautifulSoup(get_source_code_html(base_url), "html.parser")

        discovery_main_div = b_soup.find("div", "fn-c-rPmfy fn-c-rPmfy-jusojb-maxWidth-none fn-c-rPmfy-jXmjIw-padding-med")
        all_discovery_maps = []
        all_mapinfos = []
        discovery_dao = DiscoveryTrackerDAO()

        for discovery_category in discovery_main_div.find_all("div", "fn-c-cuqgZp-dFRkxg-gap-lg"):
            temp_title_div = discovery_category.find("div", "fn-c-cuqgZp-ibCbUR-gap-none")
            temp_maps_div = discovery_category.find("ul", "c-bqMggx")
            category = temp_title_div.find('div', 'c-fxrEBZ-jXBwIa-lines-single').getText()
            #print(f"Titre categorie : {category}")
            #print(f"Nombre de map dans la catégorie : {temp_maps_div}")
            index: int = 0
            for map in discovery_category.find_all("li", "fn-c-fqscxu"):
                map_soup = BeautifulSoup(map.text, "html.parser")
                try:
                    map_name = map.find("div", "c-fxrEBZ").get_text()
                    print("Map Name : " + map_name)
                    player_number = map.find("div", "c-dhzjXW-jroWjL-align-center").get_text().replace("Concurrent users", "").replace("k", "")
                    if "." in player_number:
                        #print(player_number)
                        player_number = int(float(player_number) * 1000)
                        #print(player_number)

                    print("Number of players playing : " + str(player_number))
                    island_link = map.find("a", "fn-c-jcHSmV").get("href")
                    print("Island link + code : " + island_link)
                    currentDiscovery = Discovery(map_name, island_link, category, index, player_number)

                    all_discovery_maps.append(currentDiscovery)
                    current_map_info = browse_map_info(currentDiscovery)
                    all_mapinfos.append(current_map_info)

                    if len(discovery_dao.select_from_map_info(currentDiscovery.get_map_url())) == 0:
                        print("--> Not in mapinfo table !")
                        discovery_dao.insert_mapinfo(current_map_info)
                    discovery_dao.insert_discovery(currentDiscovery)

                except Exception as e:
                    print(f"---> An error occured : {e}")
                    pass
                print("Island position in the category : " + str(index))
                index += 1

        for directory in [d for d in os.listdir('../../../../tmp/')]:
            try:
                shutil.rmtree(f'../../../../tmp/{directory}')
            except Exception as e:
               print(f"Error dir remove : {e}")
