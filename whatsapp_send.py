from playwright.sync_api import sync_playwright
import time 

def whatsapp_sending(pdf, phone):
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir="./whatsapp_session",
            headless=False
        )
        page = context.new_page()
        
        page.goto("https://web.whatsapp.com")
        page.wait_for_load_state("networkidle")
        time.sleep(10) 

        page.get_by_role("textbox").first.click()
        page.get_by_role("textbox").first.type(phone)
        time.sleep(1)
        page.keyboard.press("Enter")
        time.sleep(1)
        page.get_by_role("button", name="附加").click() 
        time.sleep(1)
        with page.expect_file_chooser() as fc_info:
            page.get_by_role("menuitem", name="文件").click()
            file_chooser = fc_info.value
            file_chooser.set_files(pdf)
        time.sleep(1)
        page.keyboard.press("Enter")
        time.sleep(40)

        context.close()





