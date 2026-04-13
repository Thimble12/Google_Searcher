from os import link
import os
import random
from datetime import datetime
import sys
import time
from time import sleep
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
global _link
_link = None # Initializes the link variable to None. This variable will be used to store the current link being generated and checked for validity.
##################################################################### GOOGLE DOCS
global valid_doc_color1
global valid_doc_color2
global doc_sample_1
global doc_sample_2
valid_doc_color1 = (11, 87, 208) # Should be the blue log in button
valid_doc_color2 = (14, 14, 14) # Should be the black log in screen
doc_sample_1 = (984, 188) # Should be the blue log in button
doc_sample_2 = (803, 340) # Should be the black log in screen
##################################################################### GOOGLE SPREADSHEETS
global valid_spr_color1
global valid_spr_color2
global spr_sample_1
global spr_sample_2
valid_spr_color1 = (11, 87, 208) # Should be the blue log in button
valid_spr_color2 = (14, 14, 14) # Should be the black log in screen
spr_sample_1 = (984, 188) # Should be the blue log in button
spr_sample_2 = (803, 340) # Should be the black log in screen
##################################################################### GOOGLE SLIDES
global valid_sli_color1
global valid_sli_color2
global sli_sample_1
global sli_sample_2
valid_sli_color1 = (11, 87, 208) # Should be the blue log in button
valid_sli_color2 = (14, 14, 14) # Should be the black log in screen
sli_sample_1 = (984, 188) # Should be the blue log in button
sli_sample_2 = (803, 340) # Should be the black log in screen
##################################################################### GOOGLE DOCS ELEMENTS
global valid_doc_element1
global valid_doc_element2
valid_doc_element1 = "docs-chrome" # Should be an element only present on valid doc links with full access (ID)
valid_doc_element2 = "eC9N2e" # Should be an element only present on valid doc links with restricted access (CLASS NAME)
##################################################################### GOOGLE SPREADSHEETS ELEMENTS
global valid_spr_element1
global valid_spr_element2
valid_spr_element1 = "docs-chrome" # Should be an element only present on valid spreadsheet links with full access (ID)
valid_spr_element2 = "eC9N2e" # Should be an element only present on valid spreadsheet links with restricted access (CLASS NAME)
##################################################################### GOOGLE SLIDES ELEMENTS
global valid_sli_element1
global valid_sli_element2
valid_sli_element1 = "docs-chrome" # Should be an element only present on valid slides links with full access (ID)
valid_sli_element2 = "eC9N2e" # Should be an element only present on valid slides links with restricted access (CLASS NAME)
##################################################################### LINK BASES
global base_doc_link
base_doc_link = "https://docs.google.com/document/d/"
global base_spr_link
base_spr_link = "https://docs.google.com/spreadsheets/d/"
global base_sli_link
base_sli_link = "https://docs.google.com/presentation/d/"
##################################################################### OTHER SETTINGS
global driver
driver = None # Initializes the web driver variable to None. This variable will be used to store the instance of the web driver that is created and used to open links and check their validity.
global length
length = 44 # Length of UUID generated for links. Google Docs, Sheets, and Slides links have a 44 character UUID.
global delay
delay = 0 # Delay in seconds for waiting after loading a webpage before checking for validity, and other network operations.
global load_delay
load_delay = 0 # Delay for waiting for a webpage to load before performing any actions.
sys.setrecursionlimit(100) # Sets the maximum depth of the Python interpreter stack to 100. This is necessary because the program uses recursion to generate and check links, and a large number of iterations could cause a stack overflow if the limit is to high.
global iteration
iteration = 0 # Sets the initial iteration count to 0. This variable is used to keep track of how many links have been generated and checked, and to determine when to restart the web driver.
global RESTART_INTERVAL
RESTART_INTERVAL = 1000 # Number of iterations after which the web driver will be restarted to prevent memory leaks and other issues.
#####################################################################

def clear_terminal(): # Clears the terminal screen. Used for better readability of output.
    if sys.platform.startswith('win'):
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def create_driver(headless=False): # Creates a new instance of the Chrome WebDriver with specified options.
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    if headless:
        options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(10)
    return driver

def generate_google_link(type="doc"): # Creates a random UUID and appends it to the base link for the specified Google service (Docs, Sheets, or Slides) to create a random link.
    global _link
    random.seed()
    randdoclink = ""
    randsprlink = ""
    randslilink = ""
    rand_letters = []
    for i in range(length):
        random.seed()
        randtemp = random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","-","_","0","1","2","3","4","5","6","7","8","9"])
        rand_letters.append(randtemp)
        
    rand_ending = "".join(rand_letters)
    
    randdoclink = base_doc_link + rand_ending
    randsprlink = base_spr_link + rand_ending
    randslilink = base_sli_link + rand_ending

    if type == "doc":
        _link = randdoclink
        return {"link": randdoclink, "type": type}
    elif type == "spr":
        _link = randsprlink
        return {"link": randsprlink, "type": type}
    elif type == "sli":
        _link = randslilink
        return {"link": randslilink, "type": type}
    else:
        print("Invalid type specified. Please choose 'doc', 'spr', or 'sli'.")
        return None, None

