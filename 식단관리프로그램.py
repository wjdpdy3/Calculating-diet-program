from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox

root = Tk()
root.title("식단 계산 프로그램")
root.geometry("+700+200")

##########################################################################

def start():

    if len(gender.get())==0:
        msgbox.showwarning("경고", "성별을 선택해주세요")
        return
    if len(e_weight.get())==0:
        msgbox.showwarning("경고", "체중(kg)을 입력해주세요.")
        return
    if len(e_height.get())==0:
        msgbox.showwarning("경고", "신장(cm)을 입력해주세요")
        return
    if len(age.get())==0:
        msgbox.showwarning("경고", "연령을 선택해주세요.")
        return
    if len(percent.get())==0:
        msgbox.showwarning("경고", "체중 증량/감량 목표를 설정해주세요.")
        return
    if len(active.get())==0:
        msgbox.showwarning("경고", "활동량을 선택해주세요.")

    n_weigth = int(e_weight.get())
    n_height = int(e_height.get())
    n_age = int(age.get())


    if gender.get() == "남자":
        basal_metabolism = 66 + (13.7*n_weigth) + (5*n_height) - (6.8*n_age)
        e_metabolism.delete(0,END)
        e_metabolism.insert(0,str(round(basal_metabolism))+" kcal")
    elif gender.get() == "여자":
        basal_metabolism = 655 + (9.6 * n_weigth) + (1.7*n_height) - (4.7*n_age)
        e_metabolism.delete(0,END)
        e_metabolism.insert(0,str(round(basal_metabolism))+" kcal")

    # opt_active = ["거의없음", "조금있다", "보통", "꽤 있다", "아주 많다"]
    if active.get()=="거의없다":
        basal_metabolism *= 1.2
    elif active.get()=="조금있다":
        basal_metabolism *= 1.375
    elif active.get() == "보통":
        basal_metabolism *= 1.55
    elif active.get() == "꽤 있다":
        basal_metabolism *= 1.725
    elif active.get() == "아주 많다":
        basal_metabolism *= 1.9



    if percent.get() == "-20%":
        goal_calorie = basal_metabolism - basal_metabolism * 0.2
    elif percent.get() == "-10%":
        goal_calorie = basal_metabolism - basal_metabolism * 0.1
    elif percent.get() == "+10%":
        goal_calorie = basal_metabolism + basal_metabolism * 0.1
    elif percent.get() == "+20%":
        goal_calorie = basal_metabolism + basal_metabolism * 0.2

    e_day_calorie.delete(0,END)
    e_day_calorie.insert(0,str(round(goal_calorie))+" kcal")

    n_carbohydrate = goal_calorie * 0.5 / 4
    n_protein = goal_calorie * 0.3 / 4
    n_fat = goal_calorie * 0.2 / 9

    total_carbohydrate_e.delete(0,END)
    total_protein_e.delete(0,END)
    total_fat_e.delete(0,END)
    total_carbohydrate_e.insert(0,"{:.1f}".format(n_carbohydrate)+"g")
    total_protein_e.insert(0,"{:.1f}".format(n_protein)+"g")
    total_fat_e.insert(0,"{:.1f}".format(n_fat)+"g")

    one_carbohydrate_e.delete(0,END)
    one_protein_e.delete(0,END)
    one_fat_e.delete(0,END)
    one_carbohydrate_e.insert(0,"{:.1f}".format(n_carbohydrate/meals_num_var.get())+"g")
    one_protein_e.insert(0,"{:.1f}".format(n_protein/meals_num_var.get())+"g")
    one_fat_e.insert(0,"{:.1f}".format(n_fat/meals_num_var.get())+"g")




##########################################################################

# 기초대사량, 하루 목표 칼로리
##########################################################################
metabolism_frame = Frame(root)
metabolism_frame.pack(padx=5, pady=(20, 5), ipady=5)

label_metabolism = Label(metabolism_frame, text="기초대사량")
label_metabolism.pack(side="left", padx=5, pady=5)
e_metabolism = Entry(metabolism_frame, width=10)
e_metabolism.pack(side="left", padx=5, pady=5)

e_day_calorie = Entry(metabolism_frame, width=10)
e_day_calorie.pack(side="right", padx=5, pady=5)
label_calorie = Label(metabolism_frame, text="하루 목표 칼로리")
label_calorie.pack(side="right", padx=5, pady=5)

##########################################################################


# 총 탄수화물/단백질/지방
##########################################################################
total_meal_frame = LabelFrame(root, text="하루총량")
total_meal_frame.pack(padx=5, pady=5, ipady=10)

# 총 탄수화물
label_total_carbohydrate = Label(total_meal_frame, text="탄수화물")
label_total_carbohydrate.pack(side="left")
total_carbohydrate_e = Entry(total_meal_frame, width=10)
total_carbohydrate_e.pack(side="left", padx=5, pady=5)

