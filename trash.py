import os
msg = "Error: Environment variable {} not found"
for varname in ["HEREMAPS_APP_ID", "HEREMAPS_APP_CODE"]:
    assert os.getenv(varname), msg.format(varname)

import folium
import requests
import ipywidgets

print("You are ready to go!")