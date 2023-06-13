menu = {
    # 한식
    "한식": {
        "반계탕": 5500,
        "육개장": 5000,
        "돈까스김치나베": 5000,
        "알김치돌솥밥": 5000,
        "김치찌개": 5000,
    },
    # 분식
    "분식": {
        "비빔돈까스": 6000,
        "돈까스": 5500,
        "치즈돈까스": 6000,
        "참치마요덮밥": 5000,
        "짜장탕수육세트": 5500,
        "고추장계란밥": 4500,
        "짜장면": 4500,
        "짬뽕탕수육세트": 5500,
        "탕수덮밥": 5000,
        "제육덮밥": 5500,
        "간장계란밥": 4500,
        "짜장덮밥": 5000,
    },
    # 면류
    "면류": {
        "쫄면": 4000,
        "떡라면": 3800,
        "카레치즈라면": 4000,
        "짬뽕": 4500,
        "만두백반": 4500,
        "치즈라면": 3800,
        "라면": 3500,
        "물냉면": 5000,
        "떡만두라면": 4000,
        "만두라면": 3800,
        "라볶이": 5500,
    },

    # 추가
    "추가": {
        "계란후라이": 500,
    },
}

menu_sum = 0
answer = "네"

while answer == "네":
    food_category = input("한식, 분식, 면류, 추가 중에서 선택하세요: ")  # 선택 카테고리 하나
    if food_category in menu:
        category_menu = menu[food_category]
        input_menu = input("메뉴를 선택하세요: ")  # 메뉴 선택

        if input_menu in category_menu:
            menu_sum += category_menu[input_menu]
        else:
            print("다른 메뉴를 선택해주세요.")
    else:
        print("올바른 카테고리를 선택해주세요.")
    answer = input("주문을 하시겠습니까? (네/아니오): ")

    if answer != "네":
        break

    additional_order = input("추가 주문하시겠습니까? (네/아니오): ")
    if additional_order != "네":
        break

# 결제 코드

payment_method = input("결제 방법을 선택하세요. (현금/카드): ")  # 결제 현금oror카드
if payment_method == "현금":
    print("현금으로 결제하셨습니다.")
elif payment_method == "카드":
    print("카드로 결제하셨습니다.")
else:
    print("결제 방법을 선택해주세요.") 

print("결제 금액은", menu_sum, "원입니다.") # 계산 끝
print("식권을 발급받으세요")                # 식권발급
