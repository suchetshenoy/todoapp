import unittest
from app import create_app, db
from app.models import List, Item

class TodoAppTestCase(unittest.TestCase):
    def setUp(self):
        # Create a test client and configure it to use an in-memory database
        self.app = create_app({
            'TESTING': True,
            'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'
        })
        self.client = self.app.test_client()

    def tearDown(self):
        # Drop all tables and clean up the session
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
            db.engine.dispose()

    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_list(self):
        response = self.client.post('/list', data={'title': 'Test List'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
        with self.app.app_context():
            lst = List.query.first()
            self.assertIsNotNone(lst)
            self.assertEqual(lst.title, 'Test List')

    def test_delete_list(self):
        with self.app.app_context():
            lst = List(title='List to Delete')
            db.session.add(lst)
            db.session.commit()
            lst_id = lst.id

        response = self.client.post(f'/list/{lst_id}/delete', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
        with self.app.app_context():
            lst = List.query.get(lst_id)
            self.assertIsNone(lst)

    def test_add_item(self):
        with self.app.app_context():
            lst = List(title='My List')
            db.session.add(lst)
            db.session.commit()
            lst_id = lst.id

        response = self.client.post(f'/list/{lst_id}/item', data={'item_name': 'Test Item'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
        with self.app.app_context():
            item = Item.query.first()
            self.assertIsNotNone(item)
            self.assertEqual(item.item_name, 'Test Item')
            self.assertEqual(item.list_id, lst_id)

    def test_toggle_item(self):
        with self.app.app_context():
            lst = List(title='My List')
            db.session.add(lst)
            db.session.commit()
            
            item = Item(list_id=lst.id, item_name='Task 1', item_status=False)
            db.session.add(item)
            db.session.commit()
            item_id = item.id

        response = self.client.post(f'/item/{item_id}/toggle', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
        with self.app.app_context():
            item = Item.query.get(item_id)
            self.assertTrue(item.item_status)

if __name__ == '__main__':
    unittest.main()