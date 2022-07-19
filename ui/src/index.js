import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import {
  Navigation,
  Footer,
  Home,
  MyAccount,
  WorkoutPlan,
  WorkoutPlans,
  WorkoutPLansList,
  Workout,
  WorkoutLog,
  Workouts,
  WeightEntries,
  WeightEntry,
  WeightLog
} from "./components";

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <Router>
    <Navigation />
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/my-account" element={<MyAccount />} />
      <Route path="/workout-plans" element={<WorkoutPLansList />}>
        <Route path="" element={<WorkoutPlans />} />
        <Route path=":workoutPlanId" element={<WorkoutPlan />} />
      </Route>
      <Route path="/workout-log" element={<WorkoutLog />}>
        <Route path="" element={<Workouts />} />
        <Route path=":workoutId" element={<Workout />} />
      </Route>
      <Route path="/weight-log" element={<WeightLog />}>
        <Route path="" element={<WeightEntries />} />
        <Route path=":weightEntryId" element={<WeightEntry />} />
      </Route>
    </Routes>
    <Footer />
  </Router>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
