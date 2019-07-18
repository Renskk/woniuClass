from meClass.mock_learn.res import Users
from unittest.mock import patch
import unittest

class TestUsers(unittest.TestCase):

    @patch('meClass.mock_learn.res.Users.list_users', autospec=True)
    def test_user_set(self, mock_list_users):
        mock_list_users.return_value.status_code = 200
        mock_list_users.return_value.json.return_value = {
            "data":[
                {
                    "id": 5,
                    "first_name": "eve"
                }
            ]
        }
        u = Users()
        resp = u.list_users()
        assert resp.status_code == 200
        self.assertEqual(resp.json()['data'][0]['id'], 5)

if __name__ == '__main__':
    unittest.main()
