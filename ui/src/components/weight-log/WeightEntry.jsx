import React, { useEffect } from "react";
import { useParams } from "react-router";

function WeightEntry() {
  let { weightEntryId } = useParams();

  useEffect(() => {
    // Fetch workout using the workoutNameDate
  }, [weightEntryId]);

  return (
    <div className="home">
      <div class="container">
        <h1 className="mt-5">This is the Weight Entry Title</h1>
        <h6 className="mb-5">The weight entry ID is, {weightEntryId}</h6>
        <p>
          This is some information about the weight entry
        </p>
      </div>
    </div>
  );
}

export default WeightEntry;
