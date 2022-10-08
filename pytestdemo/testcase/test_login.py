import pytest


class TestLogin:

    code = 666

    def test_04_login(self):
        print("登录测试")

    @pytest.mark.run(order=1)
    @pytest.mark.usermanage
    def test_05_username(self):
        print("用户名测试")

    @pytest.mark.smoke
    def test_02_password(self):
        print("密码测试")
        # assert 1==2

    @pytest.mark.run(order=2)
    @pytest.mark.skipif(code=666)
    def test_03_verification_code(self):
        print("验证码测试")

    @pytest.mark.run(order=3)
    @pytest.mark.skip(reason='不需要勾选协议，所以跳过')
    def test_01_protocol(self):
        print("勾选协议测试")