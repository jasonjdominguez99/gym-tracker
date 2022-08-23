import React, { useState } from "react";
import { Link } from "react-router-dom";
import Calendar from 'react-calendar';

function Workouts() {
  const [value, onChange] = useState(new Date());

  return (
    <div className="home">
      <div class="container">
        <Calendar onChange={onChange} value={value} />
        <Link to="/workout-log/workoutId">
          <div class="row align-items-center my-5">
            <div class="col-lg-5">
              <h1 class="font-weight-light">This workout</h1>
              <p>
                This is one workout
              </p>
            </div>
          </div>
        </Link>
      </div>
    </div>
  );
}

export default Workouts;
