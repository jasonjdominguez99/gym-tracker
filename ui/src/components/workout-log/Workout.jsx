import React, { useEffect } from "react";
import { useParams } from "react-router";

function Workout() {
  let { workoutId } = useParams();

  useEffect(() => {
    // Fetch workout using the workoutNameDate
  }, [workoutId]);

  return (
    <div className="home">
      <div class="container">
        <h1 className="mt-5">This is the Workout Title</h1>
        <h6 className="mb-5">The workout ID is, {workoutId}</h6>
        <p>
          This is some information about the workout.
        </p>
        <p>
          This is some more info about the workout.
        </p>
        <p>
          This is even more info about the workout!
        </p>
      </div>
    </div>
  );
}

export default Workout;
