import React from "react";
import styles from "../styles/Sidebar.module.css";
import HomeIcon from "@mui/icons-material/Home";
import StorageIcon from "@mui/icons-material/Storage";

const Sidebar = () => {
  return (
    <div className={styles.sidebar}>
      <ul>
        <li>
          <HomeIcon />
          <span>Home</span>
        </li>
        <li>
          <StorageIcon />
          <span>Records</span>
        </li>
      </ul>
    </div>
  );
};

export default Sidebar;
