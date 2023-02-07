import os
import time
import pytest


if __name__ == '__main__':
    print('testyiha')
    pytest.main()
    time.sleep(1)
    os.system("allure generate ./temps -o ./reports --clean")














