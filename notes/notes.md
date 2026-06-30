# Python 學習筆記

## Pandas
- groupby = 分組計算
- apply = 把函式套用到每一行
- isin = 篩選某欄位是否在清單裡
- value_counts = 算每個值出現幾次
- pct.cgange = 算每天的漲跌幅，類似np.diff
- shift = 往後移
- cumprod = 累積相乘
- iloc = 取值
- loc = 透過欄位選取資料
- isnull = 檢查資料缺失的值，並回傳一個布林值
- duplicated = 用來檢查 DataFrame 中是否有重複的列（Row），並回傳一個布林值
- astype = 將資料形式轉換成想要的種類
- pd.set_option('display.max_rows', None)，設定最多顯示幾列
- pd.set_option('display.max_columns', None)，設定最多顯示幾欄
- pd.set_option('display.max_colwidth', None)，設定每個儲存格的最大文字寬度

## Matplotlib
- barh = 水平長條圖
- bar = 垂直長條圖
- scatter = 散佈圖
- annotate = 在圖上標文字
- tight_layout = 自動調整間距避免文字被切掉
- fill_between(X軸範圍, 下邊界, 上邊界) = 在兩條線之間填滿顏色
- legend = 把圖的label顯示出來

## Numpy
- array = np.array出來的串列可以直接做運算
- max、min、mean、std... = 有多統計量可以使用做運算
- diff = 可以將串列的每一個元素做後減前的運算，所以最後會生成一個比原本串列少一個元素的串列
- sqrt = 開根號
- reshape = 重塑陣列微度，後面的-1代表的是自動計算微度


## Function
- cummax() = 計算出整體資料的最大值

## Scikit-learn
- model.fit() = 讓模型去適應(訓練)數據，x:用來訓練的變數 y:目標變數，想要預測的值
