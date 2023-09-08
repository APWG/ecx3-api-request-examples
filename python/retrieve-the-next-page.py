import urllib.request
import json


def main():
    """
    Retrieves the next page of a previous search results
    Prints the response content in a human-readable format.
    """
    module_name = "mal-ip"
    api_url = "https://ecx3-stage.ecrimex.net/api/v1/" + module_name
    
    # use your own api key! this is an example do not commit your secret key
    api_token = ""
    
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",  # Specify content type for the request
    }
    
    request_all = urllib.request.Request(
        api_url,  headers=headers, method="GET"
    )

    next_page_url = ''
    # Get the paginated list of documents
    with urllib.request.urlopen(request_all) as response:
        response_content = response.read()
        parsed_response = json.loads(response_content.decode())  # Decode and parse JSON
        # assign the next page url
        next_page_url = parsed_response['next_page_url']
    
    # set up next request to retrieve the next page of the previous search
    request_next_page = urllib.request.Request(
        next_page_url,  headers=headers, method="GET"
    )

    # make the request to the next page
    with urllib.request.urlopen(request_next_page) as response:
        response_content = response.read()
        parsed_response = json.loads(response_content.decode())  # Decode and parse JSON
        formatted_response = json.dumps(parsed_response, indent=2)  # Format JSON
        print("API Response:")
        print(formatted_response)

if __name__ == "__main__":
    main()
