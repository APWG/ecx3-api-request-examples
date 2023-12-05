import urllib.request
import json


def main():
    """
    Sends a GET request to phish module to retrieve a single document.
    Prints the response content in a human-readable format.
    """
    document_id = "108866279"
    api_url = "https://sandbox.ecx2.ecrimex.net/api/v1/phish/" + document_id

    # use your own api key! this is an example do not commit your secret key
    api_token = ""

    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",  # Specify content type for the request
    }

    request = urllib.request.Request(
        api_url, headers=headers, method="GET"
    )

    with urllib.request.urlopen(request) as response:
        response_content = response.read()
        parsed_response = json.loads(response_content.decode())  # Decode and parse JSON
        formatted_response = json.dumps(parsed_response, indent=2)  # Format JSON

        print("API Response:")
        print(formatted_response)


if __name__ == "__main__":
    main()
