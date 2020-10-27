from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import datetime
import time
import os
import keyboard

os.system("")

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

print(style.GREEN + "  ______________________________________________________________")
print(style.GREEN + "^|                                                              ^|")
print(style.GREEN + "^|       This program is created for educational purposes       ^|")
print(style.GREEN + "^|         I am not responisble for the way you use it.         ^|")
print(style.GREEN + "^|                                                              ^|")
print(style.GREEN + "^|      Created By : Owen :)                                    ^|")
print(style.GREEN + "^|                                                              ^|")
print(style.GREEN + "^|                                                              ^|")
print(style.GREEN + "^|      ___________________________________________________     ^|")
print(style.GREEN + "^|      [1] Activate                                            ^|")
print(style.GREEN + "^|      ___________________________________________________     ^|")
print(style.GREEN + "^|      [2] Exit                                                ^|")
print(style.GREEN + "^|                   Created with Python <3                     ^|")
print(style.GREEN + "^|______________________________________________________________^|")

option = int(input())

if option == 1:

    try:
        # f = open("./status.txt",'r',encoding = 'utf-8')
        with open("status.txt",'r',encoding = 'utf-8') as f:
            output = ''
            for line in f:
                output = output + line
            output = output.split('\n')
            email = output[0]
            password = output[1]
            attendance = output[2]
            Meet_Link = output[3]
            Time_start1 = output[4]
            Time_start2 = output[5]
            Time_start3 = output[6]
            Time_end = int(output[7])
    except:
        email = input(style.CYAN + "Enter Your Class Room Email: ")
        while "@" not in email:
            if os.name == 'posix':
                _ = os.system('clear')
            else:
                _ = os.system('cls')
            email = input(style.CYAN + "Enter Your Class Room Email: ")

        password = input(style.BLUE + "Enter Your Class Room Password: ")
        attendance = input(style.MAGENTA + "Enter Your Name and Roll Number\nExample: John 1903072:\n")
        Meet_Link = input(style.YELLOW + "Paste Google Meet Link (Must Include https:// in url): ")
        print(style.RED + "Format for time before 12:00pm : 09:13 | Format for time after 12:00pm : 13:15 - This format is necessary")
        Time_start1 = input(style.BLUE + "Enter 1st Lecture Start Time: ")
        Time_start2 = input(style.GREEN + "Enter 2nd Lecture Start Time: ")
        Time_start3 = input(style.WHITE + "Enter 3rd Lecture Start Time: ")
        Time_end = int(input(style.YELLOW + "Enter the Lecture End Time in Seconds\nExample 40 Minutes = 2400 Seconds so enter: 2400\n"))
        with open("status.txt",'w',encoding = 'utf-8') as f:
            f.write(f"{email}\n")
            f.write(f"{password}\n")
            f.write(f"{attendance}\n")
            f.write(f"{Meet_Link}\n")
            f.write(f"{Time_start1}\n")
            f.write(f"{Time_start2}\n")
            f.write(f"{Time_start3}\n")
            f.write(f"{Time_end}")

    while True:
        now = datetime.datetime.now()
        class_time = now.strftime("%H:%M / %A")
        print(style.RED + class_time)

        opt = Options()
        opt.add_argument("--disable-infobars")
        opt.add_argument("start-maximized")
        opt.add_argument("--disable-extensions")

        # You can use these features below as well but i have commented them because for some reason there is a bug in chrome driver because in mozilla its working fine.
        # so I added a simple script below that clicks and allow notifications, and allow other permissions as well.

        # opt.add_experimental_option("prefs", { \
        #     "profile.default_content_setting_values.media_stream_mic": 1,
        #     "profile.default_content_setting_values.media_stream_camera": 1,
        #     "profile.default_content_setting_values.geolocation": 0,
        #     "profile.default_content_setting_values.notifications": 1
        # })


        def gmail():
            subject = f"{Meet_Link}"
            driver = webdriver.Chrome(
                chrome_options=opt, executable_path=r'chromedriver')

            driver.get("https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1#identifier")
            time.sleep(4)
            driver.find_element_by_xpath(
                "//input[@name='identifier']").send_keys(f"{email}")
            time.sleep(2)
            # Next Button:
            driver.find_element_by_xpath(
                "//*[@id='identifierNext']/div/button/div[2]").click()
            time.sleep(5)
            # my Password:
            driver.find_element_by_xpath(
                "//input[@name='password']").send_keys(f"{password}")
            time.sleep(2)
            # next button:
            driver.find_element_by_xpath(
                "//*[@id='passwordNext']/div/button").click()
            time.sleep(5)
            # open Meet:
            driver.get(subject)
            
            # tab tab enable notifications
            time.sleep(5)
            keyboard.press_and_release('tab, tab')
            keyboard.press_and_release('enter, enter')
            time.sleep(2)
            keyboard.press_and_release('tab, tab')
            keyboard.press_and_release('enter, enter')

            #Error handling when the bot is unable to locate the chat box (means you are not inside the lobby then the bot will restart and try again)
            try:
            # Turning off audio video
                time.sleep(1)
                #camera
                driver.find_element_by_xpath(
                     "//*[@id='yDmH0d']/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div[4]/div[2]/div/div").click()
                #mic
                driver.find_element_by_xpath(
                "//*[@id='yDmH0d']/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div").click()
                #Join class
                time.sleep(7)
                driver.find_element_by_xpath(
                    "//*[@id='yDmH0d']/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span").click()

                #send present
                time.sleep(6)
                driver.find_element_by_xpath(
                    "//*[@id='ow3']/div[1]/div/div[5]/div[3]/div[6]/div[3]/div/div[2]/div[3]/span/span").click()
                time.sleep(10)
                driver.find_element_by_xpath(
                    "//*[@id='ow3']/div[1]/div/div[5]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[1]/div[1]/div[2]/textarea").send_keys(f"Present {attendance}")
                time.sleep(2)
                driver.find_element_by_xpath(
                    "//*[@id='ow3']/div[1]/div/div[5]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[2]/span").click()
                
                time.sleep(Time_end)
                driver.close()

            except:
                # driver.close()
                print('Retrying again in 2 minutes....')
                time.sleep(2)
                driver.close()
                time.sleep(120)
                gmail()


        # Class time + Meet link + Class Time End
        # I have only added one class url but you can make more fstrings and take more inputs save more urls and customize it according to your prefernace.
        # Only 3 Lectures added you can add more by yourself.

        if class_time == f"{Time_start1} / Monday" or class_time == f"{Time_start2} / Monday" or class_time == f"{Time_start3} / Monday":
            gmail()

        elif class_time == f"{Time_start1} / Tuesday" or class_time == f"{Time_start2} / Tuesday" or class_time == f"{Time_start3} / Tuesday":
            gmail()

        elif class_time == f"{Time_start1} / Wednesday" or class_time == f"{Time_start2} / Wednesday" or class_time == f"{Time_start3} / Wednesday":
            gmail()

        elif class_time == f"{Time_start1} / Thursday" or class_time == f"{Time_start2} / Thursday" or class_time == f"{Time_start3} / Thursday":
            gmail()

        elif class_time == f"{Time_start1} / Friday" or class_time == f"{Time_start2} / Friday" or class_time == f"{Time_start3} / Friday":
            gmail()

        else:
            time.sleep(1)
            print(style.RED + "No classes atm lad!")

else:
    exit(1)
