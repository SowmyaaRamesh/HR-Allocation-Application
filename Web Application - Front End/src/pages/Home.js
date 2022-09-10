import React, { useState } from "react";
import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import styles from "../styles/Home.module.css";
import FormInput from "../components/FormInput";

const Home = () => {
  return (
    <div className={styles.home}>
      <Navbar />
      <div className={styles.bottom__container}>
        <Sidebar />
        <div className={styles.content}>
          <h1>Welcome back!</h1>
          <hr />

          <FormInput />
        </div>
      </div>
    </div>
  );
};

export default React.memo(Home);
