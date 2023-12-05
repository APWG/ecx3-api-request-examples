import urllib.request
import json


def main():
    """
    Sends a POST request to an API endpoint to add a cryptocurrency address document.
    Prints the response content in a human-readable format.
    """
    api_url = "https://sandbox.ecx2.ecrimex.net/api/v1/cryptocurrency-addresses"
    
    # use your own api key! this is an example do not commit your secret key
    api_token = ""

    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",  # Specify content type for the request
    }

    document = {
        "source": "blackmail.com",
        "procedure": "automated",
        "currency": "ADA",
        "address": "113FuvPmoZZgrZ5j9Z6fESU6mTXgFjUh10",
        "crimeCategory": "blackmail",
        "actorCategory": "any",
        "discoveredAt": "2023-12-29T00:59:56+00:00",
        "siteLink": "demolink.com",
        "price": 3.50,
        "email": "test@gmail.com",
        "confidence": 90,
    }

    encoded_data = json.dumps(document).encode()
    request = urllib.request.Request(
        api_url, data=encoded_data, headers=headers, method="POST"
    )

    with urllib.request.urlopen(request) as response:
        response_content = response.read()
        parsed_response = json.loads(response_content.decode())  # Decode and parse JSON
        formatted_response = json.dumps(parsed_response, indent=2)  # Format JSON

        print("API Response:")
        print(formatted_response)


if __name__ == "__main__":
    main()