def open_link(link_data, check_type): # Opens the specified link in the web driver and waits for the page to load before returning the link data. The check_type parameter specifies whether the validity of the link will be checked using color or element methods.
    link = link_data["link"]
    type = link_data["type"]

    if check_type == "color":
        pass
    elif check_type == "element":
        pass
    else:
        print("Invalid check type specified. Please choose 'color' or 'element'.")

    if type == "doc":
        driver.get(link)
        WebDriverWait(driver, 15)
        sleep(delay)
        return {"link": link, "type": type, "check_type": check_type}
    elif type == "spr":
        driver.get(link)
        WebDriverWait(driver, 15)
        sleep(delay)
        return {"link": link, "type": type, "check_type": check_type}
    elif type == "sli":
        driver.get(link)
        WebDriverWait(driver, 15)
        sleep(delay)
        return {"link": link, "type": type, "check_type": check_type}
    else:
        print("Invalid type specified. Please choose 'doc', 'spr', or 'sli'.")

def check_color_validity(link_data): # A method of checking the validity of a link by checking the color of specific pixels on the webpage.
    link = link_data["link"]
    type = link_data["type"]

    if type == "doc":
        color1 = pyautogui.pixel(x=doc_sample_1[0], y=doc_sample_1[1])
        color2 = pyautogui.pixel(x=doc_sample_2[0], y=doc_sample_2[1])

        print(f"\n\n\nExpecting {valid_doc_color1}, got {color1}.")

        print(f"\nExpecting {valid_doc_color2}, got {color2}.\n")

        if color1 == valid_doc_color1:
            print(f"{link} is a valid link, with full access (iteration {iteration})\n")
            with open("Valid_links.txt", "a") as file:
                file.write(f"{link} is a valid link, with full access. Generated at {datetime.now()} (iteration {iteration})\n")
        elif color2 == valid_doc_color2:
            print(f"{link} is a valid link, but access is restricted (iteration {iteration})\n")
            with open("Valid_links.txt", "a") as file:
                file.write(f"{link} is a valid link, but access is restricted. Generated at {datetime.now()} (iteration {iteration})\n")
        else:
            print(f"{link} is an invalid link (iteration {iteration})\n\n\n")
    elif type == "spr":
        color1 = pyautogui.pixel(x=spr_sample_1[0], y=spr_sample_1[1])
        color2 = pyautogui.pixel(x=spr_sample_2[0], y=spr_sample_2[1])

        print(f"\n\n\nExpecting {valid_spr_color1}, got {color1}.")

        print(f"\nExpecting {valid_spr_color2}, got {color2}.\n")

        if color1 == valid_spr_color1:
            print(f"{link} is a valid link, with full access (iteration {iteration})\n")
            with open("Valid_links.txt", "a") as file:
                file.write(f"{link} is a valid link, with full access. Generated at {datetime.now()} (iteration {iteration})\n")
        elif color2 == valid_spr_color2:
            print(f"{link} is a valid link, but access is restricted (iteration {iteration})\n")
            with open("Valid_links.txt", "a") as file:
                file.write(f"{link} is a valid link, but access is restricted. Generated at {datetime.now()} (iteration {iteration})\n")
        else:
            print(f"{link} is an invalid link (iteration {iteration})\n\n\n")
    elif type == "sli":
        color1 = pyautogui.pixel(x=sli_sample_1[0], y=sli_sample_1[1])
        color2 = pyautogui.pixel(x=sli_sample_2[0], y=sli_sample_2[1])
        
        print(f"\n\n\nExpecting {valid_sli_color1}, got {color1}.")

        print(f"\nExpecting {valid_sli_color2}, got {color2}.\n")

        if color1 == valid_sli_color1:
            print(f"{link} is a valid link, with full access\n")
            with open("Valid_links.txt", "a") as file:
                file.write(f"{link} is a valid link, with full access. Generated at {datetime.now()} (iteration {iteration})\n")
        elif color2 == valid_sli_color2:
            print(f"{link} is a valid link, but access is restricted\n")
            with open("Valid_links.txt", "a") as file:
                file.write(f"{link} is a valid link, but access is restricted. Generated at {datetime.now()} (iteration {iteration})\n")
        else:
            print(f"{link} is an invalid link (iteration {iteration})\n\n\n")
    else:
        print("Invalid type specified. Please choose 'doc', 'spr', or 'sli'.")

