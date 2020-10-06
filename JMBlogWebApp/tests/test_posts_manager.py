import pytest
from views import post_manager

class TestPostManagerClass:
    def test_first(self):
        post_manager.test_mode = True

if __name__ == '__main__':
    pytest.main()
