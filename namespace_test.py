import namespace
import unittest

class NamespaceTestCase(unittest.TestCase):

  def testNearestNamespace(self):
    closest = namespace.GetClosestNamespaceForSymbol(
      'aaa.bbb.ccc',
      set(['aaa.bbb.ccc.ddd', 'aaa.bbb.ccc.eee']))
    self.assertIsNone(closest)

    closest = namespace.GetClosestNamespaceForSymbol(
      'aaa.bbb.ccc',
      set(['aaa.bbb', 'aaa.bbb.ccc.ddd']))
    self.assertEquals('aaa.bbb', closest)

  def testGetNamespaceParts(self):
    self.assertEquals(
      ['goog', 'string', 'startsWith'],
      namespace.GetNamespaceParts('goog.string.startsWith'))

  def testIsSymbolPartOfNamespace(self):
    self.assertTrue(
      namespace.IsSymbolPartOfNamespace(
        'goog.string.startsWith',
        'goog.string'))

    self.assertFalse(
      namespace.IsSymbolPartOfNamespace(
        'goog.string',
        'goog.string.startsWith'))

    self.assertTrue(
      namespace.IsSymbolPartOfNamespace(
        'aaa.bbb.foo',
        'aaa.bbb.foo'))


if __name__ == '__main__':
    unittest.main()



