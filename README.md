### covid_vaccine_appointment_alert
First of all, I created this project because I was frustrated with not getting the appointment slots for vaccination. 
I spent a few hours building this and added the python cron job interval to time check if any slot is available.

This repository contains a python script with the use of selenium and chrome driver to automatically search available vaccine appointments in the district.

Here are packages and steps I have used for creating this project - 
1. Installed python selenium library, its windows exe file along chrome driver.
2. Used selenium xapth extensively to click every event on Cowin website.
3. Script will count the total number of slots available in the entire district and add that to the python list.
4. Finally to send the alerts, I have registered with the Twillio application for free. This will send WhatsApp, text messages to the dict of users I have added.
5. Added an email alert as well in case Twillio free service stops working.
6. Last to run the script automatically, I have used the python APScheduler library, which will execute the script automatically every after 2 minutes and send the alert.

### Note: 
I used this small project to send notifications only for my district, so I hardcoded the state and district. But this can be enhanced further and made dynamic for different districts.




