#https://learndataanalysis.org/google-py-file-source-code/
#username: coffeeprojectgroup1@gmail.com
#password: CoffeeCoffeeCoffee
#form link: https://docs.google.com/forms/d/e/1FAIpQLSfTtx1Zv_239qeMjlAAfU8BOABsQGbILvXG9_RGsnLRJbB_BQ/viewform?usp=publish-editor

import os
import datetime
from collections import namedtuple
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
import csv


def create_service(client_secret_file, api_name, api_version, *scopes, prefix=''):
import gspread
import pandas as pd
from google.oauth2.service_account import Credentials

# Step 1: Define API scope
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Step 2: Load credentials
creds = Credentials.from_service_account_file(
    "coffeekey.json",
    scopes=scope
)

# Step 3: Authorize connection
client = gspread.authorize(creds)

# Step 4: Open the Google Sheet with form responses
sheet = client.open("Coffee Pairing Responses").sheet1

# Step 5: Get all rows
data = sheet.get_all_records()

# Step 6: Convert to dataframe
df = pd.DataFrame(data)

# Step 7: Save as CSV
df.to_csv("participants.csv", index=False)

print("Participants CSV downloaded successfully!")

participants = []

with open("participants.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["Your name"]
        email = row["Your e-mail"]
        participants.append((name, email))

print(participants)