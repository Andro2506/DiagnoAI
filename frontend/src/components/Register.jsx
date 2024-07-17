import React, { useState } from 'react';
import './Login.css';
import { useNavigate } from 'react-router-dom';
import vid from '../assets/homevid.mp4';

const Register = () => {
    const [email, Setemail] = useState('')
    const [name, Setname] = useState('')
    const [password, Setpassword] = useState('')
    const [password2, Setpassword2] = useState('')
    const [tc, Settc] = useState(false)

    const navigate = useNavigate()

    const handleSubmit = async(e) => {
        e.preventDefault();
        try {
            const response = await fetch('http://127.0.0.1:8000/api/user/register/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ email, name, password, password2, tc }),
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
            <div className="row"></div>
            <div className="row">
                <div className="col-md-4 col-sm-12 col-xs-12"></div>
                <div className="col-md-4 col-sm-12 col-xs-12">
                    <form className="form-container" onSubmit={handleSubmit}>
                        <h1>Registration Form</h1>
                        <div className="mb-3">
                            <label htmlFor="email" className="form-label">Email</label>
                            <input value={email} onChange={(e) => Setemail(e.target.value)} name="email" type="email" className="form-control" id="email" aria-describedby="IdHelp" required />
                            <div id="IdHelp" className="form-text text-white"></div>
                        </div>
                        <div className="mb-3">
                            <label htmlFor="name" className="form-label">Name</label>
                            <input value={name} onChange={(e) => Setname(e.target.value)} name="name" type="text" className="form-control" id="name" aria-describedby="IdHelp" required />
                            <div id="IdHelp" className="form-text text-white"></div>
                        </div>
                        <div className="mb-3">
                            <label htmlFor="exampleInputPassword1" className="form-label">Password</label>
                            <input value={password} onChange={(e) => Setpassword(e.target.value)} name="password" type="password" className="form-control" id="exampleInputPassword1" required />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="exampleInputPassword1" className="form-label">Password2</label>
                            <input value={password2} onChange={(e) => Setpassword2(e.target.value)} name="password2" type="password" className="form-control" id="exampleInputPassword1" required />
                        </div>
                        <div className="mb-3 form-check">
                            <input name="tc" checked={tc} onChange={(e) => Settc(e.target.checked)} type="checkbox" className="form-check-input" id="exampleCheck1" required />
                            <label className="form-check-label" htmlFor="exampleCheck1">Tc</label>
                        </div>
                        <div className="row justify-content-center">
                            <div className="col-md-4 col-sm-12 col-xs-12">
                                <button type="submit" className="btn btn-success btn-block">Submit</button>
                            </div>
                        </div>
                        <a style={{color:'white'}} href='/Login'>Registered User? Click to Login</a>
                    </form>
                </div>
                <div className="col-md-4 col-sm-12 col-xs-12"></div>
            </div>
        </div>
    );
}

export default Register