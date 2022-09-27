import React, { useState } from "react";
import Button from "@mui/material/Button";
import { Link } from "react-router-dom";
import styles from "../styles/Home.module.css";
import axios from 'axios';

const DownloadButton = (props) => {
  const [isDisabled, setIsDisabled] = useState(true);
  console.log(isDisabled);
 const handler =()=>{axios({
  url: 'http://localhost:5000/download', //your url
  method: 'GET',
  responseType: 'blob', // important
}).then((response) => {
  // create file link in browser's memory
  const href = URL.createObjectURL(response.data);

  // create "a" HTLM element with href to file & click
  const link = document.createElement('a');
  link.href = href;
  link.setAttribute('download', 'file.xlsx'); //or any other extension
  document.body.appendChild(link);
  link.click();

  // clean up "a" element & remove ObjectURL
  document.body.removeChild(link);
  URL.revokeObjectURL(href);
});}
  return (
    <Button variant="contained" className={styles.btn} disabled={false} onClick={handler}>
        Download Detailed Structure
 
    </Button>
  );
};

export default DownloadButton;
