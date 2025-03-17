"use client";
import React, { useEffect, useState } from "react";
import { useSearchParams } from "next/navigation";

function page() {
  const searchParams = useSearchParams();
  const topic = searchParams.get("topic");
  const [selectedOption, setSelectedOption] = useState(null);
  const [titles, setTitles] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleOptionChange = (event) => {
    setSelectedOption(event.target.value);
  };
  const getTitles = async () => {
    setLoading(true);
    try {
      const response = await fetch("http://127.0.0.1:8001/titles", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          text: topic,
        }),
      });
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      setTitles(await response.json());
      setLoading(false);
    } catch (error) {
      console.error("Failed to fetch titles:", error);
    }
  };
  const handleRegenerate = () =>{
    setTitles([])
    getTitles()
  }


  useEffect(() => {
    getTitles();
  }, []);

  return (
    <div>
      <h2>{topic}</h2>
      {loading && <p>Loading...</p>}
      <div className="flex gap-2">
        {titles.map((title, index) => (
          <label
            key={index}
            className={`p-2 ${
              selectedOption === title ? "border border-red" : ""
            }`}
          >
            <input
              type="radio"
              name="option"
              value={title}
              checked={selectedOption === title}
              onChange={handleOptionChange}
            />
            {title}
          </label>
        ))}
      </div>
      <button className="border">Next</button>
      <button onClick={handleRegenerate}>Regenerate</button>
    </div>
  );
}

export default page;
