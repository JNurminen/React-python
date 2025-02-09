import React from "react";

const FriendList = ({ friends }) => {
  return (
    <div>
      <h1>Friends</h1>
      <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Role</th>
                <th>Description</th>
                <th>Email</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            {friends.map((friend) => (
                <tr key={friend.id}>
                    <td>{friend.name}</td>
                    <td>{friend.role}</td>
                    <td>{friend.description}</td>
                    <td>{friend.email}</td>
                    <td>
                        <button>Edit</button>
                        <button>Delete</button>
                    </td>
                </tr>
            ))}
        </tbody>
      </table>
    </div>
    );
}

export default FriendList;