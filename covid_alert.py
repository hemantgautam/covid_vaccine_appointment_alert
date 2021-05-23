# Send details in whatsapp
# add State and Region Dynamically

import time
import json
import requests
from time import gmtime, strftime
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from twilio.rest import Client
from apscheduler.schedulers.blocking import BlockingScheduler


mail_Mobile_dict = {
                    <mobile_no>: '<email_address>',
                    <mobile_no>: '<email_address>',
                    }
cowin_login_link = 'https://selfregistration.cowin.gov.in/'

def time_sleep():
    time.sleep(3)

def send_whatsapp(reciever, appointment_text):
    account_sid = '<twillio_account_sid>' 
    auth_token = '<twillio_auth_token>' 
    client = Client(account_sid, auth_token) 

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body = appointment_text,
        to   = 'whatsapp:+91{0}'.format(reciever)
    )
    print(message)

def send_text_message(appointment_text):
    account_sid = '<twillio_account_sid>' 
    auth_token = '<twillio_auth_token>' 
    client = Client(account_sid, auth_token) 
 
    message = client.messages.create(  
                              messaging_service_sid='<twillio_messaging_service_sid>',
                              body=appointment_text + " Login here {0} ".format(cowin_login_link),
                              to='+91<mobile_no>' 
                          ) 
    print(message.sid)


def send_email(reciever, appointment_text):
    import time
    import smtplib
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('<email_id>', 'password')
    subject = appointment_text
    body = "Login here {0} ".format(cowin_login_link)
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        '<from_email_id>',
        reciever,
        msg
    )
    print("Email is sent")
    time.time()
    server.quit()


def main():
    try:
        print("=========Start Time========")
        print(strftime("%a, %d %b %Y %H:%M:%S", gmtime()))
        driver = webdriver.Chrome('C:/Users/hemantg11/Python Code/Covid Alerts/chromedriver')
        print(strftime("%a, %d %b %Y %H:%M:%S", gmtime()))

        driver.get('https://www.cowin.gov.in/home');

        driver.find_element_by_class_name("status-switch").click()
        time_sleep()

        driver.find_element_by_id("mat-select-0").click()
        time_sleep()

        driver.find_element_by_xpath("//html/body/div[2]/div[2]/div/div/div/mat-option[21]/span[1]").click();
        time_sleep()

        driver.find_element_by_id("mat-select-2").click()
        time_sleep()

        driver.find_element_by_xpath("//html/body/div[2]/div[2]/div/div/div/mat-option[23]/span").click();
        time_sleep()

        driver.find_element_by_xpath("//button[contains(@class, 'pin-search-btn') and contains(@class, 'district-search')]").click()
        time_sleep()

        driver.find_element_by_xpath("//div[contains(@class, 'form-check') and contains(@class, 'nomargright')][1]").click()
        time_sleep()

        vaccine_list = []

        vaccine_counts = driver.find_elements_by_xpath("//div[contains(@class, 'slot-available-main')]//li[contains(@class, 'ng-star-inserted')]//a")
        for vaccine in vaccine_counts:
            if vaccine.text != "NA" and vaccine.text != "Booked":
                vaccine_list.append(int(vaccine.text))

        # vaccine_list = [1,2,3,4]
        vaccine_total = 0
        if vaccine_list != []:

            #Send message and EMail:
            vaccine_total = sum(vaccine_list)
            appointment_text = "Total {0} Appointments Available!!".format(vaccine_total)
            send_text_message(appointment_text)
            for mob, email in mail_Mobile_dict.items():
                send_email(email, appointment_text)
                send_whatsapp(mob, appointment_text)


        else:
            print("No Slots Available")
        driver.quit()
        print("=========End Time========")
        print(strftime("%a, %d %b %Y %H:%M:%S", gmtime()))

    except:
        print("Error Occured")
        driver.quit()


# main()
sched = BlockingScheduler()
sched.add_job(main, 'interval', minutes=2)

sched.start()