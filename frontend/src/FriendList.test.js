import React from 'react';
import { render, screen } from '@testing-library/react';
import FriendList from './FriendList';
import '@testing-library/jest-dom';


// Testataan, että ystävälista renderöityy oikein
test('renders a list of friends', () => {
  const friends = [
    { id: 1, name: 'Alice', role: 'admin', desgription: 'Admin', gender: 'female' },
  ];
  render(<FriendList friends={friends} />);
    const friendElement = screen.getByText('Alice', 'admin', 'Admin', 'female');

    expect(friendElement).toBeInTheDocument();
});