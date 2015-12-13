# -*- coding: utf-8 -*-
"""
Запускающий файл для всего сервера.
Содержит необходимые подклассы.
"""

from pakTransServ.modTransServ import clsTransServ


def main():
    """
    Главная запускающая функция
    для всего приложения.
    """
    app = clsTransServ()
    app.run()

if __name__ == '__main__':
    main()
