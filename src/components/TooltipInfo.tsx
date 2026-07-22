import React, { useState } from "react";

const TooltipInfo = ({ content }) => {
  const [show, setShow] = useState(false);

  return (
    <div className="relative inline-block ml-2 align-middle z-50">
      <button 
        type="button"
        onMouseEnter={() => setShow(true)}
        onMouseLeave={() => setShow(false)}
        onClick={() => setShow(!show)}
        className="w-5 h-5 rounded-full bg-gray-200 text-gray-600 flex items-center justify-center text-xs font-bold hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-gray-400 cursor-help"
        aria-label="More information"
      >
        ?
      </button>
      
      {show && (
        <div className="absolute z-50 w-64 sm:w-72 p-3 mt-2 text-sm text-left font-normal normal-case bg-gray-800 text-white rounded-lg shadow-xl -left-32 sm:left-auto sm:right-0 transform -translate-x-1/4 sm:translate-x-0">
          {content}
          <div className="absolute top-0 w-3 h-3 bg-gray-800 transform rotate-45 -mt-1.5 left-1/2 sm:left-auto sm:right-2"></div>
        </div>
      )}
    </div>
  );
};

export default TooltipInfo;