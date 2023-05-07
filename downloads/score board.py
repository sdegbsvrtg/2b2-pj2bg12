import random
import time
from zmqRemoteApi import RemoteAPIClient
 
# 利用 zmqRemoteApi 中的 RemoteAPIClient 連結場景
client = RemoteAPIClient('localhost', 23000)
sim = client.getObject('sim')
 
# 決定是否啟動模擬
#sim.startSimulation()
 
# 取得 floor handle
ground_handle = sim.getObject("/Floor")
# 準備丟下的球數量
num_of_ball = 20
# 準備丟下的球尺寸
size = [0.1, 0.1, 0.1]
# 統一從高處丟下
z_pos = 1
# 利用 for 迴圈丟球
for i in range(20):
    # 利用 createPureShape 建立圓球, 第一變數 0 為 cuboid, 1 為 sphere
    # 第二變數 8 表示所建立的物件 respondable
    # 參數設定參考 https://www.coppeliarobotics.com/helpFiles/en/regularApi/simCreatePureShape.htm
    sphere_handle = sim.createPureShape(1, 8, size, 1, None)
    # 利用浮點數建立座標位於 -1, 1 之間
    x_pos = random.uniform(-1, 1)
    y_pos = random.uniform(-1, 1)
    # 列出座標查驗
    print(x_pos, y_pos)
    # 設定丟球的座標
    _ = sim.setObjectPosition(sphere_handle, ground_handle, [x_pos, y_pos, z_pos])
    # wait for a moment to observe the simulation
    time.sleep(1)
 
# 假如要移除先前所建立的 sphere
#_ = sim.removeObject(sphere_handle)
#sim.stopSimulation()