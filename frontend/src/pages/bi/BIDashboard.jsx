import React from "react";
import { useParams } from "react-router-dom";
import "./style.scss";

const BIDashboard = () => {
  const { formId } = useParams();
  const powerBIDashboard = window?.powerBIDashboard;
  const current = powerBIDashboard?.find((x) => x.form_id === parseInt(formId));

  if (!current || !current?.content) {
    return "";
  }
  return <React.Fragment></React.Fragment>;
};

export default BIDashboard;
