import json
import requests

# Define the instance metadata URL
metadata_instance = "http://169.254.169.254/latest/dynamic/instance-identity/document"

# Send a GET request to the instance metadata service
result = requests.get(metadata_instance)

if result.status_code == 200:
    # If the request is successful, data will be put into JSON response
    instance_metadata = result.json()
    print(instance_metadata)
else:
    print("Failed to fetch instance metadata.")
    
    
#to get direct response we can use the below  insted of json:
#response = requests.get("http://169.254.169.254/latest/meta-data")
#print(r.text.split("\n"))


#for any particular keys
def get_aws_metadata():
    metadata = {
        'public-hostname': "",
        'ami-id': "",
        'instance-id': ""
    }

    for key in metadata.keys():
        resp = requests.get(
            f'http://169.254.169.254/latest/meta-data/{key}',
            timeout=1
        )
        if resp.status_code != 200:
            raise Exception()
        metadata[key] = resp.text
    return metadata
    
get_aws_metadata()