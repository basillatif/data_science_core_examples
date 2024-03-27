import keepa
import asyncio
#retrieve asings matching some parameter definition


#INSERT your access key here 
accesskey = ''
api = keepa.Keepa(accesskey)

#using async
product_parms = {'author': 'charles duhigg'}
async def main():
    api = await keepa.AsyncKeepa().create(accesskey)
    return await api.product_finder(product_parms)
asins = asyncio.run(main())
print(asins)