import requests
from tkinter import *
import tkinter.ttk as ttk


# 전체 프레임
root = Tk()
root.geometry("800x800")

# 검색 창
find_frame = LabelFrame(root, text="검색입력")
find_frame.pack(padx=15, fill="x")

find_entry = Entry(find_frame)
find_entry.pack(side="left", padx=10, pady=10, fill="x", expand=True, ipady=4)

btn_find = Button(find_frame, text="검색", width=5, padx=5, pady=5)
btn_find.pack(side="right", padx=5)

# 옵션 창

option_frame = LabelFrame(root, text="옵션")
option_frame.pack(fill="x", padx=15 ,anchor="n")

#  ,expand=True, padx=15,

browse_var = IntVar()
browse_std1 = Radiobutton(option_frame, text="쿠팡랭킹순", value=1, variable=browse_var)
browse_std1.select()
browse_std2 = Radiobutton(option_frame, text="낮은가격순", value=2, variable=browse_var)
browse_std3 = Radiobutton(option_frame, text="높은가격순", value=3, variable=browse_var)
browse_std4 = Radiobutton(option_frame, text="판매량순", value=4, variable=browse_var)
browse_std5 = Radiobutton(option_frame, text="최신순", value=5, variable=browse_var)

browse_std1.pack(side="left")
browse_std2.pack(side="left")
browse_std3.pack(side="left")
browse_std4.pack(side="left")
browse_std5.pack(side="left")

# 필터 옵션
filter_frame = Frame(root)
filter_frame.pack(fill="x", padx=15, anchor="n")


chk_var = IntVar()
chk_option = Checkbutton(filter_frame, text="광고상품제거", variable=chk_var)

chk_var2 = IntVar()
chk_option2 = Checkbutton(filter_frame, text="무료배송만보기", variable=chk_var2)

chk_option.pack(side="left")
chk_option2.pack(side="left")


# 상품 리스트 프레임

list_frame = Frame(root)
list_frame.pack()


item_list = ttk.Treeview(list_frame, columns=["one", "two", "three"], displaycolumns=["one", "two", "three"])
item_list.column()

item_list.pack()






root.resizable(False, False)
root.mainloop()
