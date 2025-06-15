from kiteconnect import KiteConnect

# Replace with your actual API key and secret
api_key = "xf4le4si393zxzfn"
api_secret = "hh2vk9sw6enc0jgpp1q45mvalkbcfxcs"

kite = KiteConnect(api_key=api_key)

# STEP 1: Print login URL
print("Login URL:", kite.login_url())
