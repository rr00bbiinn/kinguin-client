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

## What works?

- [x] Get products (`Kinguin.products().get()`)
- [x] Get orders (`Kinguin.orders().get()`)
- [x] Check your balance (`Kinguin.balance().get()`)
- [ ] Post orders (`Kinguin.orders().post(payload)`)

## License

MIT
