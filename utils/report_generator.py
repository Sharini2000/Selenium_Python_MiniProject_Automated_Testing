import pytest
import os
from datetime import datetime

class ReportGenerator:
    def __init__(self, report_dir="reports"):
        self.report_dir = os.path.join(os.getcwd(), report_dir)
        os.makedirs(self.report_dir, exist_ok=True)

    def generate_html_report(self):
        """Generate an HTML report using pytest-html."""
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        report_path = os.path.join(self.report_dir, f"tests_report_{timestamp}.html")

        try:
            pytest.main([
                "tests",  # This should point to your test directory or specific test files
                f"--html={report_path}",
                "--self-contained-html",
                "--tb=short",
                "--maxfail=1"
            ])
            print(f"HTML report generated: {report_path}")
        except Exception as e:
            print(f"Failed to generate HTML report: {e}")
