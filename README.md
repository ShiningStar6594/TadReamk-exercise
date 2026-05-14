
## Installation
Install the required libraries:
pip install yfinance pandas reportlab playwright
playwright install chromium

## Configuration
The script is currently set up for **Traditional Chinese** WhatsApp Web.
If your WhatsApp language is different, update the following selectors in `whatsapp_send.py`:
- `附加` → your language's word for "Attach"
- `文件` → your language's word for "Document"

## Running
Run python stocksdata.py in the terminal (or rename it and run it)

## Notes
- Each step has a buffer delay of a few seconds to allow WhatsApp Web to load
- After sending, the script waits briefly before closing the browser
- To fully log out of WhatsApp Web, do so manually from your mobile device
