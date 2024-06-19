import time
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Function to start the views process
def start_views():
    video_link = video_link_entry.get()
    num_views = int(num_views_entry.get())
    watch_time = int(watch_time_entry.get())
    delay_between_views = int(delay_between_views_entry.get())

    # Read proxies from file
    with open('validproxy.txt', 'r') as f:
        proxies = [line.strip() for line in f]

        # Set proxy
        proxy_index = view % len(proxies)  # Cycle through the list of proxies
        chrome_options.add_argument(f'--proxy-server={proxies[proxy_index]}')

      
        # Switch to the new window
        new_window_handle = driver.window_handles[-1]
        driver.switch_to.window(new_window_handle)

        # Wait for watch time
        time.sleep(watch_time)


        # Switch back to the main window if it's still open
        if driver.window_handles:
            driver.switch_to.window(driver.window_handles[0])

        # Add a delay between views
        if view < num_views - 1:
            time.sleep(delay_between_views)

        # Quit the WebDriver
        driver.quit()

    # Re-enable start button after execution
    start_button.config(state=tk.NORMAL)

# Create GUI window
root = tk.Tk()
root.title("YouTube Automation")