# 총 단백질
label_total_protein = Label(total_meal_frame, text="단백질")
label_total_protein.pack(side="left")
total_protein_e = Entry(total_meal_frame, width=10)
total_protein_e.pack(side="left", padx=5, pady=5)

# 총 지방
label_total_fat = Label(total_meal_frame, text="지방")
label_total_fat.pack(side="left")
total_fat_e = Entry(total_meal_frame, width=10)
total_fat_e.pack(side="left", padx=5, pady=5)
##########################################################################


# 끼니별 탄수화물/단백질/지방
##########################################################################
one_meal_frame = LabelFrame(root, text="끼니별 양")
one_meal_frame.pack(padx=5, pady=5, ipady=10)

# 끼니별 탄수화물
label_one_carbohydrate = Label(one_meal_frame, text="탄수화물")
label_one_carbohydrate.pack(side="left")
one_carbohydrate_e = Entry(one_meal_frame, width=10)
one_carbohydrate_e.pack(side="left", padx=5, pady=5)

# 끼니별 단백질
label_one_protein = Label(one_meal_frame, text="단백질")
label_one_protein.pack(side="left")
one_protein_e = Entry(one_meal_frame, width=10)
one_protein_e.pack(side="left", padx=5, pady=5)

# 끼니별 지방
label_one_fat = Label(one_meal_frame, text="지방")
label_one_fat.pack(side="left")
one_fat_e = Entry(one_meal_frame, width=10)
one_fat_e.pack(side="left", padx=5, pady=5)
##########################################################################

sp = ttk.Separator(root, orient="horizontal")
sp.pack(fill="both", pady=(20, 10))

# 기본 정보
##########################################################################
profile_frame = LabelFrame(root, text="기본정보")
profile_frame.pack(padx=5, pady=5)

# 성별
lbl_gender = Label(profile_frame, text="성별")
lbl_gender.grid(row=0, column=0, padx=(5, 0), pady=5)

opt_gender = ["남자", "여자"]
gender = ttk.Combobox(profile_frame, state="readonly", values=opt_gender, width=5)
gender.grid(row=0, column=1, padx=5, pady=5)

# 나이
lbl_age = Label(profile_frame, text="나이")
lbl_age.grid(row=0, column=2, padx=(5, 0), pady=5)

opt_age = list(range(100))
age = ttk.Combobox(profile_frame, state="readonly", values=opt_age, width=5)
age.grid(row=0, column=3, padx=5, pady=5)

# 체중
lbl_weight = Label(profile_frame, text="체중")
lbl_weight.grid(row=1, column=0, padx=(5, 0), pady=5)

e_weight = Entry(profile_frame, width=8)
e_weight.grid(row=1, column=1, padx=5, pady=5)

# 신장
lbl_height = Label(profile_frame, text="신장")
lbl_height.grid(row=1, column=2, padx=(5, 0), pady=5)

e_height = Entry(profile_frame, width=8)
e_height.grid(row=1, column=3, padx=5, pady=5)

# 활동량
lbl_active = Label(profile_frame, text="활동량")
lbl_active.grid(row=0, column=4, padx=(5, 0), pady=5)

opt_active = ["거의없다", "조금있다", "보통", "꽤 있다", "아주 많다"]
active = ttk.Combobox(profile_frame, state="readonly", values=opt_active, width=5)
active.grid(row=0, column=5, padx=5, pady=5)

# 증량/감량
lbl_percent = Label(profile_frame, text="증량/감량")
lbl_percent.grid(row=1, column=4, padx=(5, 0), pady=5)

opt_percent = ["-20%", "-10%", "+10%", "+20%"]
percent = ttk.Combobox(profile_frame, state="readonly", values=opt_percent, width=5)
percent.grid(row=1, column=5, padx=5, pady=5)

# 끼니수
lbl_meals_num = Label(profile_frame, text="끼니수")
lbl_meals_num.grid(row=2, column=0, padx=(5, 0), pady=5)

meals_num_var = IntVar()
btn_meals1 = Radiobutton(profile_frame, text="두번", value=2, variable=meals_num_var)
btn_meals2 = Radiobutton(profile_frame, text="세번", value=3, variable=meals_num_var)
btn_meals3 = Radiobutton(profile_frame, text="네번", value=4, variable=meals_num_var)
btn_meals1.select()

btn_meals1.grid(row=2, column=1)
btn_meals2.grid(row=2, column=2)
btn_meals3.grid(row=2, column=3)
##########################################################################

# 실행 프레임
##########################################################################
frame_run = Frame(root)
frame_run.pack(fill="x")

btn_close = Button(frame_run, text="닫기", padx=5, pady=5, width=12 ,command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)
btn_start = Button(frame_run, text="시작", padx=5, pady=5, width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)
##########################################################################


root.resizable(False, False)
root.mainloop()
