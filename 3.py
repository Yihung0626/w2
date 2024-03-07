# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 08:36:48 2024

@author: student
"""

while True:
    try:
        # 讓使用者輸入一個整數
        user_input = input("請輸入一個整數：")
        
        # 如果使用者輸入空字符串，則提示重新輸入
        if user_input.strip() == "":
            print("請輸入有效的整數，不得為空字符串。")
            continue

        number = int(user_input)

        # 判斷是否為偶數
        if number % 2 == 0:
            print(f"{number} 是偶數。")
        else:
            print(f"{number} 不是偶數。")
        
        # 程式執行成功，跳出迴圈
        break

    except ValueError:
        print("請輸入有效的整數，不得含有非數字字符。")
