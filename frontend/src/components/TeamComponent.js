import React from "react";
import EngineerTypeInput from "./EngineerTypeInput";
import Button from "@mui/material/Button";

const TeamComponent = (props) => {
  const confirmHandler = (data) => {
    console.log(data);
    addHandler(data);
  };
  const addHandler = (data) => {
    // props.addTeamRequirements(data);
  };
  return (
    <div>
      <EngineerTypeInput
        addHandler={addHandler}
        confirmHandler={confirmHandler}
      />
      <EngineerTypeInput
        addHandler={addHandler}
        confirmHandler={confirmHandler}
      />
      <EngineerTypeInput
        addHandler={addHandler}
        confirmHandler={confirmHandler}
      />
      <EngineerTypeInput
        addHandler={addHandler}
        confirmHandler={confirmHandler}
      />
      <Button variant="contained" onClick={confirmHandler}>
        Confirm team requirements
      </Button>
    </div>
  );
};

export default TeamComponent;
