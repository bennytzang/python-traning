# 載入內建的sys模組並取得資訊

# 建立geometry模組，並載入使用 
import sys
sys.path.append("modules") #在模組的搜尋路徑列表中[新增路徑]
import geometry
result = geometry.distance(1,1,5,5)
print(result)
result = geometry.slope(1,2,3,4)
print(result)
# 調整搜尋模組的路徑
# import sys
# print(sys.path) #印出模組的搜尋路徑列表