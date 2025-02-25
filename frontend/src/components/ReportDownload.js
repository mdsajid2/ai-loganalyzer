import React from 'react';
import axios from 'axios';

function ReportDownload({ filePath }) {
  const handleDownload = async (format) => {
    const res = await axios.post('http://localhost:8000/download', {
      file_path: filePath,
      format,
    });
    alert(res.data.message);
  };

  return (
    <div>
      <button onClick={() => handleDownload('csv')}>Download CSV</button>
      <button onClick={() => handleDownload('pdf')}>Download PDF</button>
    </div>
  );
}

export default ReportDownload;