import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BMI 计算器")
        self.geometry("300x200")

        self.label1 = tk.Label(self, text="体重（kg）：")
        self.entry1 = tk.Entry(self)
        self.label2 = tk.Label(self, text="身高（m）：")
        self.entry2 = tk.Entry(self)
        self.button = tk.Button(self, text="计算", command=self.on_click)
        self.result = tk.StringVar()
        self.label3 = tk.Label(self, textvariable=self.result)
        self.label4 = tk.Label(self)

        self.label1.pack()
        self.entry1.pack()
        self.label2.pack()
        self.entry2.pack()
        self.button.pack()
        self.label3.pack()
        self.label4.pack()

    def on_click(self):
        w = float(self.entry1.get())
        h = float(self.entry2.get())
        BMI = w / h ** 2
        
        self.result.set("BMI值为：%.2f" % (BMI))
        
        if 18.5 <= BMI <= 23.9:
            self.label4.configure(fg="green")
            self.label4.configure(text="恭喜，您的体重在正常范围内！")
        elif BMI < 18.5:
            self.label4.configure(fg="red")
            self.label4.configure(text="您的体重过低")
        elif 23.9 < BMI <= 27:
            self.label4.configure(fg="orange")
            self.label4.configure(text="您已超重")
        elif 27 < BMI < 40:
            self.label4.configure(fg="red")
            self.label4.configure(text="您的体重指标为肥胖")
        else:
            self.label4.configure(fg="red")
            self.label4.configure(text="您的体重远超正常范围，患相关疾病风险严重增加！")
    
if __name__ == "__main__":
    app = App()
    app.mainloop()
    

