import pytest
from views import post_manager

class TestPostManagerClass:
    def test_first(self):
        post_manager.TEST_MODE = True

if __name__ == '__main__':
    pytest.main()
