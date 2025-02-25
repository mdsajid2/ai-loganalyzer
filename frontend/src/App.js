import React, { useState } from 'react';
import axios from 'axios';
import ChatBox from './components/ChatBox';
import FileUpload from './components/FileUpload';
import ReportDownload from './components/ReportDownload';

function App() {
  //const [file, setFile] = useState(null); // Ensure this is used
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState('');
  const [filePath, setFilePath] = useState('');

  const handleFileUpload = async (event) => {
    const uploadedFile = event.target.files[0];
   // setFile(uploadedFile); // Use setFile
    const formData = new FormData();
    formData.append('file', uploadedFile);
    const res = await axios.post('http://localhost:8000/upload', formData);
    setFilePath(res.data.file_path);
  };

  const handleQuerySubmit = async () => {
    const res = await axios.post('http://localhost:8000/analyze', {
      query,
      file_path: filePath,
    });
    setResponse(res.data.result);
  };

  return (
    <div>
      <h1>Log Analyzer</h1>
      <FileUpload onFileUpload={handleFileUpload} />
      <ChatBox
        query={query}
        setQuery={setQuery}
        onSubmit={handleQuerySubmit}
        response={response}
      />
      <ReportDownload filePath={filePath} />
    </div>
  );
}

export default App;