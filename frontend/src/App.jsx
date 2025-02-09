import { useState, useEffect } from 'react';
import FriendList from './FriendList';
import './App.css';
import FriendForm from './FriendForm';


function App() {
  const [friends, setFriends] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [currentFriend, setCurrentFriend] = useState({});

  useEffect(() => {
    fetchFriends();
  }, []);

  const fetchFriends = async () => {
    const response = await fetch("http://127.0.0.1:5000/api/friends");
    const data = await response.json();
    setFriends(data.friends);
  };

  const closeModal = () => {
    setIsModalOpen(false);
    setCurrentFriend({});
  };

  const openCreateModal = () => {
    if(!isModalOpen) setIsModalOpen(true);
  };

  const openEditModal = (friend) => {
    if (isModalOpen) return
    setCurrentFriend(friend);
    setIsModalOpen(true);
  };

  const onUpdate = () => {
    fetchFriends();
    closeModal();
  };

  return (
    <>
    <FriendList friends={friends} updateFriend={openEditModal} updateCallback={onUpdate} />
    <button onClick={openCreateModal}>Create Friend</button>
    {isModalOpen && <div className="modal">
      <div className="modal-content">
        <span className="close" onClick={closeModal}>&times;</span>
      <FriendForm existingFriend={currentFriend} updateCallback={onUpdate}/>
      </div>
    </div>
      }
    </>
  )
}

export default App;