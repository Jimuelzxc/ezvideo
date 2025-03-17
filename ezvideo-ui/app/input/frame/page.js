'use client'
import { useEffect, useState } from "react";
import React from "react";


function page() {
  // State to track the selected option
  const [selectedOption, setSelectedOption] = useState(() => localStorage.getItem('selectedOption') || "16:9")
  useEffect(() => {
    console.log(selectedOption)
    localStorage.setItem('selectedOption', selectedOption);
  }, [selectedOption])

  // Handle radio button change
  const handleOptionChange = (event) => {
    setSelectedOption(event.target.value);
  };
  return (
    <div>
      <h2>Select an Option:</h2>
      {/* Radio Button Group */}
      <label>
        <input
          type="radio"
          name="option"
          value="16:9"
          checked={selectedOption === "16:9"}
          onChange={handleOptionChange}
        />
        Option 1 (16:9)
      </label>
      <br />

      <label>
        <input
          type="radio"
          name="option"
          value="9:16"
          checked={selectedOption === "9:16"}
          onChange={handleOptionChange}
        />
        Option 2 (9:16)
      </label>
      <br />

      <label>
        <input
          type="radio"
          name="option"
          value="1:1"
          checked={selectedOption === "1:1"}
          onChange={handleOptionChange}
        />
        Option 3 (1:1)
      </label>

      {/* Display selected option */}
      <p>Selected: {selectedOption || "None"}</p>
    </div>
  );
}

export default page;
