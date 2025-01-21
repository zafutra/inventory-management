import unittest
from app.inventory import update_stock

class TestInventory(unittest.TestCase):
    def test_update_stock(self):
        data = pd.DataFrame({'stock': [10]}, index=['P001'])
        updated_data = update_stock(data, 'P001', 5)
        self.assertEqual(updated_data.loc['P001', 'stock'], 5)

if __name__ == '__main__':
    unittest.main()
