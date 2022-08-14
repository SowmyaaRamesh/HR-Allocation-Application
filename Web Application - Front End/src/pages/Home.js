import React, { useState } from "react";
import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import styles from "../styles/Home.module.css";
import FormInput from "../components/FormInput";
import DownloadButton from "../components/DownloadButton";
import OverviewChart from "../components/OverviewChart";

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
              <DownloadButton />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default React.memo(Home);
