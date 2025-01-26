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
        `http://127.0.0.1:5000/weather?city=${city}&state=${state}'`
      );
      const data = await response.json();
      setWeather(data);
    } catch (error) {
      console.error("Error fetching weather data: ", error);
    }
  };

  return (
    <>
      <TextEntry handleEvent={handleEventCity} id="City" />
      <TextEntry handleEvent={handleEventState} id="State" />
      <Button onClick={getWeather}>Get Weather</Button>
    </>
  );
}

export default App;
