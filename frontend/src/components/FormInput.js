import React, { useState } from "react";
import Container from "@mui/material/Container";
import styles from "../styles/FormInput.module.css";
import EngineerTypeInput from "./EngineerTypeInput";
import TeamComponent from "./TeamComponent";
import AddCircleOutlineIcon from "@mui/icons-material/AddCircleOutline";
import Button from "@mui/material/Button";

const FormInput = () => {
  const [teamNumInput, setTeamNumInput] = useState(1);
  const [peopleNumInput, setPeopleNumInput] = useState(1);
  const [teamRequirements, setTeamRequirements] = useState([]);

  const addTeamRequirementsHandler = (details) => {
    console.log(details);
  };

  const submitHandler = (e) => {
    e.preventDefault();
  };
  let TeamComponentList = [];
  for (let i = 0; i < teamNumInput; i++) {
    TeamComponentList.push(<h5>Team {i + 1} details:</h5>);
    TeamComponentList.push(
      <TeamComponent addTeamRequirements={addTeamRequirementsHandler} />
    );
  }
  return (
    <div>
      <form className={styles.input__container} onSubmit={submitHandler}>
        <h2> Optimal Team Allocation</h2>
        <label htmlFor="numberOfTeams">Number of teams</label>

        <div className={styles.row__group}>
          <input
            type="text"
            disabled
            name="teamsValue"
            id="teamsValue"
            value={teamNumInput}
            onChange={(e) => {
              setTeamNumInput((prev) => setTeamNumInput(e.target.value));
            }}
          />
          <input
            type="range"
            name="numberOfTeams"
            id="numberOfTeams"
            min="1"
            max="10"
            value={teamNumInput}
            onChange={(e) => {
              setTeamNumInput((prev) => setTeamNumInput(e.target.value));
            }}
          />
        </div>

        <label htmlFor="numberOfPeople">Number of people available</label>
        <div className={styles.row__group}>
          <input
            disabled
            type="text"
            name="peopleValue"
            id="teamsValue"
            value={peopleNumInput}
            onChange={(e) => {
              setPeopleNumInput((prev) => setPeopleNumInput(e.target.value));
            }}
          />
          <input
            type="range"
            name="numberOfPeople"
            id="numberOfPeople"
            min="1"
            max="600"
            value={peopleNumInput}
            onChange={(e) => {
              setPeopleNumInput((prev) => setPeopleNumInput(e.target.value));
            }}
          />
        </div>

        <div className={styles.row__group}>
          <label htmlFor="typeOfEngineer">
            Choose requirements for the project
          </label>
          <AddCircleOutlineIcon fontSize="small" className={styles.addBtn} />
        </div>

        {TeamComponentList}

        <Button className={styles.btn} variant="contained">
          Generate Team
        </Button>
      </form>
    </div>
  );
};

export default FormInput;
