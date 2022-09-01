import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
def access_spreadsheet():
    scope = ['https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)

    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    spreadsheet = client.open("GoogleADS")
    return spreadsheet

def return_values(spreadsheet):
    return spreadsheet.worksheet("Key Words").get_all_records()

def return_values2(spreadsheet):
    return spreadsheet.worksheet("Geral").get_all_records()
