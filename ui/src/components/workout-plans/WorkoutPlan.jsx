import React, { useEffect } from "react";
import { useParams } from "react-router";

function WorkoutPlan() {
  let { workoutPlanId } = useParams();

  useEffect(() => {
    // Fetch workout using the workoutNameDate
  }, [workoutPlanId]);

  return (
    <div className="home">
      <div class="container">
        <h1 className="mt-5">This is the Workout Plan Title</h1>
        <h6 className="mb-5">The workout plan ID is, {workoutPlanId}</h6>
        <p>
          This is some information about the workout plan.
        </p>
        <p>
          This is some more info about the workout plan.
        </p>
        <p>
          This is even more info about the workout plan!
        </p>
      </div>
    </div>
  );
}

export default WorkoutPlan;
