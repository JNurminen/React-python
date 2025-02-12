import React from "react";
import { render, screen } from "@testing-library/react";
import FriendForm from "./FriendForm";


// Testataan, että lomake renderöityy oikein
test("renders a form to add a friend", () => {
  const existingFriend = {
    name: "Alice",
    role: "admin",
    description: "Admin",
    gender: "female"
  };

  render(<FriendForm existingFriend={existingFriend} />);
  
  const nameInput = screen.getByLabelText("Name:");
  const roleInput = screen.getByLabelText("Role:");
  const descriptionInput = screen.getByLabelText("Job Description:");
  const genderInput = screen.getByLabelText("Gender");

  expect(nameInput.value).toBe("Alice");
  expect(roleInput.value).toBe("admin");
  expect(descriptionInput.value).toBe("Admin");
  expect(genderInput.value).toBe("female");
});