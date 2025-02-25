from flask import Flask, request, jsonify
from flask_cors import CORS
import boto3
import os
from ai_model import analyze_logs_with_ai  # AI model integration

app = Flask(__name__)
CORS(app)

# AWS S3 Configuration
s3 = boto3.client('s3')
BUCKET_NAME = 'your-s3-bucket-name'  # Replace with your S3 bucket name

# Ensure uploads directory exists
os.makedirs('uploads', exist_ok=True)


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    file = request.files['file']
    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)
    return jsonify({"message": "File uploaded successfully", "file_path": file_path})


@app.route('/analyze', methods=['POST'])
def analyze_logs():
    data = request.json
    query = data.get('query')
    file_path = data.get('file_path')

    if not file_path or not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404

    # Analyze logs using AI model
    result = analyze_logs_with_ai(file_path, query)
    return jsonify({"result": result})


@app.route('/download', methods=['POST'])
def download_report():
    data = request.json
    file_path = data.get('file_path')
    format = data.get('format', 'csv')  # Default to CSV

    if not file_path or not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404

    # Generate report (CSV or PDF)
    if format == 'csv':
        # Generate CSV
        import pandas as pd
        df = pd.read_csv(file_path)
        output_path = file_path.replace('.log', '_report.csv')
        df.to_csv(output_path, index=False)
    elif format == 'pdf':
        # Generate PDF
        from fpdf import FPDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        with open(file_path, 'r') as file:
            for line in file:
                pdf.cell(200, 10, txt=line, ln=True)
        output_path = file_path.replace('.log', '_report.pdf')
        pdf.output(output_path)
    else:
        return jsonify({"error": "Invalid format"}), 400

    return jsonify({"message": "Report generated", "report_path": output_path})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
