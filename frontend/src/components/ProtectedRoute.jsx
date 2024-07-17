import React, { useEffect, useState } from 'react';
import { Navigate } from 'react-router-dom';

const ProtectedRoute = ({ children }) => {
    const [isValid, setIsValid] = useState(null);

    useEffect(() => {
        const validateToken = async () => {
            var email = localStorage.getItem('email');
            var token = localStorage.getItem('access');


            if (!email || !token) {
                setIsValid(false);
                return;
            }

            if (email.startsWith('"') && email.endsWith('"')) {
                email = email.slice(1, -1);
            }

            if (token.startsWith('"') && token.endsWith('"')) {
                token = token.slice(1, -1);
            }
            
            try {
                const response = await fetch('http://127.0.0.1:8000/api/user/access-check/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ email, token }),
                });

                if (!response.ok) {
                    throw new Error('Token validation failed');
                }

                const result = await response.json();
                // Assuming the backend returns a property isValid
                setIsValid(true);
            } catch (error) {
                console.error('Error validating token:', error);
                setIsValid(false);
            }
        };

        validateToken();
    }, []);

    if (isValid === null) {
        return <div>Loading...</div>;
    }

    return isValid ? children : <Navigate to="/Login" />;
};

export default ProtectedRoute;
