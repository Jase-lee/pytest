import time
import pytest

class TestLogout:

    @pytest.mark.smoke
    def test_logout(self):
        time.sleep(3)
        print("登出测试")