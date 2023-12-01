from config import (CRUNCHBASE_API_KEY)
import json
import pprint
import requests
import pandas as pd
from pandas.io.json import json_normalize
import urllib.request
url = "https://api.crunchbase.com/api/v4/entities/organizations/crunchbase?user_key={CRUNCHBASE_API_KEY}"

with urllib.request.urlopen(url) as f:
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)
    pprint.pprint(response_data)