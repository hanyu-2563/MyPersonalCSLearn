import os
import time
while 1:
    print("欢迎使用BMI计算器")
    time.sleep(0.5)
#Input
    w=float(input("请输入您的体重（kg）："))
    h=float(input("请输入您的身高（m）："))

#Calculation
    BMI=w/h**2

#Output
    print("您的BMI值为：%.2f"%(BMI))
    time.sleep(1)

#Judgment
    if 18.5<=BMI<=23.9:
        print("恭喜，您的体重在正常范围内!")
    elif BMI<18.5:
        print("您的体重过低")
    elif 23.9<BMI<=27:
        print("您已超重")
    elif 27<BMI<40:
        print("您的体重指标为肥胖")
    else:
        print ("您的体重远超正常范围，患相关疾病风险严重增加！")

#Close Tip
    again = input("是否要再计算一次？输入 Y 重新运行，输入 N 退出程序：")
    if again == 'Y' or again == 'y':
        continue
    else:
        break
input("请按回车键退出...")
os._exit(0)


#结束

        