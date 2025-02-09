import { useState, useEffect } from 'react';
import FriendList from './FriendList';
import './App.css';
import FriendForm from './FriendForm';


function App() {
  const [friends, setFriends] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false);

  useEffect(() => {
    fetchFriends();
  }, []);

  const fetchFriends = async () => {
    const response = await fetch('http://localhost:5000/friends');
    const data = await response.json();
    setFriends(data.friends);
    console.log(data.contacts);
  };

  const closeModal = () => {
    setIsModalOpen(false);
  };

  return (
    <>
    <FriendList friends={friends} />
    <FriendForm />
    </>
  )
}

export default App;