import React from "react";
import { Outlet } from "react-router-dom";

function WorkoutLog() {
  return (
    <div className="home">
      <div class="container">
        <h1 className="text-center mt-5">Workout Log</h1>
        <Outlet />
      </div>
    </div>
  );
}

export default WorkoutLog;
