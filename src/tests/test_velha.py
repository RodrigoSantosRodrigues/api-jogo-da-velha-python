import unittest
import json
from ..app import create_app

class VelhaTest(unittest.TestCase):
    """Tesst Velha

    Velha Test Case
    """
    def setUp(self):
        """
        Test Setup
        """
        self.app = create_app("testing")
        self.client = self.app.test_client
    
    def test_velha_creation(self):
        """ test velha create starting game """
        res = self.client().post('/v1/api/game', headers={'Content-Type': 'application/json'})
        json_data = json.loads(res.data)
        self.assertTrue(json_data.get('firstPlayer'))
        self.assertTrue(json_data.get('id'))
        self.assertEqual(res.status_code, 201)

    def test_velha_movement_with_different_id(self):
        """ test velha creation movement with different id"""
        res = self.client().post('/v1/api/game', headers={'Content-Type': 'application/json'})
        self.assertEqual(res.status_code, 201)
        json_data = json.loads(res.data)
        data = {
            'id': json_data.get('id'),
            "player": json_data.get('firstPlayer'),
            "position": {
                "x": 0,
                "y": 0
            }
        }
        res = self.client().post('/v1/api/game/30k34454k/movement', headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertTrue(json_data.get('msg'))

    def test_velha_movement_with_game_not_found(self):
        """ test velha creation movement with game not found"""
        data = {
            'id': "c78eb667-8230-43cb-bdca-f88940ed0d40",
            "player": "X",
            "position": {
                "x": 0,
                "y": 0
            }
        }
        res = self.client().post('/v1/api/game/c78eb667-8230-43cb-bdca-f88940ed0d40/movement', headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertTrue(json_data.get('msg'))

    def test_velha_movement_with_not_round(self):
        """ test velha creation movement with not round"""
        res = self.client().post('/v1/api/game', headers={'Content-Type': 'application/json'})
        self.assertEqual(res.status_code, 201)
        json_data = json.loads(res.data)
        if json_data.get('firstPlayer') == 'X':
            round_player = "O"
        else:
            round_player = 'X'
        data = {
            "id": json_data.get('id'),
            "player": round_player,
            "position": {
                "x": 0,
                "y": 0
            }
        }
        url = '/v1/api/game/'+json_data.get('id')+'/movement'
        res = self.client().post(url, headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertTrue(json_data.get('msg'))

if __name__ == "__main__":
    unittest.main()
