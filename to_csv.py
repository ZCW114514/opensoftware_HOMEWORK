import requests
import pandas as pd

# GitHub API URL 获取Spring项目发布记录
repo_url = "https://api.github.com/repos/spring-projects/spring-framework/releases"

# 发送请求获取发布记录
response = requests.get(repo_url)
data = response.json()

# 从数据中提取版本信息和发布日期
releases = []
for release in data:
    version = release.get('tag_name')
    date = release.get('published_at')
    releases.append({"version": version, "release_date": date})

# 转换为DataFrame并保存为CSV
df = pd.DataFrame(releases)
df['release_date'] = pd.to_datetime(df['release_date'])
df.to_csv("spring_releases.csv", index=False)

print("保存的CSV文件内容：")
print(df.head())
