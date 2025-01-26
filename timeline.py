import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 读取CSV文件
data = pd.read_csv('spring_releases.csv')

# 将release_date列转换为datetime格式
data['release_date'] = pd.to_datetime(data['release_date'])

# 创建图表
plt.figure(figsize=(12, 6))

# 绘制时间线，版本号为y轴，发布日期为x轴
plt.plot(data['release_date'], data['version'], marker='o', linestyle='-', color='b')

# 设置标题和标签
plt.title('Spring Framework Release Timeline', fontsize=16)
plt.xlabel('Release Date', fontsize=12)
plt.ylabel('Version', fontsize=12)

# 格式化x轴日期显示
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.YearLocator(1))  # 每年显示一个刻度
plt.xticks(rotation=45)

# 显示网格
plt.grid(True)

# 优化布局以避免标签重叠
plt.tight_layout()

# 展示图表
plt.show()
