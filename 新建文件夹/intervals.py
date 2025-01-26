import pandas as pd
import matplotlib.pyplot as plt

# 创建数据
data = {
    "version": [
        "Spring 1.0", "Spring 2.0", "Spring 2.5", "Spring 3.0", 
        "Spring 4.0", "Spring 5.0", "Spring 6.0"
    ],
    "release_date": [
        "2004-03-01", "2006-10-01", "2007-11-01", "2009-12-01", 
        "2013-11-01", "2017-09-01", "2022-11-01"
    ]
}

# 将数据转换为DataFrame
df = pd.DataFrame(data)

# 将日期字符串转换为日期对象
df['release_date'] = pd.to_datetime(df['release_date'])

# 计算相邻版本的发布时间间隔（单位：天）
df['interval_days'] = df['release_date'].diff().dt.days

# 去除NaN值（第一个版本没有间隔）
df = df.dropna(subset=['interval_days'])

# 绘制分布图
plt.figure(figsize=(10, 6))

# 使用hist绘制直方图
plt.hist(df['interval_days'], bins=6, color='skyblue', edgecolor='black', alpha=0.7)

# 添加标题和标签
plt.title('Distribution of Spring Release Intervals (in Days)')
plt.xlabel('Interval in Days')
plt.ylabel('Frequency')

# 显示图形
plt.show()
