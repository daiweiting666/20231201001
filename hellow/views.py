from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    """
    显示个人信息的视图函数
    """
    # 个人信息
    name = "代卫婷"
    student_id = "20231201001"
    class_name = "医学信息工程2023"
    
    # 创建HTML响应
    html_content = f"""
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>个人信息</title>
        <style>
            body {{
                font-family: 'Microsoft YaHei', Arial, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
            }}
            .container {{
                background: white;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.2);
                text-align: center;
                max-width: 500px;
                width: 90%;
            }}
            h1 {{
                color: #333;
                margin-bottom: 30px;
                font-size: 2.5em;
            }}
            .info-card {{
                background: #f8f9fa;
                padding: 20px;
                border-radius: 10px;
                margin: 15px 0;
                border-left: 5px solid #667eea;
            }}
            .info-label {{
                font-weight: bold;
                color: #555;
                font-size: 1.1em;
            }}
            .info-value {{
                color: #333;
                font-size: 1.3em;
                margin-top: 5px;
            }}
            .welcome {{
                color: #667eea;
                font-size: 1.2em;
                margin-top: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>👋 欢迎访问</h1>
            
            <div class="info-card">
                <div class="info-label">姓名</div>
                <div class="info-value">{name}</div>
            </div>
            
            <div class="info-card">
                <div class="info-label">学号</div>
                <div class="info-value">{student_id}</div>
            </div>
            
            <div class="info-card">
                <div class="info-label">班级</div>
                <div class="info-value">{class_name}</div>
            </div>
            
            <div class="welcome">
                感谢访问我的个人信息页面！
            </div>
        </div>
    </body>
    </html>
    """
    
    return HttpResponse(html_content)