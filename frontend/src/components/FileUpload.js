import React from 'react';

function FileUpload({ onFileUpload }) {
  return (
    <div>
      <input type="file" onChange={onFileUpload} />
    </div>
  );
}

export default FileUpload;