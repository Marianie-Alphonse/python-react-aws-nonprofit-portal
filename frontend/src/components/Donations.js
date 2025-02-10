import React, { useState } from 'react';

const Donations = () => {
    const [donationAmount, setDonationAmount] = useState('');
    const [donorName, setDonorName] = useState('');
    const [donations, setDonations] = useState([]);

    const handleDonation = () => {
        if (donationAmount && donorName) {
            setDonations([...donations, { name: donorName, amount: donationAmount }]);
            setDonationAmount('');
            setDonorName('');
        }
    };

    return (
        <div>
            <h2>Donations</h2>
            <input
                type="text"
                placeholder="Donor Name"
                value={donorName}
                onChange={(e) => setDonorName(e.target.value)}
            />
            <input
                type="number"
                placeholder="Donation Amount"
                value={donationAmount}
                onChange={(e) => setDonationAmount(e.target.value)}
            />
            <button onClick={handleDonation}>Donate</button>
            <ul>
                {donations.map((donation, index) => (
                    <li key={index}>
                        {donation.name} donated ${donation.amount}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Donations;