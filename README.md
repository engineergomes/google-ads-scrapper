# Google Ads Scraper

The Google Ads Scraper is a powerful tool designed for Google Sheets integration, enabling you to extract valuable data for marketing prospecting. Follow these steps to set up and use the bot effectively:

## Setup

1. **Create a Google Service Account**:

   - Navigate to [Google Cloud Console](https://console.cloud.google.com).
   - Set up a Google Service Account for your project.

2. **Download Key Documentation**:

   - Download the generated JSON key file for your Service Account.

3. **Rename and Place the Key File**:

   - Rename the downloaded JSON file to `client_secret.json`.
   - Add this renamed file to the bot folder.

## Google Sheets Configuration

To utilize the Google Sheets integration, you need to configure your Google Sheets document correctly:

1. **Create Tabs**:

   - In your Google Sheets document, create two tabs (sheets) with the same names you're using in the `spreadsheet.py` file: "Key Words" and "General."

2. **Key Words Tab**:

   - In the "Key Words" tab, list the words you want to search for in your Google Ads campaigns. Follow this format:

     ![Key Words Tab](https://user-images.githubusercontent.com/33553051/187916315-6cf44694-8877-4211-ba22-15595674686c.png)

3. **General Tab**:

   - In the "General" tab, structure your data like this (the column names can be customized):

     ![General Tab](https://user-images.githubusercontent.com/33553051/187917844-121a2f57-3e36-45c7-8ea5-8a159af7e4dd.png)

     - The ratings "100%" and "sim" indicate the quality of the ads.
     - In the "Contatos" (Contacts) column, you can find the contact details of the ad owners.

## Data Analysis and Prospecting

With this setup, you can analyze Google Ads data and identify potential clients who may benefit from your marketing services. Target those advertisers who are not achieving optimal results with their ads and offer your expertise to boost their campaigns.

## Need Help?

Encountering issues while setting up or running the bot? Create an issue, and we'll be happy to assist you!

Happy prospecting and successful marketing campaigns!
