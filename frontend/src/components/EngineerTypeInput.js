import React from "react";

const EngineerTypeInput = () => {
  return (
    <div>
      <select name="typeOfEngineers" id="typeOfEngineers">
        <option value="default">Type of engineer </option>
        <option value="sde">SDE</option>
        <option value="nfit">NFIT</option>
      </select>
      <select name="levelOfEngineers" id="levelOfEngineers">
        <option value="default">Max experience level</option>
        <option value="lvl1">Level 1</option>
        <option value="lvl2">Level 2</option>
        <option value="lvl3">Level 3</option>
      </select>
    </div>
  );
};

export default EngineerTypeInput;
