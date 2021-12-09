import React, { useState } from "react";
import Button from "@mui/material/Button";
import { Link } from "react-router-dom";
import styles from "../styles/Home.module.css";

const DownloadButton = (props) => {
  const [isDisabled, setIsDisabled] = useState(true);
  console.log(isDisabled);

  return (
    <Button variant="contained" className={styles.btn} disabled={false}>
      <Link
        className={styles.download__link}
        to="/assets/pandas_multiple.xlsx"
        target="_blank"
        download
      >
        Download Detailed Structure
      </Link>
    </Button>
  );
};

export default DownloadButton;
