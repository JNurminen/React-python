import { useState, useEffect } from 'react';
import FriendList from './FriendList';
import './App.css';

export const BASE_URL = import.meta.env.MODE === "development" ? "http://127.0.0.1:5000/api" : "/api";


function App() {
  const [friends, setFriends] = useState([]);

  useEffect(() => {
    //fetchFriends();
  }, []);

  const fetchFriends = async () => {
    const response = await fetch(`${BASE_URL}/friends/`);
    const data = await response.json();
    setFriends(data.friends);
    console.log(data.contacts);
  };

  return <FriendList friends={friends} />;
}

export default App;