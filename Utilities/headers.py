# headers_config.py

class APIHeaders:
    """
    Class to store and manage API headers
    """
    @staticmethod
    def get_default_headers():
        """
        Returns default headers used in API requests
        """
        return {
                "Content-Type": "application/json"
        }
