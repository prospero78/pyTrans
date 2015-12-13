# -*- coding: utf-8 -*-
'''
Главный запускающий файл для клиента.
'''

from pakTransClient.modTransClient import clsTransClient

def main():
    app = clsTransClient()
    app.run()
    
if __name__=='__main__':
    main()
    print('=end=')