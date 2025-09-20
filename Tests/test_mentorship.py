from urllib import response
import pytest
import json
from Utilities.api_client import APIClient
from Utilities.api_url import welcome_url, search_employee_url
from Utilities.headers import APIHeaders
from Utilities.variables import firstname, lastname, employeecode
from Utilities.common_verifications import *
from Utilities.logger import logger  # use the logger you already created

@pytest.mark.usefixtures("playwright")
class TestAPI:

    @pytest.fixture(autouse=True)
    def init_client(self, playwright):
        """
        Initialize API client with Playwright request context for all tests in this class.
        """
        self.client = APIClient(
            request=playwright.request.new_context(
                extra_http_headers=APIHeaders.get_default_headers()
            )
        )
        logger.info("API Client initialized with Playwright request context.")        
        yield
        # Dispose request context after all tests
        self.client.request.dispose()
        logger.info("API Client request context disposed.")

    # -----------------------------
    # GET Message Request Test
    # -----------------------------
    def test_get_message(self):
        logger.info("Starting GET Message test...")
        response = self.client.get(welcome_url)
        data = response.json()
        logger.info(f"GET Message response:\n{json.dumps(data, indent=4)}")
        verify_http_status_code(response, 200)
        verify_response_key(data.get("message"), "Welcome to the Mentorship Program Portal", "message")
        logger.info("GET Message test completed successfully.")

    # -----------------------------
    # GET Employee Search Request Test
    # -----------------------------
    def test_get_employee_search(self):
        logger.info("Starting GET Employee Search test...")
        response = self.client.get(search_employee_url)
        data = response.json()
        logger.info(f"GET Employee Search response:\n{json.dumps(data, indent=4)}")
        verify_http_status_code(response, 200)

        # Verify employee details in the response
        # 1. Call the API to get employee data
        response = self.client.get(search_employee_url)

        # 2. Convert the response to Python dictionary
        data = response.json()

        # 3. Loop through the list of employees
        for employee in data["UserSearchApi"]:
            # 4. Check if this employee matches our expected values
            if (
            employee["firstname"] == firstname and
            employee["lastname"] == lastname and
            employee["employeecode"] == employeecode
            ):
                print("Employee found:", employee)  # print instead of logger for simplicity
                return  # exit the test if employee is found

        # 5. If loop finishes without finding employee, print message and fail test
        print("Employee not found!")
        assert False, "Employee not found in API response"

        logger.info("GET Employee Search test completed successfully.")
