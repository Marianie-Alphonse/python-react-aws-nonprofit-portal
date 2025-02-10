import React from 'react';

const Announcements = () => {
    const announcements = [
        { id: 1, message: 'Welcome to our nonprofit portal!' },
        { id: 2, message: 'Upcoming event: Charity Run on November 20th.' },
        { id: 3, message: 'New blog post: How to get involved in your community.' }
    ];

    return (
        <div>
            <h2>Announcements</h2>
            <ul>
                {announcements.map(announcement => (
                    <li key={announcement.id}>{announcement.message}</li>
                ))}
            </ul>
        </div>
    );
};

export default Announcements;