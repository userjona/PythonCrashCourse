# 11-1 City, Country
# def city_country(city,country):
#     full = f"{city} {country}"
#     return full.title()

import unittest

# class TestCase(unittest.TestCase):
#     def test_city_country(self):
#         formatted_name = city_country('santiago','chile')
#         self.assertEqual(formatted_name, 'Santiago Chile')

# if __name__ =='__main__':
#     unittest.main()

# 11-2 Population
def city_country(city,country, population=''):
    if population:
        full = f"{city} {country} {population}"
    else:
        full = f"{city} {country}"
    return full.title()

import unittest

class TestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_name = city_country('santiago','chile')
        self.assertEqual(formatted_name, 'Santiago Chile')
    def test_city_population(self):
        formatted_name = city_country('santiago','chile','5000000')
        self.assertEqual(formatted_name, 'Santiago Chile 5000000')

if __name__ =='__main__':
    unittest.main()
