import unittest
import main


class GetNumbersTestCase(unittest.TestCase):
    def setUp(self):
        self.client = main.app.test_client()
        main.numbers.clear()

    def test_get_numbers_returns_empty_list(self):
        response = self.client.get("/getnumbers")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), [])

    def test_get_numbers_returns_added_numbers(self):
        main.numbers.append(42)
        response = self.client.get("/getnumbers")
        self.assertEqual(response.status_code, 200)
        self.assertIn(42, response.get_json())


class AddNumberTestCase(unittest.TestCase):
    def setUp(self):
        self.client = main.app.test_client()
        main.numbers.clear()

    def test_add_number_success(self):
        response = self.client.post("/addnumber", json={"number": 5})
        self.assertEqual(response.status_code, 200)
        self.assertIn(5, main.numbers)

    def test_add_number_appends_multiple(self):
        self.client.post("/addnumber", json={"number": 1})
        self.client.post("/addnumber", json={"number": 2})
        self.assertEqual(main.numbers, [1, 2])


if __name__ == '__main__':
    unittest.main()