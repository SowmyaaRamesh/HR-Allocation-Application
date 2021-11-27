import React from "react";
import AccountCircleIcon from "@mui/icons-material/AccountCircle";
import styles from "../styles/Navbar.module.css";
const Navbar = () => {
  return (
    <div className={styles.navbar}>
      <AccountCircleIcon fontSize="large" className={styles.user__icon} />
    </div>
  );
};

export default Navbar;
