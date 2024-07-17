import React, { useState } from 'react';
import '../components/Login.css'
import { useNavigate } from 'react-router-dom';
import vid from '../assets/homevid.mp4';

const Login = () => {
    const [email, Setemail] = useState('')
    const [password, Setpass] = useState('')
    const navigate = useNavigate();

    const handleSubmit = async(e) => {
        e.preventDefault();
        try {
            const response = await fetch('http://127.0.0.1:8000/api/user/login/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ email, password }),
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const result = await response.json();
            // Handle the result as needed, e.g., storing tokens, redirecting, etc.
            localStorage.setItem('email', email);
            localStorage.setItem('access', JSON.stringify(result.token.access));
            localStorage.setItem('refresh', JSON.stringify(result.token.refresh));
            console.log(result.msg)
            navigate('/')

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
                        <h1>Login Form</h1>
                        <div className="mb-3">
                            <label htmlFor="email" className="form-label">Email</label>
                            <input value={email} onChange={(e)=>Setemail(e.target.value)} name="email" type="email" className="form-control" id="email" aria-describedby="IdHelp" required />
                            <div id="IdHelp" className="form-text text-white"></div>
                        </div>
                        <div className="mb-3">
                            <label htmlFor="exampleInputPassword1" className="form-label">Password</label>
                            <input value={password} onChange={(e)=>Setpass(e.target.value)} name="password" type="password" className="form-control" id="exampleInputPassword1" required />
                        </div>
                        <div className="row justify-content-center">
                            <div className="col-md-4 col-sm-12 col-xs-12">
                                <button type="submit" className="btn btn-success btn-block">Submit</button>
                            </div>
                        </div>
                        <a style={{color:'white'}} href='/reset-pass'>Forgot password</a>
                        <a style={{color:'white', marginLeft:"10px"}} href='/Register'>New User? Click to register</a>
                    </form>
                </div>
                <div className="col-md-4 col-sm-12 col-xs-12"></div>
            </div>
        </div>
    );
};

export default Login;
