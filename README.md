
# UiPath RPA Project

This project presents an RPA process that generates User information under a defined structure and 
registers Instagranny accounts based on those details.

## Technologies used

- UiPath Studio v2022.10
- C#
- Python 3.10

## Usage

The following requirements are needed before deploying the robot:

- Instagranny social media platform deployed 
- Python path updated in the Python Scope depending on where the app is located

The robot will prompt for the number of users to be generated. Once done, it will use "behindthename.com"
website to generate random English names and store them in an excel file. Once done, it will take the names and 
using "spinxo.com" it will generate usernames. The Python script execution will provide email addresses and passwords,
completing the information required for the last sequence, which will Register accounts on the Instagranny social media
app.