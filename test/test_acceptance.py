import unittest
import os
import shutil
from subprocess import call

class TestAcceptance(unittest.TestCase):

    PATH = '.mirror'
    BARE_PATH = '.bare'
    REPO = 'duksis/mirror-test-origin'

    def cleanup(self):
        if os.path.exists(self.PATH):
            shutil.rmtree(self.PATH)

    def test_mirroring(self):
        self.cleanup()
        self.assertEqual(os.path.exists(self.PATH), False)

        self.assertEqual(call(["./script/github_mirror", self.REPO, self.REPO]), 0)

        self.assertEqual(os.path.exists(self.BARE_PATH), False)
        self.assertEqual(os.path.exists(self.PATH), True)
        self.cleanup()

if __name__ == '__main__':
    unittest.main()
