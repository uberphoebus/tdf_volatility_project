#Module Name : ML.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("0115.csv",sep="\t")
print(df.head())

import sqlite3
#import cx_Oracle
con = sqlite3.connect("test.db")
#con = pymysql.connect(host='localhost', user='custom‘, password='1111', db='testdb', charset='utf8')'
#con = cx_Oracle.connect('ncs/0000@localhost/xe')
# cur = con.cursor()
# cur.execute('select * from emp')
# # rows = curs.fetchall()
# for result in cur:
#     print(result)
# cur.close()
# con.close()

df.to_sql("ncs0206", con, if_exists="replace")
print("===done===")
con.close()

''' 
중복답변배제
select rdate, name, count(1) from ncs0113
group by rdate, name
having count(1) > 1
order by name;


출석
select distinct name from ncs0118 order by name;
select distinct name from ncs0119 order by name;
select distinct name from ncs0120 order by name;
select distinct name from ncs0121 order by name;
select distinct name from ncs0122 order by name;

답변수
select name, count(1) from ncs0113
group by name, name
-- having count(1) > 1
order by name;

select name, count(1) from ncs0113 group by name, name order by count(1) desc;
select name, count(1) from ncs0111 group by name, name order by count(1) desc;
select name, count(1) from ncs0113 group by name, name order by count(1) desc;
select name, count(1) from ncs0114 group by name, name order by count(1) desc;
select name, count(1) from ncs0115 group by name, name order by count(1) desc;
select name, count(1) from ncs0118 group by name, name order by count(1) desc;
select name, count(1) from ncs0119 group by name, name order by count(1) desc;
select name, count(1) from ncs0120 group by name, name order by count(1) desc;
select name, count(1) from ncs0121 group by name, name order by count(1) desc;
select name, count(1) from ncs0122 group by name, name order by count(1) desc;
select name, count(1) from ncs0130 group by name, name order by count(1) desc;
select name, count(1) from ncs0206 group by name, name order by count(1) desc;


** 총 답변 수 
select name, sum(cnt) as cnt
from (
select name, count(1) as cnt from ncs0113 group by name
union all
select name, count(1) as cnt from ncs0111 group by name
union all
select name, count(1) as cnt from ncs0113 group by name
union all
select name, count(1) as cnt from ncs0114 group by name
union all
select name, count(1) as cnt from ncs0115 group by name
union all
select name, count(1) as cnt from ncs0118 group by name
union all
select name, count(1) as cnt from ncs0119 group by name
union all
select name, count(1) as cnt from ncs0120 group by name
union all
select name, count(1) as cnt from ncs0121 group by name
union all
select name, count(1) as cnt from ncs0122 group by name
union all
select name, count(1) as cnt from ncs0130 group by name
union all
select name, count(1) as cnt from ncs0206 group by name
)
group by name
order by sum(cnt) desc;


'''