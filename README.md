# Google Ads Scrapper

## Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)
7. [Contact](#contact)

## Overview

This repository contains a Python script designed to scrape Google Ads data and integrate it with Google Sheets. It's a powerful tool for marketing prospecting.

## Installation

### Clone the Repository

```bash
git clone https://github.com/engineergomes/google-ads-scrapper.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Configuration

### Google Service Account

- Navigate to the [Google Cloud Console](https://console.cloud.google.com).
- Set up a Google Service Account for your project.
- Download the generated JSON key file for your Service Account.
- Rename the downloaded JSON file to `client_secret.json`.
- Add this renamed file to the bot folder.

### Google Sheets

- Create two tabs in your Google Sheets document: "Key Words" and "General."
- In the "Key Words" tab, list the words you want to search for in your Google Ads campaigns.
- In the "General" tab, structure your data as per the instructions in the previous README.

## Usage

### Run the Script

```bash
python main.py
```

### Data Analysis

- The script will populate the Google Sheets with scraped data.
- You can analyze this data to identify potential clients who may benefit from your marketing services.

## Contributing

If you would like to contribute, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

## Contact

For any queries, please open an issue in the GitHub repository.
