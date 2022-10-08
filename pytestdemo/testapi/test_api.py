import pytest

class TestApi:

    @pytest.mark.parametrize('name, age', [['张三', '18'],['周四', '45']])
    def test_01_baidu(self, name, age):
        print(name, age)