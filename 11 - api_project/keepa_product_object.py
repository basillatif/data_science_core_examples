import keepa
import asyncio
#https://keepaapi.readthedocs.io/en/latest/api_methods.html
# This script takes a single ASIN as an input and returns


#access key
accesskey = ''
api = keepa.Keepa(accesskey)

# Single ASIN query - pick a product
products = api.query('B0CCST7CCV') # returns list of product data
print(products)
print(type(products))
print(products[0])
### Plot result (requires matplotlib)
keepa.plot_product(products[0])

