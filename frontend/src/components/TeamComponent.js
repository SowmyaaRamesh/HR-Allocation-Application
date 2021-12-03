import React from "react";
import EngineerTypeInput from "./EngineerTypeInput";
import Button from "@mui/material/Button";

const TeamComponent = (props) => {
  return (
    <div>
      <EngineerTypeInput addHandler={props.addTeamRequirements} />
      <EngineerTypeInput addHandler={props.addTeamRequirements} />
      <EngineerTypeInput addHandler={props.addTeamRequirements} />
      <EngineerTypeInput addHandler={props.addTeamRequirements} />
    </div>
  );
};

export default TeamComponent;
