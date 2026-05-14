## Demo Video
https://www.youtube.com/watch?v=evrIq9XYAK0
Note that sensitive information have been covered in the video for author privacy

## Installation
Install the required libraries:
pip install yfinance pandas reportlab playwright
playwright install chromium

## Configuration
The script is currently set up for **Traditional Chinese** WhatsApp Web.
If your WhatsApp language is different, update the following selectors in `whatsapp_send.py`:
- `附加` → your language's word for "Attach"
- `文件` → your language's word for "Document"
- Set the phone number you want to send in the stocksdataa.py file
- set the author name in the toPDF file
-  time.sleep can be adjusted for a shorter time in the whatsapp_send.py during the run, tickers can be adjusted for other tickers in the stocksdata.py as well

##Whatsapp set up
Set the phone number as contact person

## Running
Run python stocksdata.py in the terminal (or rename it and run it)

## Start Running
1. Stock data is fetched live from Yahoo Finance via yfinance
2. A PDF is generated and saved as `stock_info.pdf`
3. A browser window opens automatically and navigates to WhatsApp Web
4. Scan the QR code to log in — session is saved for future runs (This can be avoided in second run unless you log out)
5. The program search for the required phone number input in stocksdata.py

## Notes
- Each step has a buffer delay of a few seconds to allow WhatsApp Web to load
- After sending, the script waits briefly before closing the browser
- To fully log out of WhatsApp Web, do so manually from your mobile device
