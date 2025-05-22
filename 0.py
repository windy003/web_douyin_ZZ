from DrissionPage import ChromiumPage, ChromiumOptions
import time
import traceback
import json

# 创建配置对象
options = ChromiumOptions()
# options.set_argument('--headless=new')  # 使用新的无头模式
# options.set_argument('--no-sandbox')    # 在Linux系统中添加此参数
# options.set_argument('--disable-dev-shm-usage')  # 避免内存不足问题
options.set_argument('--user-data-dir=./chrome_data')
# 使用配置创建页面对象
page = ChromiumPage(options)
print("已启动浏览器...")

# 抖音用户页面URL
url = "https://www.douyin.com/user/MS4wLjABAAAAYwyiRKq3-5i1YzlMJDSZc5AE7p7AuwL9qt9rU78_Y9Y?from_tab_name=main&vid=7507105148011875611"

# li元素的class,可能每个频道不一样
li_class = "niBfRBgX Q_uOVQ1u SBWUpJd_"

# 访问页面
page.get(url)
print("已打开页面...")

# 等待页面加载
time.sleep(3)


def get_page_height():
    page_height = page.run_js('return document.documentElement.scrollHeight;')
    return page_height




def  scroll_to_bottom():
    # 获取页面高度
    page_height_old = get_page_height()
    
    # 滚动到页面底部
    page.run_js(f'window.scrollTo(0, {page_height_old});')
    time.sleep(3)  

    page_height_new = get_page_height()

    if page_height_new == page_height_old:
        print("已滚动到页面底部")
    else:
        print("未滚动到页面底部")
        scroll_to_bottom()
        time.sleep(3)    




try:


    scroll_to_bottom()

    # 获取所有具有特定class的<li>元素
    li_elements = page.eles(f'css:li.{li_class.replace(" ", ".")}')
    
    if not li_elements:
        print("未找到符合条件的<li>元素")
    else:
        print(f"找到 {len(li_elements)} 个符合条件的<li>元素")
        
        # # 遍历并打印每个<li>元素的内容
        # for i, li in enumerate(li_elements):
        #     try:
        #         print(f"\n<li> 元素 {i+1}:")
        #         print(li.html)  # 打印元素的HTML内容
        #         print("-" * 50)
        #     except Exception as e:
        #         print(f"处理<li>元素 {i+1} 时出错: {str(e)}")
        
except Exception as e:
    print(f"爬取过程中出错: {str(e)}")
    traceback.print_exc()
# finally:
#     # 关闭浏览器
#     page.quit()
#     print("浏览器已关闭")






