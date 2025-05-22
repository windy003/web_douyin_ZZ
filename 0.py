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

# 访问页面
page.get(url)
print("已打开页面...")

# 等待页面加载
time.sleep(3)

try:
    # 获取所有图片元素
    images = page.eles('css:.cover-container img')
    
    if not images:
        print("未找到图片元素，尝试其他选择器...")
        images = page.eles('img')
    
    print(f"找到 {len(images)} 个图片元素")
    
    # 遍历图片元素并提取信息
    for i, img in enumerate(images):
        try:
            # 获取图片URL和alt文本
            img_url = img.attr('src')
            img_alt = img.attr('alt')
            
            if img_url:
                print(f"图片 {i+1}:")
                print(f"链接: {img_url}")
                print(f"描述: {img_alt}")
                print("-" * 50)
                
        except Exception as e:
            print(f"处理图片 {i+1} 时出错: {str(e)}")
    
    # 如果你只需要特定的图片（根据你提供的示例）
    print("\n尝试查找特定图片...")
    specific_img = page.ele('xpath://img[contains(@alt, "Ai设计")]')
    if specific_img:
        img_url = specific_img.attr('src')
        img_alt = specific_img.attr('alt')
        print("\n找到指定图片:")
        print(f"链接: {img_url}")
        print(f"描述: {img_alt}")
    else:
        print("未找到指定的图片元素")
        
except Exception as e:
    print(f"爬取过程中出错: {str(e)}")
    traceback.print_exc()
finally:
    # 关闭浏览器
    page.quit()
    print("浏览器已关闭")






