
from olx_api.authentication import OLXAuth
from olx_api.listings import Listings
from olx_api.users import Users


def integration_test():
    # Test credentials (use environment variables in production)
    username = "samnangsattva@gmail.com"
    password = ""
    device_name = "olx_api_test"

    # Log credentials and headers for debugging (remove in production)
    print("Using credentials:", {"username": username, "password": password, "device_name": device_name})

    # Authenticate with the OLX API
    auth = OLXAuth(username=username, password=password, device_name=device_name)
    token = auth.login()
    print("Token received:", token)

    # Instantiate API wrappers using the token
    items_api = Listings(token=token)
    users_api = Users(token=token)

    # Retrieve active listings for the given user (replace 'snezabnf' with a valid username)
    try:
        user_listings = users_api.get_active_listings('snezabnf')
        listing_id = user_listings['data'][0]['id']
        print("Active listings for user:", listing_id)
    except Exception as e:
        print("Error fetching active listings:", e)

    # Fetch details for a specific listing (replace 66917628 with a valid listing ID)
    try:
        listing = items_api.get_listing(listing_id)
        print("Listing details:", listing['title'])
    except Exception as e:
        print("Error fetching listing details:", e)

    # Upload an image to the listing
    image_path = "./some.jpg"  # Update the file path and extensions
    try:
        # call api
        response = items_api.image_upload(listing_id, [image_path])
        print("Image upload response:", response[0].get('name'))
    except Exception as e:
        print("Error uploading image:", e)


if __name__ == "__main__":
    integration_test()
