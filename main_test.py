import unittest
import functions
import main


class MyTestCase(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main.main("-a",1,1), 2)
        self.assertEqual(main.main("-s",1,1), 0)
        self.assertEqual(main.main("-m",1,1), 1)
        self.assertEqual(main.main("-d",1,1), 1)
        self.assertEqual(main.main("-po",1,1), 1)
        self.assertEqual(main.main("-r",1,1), 1)
        self.assertEqual(main.main("-pr",1), False)
        self.assertEqual(main.main("-pr",0), False)
        self.assertEqual(main.main("-pr",2), True)
        self.assertEqual(main.main("-pr",4), False)
        self.assertEqual(main.main("-pr",6), False)
        self.assertEqual(main.main("-pr",8), False)
        self.assertEqual(main.main("-pr",10), False)
        self.assertEqual(main.main("-pr",9), False)
        self.assertEqual(main.main("-pr",11), True)
        self.assertEqual(main.main("-pr",13), True)
        self.assertEqual(main.main("-pr",15), False)





if __name__ == '__main__':
    unittest.main()
