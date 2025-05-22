from DrissionPage import ChromiumPage
import time
import json

# 直接指定地址创建连接
page = ChromiumPage(addr_or_opts='127.0.0.1:4000')
print("已连接到现有浏览器...")

input("按回车键继续...")

try:
    
    # 获取所有视频元素
    li_class = "niBfRBgX Q_uOVQ1u SBWUpJd_"
    li_elements = page.eles(f'css:li.{li_class.replace(" ", ".")}')
    
    # 打印找到的元素数量
    print(f"找到 {len(li_elements)} 个视频元素")
    
except Exception as e:
    print(f"爬取过程中出错: {str(e)}")
    import traceback
    traceback.print_exc()


