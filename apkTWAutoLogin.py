import requests, re, os
from bs4 import BeautifulSoup

class apktw:
    def __init__(self):
        self.session = requests.session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0'
            }

    def login(self, usr, pw):
        rst = self.session.post('https://apk.tw/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1',
                          headers=self.headers,
                          data={
                                'username': usr,
                                'password': pw,
                                'quickforward': 'yes',
                                'handlekey': 'ls'
                              })
        if re.search('登錄失敗', rst.text):
            return False
        else:
            return True

    def signUp(self):
         
        pge = self.session.get('https://apk.tw', headers=self.headers)
        soup = BeautifulSoup(pge.text, 'html.parser')
        try:
            ajaxURL = 'https://apk.tw/' + soup.find('a', {'id': 'my_amupper'})['onclick'].split("'")[1]
            rst = self.session.get(ajaxURL, headers=self.headers)
            if not rst.status_code == 200:
                print('Signed Failed')
                return False
        except:
            pass
        print('Has Signed')
        return True
        
if __name__ == '__main__':
    a = apktw()
    a.login(os.environ['USR'], os.environ['PASS'])
    a.signUp()   
