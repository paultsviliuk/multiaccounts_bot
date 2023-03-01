import requests
from web3 import Web3, HTTPProvider, IPCProvider
from web3.middleware import geth_poa_middleware
from eth_account import Account

# Define the provider URL for your Ethereum network
provider_url = "http://eth-mainnet.alchemyapi.io/v2/your-api-key"
# replace with your Alchemy API key

# Define the proxy parameters
proxy_host = "proxy.host"  # replace with your proxy host
proxy_port = 47118  # replace with your proxy port
proxy_username = "username"  # replace with your proxy username
proxy_password = "password"  # replace with your proxy password

# Create a Web3 object with the specified provider URL and POA middleware
session = requests.Session()
session.proxies = {
    "http": f"http://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}",
    "https": f"https://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}"
}
session.verify = False

web3 = Web3(HTTPProvider(provider_url,
                         session=session))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Define your MetaMask address and private key
address = "your-wallet-address"
private_key = "your-pk"

# Create an account object from your private key
account = Account.from_key(private_key)

# Set the default account for your Web3 instance
web3.eth.default_account = address

print(web3.isConnected())
print("{}".format(web3.eth.get_balance(address)))

# Or check all unlocked accounts
unlocked_accounts = web3.eth._get_accounts()
print("Unlocked accounts: ", unlocked_accounts)
