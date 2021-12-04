import React from "react";
import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import styles from "../styles/Home.module.css";
import FormInput from "../components/FormInput";
import OverviewChart from "../components/OverviewChart";
import Button from "@mui/material/Button";
const Home = () => {
  return (
    <div className={styles.home}>
      <Navbar />
      <div className={styles.bottom__container}>
        <Sidebar />
        <div className={styles.content}>
          <h1>Welcome back!</h1>
          <hr />
          <div className={styles.flex__container}>
            <FormInput />
            <div className={styles.chart__right}>
              <h2>Overview of Team Distribution</h2>
              <OverviewChart />
              <Button variant="contained">View Detailed Structure</Button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;
