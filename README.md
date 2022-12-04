# kinguin-client

A tiny API wrapper in Python for Kinguin e-commerce API ([Kinguin-eCommerce-API](https://github.com/kinguinltdhk/Kinguin-eCommerce-API))

## Installation

`pip install kinguin-client`

## Basic Usage

```
from kinguin_client import Kinguin

client = Kinguin(api_key="API_KEY")

client.balance().get()
{'balance': 0}

client.orders().get()
{'results': [], 'item_count': 0}
```

## License

MIT
