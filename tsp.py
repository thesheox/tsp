import math

# تابع اصلی برای حل مسئله فروشنده دوره‌گرد
def trvel(n, w, p):
    k = int(math.pow(2, (n - 1)))  # تعداد زیرمجموعه‌های ممکن از شهرها برابر با 2^(n-1)
    D = [[0] * k for _ in range(n)]  # ماتریس برای ذخیره کمینه هزینه‌ها، n سطر و k ستون

    # مقداردهی اولیه: هزینه رفتن از هر شهر i به شهر 0
    for i in range(1, n):
        D[i][0] = w[i][0]
    
    # حلقه برای پر کردن ماتریس D با استفاده از برنامه‌ریزی پویا
    for i in range(1, n - 1):
        for subset in range(1, k):
            # اگر تعداد شهرهای موجود در زیرمجموعه برابر با i باشد
            if len_subset(subset) == i:
                for v in range(1, n):
                    # اگر شهر v-1 در زیرمجموعه نباشد
                    if not haveI(subset, v - 1):
                        # محاسبه کمترین هزینه برای سفر از شهر v به مجموعه شهرهای subset
                        D[v][subset] = min_v(v, w, D, subset, n)
                        # ذخیره شهر بعدی که باید بازدید شود
                        p[v][subset] = l

    # محاسبه کمینه هزینه برای برگشت به شهر مبدأ
    min_cycle = min_v(0, w, D, k - 1, n)
    # ذخیره مسیر بازگشت
    p[0][k - 1] = l

    # بازگشت کمترین هزینه سفر دوره‌ای
    return min_cycle

# تابع برای شمارش تعداد بیت‌های 1 در نمایش باینری یک عدد
def len_subset(j):
    count = 0
    # استفاده از الگوریتم برای شمارش تعداد بیت‌های 1
    while j != 0:
        j = j & (j - 1)
        count += 1
    return count

# تابع برای بررسی حضور یا عدم حضور یک شهر در زیرمجموعه
def haveI(subset, position):
    num = subset & ~(1 << position)  # ایجاد ماسک برای موقعیت مشخص شده
    return (num & subset) != subset  # بررسی اینکه آیا بیت در موقعیت position تنظیم شده است یا خیر

# تابع برای محاسبه کمینه هزینه سفر از شهر v به مجموعه شهرهای set
def min_v(v, w, D, set, n):
    m = [0] * len_subset(set)  # آرایه برای ذخیره هزینه‌ها
    i = [0] * len_subset(set)  # آرایه برای ذخیره شهرهای مرتبط
    ind = 0  # شاخص برای پر کردن آرایه‌ها

    # حلقه برای محاسبه هزینه‌ها برای هر شهر در مجموعه
    for j in range(n - 1):
        if haveI(set, j):  # اگر شهر j در زیرمجموعه set باشد
            num = set & ~(1 << j)  # حذف شهر j از مجموعه
            num = set & num
            # محاسبه هزینه رفتن از شهر v به j+1 و افزودن آن به هزینه‌های قبلی
            m[ind] = w[v][j + 1] + D[j + 1][num]
            i[ind] = j + 1  # ذخیره شهر j+1
            ind += 1

    min_val = m[0]  # مقدار کمینه هزینه اولیه
    global l  # استفاده از متغیر سراسری برای ذخیره شهر بهینه
    l = i[0]

    # یافتن کمترین هزینه و به‌روزرسانی شهر بهینه
    for j in range(1, len_subset(set)):
        if min_val > m[j]:
            min_val = m[j]
            l = i[j]

    # بازگشت کمترین هزینه
    return min_val

# تابع برای چاپ مسیر کمینه
def print_path(i, p, n):
    while n > 0:
        print("V" + str(p[i][n]) + " ", end="")  # چاپ شهر فعلی
        i = p[i][n]  # به‌روزرسانی شهر فعلی به شهر بعدی
        n = n & ~(1 << (i - 1))  # حذف شهر فعلی از مجموعه شهرها

# مثال استفاده از کد
w = [
    [0, 2, 9, math.inf],  # ماتریس وزن‌ها یا هزینه‌ها بین شهرها
    [1, 0, 6, 4],
    [math.inf, 7, 0, 8],
    [6, 3, math.inf, 0]
]

n = len(w[0])  # تعداد شهرها
k = int(math.pow(2, (n - 1)))  # تعداد زیرمجموعه‌ها
p = [[0] * k for _ in range(n)]  # ماتریس برای ذخیره مسیرها

# محاسبه و چاپ کمینه هزینه
print("The shortest cycle is of length", trvel(n, w, p))
print("The shortest cycle is ", end="")
print("V0 ", end="")
print_path(0, p, k - 1)  # چاپ مسیر کمینه
print("V0 ")
