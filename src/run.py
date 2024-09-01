import unittest

if __name__=="main":
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover(start_dir='.', pattern='test_*.py')
    test_suite_runner = unittest.TextTestRunner()
    test_suite_runner.run(test_suite)