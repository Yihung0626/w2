# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math

def calculate_circle(radius):
    # 計算圓周長
    circumference = 2 * math.pi * radius
    # 計算圓面積
    area = math.pi * radius ** 2
    return circumference, area

def main():
    # 輸入半徑
    radius = float(input("請輸入圓的半徑: "))
    # 呼叫函數計算圓周長與圓面積
    circumference, area = calculate_circle(radius)
    # 輸出結果
    print("圓周長為: {:.2f}".format(circumference))
    print("圓面積為: {:.2f}".format(area))

if __name__ == "__main__":
    main()
