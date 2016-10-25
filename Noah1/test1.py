#!/usr/bin/env python
"""Test task1."""
from task1 import LoginUser


def main():
    """Test task1 main method."""
    user = LoginUser('5504115007', '5504115007')
    page = user.get_page()
    assert '【赖强】' in page
    print('test pass')


if __name__ == '__main__':
    main()