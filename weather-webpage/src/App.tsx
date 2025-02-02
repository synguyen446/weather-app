import Button from "./components/Button";
import TextEntry from "./components/TextEntry";
import { useState } from "react";

function App() {
  const [city, setCity] = useState("");
  const [state, setState] = useState("");
  const [weather, setWeather] = useState("");

  const handleEventCity = (event = React.ChangeEvent<HTMLInputElement>) => {
    setCity(event.target.value);
  };

  const handleEventState = (event = React.ChangeEvent<HTMLInputElement>) => {
    setState(event.target.value);
  };

  const getWeather = async () => {
    try {
      const response = await fetch(
        `http://127.0.0.1:5000/weather?city=${city}&state=${state}`
      );
      const data = await response.json();
      setWeather(data);
      console.log(weather)
    } catch (error) {
      console.error("Error fetching weather data: ", error);
    }
  };

  return (
    <>
      <TextEntry handleEvent={handleEventCity} id="City/Address" />
      <TextEntry handleEvent={handleEventState} id="State/ZipCode/Country" />
      <Button onClick={getWeather}>Get Weather</Button>
      {Object.entries(weather).map(([key, value]) => (
        <div key={key}>
          <strong>{key}:</strong> {JSON.stringify(value)}
        </div>
      ))}
    </>
  );
}

export default App;
