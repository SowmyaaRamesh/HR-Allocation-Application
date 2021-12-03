import React, { useState, useEffect } from "react";

const EngineerTypeInput = (props) => {
  const [type, setType] = useState("");
  const [level, setLevel] = useState(0);

  useEffect(() => {
    let data = {
      type: type,
      level: level,
    };

    // props.addHandler({...team1Requirements,});
  }, [type, level]);

  return (
    <div>
      <select
        name="typeOfEngineers"
        id="typeOfEngineers"
        onChange={(e) => setType((prev) => e.target.value)}
      >
        <option value="default">Type of engineer </option>
        <option value="sde">SDE</option>
        <option value="nfit">NFIT</option>
      </select>
      <select
        name="levelOfEngineers"
        id="levelOfEngineers"
        onChange={(e) => setLevel((prev) => e.target.value)}
      >
        <option value="default">Max experience level</option>
        <option value="lvl1">Level 1</option>
        <option value="lvl2">Level 2</option>
        <option value="lvl3">Level 3</option>
      </select>
    </div>
  );
};

export default EngineerTypeInput;
