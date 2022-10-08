class TestFirm:

    # 这个在所有用例之前，只执行一次
    def setup_class(self):
        print('在每个类执行前的初始化工作：比如创建日志对象，创建数据库的连接')

    # 在每个用例之前执行一次
    def setup(self):
        print('\n在执行测试用例之前初始化的代码：打开浏览器，加载网页')

    def test_01_baidu(self):
        print("打开百度")

    def test_02_huawei(self):
        print("打开华为")

    def test_03_xiaomi(self):
        print('打开小米')

    def teardown(self):
        print('\n在执行测试用例之后的扫尾代码：关闭浏览器')

    def teardown_class(self):
        print('在每个类执行后的扫尾代码：比如，销毁日志对象，销毁数据库连接')