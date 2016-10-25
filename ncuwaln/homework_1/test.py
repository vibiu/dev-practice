from request_worm import get_page as get_page_by_urllib
from worm_cookie import get_page as get_page_by_selenium

choice = input("输入选择(urllib/selenium): ")
if choice == "urllib":
    print(get_page_by_urllib())
    print("urllib successful")

elif choice == "selenium":
    print(get_page_by_selenium())
    print("selenium successful")

else:
    print("没有这个选项")
