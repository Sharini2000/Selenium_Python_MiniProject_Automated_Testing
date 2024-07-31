import os
from datetime import datetime


class ScreenshotHelper:
    def __init__(self, screenshots_dir="tests_report/screenshots"):
        self.screenshots_dir = os.path.join(os.getcwd(), screenshots_dir)
        os.makedirs(self.screenshots_dir, exist_ok=True)

    def take_screenshot(self, driver, name="screenshot"):
        """Capture a screenshot and save it to a specified directory."""
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        screenshot_path = os.path.join(self.screenshots_dir, f"{name}_{timestamp}.png")

        try:
            driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved: {screenshot_path}")
            return screenshot_path
        except Exception as e:
            print(f"Failed to capture screenshot: {e}")
            return None
