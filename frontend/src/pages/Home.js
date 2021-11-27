import React from "react";
import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import styles from "../styles/Home.module.css";
import TeamInput from "../components/TeamInput";

const Home = () => {
  return (
    <div className={styles.home}>
      <Navbar />
      <div className={styles.right__container}>
        <Sidebar />
        <div className={styles.content}>
          <h1>Welcome back!</h1>
          <hr />
          <TeamInput />
        </div>
      </div>
    </div>
  );
};

export default Home;
