import pyautogui
import time

# Configuration
BUTTON_IMAGE = 'next_button.png'
CONFIDENCE_LEVEL = 0.8 # Adjust based on screen resolution

def auto_click_next():
    print("Automation started. Press Ctrl+C to stop.")
    try:
        while True:
            # Look for the button on the screen
            location = pyautogui.locateOnScreen(BUTTON_IMAGE, confidence=CONFIDENCE_LEVEL)
            
            if location:
                print("Next button found. Clicking...")
                pyautogui.click(location)
                # Wait for the next video to load
                time.sleep(5) 
            
            # Check every 2 seconds
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("Automation stopped.")

if __name__ == "__main__":
    auto_click_next()
