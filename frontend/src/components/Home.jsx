import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import symptomChoices from './symptomChoices';
import '../components/Homecss.css';
import vid from '../assets/homevid.mp4';

const Home = () => {
    const [user, setUser] = useState('');
    const [diseases, setDiseases] = useState([]);
    const [departments, setDepartments] = useState([]);
    const [doctors, setDoctors] = useState([]);
    const [formData, setFormData] = useState({
        symptom1: '',
        symptom2: '',
        symptom3: '',
        symptom4: '',
        symptom5: ''
    });
    const [FormHist, SetFormHist] = useState({
        email: '',
        symptom1: '',
        symptom2: '',
        symptom3: '',
        symptom4: '',
        symptom5: '',
        diseases: '',
        departments: '',
        name: ''
    });

    const navigate = useNavigate();

    useEffect(() => {
        const userEmail = localStorage.getItem('email');
        setUser(userEmail);
        SetFormHist({
            ...FormHist,
            email: userEmail
        });
    }, []);

    useEffect(() => {
        console.log("FormHist updated:", FormHist);
    }, [FormHist]);

    const handleLogout = () => {
        localStorage.removeItem('email');
        localStorage.removeItem('access');
        localStorage.removeItem('refresh');
        navigate('/Login');
    }

    const handleChange = () => {
        navigate('/change-pass');
    }
    const handlePro = () => {
        navigate('/userprofile');
    }

    const handleChanges = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
        SetFormHist({
            ...FormHist,
            [e.target.name]: e.target.value
        });
    };

    const handleform = async (e) => {
        e.preventDefault();
        try {
            const response = await fetch('http://127.0.0.1:8000/api/predict/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData),
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const result = await response.json();
            console.log(result);

            const diseaseNames = result.diseases.map(diseaseInfo => diseaseInfo.disease);
            const departmentNames = [...new Set(result.diseases.map(diseaseInfo => diseaseInfo.department))];

            setDiseases(diseaseNames);
            setDepartments(departmentNames);
            localStorage.setItem('diseases', diseaseNames);
            localStorage.setItem('departments', departmentNames);

            if (departmentNames.length > 0) {
                const fetchDoctors = async (department) => {
                    try {
                        const response = await fetch('http://127.0.0.1:8000/api/getdoctor/', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                            },
                            body: JSON.stringify({ department }),
                        });

                        if (!response.ok) {
                            throw new Error('Network response was not ok');
                        }

                        const doctorsResult = await response.json();
                        let existingValue = localStorage.getItem('doctors');
                        let updatedValue = [];

                        if (existingValue) {
                            updatedValue = JSON.parse(existingValue);
                        }

                        updatedValue = [...updatedValue, ...doctorsResult.doctors];

                        localStorage.setItem('doctors', JSON.stringify(updatedValue));
                        setDoctors(prevState => [...prevState, ...doctorsResult.doctors]);
                    } catch (error) {
                        console.error('There was an error fetching the doctors!', error);
                    }
                };

                for (const department of departmentNames) {
                    await fetchDoctors(department);
                }
            }

            alert("Symptoms submitted successfully!");

        } catch (error) {
            console.error('There was an error submitting the symptoms!', error);
        }
    };

    const handlerefresh = async () => {
        var diseasesfield = localStorage.getItem('diseases');
        var deptfield = localStorage.getItem('departments');
        var docfield = localStorage.getItem('doctors')
    
        let doctorNames = '';
        const docArray = JSON.parse(docfield);
        doctorNames = docArray.map(doc => doc.name).join(', ');
    
        SetFormHist((prevFormHist) => ({
            ...prevFormHist,
            diseases: diseasesfield,
            departments: deptfield,
            name: doctorNames
        }));
    };
    
    useEffect(() => {
        const postFormHist = async () => {
            try {
                const response = await fetch('http://127.0.0.1:8000/api/history/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(FormHist),
                });
    
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
    
                const Result = await response.json();
                console.log(Result);
                localStorage.removeItem('diseases');
                localStorage.removeItem('departments');
                localStorage.removeItem('doctors');
                navigate('/');
                window.location.reload();
            } catch (error) {
                console.error(error);
            }
        };
    
        if (FormHist.diseases && FormHist.departments && FormHist.name) {
            postFormHist();
        }
    }, [FormHist]);

    return (
            
        <div className="container" >
            <video autoPlay loop muted>
                <source src={vid} type="video/mp4" />
                Your browser does not support the video tag.
            </video>
            <p style={{ position: 'absolute', top: "5px", color: 'white', zIndex:'1' }}>User: {user}</p>
            <button onClick={handleLogout} style={{ position: 'absolute', right: "10px", top: "5px", zIndex:'1' }} type="button" className="btn btn-primary">Logout</button>
            <button onClick={handleChange} style={{ position: 'absolute', right: "10px", top: "45px", zIndex:'1' }} type="button" className="btn btn-primary">Change Password</button>
            <button onClick={handlePro} style={{ position: 'absolute', right: "10px", top: "85px", zIndex:'1' }} type="button" className="btn btn-primary">Profile</button>

            <div className="form-container1">
                <form id='homeform' onSubmit={handleform}>
                    {['symptom1', 'symptom2', 'symptom3', 'symptom4', 'symptom5'].map((symptom, index) => (
                        <div style={{marginTop:'10px'}} key={index}>
                            <label style={{ color: 'white' }}>
                                {symptom.charAt(0).toUpperCase() + symptom.slice(1)}:
                                <select style={{ color: 'black', borderRadius: '2px' }} name={symptom} value={formData[symptom]} onChange={handleChanges}>
                                    <option style={{ color: 'black', borderRadius: '2px' }} value="">Select a symptom</option>
                                    {symptomChoices.map(choice => (
                                        <option style={{ color: 'black', borderRadius: '2px' }} key={choice.value} value={choice.value}>
                                            {choice.label}
                                        </option>
                                    ))}
                                </select>
                            </label>
                        </div>
                    ))}
                    <button style={{marginTop: '10px', marginBottom: '5px'}} type="submit" className="btn btn-primary">Submit</button>
                    <button onClick={handlerefresh} style={{marginTop: '2px', marginBottom: '5px'}} type="button" className="btn btn-primary">New prediction</button>
                </form>
            </div>

            <div id="table-container">
                <table id='hometable'>
                    <tbody>
                        <tr>
                            <td style={{ color: 'white', padding: '2px 2px 2px 2px' }}>Diseases:</td>
                            {diseases.map((disease, index) => (<td key={index} style={{ color: 'white' }}>{disease}</td>))}
                        </tr>
                        <tr>
                            <td style={{ color: 'white' }}>Departments:</td>
                            {departments.map((department, index) => (<td key={index} style={{ color: 'white' }}>{department}</td>))}
                        </tr>
                        <tr>
                            <td style={{ color: 'white' }}>Doctors:</td>
                            {doctors.map((doctor, index) => (<td key={index} style={{ color: 'white' }}>{doctor.name}</td>))}
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    );
};

export default Home;
