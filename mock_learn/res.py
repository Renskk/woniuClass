import requests

class Users:
    def list_users(self):
        url = 'http://reqres.in'
        resp = requests.get(url + '/api/users?page=2')
        return resp