def check_webpage_element_validity(link_data): # A method of checking the validity of a link by checking for the presence of specific elements on the webpage.
    link = link_data["link"]
    type = link_data["type"]
    check_type = link_data["check_type"]

    if check_type == "element":
        if type == "doc":
            try:
                WebDriverWait(driver, load_delay).until(EC.presence_of_element_located((By.ID, valid_doc_element1)))
                print(f"{link} is a valid link, with full access (iteration {iteration})\n\n\n")
                with open("Valid_links.txt", "a") as file:
                    file.write(f"{link} is a valid link, with full access. Generated at {datetime.now()}\n")
            except:
                try:
                    WebDriverWait(driver, load_delay).until(EC.presence_of_element_located((By.CLASS_NAME, valid_doc_element2)))
                    print(f"{link} is a valid link, but access is restricted (iteration {iteration})\n\n\n")
                    with open("Valid_links.txt", "a") as file:
                        file.write(f"{link} is a valid link, but access is restricted. Generated at {datetime.now()}\n")
                except:
                    print(f"{link} is an invalid link (iteration {iteration})\n\n\n")
        elif type == "spr":
            try:
                WebDriverWait(driver, load_delay).until(EC.presence_of_element_located((By.ID, valid_spr_element1)))
                print(f"{link} is a valid link, with full access (iteration {iteration})\n\n\n")
                with open("Valid_links.txt", "a") as file:
                    file.write(f"{link} is a valid link, with full access. Generated at {datetime.now()}\n")
            except:
                try:
                    WebDriverWait(driver, load_delay).until(EC.presence_of_element_located((By.CLASS_NAME, valid_spr_element2)))
                    print(f"{link} is a valid link, but access is restricted (iteration {iteration})\n\n\n")
                    with open("Valid_links.txt", "a") as file:
                        file.write(f"{link} is a valid link, but access is restricted. Generated at {datetime.now()}\n")
                except:
                    print(f"{link} is an invalid link (iteration {iteration})\n\n\n")
        elif type == "sli":
            try:
                WebDriverWait(driver, load_delay).until(EC.presence_of_element_located((By.ID, valid_sli_element1)))
                print(f"{link} is a valid link, with full access (iteration {iteration})\n\n\n")
                with open("Valid_links.txt", "a") as file:
                    file.write(f"{link} is a valid link, with full access. Generated at {datetime.now()}\n")
            except:
                try:
                    WebDriverWait(driver, load_delay).until(EC.presence_of_element_located((By.CLASS_NAME, valid_sli_element2)))
                    print(f"{link} is a valid link, but access is restricted (iteration {iteration})\n\n\n")
                    with open("Valid_links.txt", "a") as file:
                        file.write(f"{link} is a valid link, but access is restricted. Generated at {datetime.now()}\n")
                except:
                    print(f"{link} is an invalid link (iteration {iteration})\n\n\n")
        else:
            print("Invalid type specified. Please choose 'doc', 'spr', or 'sli'.")

def check_link_list_validity(): # A function used to test a set set of links, with some valid, restricted, and invalid, to test the accuracy of the validity checking methods.
    start_time = datetime.now()
    with open("Link_List.txt", "r") as file:
        links = file.readlines()
        for link in links:
            link = link.strip()
            if "docs.google.com/document/d/" in link:
                check_webpage_element_validity(open_link({"link": link, "type": "doc"}, "element"))
            elif "docs.google.com/spreadsheets/d/" in link:
                check_webpage_element_validity(open_link({"link": link, "type": "spr"}, "element"))
            elif "docs.google.com/presentation/d/" in link:
                check_webpage_element_validity(open_link({"link": link, "type": "sli"}, "element"))
            else:
                print(f"{link} is an invalid link\n\n\n")
    end_time = datetime.now()
    print(f"Checked the validity of {len(links)} links in {end_time - start_time}.")
    driver.quit()

def main(link_type="doc", search_type="element"):
    global iteration
    global RESTART_INTERVAL
    global driver
    driver = create_driver() # Creates an instance of the web driver to be used for opening links and checking their validity.
    clear_terminal()
    while True:
        try:
            iteration += 1
            check_webpage_element_validity(open_link(generate_google_link(link_type), search_type))
            time.sleep(delay)
            print("\n\n\n\n\n\n")
            if iteration % RESTART_INTERVAL == 0:
                print("Restarting driver...\n")
                with open("Errors.txt", "a") as file:
                    file.write(f"\nDriver scheduled restart at {datetime.now()}\n iteration: {iteration}\n")
                driver.quit()
                driver = create_driver()
                print("Driver restarted!")
        except KeyboardInterrupt:
            print("Program interrupted by user. Exiting...")
            driver.quit()
        except Exception as e:
            print(f"Error: {e}")
            with open("Errors.txt", "a") as file:
                file.write(f"\nError: {e}.\n Occurred at {datetime.now()}\n Link: {_link}\n iteration: {iteration}\n")
            with open("Error_causing_links.txt", "a") as file:
                file.write(f"{_link}\n")
            driver.quit()
            driver = create_driver()
            with open("Errors.txt", "a") as file:
                file.write(f"\nDriver restarted due to error at {datetime.now()}\n iteration: {iteration}\n")
                print("Driver restarted due to error...\n")

main("doc", "element")