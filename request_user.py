import requests
 
def get_user_data(user_id):
    # url = f"https://example.com/users/{user_id}"
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    response = requests.get(url)
    
    # Jika status code bukan 200, return None (mengindikasikan sebuah kesalahan atau data tidak ditemukan)
    if response.status_code != 200:
        return None
 
    # Return data berupa JSON jika request berhasil
    return response.json()

if __name__ == "__main__":
    user_data = get_user_data(1)
    print(user_data)
