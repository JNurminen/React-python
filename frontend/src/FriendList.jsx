import React from "react";

const FriendList = ({ friends, updateFriend, updateCallback }) => {
    const onDelete = async (id) => {
        try {
            const options = {
                method: "DELETE"
            };
            const response = await fetch (`http://127.0.0.1:5000/delete_friend/${id}`, options);
            if(response.status === 200) {
                updateCallback();
            } else {
                console.error("Failed to delete friend");
            }
        } catch (error) {
            alert(error);
        }
    }


  return <div>
      <h1>Contacts</h1>
      <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Role</th>
                <th>Job Description</th>
                <th>Gender</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            {friends.map((friend) => (
                <tr key={friend.id}>
                    <td>{friend.name}</td>
                    <td>{friend.role}</td>
                    <td>{friend.description}</td>
                    <td>{friend.gender}</td>
                    <td>
                        <button onClick={() => updateFriend(friend)}>Update</button>
                        <button onClick={() => onDelete(friend.id)}>Delete</button>
                    </td>
                </tr>
            ))}
        </tbody>
      </table>
    </div>
    
}

export default FriendList;