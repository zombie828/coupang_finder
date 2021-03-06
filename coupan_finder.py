import requests
from bs4 import BeautifulSoup
from tkinter import *
import tkinter.ttk as ttk
import re

def create_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

# 상품 검색
def search_goods():
    word = find_entry.get()
    url = "https://www.coupang.com/np/search?component=&q={}&channel=user".format(word)
    print(url)
    soup = create_soup(url)

    # 상품 정보 가져오기
    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

    for idx, item in enumerate(items):

        # 상품 이름 출력
        name = [item.find("div", attrs={"class":"name"}).get_text().replace(",",""),0,0]
        item_list.insert("", END, text=idx+1, values=name)
        # print(name)








# 전체 프레임
root = Tk()
root.geometry("800x800")

# 검색 창
find_frame = LabelFrame(root, text="검색입력")
find_frame.pack(padx=15, fill="x")

find_entry = Entry(find_frame)
find_entry.pack(side="left", padx=10, pady=10, fill="x", expand=True, ipady=4)

btn_find = Button(find_frame, text="검색", width=5, padx=5, pady=5, command=search_goods)
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

list_frame = Frame(root, padx=15)
list_frame.pack(fill="both", expand=True)

list_scrollbar = Scrollbar(list_frame)
list_scrollbar.pack(fill="y", side="right")


item_list = ttk.Treeview(list_frame, columns=["one", "two", "three"], displaycolumns=["one", "two", "three"], selectmode="browse")

item_list.column("#0", width=60, stretch=False)
item_list.heading("#0", text="항목")

item_list.column("#1")
item_list.heading("#1", text="상품명")

item_list.column("#2", width=150, stretch=False)
item_list.heading("#2", text="가격")

item_list.column("#3", width=120, stretch=False)
item_list.heading("#3", text="별점")

item_list.pack(fill="both", expand=True)



item_list.config(yscrollcommand=list_scrollbar.set)

list_scrollbar.config(command=item_list.yview)





# 세부사항 프레임

detail_frame = Frame(root, padx=15, background="red")
detail_frame.pack(side="left")

picture = Label(detail_frame, width=50, height=20)
picture.pack()



txt_frame = Frame(root, padx=30, background="red")
txt_frame.pack(side="right")

txt = Text(txt_frame,height=5)
txt.pack()





root.resizable(False, False)
root.mainloop()
