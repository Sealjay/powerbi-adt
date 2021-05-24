import pandas as pd
from azure.digitaltwins.core import DigitalTwinsClient
from azure.identity import (
    DefaultAzureCredential,
    AzureCliCredential,
    ChainedTokenCredential,
)

url = "https://powerbidemo.api.uks.digitaltwins.azure.net"

default_credential = DefaultAzureCredential(
    exclude_interactive_browser_credential=False
)
azure_cli = AzureCliCredential()
credential_chain = ChainedTokenCredential(azure_cli, default_credential)

service_client = DigitalTwinsClient(url, credential_chain)
query_expression = "SELECT * FROM digitaltwins"
query_result = service_client.query_twins(query_expression)

twin_list = pd.DataFrame(query_result)
