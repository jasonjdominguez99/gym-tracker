import React from "react";
import { Link } from "react-router-dom";

function WeightEntries() {
  return (
    <div className="home">
      <div class="container">
        <Link to="/weight-log/weightEntryId">
          <div class="row align-items-center my-5">
            <div class="col-lg-7">
              <img
                class="img-fluid rounded mb-4 mb-lg-0"
                src="http://placehold.it/900x400"
                alt=""
              />
            </div>
            <div class="col-lg-5">
              <h1 class="font-weight-light">This weight entry</h1>
              <p>
                This is one weight entry
              </p>
            </div>
          </div>
        </Link>
      </div>
    </div>
  );
}

export default WeightEntries;
