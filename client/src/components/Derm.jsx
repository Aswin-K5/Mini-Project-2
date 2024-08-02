import React, { useEffect, useState } from "react";
import "../styles/Derm.css";
import "@googlemaps/extended-component-library/overlay_layout.js";

const Derm = () => {
  const api = import.meta.env.VITE_API_KEY;
  console.log(api);
  const [latitude, setLatitude] = useState(null);
  const [longitude, setLongitude] = useState(null);
  const [loading, setLoading] = useState(true);
  const [nearbyDermatologists, setNearbyDermatologists] = useState([]);
  useEffect(() => {
    if ("geolocation" in navigator) {
      navigator.geolocation.getCurrentPosition(
        async (position) => {
          const { latitude, longitude } = position.coords;
          setLatitude(11.10219998);
          setLongitude(76.9656897);
          setLoading(false);
        },
        (error) => {
          console.error("Error getting user location:", error);
          setLoading(false);
        }
      );
    } else {
      console.error("Geolocation is not supported by this browser.");
    }
  }, []);
  console.log("Latitude:", latitude);
  console.log("Longitude:", longitude);
  return (
    <div className="derm-parent">
      <div className="derm-left">
        {latitude && longitude ? (
          <iframe
            title="Nearby Dermatologist"
            width="100%"
            height="500px"
            frameBorder="0"
            src={`https://www.google.com/maps/embed/v1/search?key=${api}&q=dermatologist+near+me&center=${latitude},${longitude}&zoom=13&maptype=roadmap`}
            allowFullScreen
          ></iframe>
        ) : (
          <p>Loading map...</p>
        )}
      </div>
      <div className="derm-right">
        <ul>
          <li>Map Showing your location and the nearby dermatologist.</li>
          <li>
            If want to know more click on the view larger icon on the map frame
          </li>
          <li>On clicking the view larger it will redirected to map page for detailed information</li>
        </ul>
      </div>
    </div>
  );
};

export default Derm;
