/
│
├── app.py                  			# Flask 主程序入口
├── requirements.txt        		# Python 依赖项列表
├── uploads/                			# 临时存储上传的文件
│   └── (临时文件)           			# 用户上传的 PDF 文件
├── static/                 				# 存放静态资源（停用词、CSS、JS、图片等）
│   ├── must_words.txt           	# 停用词
│   ├── css/
│   │   └── styles.css      			# 自定义样式表
│   └── js/
│       └── script.js       			# 自定义 JavaScript 文件
├── templates/              			# 存放 HTML 模板（如果需要动态模板渲染）
│   └── index.html          			# 前端页面
├── utils/                  				# 存放辅助函数和工具模块
│   ├── __init__.py         			# 标记为 Python 包
│   ├── file_processing.py  		# 文件处理逻辑
│   ├── json_utils.py 				# json处理逻辑
│   └── pdf_utils.py        			# PDF 相关工具函数
└── models/                 			# 存放核心业务逻辑或模型
    ├── __init__.py         			# 标记为 Python 包
    ├── details_abstract.py         	# 模板有效信息提取
    ├── flexible_area_abstract.py   # 模板区域提取
    ├── logic_search.py         		# 模板逻辑寻找
    └── demo.py             			# 示例处理逻辑（如 demo.process 函数）
