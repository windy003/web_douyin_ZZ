from DrissionPage import ChromiumPage
import time
import json

# 直接指定地址创建连接
page = ChromiumPage(addr_or_opts='127.0.0.1:4000')
print("已连接到现有浏览器...")

input("按回车键继续...")


content = ""
try:
    
    # 获取所有视频元素
    li_class = "niBfRBgX Q_uOVQ1u SBWUpJd_"
    li_elements = page.eles(f'css:li.{li_class.replace(" ", ".")}')
    
    # 打印找到的元素数量
    print(f"找到 {len(li_elements)} 个视频元素")
    
    for element in li_elements:
        try:
            # 查找 href 以 /video 开头的 <a> 标签
            video_link = element.ele('css:a[href^="/video"]')
            
            if video_link:
                # 获取完整的视频链接
                video_url = video_link.attr('href')
                if not video_url.startswith('http'):
                    video_url = 'https://www.douyin.com' + video_url
                content += video_url + "\n"
                
                print(f"找到视频链接: {video_url}")
            else:
                print("未找到符合条件的视频链接")
        except Exception as e:
            print(f"处理元素时出错: {str(e)}")


        try:
            img = element.ele('css:img')
            content += img.html + "\n"
        except Exception as e:
            print(f"获取图片时出错: {str(e)}")


        with open('content.txt', 'w', encoding='utf-8') as f:
            f.write(content)


except Exception as e:
    print(f"爬取过程中出错: {str(e)}")
    import traceback
    traceback.print_exc()


