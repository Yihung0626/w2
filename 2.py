# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 08:29:49 2024

@author: student
"""
def collect_personal_data():
    print("請輸入您的個人資料：")
    name = input("姓名: ")
    age = int(input("年齡: "))
    height = float(input("身高（米）: "))
    favorite_color = input("喜愛的顏色: ")
    return name, age, height, favorite_color

def generate_summary(name, age, height, favorite_color):
    summary = f"{name}, {age}歲, 身高{height}米, 喜愛的顏色是{favorite_color}。"
    return summary

def main():
    name, age, height, favorite_color = collect_personal_data()
    summary = generate_summary(name, age, height, favorite_color)
    print("\n個人資料摘要:")
    print(summary)

if __name__ == "__main__":
    main()

