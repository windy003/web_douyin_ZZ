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
# print("已启动无头浏览器...")


url = "https://www.douyin.com/user/MS4wLjABAAAAwZrkda60dI-2jTY4KnqcboBa78d84QYzz4KifgDzWc4?from_tab_name=main"

# url = "https://www.douyin.com/user/MS4wLjABAAAA_TS-DyQ0J6mVqXW1QNgA5nZHA0QOLTBFK9fIn0Kzp68B9GGZNOrQz4TN6s-OAzap?from_tab_name=main&vid=7091959856512486671"


page.get(url)







def prepare_page_for_scrolling(page):
    """
    准备页面以便进行键盘滚动:
    1. 将页面缩放到25%
    2. 点击左右两侧空白区域
    """
    # 缩放页面到25%
    page.run_js('document.body.style.zoom = "1%"')
    time.sleep(1)  # 等待缩放生效

    # 获取窗口尺寸
    page.run_js("""
    function clickBothSides() {
        const width = window.innerWidth;
        const height = window.innerHeight;
        
        // 点击左侧空白处
        const leftClickEvent = new MouseEvent('click', {
            bubbles: true,
            cancelable: true,
            view: window,
            clientX: width * 0.1,  // 左侧10%位置
            clientY: height * 0.5   // 垂直居中
        });
        document.elementFromPoint(width * 0.1, height * 0.5).dispatchEvent(leftClickEvent);
        
        // 稍等片刻
        setTimeout(() => {
            // 点击右侧空白处
            const rightClickEvent = new MouseEvent('click', {
                bubbles: true,
                cancelable: true,
                view: window,
                clientX: width * 0.9,  // 右侧90%位置
                clientY: height * 0.5   // 垂直居中
            });
            document.elementFromPoint(width * 0.9, height * 0.5).dispatchEvent(rightClickEvent);
        }, 300);
    }
    clickBothSides();
    """)
    time.sleep(1)  # 等待点击生效

def press_page_down(page):
    """模拟按下PageDown键"""
    page.run_js("""
    document.dispatchEvent(new KeyboardEvent('keydown', {
        key: 'PageDown',
        code: 'PageDown',
        keyCode: 34,
        which: 34,
        bubbles: true
    }));
    """)

def scroll_douyin_page(page, scroll_count=10, wait_time=2):
    """
    滚动抖音页面
    :param page: DrissionPage 页面对象
    :param scroll_count: 滚动次数
    :param wait_time: 每次滚动后的等待时间(秒)
    """
    
    # 准备页面
    prepare_page_for_scrolling(page)
    
    print("开始滚动页面...")
    for i in range(scroll_count):
        # 按下PageDown键
        press_page_down(page)
        
        # 等待内容加载
        time.sleep(wait_time)
        
        print(f"已完成第{i+1}/{scroll_count}次翻页")
        
        # 可以在这里添加检查是否有新内容加载的代码
        try:
            current_videos = len(page.eles('xpath://a[contains(@href, "/video/")]'))
            print(f"  当前已加载视频数: {current_videos}")
        except:
            pass






scroll_douyin_page(page,scroll_count=10,wait_time=2)



# 使用示例
# scroll_douyin_page(page, scroll_count=15)






# 获得文章和微头条链接块包括标题
# data = ""

# try:
#     eles = page.eles('xpath://a[contains(@href, "/video/")]')
#     print(f"找到{len(eles)}个视频")
#     # print(f"视频列表: {eles}")
#     data = {}
#     for ele in eles:
#         # 使用attr()方法获取href属性
#         href = ele.attr('href')
#         # print(f"视频链接: {href}")
#         if href:  # 确保href存在
#             url = "https://www.douyin.com" + href

#             desc = ele.ele('xpath:./p').text
#             # print(f"视频描述: {desc}")

#             data[url] = desc
    
    
    
#     with open('0.json', 'w', encoding='utf-8') as f:
#         json.dump(data, f, ensure_ascii=False)
# except Exception as e:
#     traceback.print_exc()



# finally:
#     page.close()

