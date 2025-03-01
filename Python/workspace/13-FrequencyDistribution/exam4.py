# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 17:10:02 2020

@author: kimyongkuk
"""


from pandas import DataFrame
from pandas import read_csv
from matplotlib import pyplot
from stemgraphic import stem_graphic

grade_csv = read_csv("data/grade.csv",encoding='euc-kr')

#전처리 컬럼 이름을 인덱스로 설정
grade_df = grade_csv.rename(index=grade_csv['이름']).drop('이름',axis=1)

#평균점수 컬럼 추가: axis=1 행
grade_df['평균']=grade_df.mean(axis=1)
print(grade_df)

pyplot.rcParams['font.family']='Malgun Gothic'
pyplot.rcParams['font.size']=20
pyplot.rcParams['figure.figsize']=(15,8)

stem_graphic(grade_df['평균'],scale=10)
pyplot.savefig('stem.png')