#说明读取excel文件并按分数降序排序
import pandas as pd

def process_scores(file_path):
    df = pd.read_excel(file_path)
    # 按分数（假设列名为 'Score (40)'）降序排序
    df_sorted = df.sort_values(by='Score (40)', ascending=False)
    df_sorted.reset_index(drop=True, inplace=True)
    df_sorted.index = range(1, len(df_sorted) + 1)
    df_sorted.insert(0, '序号', range(1, len(df_sorted) + 1))
    df_sorted = df_sorted.iloc[:, 1:]

    return df_sorted

def main():
    file_path = 'Copy of CSX2006_M1_Sec544.xlsx'
    df_sorted = process_scores(file_path)
    print(df_sorted)

if __name__ == "__main__":
    main()
