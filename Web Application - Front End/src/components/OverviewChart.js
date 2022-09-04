import React from "react";
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";
import { Pie } from "react-chartjs-2";

ChartJS.register(ArcElement, Tooltip, Legend);

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
      data: [1, 2, 3, 5, 6, 7, 0, 0, 0],
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

function OverviewChart(props) {
  data.datasets.data = props;
  return (
    <div>
      <Pie data={data} />
    </div>
  );
}

export default OverviewChart;
