import requests 
from requests.exceptions import ConnectionError, HTTPError

url = '' 

try:
    r = requests.get(url)   
    print(r.status_code)   
    if r.status_code >= 400:
        print('Oops, something went wrong')
    else:     
        print("All fine, let's do something")

except ConnectionError as conn_err:      
    print(f'Connection Error! {conn_err}.') 

except HTTPError as http_err:     
    print(f'HTTP error occurred: {http_err}') 
