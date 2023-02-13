import pytest
import requests


class TestBooksAPI:

    API_URL = 'https://simple-books-api.glitch.me'

    def get_token(self):
        if hasattr(self, 'token'):
            return self.token
        info = {
            "clientName": "Marcelfga",
            "clientEmail": "madiin@example.com"
            }
        r = requests.post(f'{self.API_URL}/api-clients/', json=info)
        self.token = r.json()["accessToken"]
        return self.token

    # def test_status(self):
    #     r = requests.get(f'{self.API_URL}/status')
    #     assert r.status_code == 200
    #     response_dictionary = r.json()
    #     assert response_dictionary["status"] == "OK"
    #
    # def test_books_list(self):
    #     r = requests.get(f'{self.API_URL}/books')
    #     assert r.status_code == 200
    #     assert len(r.json()) == 6
    #
    # def test_fiction_books(self):
    #     payload = {'type': 'fiction'}
    #     r = requests.get(f'{self.API_URL}/books', params=payload)
    #     assert r.status_code == 200
    #     assert len(r.json()) == 4
    #     for item in r.json():
    #         assert item["type"] == "fiction"

    def test_order(self):
        self.get_token()
        # print(self.token)
        payload = {
                "bookId": 1,
                "customerName": "Marcela"
                }
        headers = {"authorization": f'Bearer {self.token}'}
        r = requests.post(f'{self.API_URL}/orders', json=payload, headers=headers)
        assert r.status_code == 201
        assert r.json()['created']