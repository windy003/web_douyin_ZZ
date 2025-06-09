from DrissionPage import ChromiumPage
import time
import json




start_time = time.time()
# 直接指定地址创建连接
page = ChromiumPage(addr_or_opts='127.0.0.1:4000')
print("已连接到现有浏览器...")

input("按回车键继续...")


content = ""
try:
    
    # 获取所有视频元素
    # li_class = "niBfRBgX Q_uOVQ1u SBWUpJd_"
    li_class = "SmHs0qqX Q_uOVQ1u SBWUpJd_"
    li_elements = page.eles(f'css:li.{li_class.replace(" ", ".")}')
    
    # 打印找到的元素数量
    print(f"找到 {len(li_elements)} 个视频元素")
    
    for i, element in enumerate(li_elements):
        try:
            # 查找 href 以 /video 开头的 <a> 标签
            # 注意timeout前面不加空格如果报错,就加空格
            if element.ele('css:a[href^="/video"]', timeout=1):
                video_link = element.ele('css:a[href^="/video"]', timeout=1)
                # 获取完整的视频链接
                video_url = video_link.attr('href')
                if not video_url.startswith('http'):
                    video_url = 'https://www.douyin.com' + video_url
                content += video_url + "\n"
                
                print(f"{i+1}找到视频链接: {video_url}")
            else:
                video_link = element.ele('css:a[href^="/video"]', timeout=1)
                print(f"{i+1}未找到符合条件的视频链接:video_link:{video_link},element:{element}")
                continue
        except Exception as e:
            print(f"处理元素时出错: {str(e)}")


        try:
            if element.ele('css:img', timeout=1):
            
                
                img = element.ele('css:img', timeout=1)
                content += img.html.replace("\n", "") + "\n"

            else:
                img = element.ele('css:img')
                continue
                print(f"未找到图片:element:{element}")
        except Exception as e:
            print(f"获取图片时出错: {str(e)}")


    with open('content.txt', 'w', encoding='utf-8') as f:
        f.write(content)


    end_time = time.time()
    total_time = (end_time - start_time)/60
    print(f"爬取完成，用时: {total_time:.2f} 分钟")

except Exception as e:
    print(f"爬取过程中出错: {str(e)}")
    import traceback
    traceback.print_exc()


