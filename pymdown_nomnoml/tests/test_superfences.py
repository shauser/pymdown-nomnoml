from unittest import TestCase
from typing import Optional
import xml.etree.ElementTree as ET

from ..superfences import nomnoml_to_svg

class SuperfencesTestCase(TestCase):
	def _check_element(self, nomnoml: str, element: Optional[str]):
		svg = nomnoml_to_svg(nomnoml)
		tree = ET.fromstring(svg)
		
		if element is not None:
		    elem = tree.findall('.//{http://www.w3.org/2000/svg}' + element)
		    self.assertIsNotNone(elem)
		    self.assertNotEqual(len(elem), 0)
		    
		    return elem
		
		return tree
	
	def test_text_present(self):
		elem = self._check_element('[a]', 'text')
		self.assertEqual(elem[0].text, 'a')

if __name__ == '__main__':
    unittest.main()
