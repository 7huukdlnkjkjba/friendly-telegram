## 功能有:
-下载YouTube视频字幕
- 自动识别中英文
- 保存为txt文件



          
# YouTube字幕下载工具使用教程

功能有:-
下载YouTube视频字幕
- 自动识别中英文
- 保存为txt文件

## 1️⃣ 准备工作
1. 确保电脑安装了Python（建议3.6以上版本）
2. 打开命令提示符（按Win+R，输入cmd回车）

## 2️⃣ 安装工具包
在命令提示符输入：
```bash
pip install pytube youtube-transcript-api
```

## 3️⃣ 使用步骤
1. 把代码文件`youtube_transcript.py`保存到电脑（比如桌面）
2. 双击运行这个.py文件，或者右键选"用Python打开"

## 4️⃣ 操作流程
1. 程序运行后会问你要YouTube视频链接：
   ```
   请输入YouTube视频URL: 
   ```
2. 粘贴视频链接（例如：`https://www.youtube.com/watch?v=dQw4w9WgXcQ`）
3. 按回车等待处理

## 5️⃣ 结果查看
- 成功时会显示：
  ```
  视频文字内容:
  [这里是全部字幕文本...]
  
  字幕已保存到 youtube_transcript.txt 文件
  ```
- 失败时会显示错误原因

## 6️⃣ 常见问题
❌ 报错"发生错误"怎么办？
- 检查链接是否正确（必须是完整YouTube网址）
- 确认视频有字幕（不是所有视频都有）
- 网络是否正常（有时需要科学上网）

💡 小技巧：
- 生成的字幕文件`youtube_transcript.txt`会保存在.py文件同一个文件夹
- 可以用记事本或Word打开这个txt文件

## 7️⃣ 进阶使用
想修改代码的话：
- 用记事本打开.py文件
- 修改`languages=['zh','en']`可以调整优先语言
- 修改保存路径可以改`open("youtube_transcript.txt"...`这行

是不是超简单？就像用微波炉热饭一样，按几个按钮就搞定啦！🍿

        
