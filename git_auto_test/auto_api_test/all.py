import os
import time
import pytest


if __name__ == '__main__':
    pytest.main()
    time.sleep(2)
    os.system("allure generate ./temps -o ./reports --clean")














