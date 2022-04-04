import requests


class YaUploader:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return{
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_path(self, name):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": name, "overwrite": "true"}
        response = requests.put(upload_url, headers=headers, params=params)
        if response.status_code == 201:
            print('Created')
        elif response.status_code == 204:
            print('No Content')
        elif response.status_code == 500:
            print('Internal Server Error')
        return response.status_code