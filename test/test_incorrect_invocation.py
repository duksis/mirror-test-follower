import unittest
from subprocess import Popen, PIPE

class TestIncorrectInvocation(unittest.TestCase):

    def test_error_message(self):
        expected_message = "Accepts only 2 arguments in form of 'githubuser/reponame'\n"
        process = Popen(["./script/github_mirror"], stdout=PIPE)

        output, error = process.communicate()

        self.assertEqual(output, expected_message)


    def test_return_code(self):
        process = Popen(["./script/github_mirror"], stdout=PIPE)
        process.communicate()

        self.assertEqual(process.returncode, 1)


    def test_return_code_with_one_argument(self):
        process = Popen(["./script/github_mirror", "arg1"], stdout=PIPE)
        process.communicate()

        self.assertEqual(process.returncode, 1)


    def test_return_code_with_three_arguments(self):
        process = Popen(["./script/github_mirror", "arg1", "arg2", "arg3"], stdout=PIPE)
        process.communicate()

        self.assertEqual(process.returncode, 1)


if __name__ == '__main__':
    unittest.main()
