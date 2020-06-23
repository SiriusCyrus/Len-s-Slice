import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv', parse_dates=[1])
cart = pd.read_csv('cart.csv', parse_dates=[1])
checkout = pd.read_csv('checkout.csv', parse_dates=[1])
purchase = pd.read_csv('purchase.csv', parse_dates=[1])
print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

visit_cart = pd.merge(visits, cart, how='left')
print(visit_cart)
print(len(visit_cart)) #2052

nullval = visit_cart[visit_cart.cart_time.isnull()]
print(len(nullval)) #1652
print(float((len(nullval))) / (len(visit_cart)) * 100) #80.5068226121

cart_check = pd.merge(cart, checkout, how='left')
#print(cart_check)
nullcheckout = cart_check[cart_check.checkout_time.isnull()]
print(float((len(nullcheckout))) / (len(cart_check)) * 100) #20.9302325581

df1 = pd.merge(visit_cart, checkout, how='left')
all_data = pd.merge(df1, purchase, how='left')
print(all_data.head())

null_check = all_data[all_data.checkout_time.isnull()]
null_purchase = all_data[all_data.purchase_time.isnull()]
print(float((len(null_purchase))) / (len(all_data)) * 100) #73.1688511951

check_purchase = pd.merge(checkout,purchase, how='left')
print(check_purchase)
weak = check_purchase[check_purchase.purchase_time.isnull()]
print(float(len(weak)) / len(check_purchase) * 100) #16.889632107

all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time
print(all_data.time_to_purchase)
print(all_data.time_to_purchase.mean())