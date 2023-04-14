import requests,pytest
import json

class Test_port:

    @staticmethod
    def  get_token():
        url = "https://api.weixin.qq.com/cgi-bin/token"
        data = {
            "grant_type":"client_credential",
            "appid":"wx6b11b3efd1cdc290",
            "secret":"106a9c6157c4db5f6029918738f9529d"
        }
        rep = requests.get(url=url,params=data)
        print(rep.json())

    def setup_class(self):
        self.access_token=Test_port.get_token()

    def test_edit_flag(self):
        url = f"https://api.weixin.qq.com/cgi-bin/tags/update?access_token={self.access_token}"
        data = {"tag":{"id":134,"name":"广东人"}}
        rep=requests.post(url=url,json=data)
        print(rep)


if __name__ == "__main__":
   pytest.main("-vs")
   Test_port.get_token()
