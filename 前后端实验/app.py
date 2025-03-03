from flask import Flask, request, jsonify, send_file
from flask_cors import CORS  # 处理跨域请求
import os
from models.demo import process  # 核心处理逻辑
from utils.file_processing import save_file, delete_file  # 文件处理工具

# 创建 Flask 应用
app = Flask(__name__)

# 启用 CORS 支持
CORS(app, resources={r"/process": {"origins": "*"}})

# 配置上传目录和输出文件路径
UPLOAD_DIR = 'uploads'
OUTPUT_FILE = 'output.json'

# 确保上传目录存在
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.route('/')
def index():
    return "Welcome to the PDF Processing Service!"

@app.route('/process', methods=['POST'])
def process_files():
    """
    处理文件上传和逻辑处理的 API 路由。
    """
    try:
        # 检查是否提供了必要的文件字段
        if 'scanFile' not in request.files or 'templateFile' not in request.files:
            return jsonify({"error": "Missing file part"}), 400

        scan_file = request.files['scanFile']
        template_file = request.files['templateFile']

        # 检查文件名是否为空
        if scan_file.filename == '' or template_file.filename == '':
            return jsonify({"error": "No selected file"}), 400

        # 检查文件类型是否为 PDF
        if not (scan_file and scan_file.filename.endswith('.pdf') and template_file and template_file.filename.endswith('.pdf')):
            return jsonify({"error": "Invalid file type. Only PDF files are allowed."}), 400

        # 保存上传的文件
        scan_path = save_file(scan_file, UPLOAD_DIR)
        template_path = save_file(template_file, UPLOAD_DIR)

        # 调用核心处理逻辑
        result = process(template_path, scan_path)

        # 将结果保存为 JSON 文件
        with open(OUTPUT_FILE, 'w', encoding = 'utf-8') as f:
            import json
            json.dump(result, f, indent=4, ensure_ascii= False)

        return jsonify(result)  # 返回处理结果

    except Exception as e:
        # 捕获异常并返回错误信息
        print(f"Error processing files: {e}")
        return jsonify({"error": str(e)}), 500

    finally:
        # 删除临时文件
        delete_file(scan_path)
        delete_file(template_path)


@app.route('/download', methods=['GET'])
def download():
    """
    提供下载处理结果的 API 路由。
    """
    if os.path.exists(OUTPUT_FILE):
        return send_file(
            OUTPUT_FILE,
            as_attachment=True,
            mimetype='application/json;charset=utf-8',  # 设置 MIME 类型和编码
            download_name='result.json'  # 下载文件名
        )
    else:
        return jsonify({"error": "File not found"}), 404


if __name__ == '__main__':
    """
    启动 Flask 应用。
    """
    app.run(debug=True)