// import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";
// import { Pie } from "react-chartjs-2";
// import React, { useState, useEffect, useRef } from "react";
// ChartJS.register(ArcElement, Tooltip, Legend);

import React, { useRef, useEffect, useState } from "react";
import Chart from 'chart.js/auto'


const data = {
  labels: [
    "Team 1",
    "Team 2",
    "Team 3",
    "Team 4",
    "Team 5",
    "Team 6",
    "Team 7",
    "Team 8",
    "Team 9",
    "Team 10",
  ],
  datasets: [
    {
      label: "# of people",
      data: [0,0, 0, 0, 0, 0, 0, 0, 0, 0],
      backgroundColor: [
        "rgba(255, 99, 132, 0.2)",
        "rgba(54, 162, 235, 0.2)",
        "rgba(255, 206, 86, 0.2)",
        "rgba(75, 192, 192, 0.2)",
        "rgba(153, 102, 255, 0.2)",
        "rgba(255, 159, 64, 0.2)",
        "rgba(0, 206, 86, 0.2)",
        "rgba(75, 0, 192, 0.2)",
        "rgba(153, 102, 0, 0.2)",
        "rgba(255, 159, 233, 0.2)",
      ],
      borderColor: [
        "rgba(255, 99, 132, 1)",
        "rgba(54, 162, 235, 1)",
        "rgba(255, 206, 86, 1)",
        "rgba(75, 192, 192, 1)",
        "rgba(153, 102, 255, 1)",
        "rgba(255, 159, 64, 1)",
        "rgba(0, 206, 86, 1)",
        "rgba(75, 0, 192, 1)",
        "rgba(153, 102, 0, 1)",
        "rgba(255, 159, 233, 1)",
      ],
      borderWidth: 1,
    },
  ],
};

// function OverviewChart(props) {
//   const [msg, setMsg] = useState(data);
//   const ref = useRef()
//   console.log("isnide overviewcahrt");
//   console.log(props);
//   console.log("assertion isarray", typeof props.props);
//   if (typeof props.props === "object") {
//     console.log("isnide overviewcahrt IFFFFFF");
//     data.datasets.data = [];
//     props.props.forEach((i) => {
//       console.log("pushed", i);
//       data.datasets.data.push(parseInt(i));
//     });
//     while (data.datasets.data.length < 10) {
//       data.datasets.data.push(0);
//     }
//   }
//   return (
//     <div>
//       <Pie data={data} ref = {ref}/>
//     </div>
//   );
// }

// export default OverviewChart;


function OverviewChart( { formData } ){
  console.log(formData)
  const chartRef = useRef(null);
  const [myChart, setMyChart] = useState(null);
  useEffect(() => {
    console.log("ac", data.datasets[0].data)
    if (!chartRef) return;
    const ctx = chartRef.current.getContext("2d");
    const myChart = new Chart(ctx, {
      type: "pie",
      data: data
    })
    setMyChart(myChart);
  }, [chartRef]);

  useEffect(() => {
    if (!myChart) return;
    if (typeof formData === "object") {
    console.log("isnide overviewcahrt IFFFFFF");
    data.datasets[0].data = [];
    formData.forEach((i) => {
    console.log("pushed", i);
    data.datasets[0].data.push(parseInt(i));
  });
  while (data.datasets[0].data.length < 10) {
    data.datasets[0].data.push(0);
  }
  console.log(data.datasets[0].data)
}
  myChart.data.datasets[0].data = data.datasets[0].data;
  myChart.update();
  }, [formData, myChart]);

  return <canvas ref={chartRef} id="myChart" width="400" height="400" />;
};

export default OverviewChart;

