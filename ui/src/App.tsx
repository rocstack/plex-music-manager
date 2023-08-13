import { useState } from 'react';
import reactLogo from './assets/react.svg';
import viteLogo from '/vite.svg';
import './App.css';

function App() {
  // const [count, setCount] = useState(0);

  const connectToSpotify = async () => {
    console.log('connect to spotify');
    const result = await fetch('http://localhost:5000/spotify/login', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    });
    const data = await result.json();
    console.log(data);
    window.location.href = data.auth_url;
  };

  const getPlaylists = async () => {
    console.log('get playlists');
    const result = await fetch('http://localhost:5000/spotify/playlists', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    });
    const res = await result.json();
    console.log(res);
  };

  return (
    <>
      <div>
        <h1>Plex Music Manager</h1>
        <button onClick={() => connectToSpotify()}>Connect to Spotify</button>
        <button onClick={() => getPlaylists()}>playlists</button>
        {/* <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a> */}
      </div>
    </>
  );
}

export default App;
