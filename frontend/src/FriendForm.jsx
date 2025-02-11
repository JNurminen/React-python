import { useState } from "react";

const FriendForm = ({ existingFriend = {}, updateCallback }) => {
    const [name, setName] = useState(existingFriend.name || "");
    const [role, setRole] = useState(existingFriend.role || "");
    const [description, setDescription] = useState(existingFriend.description || "");
    const [gender, setGender] = useState(existingFriend.gender || "");

    const updating = Object.entries(existingFriend).length !== 0;

    const onSubmit = async (e) => {
        e.preventDefault();
        
        const data = {
            name,
            role,
            description,
            gender
        };
        const url = "http://localhost:5000/" + (updating ? `update_friend/${existingFriend.id}` : "create_friend");
        const options = {
            method: updating ? "PATCH":"POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        };
        const response = await fetch(url, options);
        if(response.status !== 201 && response.status !== 200) {
            const data = await response.json();
            alert(data.message);
        } else {
            updateCallback();
        }
    }

    return (
        <form onSubmit={onSubmit}>
            <div>
                <label htmlFor="name">Name</label>
                <input type="text" id="name" value={name} onChange={(e) => setName(e.target.value)} />
            </div>
            <div>
                <label htmlFor="role">Role</label>
                <input type="text" id="role" value={role} onChange={(e) => setRole(e.target.value)} />
            </div>
            <div>
                <label htmlFor="description">Description</label>
                <input type="text" id="description" value={description} onChange={(e) => setDescription(e.target.value)} />
            </div>
            <div>
                <label htmlFor="gender">Gender</label>
                <input type="text" id="gender" value={gender} onChange={(e) => setGender(e.target.value)} />
            </div>
            <button type="submit">{updating ? "Update" : "Create"}</button>
        </form>
    )
};

export default FriendForm;