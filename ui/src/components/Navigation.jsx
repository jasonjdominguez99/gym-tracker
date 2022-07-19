import React from "react";
import { NavLink } from "react-router-dom";

function Navigation() {
  return (
    <div className="navigation">
      <nav className="navbar navbar-expand navbar-dark bg-dark">
        <div className="container">
          <NavLink className="navbar-brand" to="/">
            Gym Tracker
          </NavLink>
          <div>
            <ul className="navbar-nav ml-auto">
              <li className="nav-item">
                <NavLink className="nav-link" to="/">
                  Home
                  <span className="sr-only">(current)</span>
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" to="/workout-log">
                  Workout Log
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" to="/workout-plans">
                  Workout Plans
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" to="/weight-log">
                  Weight Log
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" to="/my-account">
                  My Account
                </NavLink>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </div>
  );
}

export default Navigation;
