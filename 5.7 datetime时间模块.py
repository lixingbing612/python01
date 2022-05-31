import datetime

print(datetime.datetime.now())

from datetime import datetime
now = datetime.now()
print(now)

df = now.strftime("%Y-%m-%d %H:%M:%S")
print(df)

dp = datetime.strptime(df, "%Y-%m-%d %H:%M:%S")
print(dp)


# sys模块
import sys
print(sys.path)