from kiteconnect import KiteConnect

# Replace with your actual API key and secret
api_key = "xf4le4si393zxzfn"
api_secret = "xmgt9d7ob7rivmooxj56dstpszbocdxd"

kite = KiteConnect(api_key=api_key)

# STEP 1: Print login URL
print("Login URL:", kite.login_url())