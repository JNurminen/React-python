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
  };

  const closeModal = () => {
    setIsModalOpen(false);
  };

  const openCreateModal = () => {
    if(!isModalOpen) setIsModalOpen(true);
  };


  return (
    <>
    <FriendList friends={friends} />
    <button onClick={openCreateModal}>Create Friend</button>
    {isModalOpen && <div className="modal">
      <div className="modal-content">
        <span className="close" onClick={closeModal}>&times;</span>
        <FriendForm />
      <FriendForm />
      </div>
    </div>
      }
    </>
  )
}

export default App;