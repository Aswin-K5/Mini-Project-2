import React from "react";
import "../styles/About.css";

const About = () => {
  return (
    <div className="about-parent">
      <div className="content">
        <h3>Get To Know</h3>
        Welcome to DermAid ProVision, the intersection of cutting-edge
        technology and expert dermatological care. Our mission is to
        revolutionize the way we approach dermatological care, combining
        cutting-edge technology with expert insights.
      </div>
      <div className="content">
        <h3>What Set us Apart</h3>
        <ul>
          <li>
            Expert-Driven Precision: DermAid ProVision bridges the gap between
            automated analysis and dermatological expertise, ensuring accurate
            and nuanced insights.
          </li>
          <li>
            User-Friendly Interface: Tailored for both dermatologists and
            general users, our application offers a seamless experience, making
            skin health accessible to all.
          </li>
          <li>
            Proactive Intervention: Beyond predictions, we believe in early
            intervention. DermAid ProVision actively suggests remedies,
            fostering a preventative approach to skin care.
          </li>
        </ul>
      </div>
      <div className="content">
        <h3>Our Mission</h3>
        We are committed to redefining skin disease detection, fostering
        collaboration between technology and dermatological proficiency. DermAid
        ProVision is not just an app; it's a step towards a future where skin
        health is personalized, precise, and within everyone's reach.
      </div>
    </div>
  );
};

export default About;
