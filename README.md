# Spring 框架版本发布时间线

这个项目可视化了 Spring 框架不同版本的发布时间线，帮助用户查看各版本的历史发布日期，并分析版本之间的发布时间间隔。

## 项目概述

本仓库包含了用来绘制 Spring 框架版本发布历史的脚本。目的是提供一个易于理解的图形化表示，同时计算相邻版本之间的发布时间间隔。

## 文件说明

- `spring_releases.csv`：包含了 Spring 框架各个版本的发布数据。文件中有两列：
  - `version`：Spring 框架的版本（例如：Spring 1.0, Spring 2.0）。
  - `release_date`：该版本的发布日期。

- `plot_release_timeline.py`：这个 Python 脚本读取 `spring_releases.csv` 文件，并生成一个显示 Spring 框架版本发布时间线的折线图。X 轴为发布日期，Y 轴为版本号。

- `analyze_release_intervals.py`：这个 Python 脚本读取一个版本发布日期的字典，计算相邻版本之间的发布时间间隔（以天为单位）。这个分析有助于了解 Spring 发布的频率。

## 环境要求

- Python 3.x
- pandas
- matplotlib

你可以使用 `pip` 来安装依赖：

```bash
pip install pandas matplotlib
```

## 如何运行

### 1. 生成发布发布时间线图

要生成版本发布时间线图，只需运行 `plot_release_timeline.py` 脚本：

```bash
python plot_release_timeline.py
```

运行后，程序会生成一张可视化的图表，展示 Spring 各版本的发布日期。

### 2. 分析发布间隔

要计算每个版本之间的发布时间间隔，运行 `analyze_release_intervals.py` 脚本：

```bash
python analyze_release_intervals.py
```

运行后，程序会输出各个版本之间的时间间隔（以天为单位）。