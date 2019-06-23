import allure,pytest


class TestAdd:

    @allure.step(title="这是一个描述信息")
    def test_01(self):
        with open("C:\\Users\\Ming123\\Desktop\\app\\scripts\\01.png","rb") as f:
            allure.attach("截图", f.read(), allure.attach_type.PNG)
        # print("------->test01")
        # allure.attach("标题", "具体内容")
        # assert True
