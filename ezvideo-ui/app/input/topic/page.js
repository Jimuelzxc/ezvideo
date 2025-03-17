"use client";
import React, { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

function page() {
  const [topic, setTopic] = useState(localStorage.getItem("topic") || "");
  const route = useRouter();

  return (
    <div className="h-screen flex items-center justify-center flex-col">
      <h2>What's on your mind?</h2>
      <input
        type="text"
        placeholder="Search"
        className="border p-2"
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
      />
      <button
        className="p-2 bg-blue-500 px-6"
        onClick={() => {
          if (localStorage.getItem("topic")) {
            route.push(`/input/titles?topic=${topic}`);
          }
        }}
      >
        Next
      </button>
    </div>
  );
}

export default page;
