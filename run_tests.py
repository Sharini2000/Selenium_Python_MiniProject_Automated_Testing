import pytest
from utils.report_generator import ReportGenerator


def run_tests():
    # Run tests in the specified order
    pytest.main(['tests/test_job_search.py'])
    pytest.main(['tests/test_job_apply.py'])
    pytest.main(['tests/test_Signin.py'])


if __name__ == '__main__':
    # Run the tests
    run_tests()
# Generate the HTML report and run tests
    report_generator = ReportGenerator()
    report_generator.generate_html_report()
