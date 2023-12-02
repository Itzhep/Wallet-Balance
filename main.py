import requests

# URL API
api_url = 'https://apilist.tronscanapi.com/api/accountv2'

# آدرس کیف پول TRX مورد نظر
wallet_address = 'ادرس کیف پول شما'

# ایجاد پارامترهای درخواست
params = {'address': wallet_address}

# ارسال درخواست GET به API
response = requests.get(api_url, params=params)

# بررسی موفقیت درخواست
if response.status_code == 200:
    # دریافت داده‌های JSON بازگشتی از API
    data = response.json()

    # چک کردن اگر داده‌های مورد نظر وجود دارند
    if 'balance' in data:
        # دریافت مقدار balance و پرینت آن
        balance = data['balance']
        print(f'Balance of {wallet_address}: {balance} TRX')
    else:
        print('Balance data not found in the API response.')
else:
    print('Failed to retrieve data from the API.')
