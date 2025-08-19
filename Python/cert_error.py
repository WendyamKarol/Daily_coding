import certifi, ssl
print(certifi.where())
print(ssl.get_default_verify_paths())
