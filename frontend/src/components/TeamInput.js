import React, { useRef, useState } from "react";
import Container from "@mui/material/Container";
import styles from "../styles/TeamInput.module.css";
import EngineerTypeInput from "./EngineerTypeInput";
import AddCircleOutlineIcon from "@mui/icons-material/AddCircleOutline";
import Button from "@mui/material/Button";

const TeamInput = () => {
  const [teamNumInput, setTeamNumInput] = useState(1);
  const [peopleNumInput, setPeopleNumInput] = useState(1);

  const submitHandler = (e) => {
    e.preventDefault();
  };
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
            max="10"
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

        <EngineerTypeInput />

        <Button className={styles.btn} variant="contained">
          Generate Team
        </Button>
      </form>
    </div>
  );
};

export default TeamInput;
