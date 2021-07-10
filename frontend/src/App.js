import React, { useEffect } from "react";

function App() {
  useEffect(() => {
    fetch("http://127.0.0.1:5000/hello", {
      headers: {
        "Access-Control-Allow-Origin": "*",
      },
      method: "GET",
      // mode: "no-cors",
    })
      .then((res) => res.json())
      .then((data) => console.log(data)); //check the output in console
  });
  return (
    <div>
      <p>
        Edit <code>src/App.js</code> and save to reload.
      </p>
      
      Learn React
    </div>
  );
}

export default App;
