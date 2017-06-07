
#做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）
import uuid


def create_card(number):
    for i in range (0,number):
        cardID = str(uuid.uuid4())
        print(cardID)
    return


create_card(18)


