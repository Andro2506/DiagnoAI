import React, { useState, useEffect } from 'react';
import '../components/Profile.css';
import vid from '../assets/homevid.mp4';

const UserProfile = () => {
  const [id, Setid] = useState('')
  const [email, Setemail] = useState('')
  const [name, Setname] = useState('')

  useEffect(() => {
    const userEmail = localStorage.getItem('email');
    Setemail(userEmail);
    var token = localStorage.getItem('access')
    if (token.startsWith('"') && token.endsWith('"')) {
      token = token.slice(1, -1);
    }
    const fetchfun = async () => {
      try {
        const response = await fetch(`http://127.0.0.1:8000/api/user/profile/?email=${userEmail}`, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`,
          },
        });

        if (!response.ok) {
          throw new Error('Network response was not ok');
        }

        const result = await response.json();
        console.log(result.id)
        console.log(result.email)
        console.log(result.name)
        Setid(result.id)
        Setname(result.name)

      } catch (error) {
        console.error('Error:', error);
      }
    }

    fetchfun();

  }, []);

  return (
    <div className='bg1'>
      <video autoPlay loop muted>
        <source src={vid} type="video/mp4" />
        Your browser does not support the video tag.
      </video>
      <table id='protable' style={{ position: 'absolute' }}>
        <tbody>
          <tr>
            <td style={{ color: 'while' }}>ID:</td>
            <td style={{ color: 'while' }}>{id}</td>
          </tr>
          <tr>
            <td style={{ color: 'while' }}>Email:</td>
            <td style={{ color: 'while' }}>{email}</td>
          </tr>
          <tr>
            <td style={{ color: 'while' }}>Name:</td>
            <td style={{ color: 'while' }}>{name}</td>
          </tr>
        </tbody>
      </table>
    </div>
  )
}

export default UserProfile