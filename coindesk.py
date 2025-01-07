import requests

def test_coindesk_api():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # print(data)

        bpi = data.get('bpi', {})

        usd = bpi.get('USD')
        gbp = bpi.get('GBP')
        eur = bpi.get('EUR')

        print(usd)
        print("==============")
        print(gbp)
        print("===============")
        print(eur)

        if usd and gbp and eur:
            print("USD, GBP and EUR BPIs present")

            if gbp.get('description') == 'British Pound Sterling':
                print("GBP description is correct")
            else:
                print("GBP description is incorrect")

        else:
            print("BPI missing")


test_coindesk_api()
