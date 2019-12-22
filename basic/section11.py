# Section 11
# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MIME - text/csv

import csv

# 예제 1
with open('./basic/resource/sample1.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # columm(헤더)을 next 메소드로 넘김

    #확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        print(c)

# 예제 2
with open('./basic/resource/sample2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')
    next(reader)  # columm(헤더)을 next 메소드로 넘김

    #확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        print(c)

# 예제 3
with open('./basic/resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f)
    for c in reader:
        for k, v in c.items():
            print(k, v)
        print('--------------')

# 예제 4
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]

with open('./basic/resource/sample3.csv', 'w', newline='') as f:
    wt = csv.writer(f)
    for value in w:
        wt.writerow(value)


# 예제 5
with open('./basic/resource/sample4.csv', 'w', newline='') as f:
    wt = csv.writer(f)
    wt.writerows(w)

# 예제 4 / 예제 5 차이점 => 어떠한 조건에 대한 필터링이 필요할때 writerow

# XSL, XLSX
# openpyxl, xlsxwriter, xlrd, xlwt, xlutils
# pandas를 주로 사용 / 데이터 과학에서 열과 셋을 만들어서 정확한 통계 등...numpy (openpyxl, xlrd)을 pandas가 내부 사용.

import pandas as pd

# sheetname = '시트명' 또는 숫자, header = 3, skiprow = 숫자, 
xlsx = pd.read_excel('./basic/resource/sample.xlsx')

# 상위 데이터 확인

print(xlsx.head()) # 첫번째 부터 5번째까지 보여줌
print()

# 데이터 확인

print(xlsx.tail())
print()

# 데이터 확인

print(xlsx.shape)

# 엑셀 or CSV 다시 쓰기

xlsx.to_excel('./basic/resource/result.xlsx', index = False)
xlsx.to_csv('./basic/resource/result.csv', index = False)
