import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import './Login.css';
import vid from '../assets/homevid.mp4';

const ResetPassEmail = () => {
  const [email, Setemail] = useState('')
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://127.0.0.1:8000/api/user/send-reset-password-email/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email }),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const result = await response.json();
      console.log(result.msg)
      alert(`${result.msg}`)
      navigate('/Login')

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
            <h1>Reset password Email Form</h1>
            <div className="mb-3">
              <label htmlFor="exampleInputPassword1" className="form-label">Email</label>
              <input
                value={email}
                onChange={(e) => Setemail(e.target.value)}
                name="email"
                type="email"
                className="form-control"
                id="exampleInputEmail"
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
}

export default ResetPassEmail