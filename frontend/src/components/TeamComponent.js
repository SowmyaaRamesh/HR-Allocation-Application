import React from "react";
import EngineerTypeInput from "./EngineerTypeInput";
import Button from "@mui/material/Button";

const TeamComponent = (props) => {
  const addHandler = (data) => {
    props.addTeamRequirements(data);
  };
  return (
    <div>
      <EngineerTypeInput addHandler={addHandler} />
      <EngineerTypeInput addHandler={addHandler} />
      <EngineerTypeInput addHandler={addHandler} />
      <EngineerTypeInput addHandler={addHandler} />
      <Button variant="contained" onClick={confirmHandler}>
        Confirm team requirements
      </Button>
    </div>
  );
};

export default TeamComponent;
