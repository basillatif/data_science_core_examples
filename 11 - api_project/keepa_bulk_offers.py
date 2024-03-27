import keepa
import asyncio

#INSERT access key
accesskey = ''
api = keepa.Keepa(accesskey)

#list of asins
asins = ['B001NYTR7O', 'B000HRMAR2', 'B07TF6GNDZ', 'B008KA4UOE', 'B07PW1SVHM', 'B07RC914D5', 'B000QCU9T4', 'B0CD3Q77MT', 'B0142YXY8O', 'B000XEHYSE', 'B0CD3TFSGX', '3598611188', 'B0CGV6V5LL', 'B000001DUR', 'B0CJR9F9YP', 'B0CGV8CLKL', 'B0CFHGDLWC', 'B0CFH9C1RS', 'B004OBY9N0', 'B0969H25W5', 'B086QPY295', 'B000E1KMJE', 'B0789VXS6K', 'B0789Y63QB', 'B07MT4QXTL', 'B0CGV95W32', 'B0CGV98TDH', 'B0CD3SLPCM', 'B086PDK29G', 'B07ZXPC3KV', 'B09MW5QPP2', 'B093CFJXVX', 'B0789Y1Q8J', 'B0CG9KNNJB', 'B0CG9JB2FY', 'B0CG9HGN9J', 'B0CG9HC93G', 'B0CG9G5PHL', 'B08VVT6T3S', 'B086PHSFSC', 'B000IZJ1KC', 'B08KZWD7QT', 'B086PQD9JB', 'B08KZY1N3Y', 'B08KZQKG8V', 'B08KZVGW72', 'B08BHVSN63', 'B009DKCACO', 'B000JCF19E', 'B0BZWJV3MQ']
single_asin = ['B001NYTR7O']

#return 
products = api.query(single_asin, offers=20)
product = products[0]
#print(product)
offers = product['offers']
print(offers)

# each offer contains the price history of each offer
offer = offers[0]
print(offer)
csv = offer['offerCSV']

# convert these values to numpy arrays
times, prices = keepa.convert_offer_history(csv)
print(times)
print(prices)
# for a list of active offers, see
indices = product['liveOffersOrder']

# with this you can loop through active offers:
indices = product['liveOffersOrder']
offer_times = []
offer_prices = []
exit()
for index in indices:
    csv = offers[index]['offerCSV']
    times, prices = keepa.convert_offer_history(csv)
    offer_times.append(times)
    offer_prices.append(prices)

# you can aggregate these using np.hstack or plot at the history individually
import matplotlib.pyplot as plt
for i in range(len(offer_prices)):
    plt.step(offer_times[i], offer_prices[i])
plt.show()