import React, { useState } from "react";

interface TextEntryProps {
  id: string;
  handleEvent: () => void;
}

function TextEntry({ id, handleEvent}: TextEntryProps) {
  
  return (
    <div className="form-floating mb-3">
      <input id={id} className="form-control" onChange={handleEvent} />
      <label htmlFor={id}>{id}</label>
    </div>
  );
}

export default TextEntry;
