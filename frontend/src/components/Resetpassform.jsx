import React, { useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import '../components/Login.css';
import vid from '../assets/homevid.mp4';

const Resetpassform = () => {
  const [password, setPass] = useState('');
  const [password2, setPass2] = useState('');

  const navigate = useNavigate();
  const { uid: urlUid, token: urlToken } = useParams();

  const localStorageToken = localStorage.getItem('access');
  const uid = localStorageToken ? null : urlUid;
  var token = localStorageToken || urlToken;

  if (token.startsWith('"') && token.endsWith('"')) {
    token = token.slice(1, -1);
  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const endpoint = uid && token
        ? `http://127.0.0.1:8000/api/user/reset-password/${uid}/${token}/`
        : 'http://127.0.0.1:8000/api/user/changepassword/';

      const headers = {
        'Content-Type': 'application/json',
      };

      if (!uid) {
        headers['Authorization'] = `Bearer ${token}`;
      }

      const response = await fetch(endpoint, {
        method: 'POST',
        headers: headers,
        body: JSON.stringify({ password, password2 }),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const result = await response.json();
      console.log(result.msg);
      alert(result.msg);

      if (uid && token) {
        navigate('/Login');
      } else {
        navigate('/');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="container-fluid bg">
      <video autoPlay loop muted>
        <source src={vid} type="video/mp4" />
        Your browser does not support the video tag.
      </video>
      <div className="row">
        <div className="col-md-4 col-sm-12 col-xs-12"></div>
        <div className="col-md-4 col-sm-12 col-xs-12">
          <form className="form-container" onSubmit={handleSubmit}>
            <h1>Reset password Form</h1>
            <div className="mb-3">
              <label htmlFor="exampleInputPassword1" className="form-label">Password</label>
              <input
                value={password}
                onChange={(e) => setPass(e.target.value)}
                name="password"
                type="password"
                className="form-control"
                id="exampleInputPassword1"
                required
              />
            </div>
            <div className="mb-3">
              <label htmlFor="exampleInputPassword2" className="form-label">Password2</label>
              <input
                value={password2}
                onChange={(e) => setPass2(e.target.value)}
                name="password2"
                type="password"
                className="form-control"
                id="exampleInputPassword2"
                required
              />
            </div>
            <div className="row justify-content-center">
              <div className="col-md-4 col-sm-12 col-xs-12">
                <button type="submit" className="btn btn-success btn-block">Submit</button>
              </div>
            </div>
          </form>
        </div>
        <div className="col-md-4 col-sm-12 col-xs-12"></div>
      </div>
    </div>
  );
};

export default Resetpassform;
