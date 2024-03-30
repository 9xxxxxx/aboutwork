import tkinter as tk
from tkinter import filedialog

def start_action():
    # 添加开始按钮的逻辑
    output_box.insert(tk.END, "开始...\n")

def stop_action():
    # 添加停止按钮的逻辑
    output_box.insert(tk.END, "停止...\n")

def file_picker():
    filepath.set(filedialog.askopenfilename())
    output_box.insert(tk.END, f"选定文件: {filepath.get()}\n")

# 主窗口
root = tk.Tk()
root.title("软件 GUI")

# 文件路径存储
filepath = tk.StringVar()

# 开始按钮
start_button = tk.Button(root, text="开始", command=start_action)
start_button.pack()

# 文件选择器和输入框
file_picker_button = tk.Button(root, text="选择文件", command=file_picker)
file_picker_button.pack()

file_path_entry = tk.Entry(root, textvariable=filepath, state='readonly')  # 文件路径输入框只读
file_path_entry.pack()

# 两个输入框
input1 = tk.Entry(root)
input1.pack(pady=5)

input2 = tk.Entry(root)
input2.pack(pady=5)

# 输出框
output_box = tk.Text(root, height=10, width=50)
output_box.pack(pady=5)

# 停止按钮
stop_button = tk.Button(root, text="停止", command=stop_action)
stop_button.pack(pady=20)

# 开始事件循环
root.mainloop()
