import pytest


@pytest.fixture(scope='function', params=['郭静', '周明', '王磊'])
def my_fixture(request):
    print('前置')
    yield
    print('后置')
    return request.param


class TestMashan:

    def test_01_baidu(self):
        print('测试百度')

    def test_02_huawei(self):
        print('测试华为')
        print('------------' + str(my_fixture))