from DrissionPage import ChromiumPage
import time
import json





start_time = time.time()
# 直接指定地址创建连接
page = ChromiumPage(addr_or_opts='127.0.0.1:4000')
print("已连接到现有浏览器...")

input("按回车键继续...")



def get_img(element):
    img = element.ele('css:img', timeout=1)
    return img.html.replace("\n", "") + "\n"
        




content = ""
try:
    
    # 获取所有视频元素
    # li_class = "niBfRBgX Q_uOVQ1u SBWUpJd_"
    li_class = "wqW3g_Kl WPzYSlFQ OguQAD1e"
    li_elements = page.eles(f'css:li.{li_class.replace(" ", ".")}')
    


    # 打印找到的元素数量
    print(f"找到 {len(li_elements)} 个视频元素")
    
    for i, element in enumerate(li_elements):
        try:
            # 先尝试查找 /video 链接
            video_link = element.ele('css:a[href^="/video"]',timeout=0)
            note_link = element.ele('css:a[href*="/note"]',timeout=0)
            if video_link:
                video_url = video_link.attr('href')
                if not video_url.startswith('http'):
                    video_url = 'https://www.douyin.com' + video_url
                content += video_url + "\n"
                print(f"{i+1}找到视频链接: {video_url}")
                content += get_img(element)
            elif note_link:
                    note_url = note_link.attr('href')
                    if not note_url.startswith('http'):
                        note_url = 'https://www.douyin.com' + note_url
                    content += note_url + "\n"
                    print(f"{i+1}找到笔记链接: {note_url}")
                    content += get_img(element)

        
        except Exception as e:
            print(f"获取图片时出错: {str(e)}")

        continue



    with open('content.txt', 'w', encoding='utf-8') as f:
        f.write(content)


    end_time = time.time()
    total_time = (end_time - start_time)/60
    print(f"爬取完成，用时: {total_time:.2f} 分钟")

except Exception as e:
    print(f"爬取过程中出错: {str(e)}")
    import traceback
    traceback.print_exc()

