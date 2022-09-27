import React, { useState } from "react";
import styles from "../styles/FormInput.module.css";
import Button from "@mui/material/Button";
import axios from "axios";
import DownloadButton from "../components/DownloadButton";
import OverviewChart from "../components/OverviewChart";
import { CacheProvider } from "@emotion/react";
// import saveAs from "file-saver";

const FormInput = (props) => {
  const [teamNumInput, setTeamNumInput] = useState(1);
  const [peopleNumInput, setPeopleNumInput] = useState(1);
  const [msg, setMsg] = useState("");

  const [teamRequirements, setTeamRequirements] = useState([
    {
      type1: "",
      type2: "",
      type3: "",
      type4: "",
      lvl_type1: "0",
      lvl_type2: "0",
      lvl_type3: "0",
      lvl_type4: "0",
    },
  ]);
  // const prevTeamNumInput = usePrevious(teamNumInput);
  // function usePrevious(value) {
  //   const ref = useRef();
  //   useEffect(() => {
  //     ref.current = value;
  //   });
  //   return ref.current;
  // }
  const handleTeamRequirementsChange = (index, e) => {
    const values = [...teamRequirements];
    values[index][e.target.name] = e.target.value;
    setTeamRequirements(values);
  };

  const submitHandler = async (e) => {
    console.log("on submitting-----");
    e.preventDefault();
    // console.log(e);

    // e.stopPropagation();
    // e.nativeEvent.stopImmediatePropagation();
    let data = {
      noOfTeams: teamNumInput,
      numberOfPeople: peopleNumInput,
      teamRequirements: teamRequirements,
    };
    // console.log(data);
    console.log("generating data, wait for the alert to download it");
    // const res = await axios.post("http://localhost:5000/teamRequirements", {
    //   data: data,
    // });
    const rawResponse = await fetch("http://localhost:5000/teamRequirements", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });
    const content = await rawResponse.json();
    console.log(content);
    const pi_param = content.data;

    setMsg(pi_param);

    alert("The team structure can now be downloaded!");
    // e.preventDefault();
    // e.stopPropagation();
    // console.log(global, "hello world!!");
    // e.nativeEvent.stopImmediatePropagation();
    // return true;
  };

  const handleTeamNumInput = (e) => {
    // setTeamNumInput((prev) => setTeamNumInput(e.target.value));
    setTeamNumInput(teamNumInput + 1);
    setTeamRequirements([
      ...teamRequirements,
      {
        type1: "",
        type2: "",
        type3: "",
        type4: "",
        lvl_type1: "0",
        lvl_type2: "0",
        lvl_type3: "0",
        lvl_type4: "0",
      },
    ]);
  };
  const handleTeamNumInputSub = (e) => {
    if (teamNumInput > 1) {
      setTeamNumInput(teamNumInput - 1);
      setTeamRequirements(teamRequirements.slice(0, -1));
    }
  };
  return (
    <div className={styles.flex__container}>
      <div>
        <form
          className={styles.input__container}
          // onSubmit={(e) => submitHandler(e)}
        >
          <h2> Optimal Team Allocation</h2>
          <p>{msg}</p>
          <label htmlFor="numberOfTeams">Number of teams</label>

          <div className={styles.row__group}>
            <input
              type="text"
              disabled
              name="teamsValue"
              id="teamsValue"
              value={teamNumInput}
            />
            <input
              type="button"
              name="numberOfTeams"
              id="numberOfTeams"
              value={"+"}
              onClick={handleTeamNumInput}
            />
            <input
              type="button"
              name="numberOfTeams"
              id="numberOfTeams"
              value={"-"}
              onClick={handleTeamNumInputSub}
            />
          </div>
          <label htmlFor="typeOfEngineer">
            Choose requirements for the project
          </label>

          {teamRequirements.map((team, index) => (
            <div key={index}>
              <h5>Team {index + 1} details:</h5>
              <select
                name="type1"
                id="type1"
                value={team.type1}
                onChange={(e) => handleTeamRequirementsChange(index, e)}
              >
                <option value="default">Type of engineer </option>
                <option value="sde">SDE</option>
                <option value="nfit">NFIT</option>
                <option value="sdn">SDN</option>
                <option value="ne">NE</option>
              </select>
              <select
                name="lvl_type1"
                id="lvl_type1"
                value={team.lvl_type1}
                onChange={(e) => handleTeamRequirementsChange(index, e)}
              >
                <option value="default">Max experience level</option>
                <option value="1">Level 1</option>
                <option value="2">Level 2</option>
                <option value="3">Level 3</option>
              </select>
              <select
                name="type2"
                id="type2"
                value={team.type2}
                onChange={(e) => handleTeamRequirementsChange(index, e)}
              >
                <option value="default">Type of engineer </option>
                <option value="sde">SDE</option>
                <option value="nfit">NFIT</option>
                <option value="sdn">SDN</option>
                <option value="ne">NE</option>
              </select>
              <select
                name="lvl_type2"
                id="lvl_type2"
                value={team.lvl_type2}
                onChange={(e) => handleTeamRequirementsChange(index, e)}
              >
                <option value="default">Max experience level</option>
                <option value="1">Level 1</option>
                <option value="2">Level 2</option>
                <option value="3">Level 3</option>
              </select>
              <select
                name="type3"
                id="type3"
                value={team.type3}
                onChange={(e) => handleTeamRequirementsChange(index, e)}
              >
                <option value="default">Type of engineer </option>
                <option value="sde">SDE</option>
                <option value="nfit">NFIT</option>
                <option value="sdn">SDN</option>
                <option value="ne">NE</option>
              </select>
              <select
                name="lvl_type3"
                id="lvl_type3"
                value={team.lvl_type3}
                onChange={(e) => handleTeamRequirementsChange(index, e)}
              >
                <option value="default">Max experience level</option>
                <option value="1">Level 1</option>
                <option value="2">Level 2</option>
                <option value="3">Level 3</option>
              </select>
              <select
                name="type4"
                id="type4"
                value={team.type4}
                onChange={(e) => handleTeamRequirementsChange(index, e)}
              >
                <option value="default">Type of engineer </option>
                <option value="sde">SDE</option>
                <option value="nfit">NFIT</option>
                <option value="sdn">SDN</option>
                <option value="ne">NE</option>
              </select>
              <select
                name="lvl_type4"
                id="lvl_type4"
                value={team.lvl_type4}
                onChange={(e) => handleTeamRequirementsChange(index, e)}
              >
                <option value="default">Max experience level</option>
                <option value="1">Level 1</option>
                <option value="2">Level 2</option>
                <option value="3">Level 3</option>
              </select>
            </div>
          ))}

          <button onClick={submitHandler} className={styles.btn}>
            Generate Team
          </button>
        </form>
      </div>
      <div className={styles.chart__right}>
        <h2>Overview of Team Distribution</h2>
        <OverviewChart formData={msg} />
        <DownloadButton />
      </div>
    </div>
  );
};

export default FormInput;