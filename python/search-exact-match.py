import urllib.request
import json


def main():
    """
    Sends a POST request to an API endpoint to search for a malicious domain.
    Prints the response content in a human-readable format.
    """
    api_url = "https://ecx3-stage.ecrimex.net/api/v1/malicious-domain/search"

    # use your own api key! this is an example do not commit your secret key
    api_token = ""
    
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",  # Specify content type for the request
    }
    # Send a filters object searching for specific attributes values
    request_data = {
        "filters": {
            "id": "167593",
            "classification": "fake store",
            "confidence": 100,
            "discoveredAt": "2022-12-29T00:59:40+00:00",
            "cratedAt": "2022-12-29T00:59:40+00:00",
            "domain": "gwfkb.userdental.top",
            "updatedAt": "2022-12-29T00:59:40+00:00",
            "status": "active",
        }
    }

    encoded_data = json.dumps(request_data).encode()
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
